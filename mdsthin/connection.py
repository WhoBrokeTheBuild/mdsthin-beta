
import os
import sys
import ctypes
import socket

from .message import *
from .exceptions import *

INVALID_MESSAGE_ID = 0

MDSIP_VERSION = 3

class Connection:
    
    def __init__(self, url, username=None):

        self._socket = None
        self._message_id = INVALID_MESSAGE_ID
        self._server_version = None
        self._compression_level = None

        self._username = username
        if self._username is None:
            self._username = os.getlogin()

        self._host = url
        self._protocol = 'tcp'
        if '://' in self._host:
            self._protocol, self._host = self._host.split('://', maxsplit=1)
        
        self._port = 8000
        if ':' in self._host:
            self._port, self._host = self._host.split(':', maxsplit=1)
            self._port = int(self._port)

        if self._protocol != 'tcp':
            raise Exception('Only tcp:// is supported')
        
        self.connect()

    def __del__(self):
        self.disconnect()
        
    def connect(self):
        
        if self._protocol == 'tcp':
            socket_family = socket.AF_INET
            socket_type = socket.SOCK_STREAM
        
        elif self._protocol == 'tcp6':
            socket_family = socket.AF_INET6
            socket_type = socket.SOCK_STREAM

        self._socket = socket.socket(socket_family, socket_type)
        
        # This causes a massive speed increase
        # It was designed to reduce the number of small packets on the wire, but we use
        # small packets for a lot of things, so it only hurts us
        self._socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        
        # Regular MDSplus also sets SO_KEEPALIVE and SO_OOBINLINE

        address_list = socket.getaddrinfo(self._host, self._port, family=socket_family, type=socket_type)
        self._address = address_list[0][4]

        self._socket.connect(self._address)

        mlogin = Message(String(self._username))
        mlogin.ndims = 1
        mlogin.dims[0] = MDSIP_VERSION

        self.send(mlogin)

        # The login response does not contain data
        self._socket.recv_into(mlogin, ctypes.sizeof(mlogin), socket.MSG_WAITALL)

        if STATUS_NOT_OK(mlogin.status):
            raise Exception('Failed to login')
        
        self._compression_level = (mlogin.status & 0x1E) >> 1
        self._client_type = mlogin.client_type
        
        if mlogin.ndims > 0:
            self.version = mlogin.dims[0]

    def disconnect(self):

        if self._socket:
            self._socket.close()
            self._socket = None

    def send(self, msg: Message):

        buffer = msg.pack()
        self._socket.sendall(buffer)

    def recv(self):

        msg = Message()
        data = Descriptor()

        self._socket.recv_into(msg, ctypes.sizeof(msg), socket.MSG_WAITALL)

        data_length = msg.msglen - ctypes.sizeof(Message)
        if data_length > 0:
            buffer = bytearray(self._socket.recv(data_length, socket.MSG_WAITALL))
            data = msg.unpack_data(buffer)

        return msg, data

    def get(self, expr, *args):

        if expr.strip() == '':
            return Descriptor()
        
        mget = Message(expr, compression_level=self._compression_level)
        mget.nargs = 1 + len(args)

        self._message_id += 1
        mget.message_id = self._message_id

        self.send(mget)

        for i, arg in enumerate(args):
            marg = Message(arg, compression_level=self._compression_level)
            marg.nargs = mget.nargs
            marg.message_id = mget.message_id
            marg.descriptor_idx = i + 1

            self.send(marg)

        manswer, data = self.recv()

        if STATUS_NOT_OK(manswer.status):
            raise getException(manswer.status)

        return data

    def getObject(self, expr, *args):
        return self.get(f'SerializeOut(`({expr};))', *args).deserialize(conn=self)

    def put(self, path, expr, *args):
        args = [path, expr] + list(args)
        args_format = ','.join('$' * len(args))
        status = self.get(f'TreePut({args_format})', *args)

        if STATUS_NOT_OK(status):
            raise getException(status)

    def getMany(self):
        return GetMany(self)

    def putMany(self):
        return PutMany(self)

    def openTree(self, tree, shot):
        status = self.get('TreeOpen($,$)', tree, shot).data()

        if STATUS_NOT_OK(status):
            raise getException(status)

    def closeTree(self, tree, shot):
        status = self.get('TreeClose($,$)', tree, shot).data()

        if STATUS_NOT_OK(status):
            raise getException(status)
        
    def closeAllTrees(self):
        self.get("_i=0;WHILE(IAND(TreeClose(),1)) _i++;_i")

    def setDefault(self, path):
        status = self.get('TreeSetDefault($)', path).data()

        if STATUS_NOT_OK(status):
            raise getException(status)

    def tcl(self, command):
        result = self.get('Tcl($,_res);_res', command)
        if result is None:
            return ''
        return result.data()
    
    def mdstcl(self):

        while True:
            # Use sys.stdout to avoid cluttering the python history with TCL commands
            sys.stdout.write('TCL> ')
            sys.stdout.flush()
            command = sys.stdin.readline()

            # Ctrl+D
            if len(command) == 0:
                print()
                break

            command = command.strip()
            
            # Empty command
            if len(command) == 0:
                continue

            if command == 'exit':
                break

            result = self.tcl(command)
            if result is not None:
                print(result, end='')
    
    def tdic(self):

        while True:
            # Use sys.stdout to avoid cluttering the python history with TCL commands
            sys.stdout.write('TDI> ')
            sys.stdout.flush()
            command = sys.stdin.readline()

            # Ctrl+D
            if len(command) == 0:
                print()
                break

            command = command.strip()

            if command == 'exit':
                break

            result = None
            try:
                result = self.get(command)
            except MdsException as e:
                print(e)

            if result is None:
                print(repr(dMISSING()))
            else:
                print(repr(result))

class GetMany:
    
    def __init__(self, connection: Connection):
        self._connection = connection
        self._queries = List()
        self._result = Dictionary()

    def append(self, name, exp, *args):
        self._queries.append(Dictionary({
            'name': name,
            'exp': exp,
            'args': list(args),
        }))

    def remove(self, name):
        for query in self._queries:
            if query['name'] == name:
                self._queries.remove(query)
                break

    def execute(self):
        result = self._connection.get('GetManyExecute($)', self._queries.serialize())
        
        if isinstance(self._result, String):
            raise MDSplusException(f'GetMany Error: {self._result.data()}')
        
        self._result = result.deserialize()
        return self._result
    
    def get(self, name):
        if name not in self._result:
            return None
        
        result = self._result[name]
        if 'value' in result:
            return result['value']
        
        raise getExceptionFromError(result['error'].data())

class PutMany:
    
    def __init__(self, connection: Connection):
        self._connection = connection
        self._queries = List()
        self._result = Dictionary()
    
    def append(self, name, exp, *args):
        self._queries.append(Dictionary({
            'name': name,
            'exp': exp,
            'args': list(args),
        }))

    def execute(self):
        result = self._connection.get('PutManyExecute($)', self._queries.serialize())
        
        if isinstance(self._result, String):
            raise MDSplusException(f'PutMany Error: {self._result.data()}')
        
        self._result = result.deserialize(conn=self)
        return self._result
