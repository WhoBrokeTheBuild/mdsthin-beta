from __future__ import annotations

from .descriptors import *

client_t = ctypes.c_int8

INVALID_CLIENT = 0
IEEE_CLIENT = 2

COMPRESSED = 0x20
SENDCAPABILITIES = 0xF

MAX_DIMS = 8

class MsgHdr(ctypes.LittleEndianStructure):
    _pack_ = 4
    _fields_ = [
        ('msglen', ctypes.c_int),
        ('status', ctypes.c_int),
        ('length', ctypes.c_int16),
        ('nargs', ctypes.c_ubyte),
        ('descriptor_idx', ctypes.c_ubyte),
        ('message_id', ctypes.c_ubyte),
        ('dtype_id', dtype_t),
        ('client_type', client_t),
        ('ndims', ctypes.c_ubyte),
        ('dims', ctypes.c_int * MAX_DIMS)
    ]

class Message(MsgHdr):
    
    def __init__(self, dsc = None, compression_level: int = 0):

        if not isinstance(dsc, Descriptor):
            dsc = Descriptor(dsc)

        if type(dsc) is Descriptor:
            self.buffer = bytearray()
            self.length = 0
            self.dtype_id = DTYPE_MISSING

        else:
            if not isinstance(dsc, (DescriptorS, DescriptorA)):
                raise Exception('Only able to send CLASS_S and CLASS_A descriptors, use `SerializeIn`')
            
            self.buffer = dsc.pack_data()
            self.length = len(self.buffer)
            self.dtype_id = dsc.dtype_id

            if isinstance(dsc, DescriptorA):
                self.ndims = dsc.dimct
                for i in range(self.ndims):
                    self.dims[i] = dsc.dims[i]

        self.client_type = IEEE_CLIENT

        self.msglen = ctypes.sizeof(Message) + len(self.buffer)

        if len(self.buffer) > 0 and compression_level > 0:
            import zlib

            compressed_buffer = zlib.compress(self.buffer, compression_level)
            if len(compressed_buffer) < len(self.buffer):
                original_msglen = self.msglen
                compressed_buffer = bytearray(original_msglen) + compressed_buffer

                self.client_type |= COMPRESSED
                self.buffer = compressed_buffer
                self.msglen = ctypes.sizeof(Message) + len(self.buffer)

    def pack(self):
        return bytes(self) + self.buffer

    def unpack_data(self, buffer):

        if (self.client_type & COMPRESSED) > 0:
            raise Exception('Compression is not implemented')
        
        dtype_id = self.dtype_id

        # The data for deprecated dtypes gets converted automatically
        # but for some reason, the dtype id remains the same
        if dtype_id == DTYPE_F:
            dtype_id = DTYPE_FS
        elif dtype_id == DTYPE_D:
            dtype_id = DTYPE_FT
        elif dtype_id == DTYPE_FC:
            dtype_id = DTYPE_FSC
        elif dtype_id == DTYPE_DC:
            dtype_id = DTYPE_FTC
        
        if self.ndims > 0:
            return DescriptorA.unpack_data(dtype_id, buffer, dims=self.dims[: self.ndims])
            
        else:
            return DescriptorS.unpack_data(dtype_id, buffer)
