
import ctypes
import numpy

from .exceptions import *
from .internals.dtypedef import *
from .internals.classdef import *
from .internals.mdsdescrip import *
from .internals.CvtConvertFloat import convert_float, convert_float_array

###
### Numeric
###

class Numeric:
    """
    Numeric type base class

    This contains the useful mathematical operators for all numeric types
    """

    def __new__(cls, *args, **kwargs):
        if cls is Numeric:
            raise Exception(f'Numeric cannot be instantiated directly')
        
        return object.__new__(cls)
    
    @property
    def __array_interface__(self):
        return self._data.__array_interface__
    
    def __int__(self):
        return int(self._data)
    
    def __float__(self):
        return float(self._data)
    
    def __add__(self, other):
        if isinstance(other, Signal):
            return Signal(self._data + other.data(), None, *other.dimensions)
        return Descriptor.from_data(self._data + other)
    
    def __sub__(self, other):
        if isinstance(other, Signal):
            return Signal(self._data - other.data(), None, *other.dimensions)
        return Descriptor.from_data(self._data - other)
    
    def __mul__(self, other):
        if isinstance(other, Signal):
            return Signal(self._data * other.data(), None, *other.dimensions)
        return Descriptor.from_data(self._data * other)
    
    def __pow__(self, other):
        if isinstance(other, Signal):
            return Signal(self._data ** other.data(), None, *other.dimensions)
        return Descriptor.from_data(self._data ** other)
    
    def __truediv__(self, other):
        if isinstance(other, Signal):
            return Signal(self._data / other.data(), None, *other.dimensions)
        return Descriptor.from_data(self._data / other)
    
    def __floordiv__(self, other):
        if isinstance(other, Signal):
            return Signal(self._data // other.data(), None, *other.dimensions)
        return Descriptor.from_data(self._data // other)
    
    def __mod__(self, other):
        if isinstance(other, Signal):
            return Signal(self._data % other.data(), None, *other.dimensions)
        return Descriptor.from_data(self._data % other)
    
    def __lshift__(self, other):
        return self.__class__(self._data << other)
    
    def __rshift__(self, other):
        return self.__class__(self._data >> other)
    
    def __and__(self, other):
        return self.__class__(self._data & other)
    
    def __or__(self, other):
        return self.__class__(self._data | other)
    
    def __xor__(self, other):
        return self.__class__(self._data ^ other)
    
    def __not__(self):
        return self.__class__(~self._data)
    
###
### Descriptor
###

class Descriptor:
    """
    Descriptor base class
    """

    def __new__(cls, data=None, dsc=None, *args, **kwargs):

        if cls is Descriptor:

            if dsc is not None:
                cls = DTYPE_CLASS_MAP[dsc.class_id][dsc.dtype_id]

            else:
                if isinstance(data, (DescriptorS, DescriptorA)):
                    cls = type(data)
                    data = data.data()

                # TODO: APD

                elif isinstance(data, DescriptorR):
                    arguments = list(data.dscptrs)
                    if data._data is not None:
                        arguments = [data._data] + arguments
                    
                    

                elif isinstance(data, str):
                    cls = String
                elif isinstance(data, bool):
                    cls = UInt8
                elif isinstance(data, int):
                    cls = Int64
                elif isinstance(data, float):
                    cls = Float64

                elif isinstance(data, (bytes, bytearray, memoryview)):
                    cls = UInt8Array
                elif isinstance(data, list):
                    cls = List
                elif isinstance(data, tuple):
                    cls = Tuple
                elif isinstance(data, dict):
                    cls = Dictionary

                elif isinstance(data, numpy.number):
                    
                    for dtype_id, numpy_dtype in NUMPY_DTYPE_MAP.items():
                        if data.dtype == numpy_dtype:
                            cls = DTYPE_CLASS_MAP[CLASS_S][dtype_id]
                            break

                elif isinstance(data, numpy.ndarray):
                    
                    for dtype_id, numpy_dtype in NUMPY_DTYPE_MAP.items():
                        if data.dtype == numpy_dtype:
                            cls = DTYPE_CLASS_MAP[CLASS_A][dtype_id]
                            break

                    if data.dtype.char in ['U', 'S']:
                        cls = StringArray
        
        if cls is Descriptor:
            return object.__new__(cls)
        
        return cls.__new__(cls)

    def __init__(self, data=None, dsc=None):
        self._dsc = dsc
        self._data = data

        if self._dsc is None:
            self._dsc = mdsdsc_t(
                length=0,
                class_id=CLASS_MISSING,
                dtype_id=DTYPE_MISSING,
                offset=0
            )

    @property
    def length(self):
        return self._dsc.length
    
    @property
    def dtype_id(self):
        return self._dsc.dtype_id

    @property
    def dtype_str(self):
        return dtype_to_string(self._dsc.dtype_id)
    
    @property
    def class_id(self):
        return self._dsc.class_id
    
    @property
    def class_str(self):
        return class_to_string(self._dsc.class_id)

    @property
    def offset(self):
        return self._dsc.offset

    def data(self):
        return self._data

    def __repr__(self):
        return f'{self.__class__.__name__}({self._data})'
    
    def __eq__(self, other):
        if isinstance(other, Descriptor):
            other = other.data()
        return self.data() == other
    
    def __hash__(self):
        return hash(self.data())
    
    def serialize(self):
        return UInt8Array(self.pack())
    
    @staticmethod
    def from_data(data):
        if isinstance(data, Descriptor):
            return data
        
        return Descriptor(data)
    
    def pack(self):
        return bytes()
    
    @staticmethod
    def unpack(buffer):

        buffer = bytearray(buffer)
        
        # TODO: Improve?
        dtype_id = buffer[2]
        class_id = buffer[3]

        if class_id not in DTYPE_CLASS_MAP:
            raise Exception('Invalid class:', class_to_string(class_id))
        
        if dtype_id not in DTYPE_CLASS_MAP[class_id]:
            raise Exception('Invalid dtype for class:', dtype_to_string(dtype_id), class_to_string(class_id))

        dtype_class = DTYPE_CLASS_MAP[class_id][dtype_id]

        if issubclass(dtype_class, DescriptorS):

            dsc = mdsdsc_s_t.from_buffer(buffer)

            if dsc.length == 0:
                dsc.length = get_dtype_size(dsc.dtype_id)

            if dsc.offset == 0:
                dsc.offset = ctypes.sizeof(dsc)

            data = None
            data_buffer = buffer[ dsc.offset : dsc.offset + dsc.length ]
            
            if dsc.dtype_id in NUMPY_DTYPE_MAP:
                data = numpy.frombuffer(data_buffer, dtype=NUMPY_DTYPE_MAP[dtype_id], count=1)[0]
            
            elif dsc.dtype_id == DTYPE_T:
                data = data_buffer.decode('ascii')
            
            elif dsc.dtype_id in [ DTYPE_F, DTYPE_D, DTYPE_G ]:
                data = convert_float(dsc.dtype_id, data_buffer)
                
            return dtype_class(data)

        elif issubclass(dtype_class, DescriptorA):

            dsc = mdsdsc_a_t.from_buffer(buffer)

            if dsc.length == 0:
                dsc.length = get_dtype_size(dsc.dtype_id)

            count = dsc.arsize // dsc.length
            shape = (count,)
            order = 'C' # C-style Row-Major

            if dsc.scale > 0:
                raise Exception('Array scale unimplemented')
            
            if dsc.digits > 0:
                raise Exception('Array digits unimplemented')
            
            if dsc.aflags.binscale:
                raise Exception('Array binscale unimplemented')
            
            # if dsc.aflags.redim:
            #     raise Exception('Array redim unimplemented')

            if dsc.aflags.coeff:

                a0_coeff_buffer = buffer[ ctypes.sizeof(dsc) : ]
                a0_coeff = numpy.frombuffer(a0_coeff_buffer, dtype='uint32', count=(1 + dsc.dimct))
                
                a0 = a0_coeff[0]
                coeff = a0_coeff[1 : ]

                dsc.offset = a0 # "address of element whos index is all zeros"
                shape = coeff[ : : -1]

                if dsc.aflags.bounds:
                    raise Exception('Array bounds unimplemented')
            
            # The inverse from what the documentation claims...
            if not dsc.aflags.column:
                order = 'F' # Fortran-style Column-Major

            data = None
            data_buffer = buffer[ dsc.offset : dsc.offset + dsc.arsize ]
            
            if dtype_id in NUMPY_DTYPE_MAP:
                data = numpy.frombuffer(data_buffer, dtype=NUMPY_DTYPE_MAP[dtype_id], count=count)
            
            elif dtype_id == DTYPE_T:
                data = numpy.frombuffer(data_buffer, dtype=f'|S{dsc.length}').astype(str)

            elif dsc.dtype_id in [ DTYPE_F, DTYPE_D, DTYPE_G ]:
                data = convert_float_array(dsc.dtype_id, data_buffer)

            data = data.reshape(shape, order=order)
                
            return dtype_class(data)
        
        elif issubclass(dtype_class, DescriptorAPD):

            dsc = mdsdsc_a_t.from_buffer(buffer)

            if dsc.offset == 0:
                dsc.offset = ctypes.sizeof(dsc)

            if dsc.length != 4:
                raise Exception('APD length != 4')

            offsets_buffer = buffer[ dsc.offset : dsc.offset + dsc.arsize ]
            offsets = numpy.frombuffer(offsets_buffer, dtype=numpy.uint32)

            descs = []
            for offset in offsets:
                if offset == 0:
                    descs.append(Descriptor())
                    continue

                data_buffer = buffer[offset : ]
                descs.append(Descriptor.unpack(data_buffer))

            return dtype_class(descs=descs)
            
        elif issubclass(dtype_class, DescriptorR):

            dsc = mdsdsc_r_t.from_buffer(buffer)

            offsets_buffer = buffer[ ctypes.sizeof(dsc) : ]
            offsets = numpy.frombuffer(offsets_buffer, dtype=numpy.uint32, count=dsc.ndesc)

            arguments = []

            data_buffer = buffer[ dsc.offset : ]
            if dsc.length == 1:
                arguments.append(Int8(numpy.frombuffer(data_buffer, dtype=numpy.uint8, count=1)[0]))
            elif dsc.length == 2:
                arguments.append(Int16(numpy.frombuffer(data_buffer, dtype=numpy.uint16, count=1)[0]))

            for i in range(dsc.ndesc):
                if offsets[i] == 0:
                    arguments.append(Descriptor())
                    continue

                dscptr_buffer = buffer[ offsets[i] : ]
                arguments.append(Descriptor.unpack(dscptr_buffer))

            return dtype_class(*arguments)

###
### DescriptorS
###

class DescriptorS(Descriptor):

    def __new__(cls, *args, **kwargs):
        if cls is DescriptorS:
            raise Exception(f'DescriptorS cannot be instantiated directly')
        
        return object.__new__(cls)

    def __init__(self, data, dsc):
        
        dsc.class_id = CLASS_S
        dsc.offset = ctypes.sizeof(dsc)

        super().__init__(data=data, dsc=dsc)
    
    def pack(self):
        return self.pack_header() + self.pack_data()
    
    def pack_header(self):
        return bytearray(self._dsc)
        
    def pack_data(self):
        return bytearray(self._data.tobytes())
    
    @staticmethod
    def unpack_data(dtype_id, buffer):
        dtype_class = DTYPE_CLASS_MAP[CLASS_S][dtype_id]

        if dtype_id in NUMPY_DTYPE_MAP:
            numpy_dtype = NUMPY_DTYPE_MAP[dtype_id]
            data = numpy.frombuffer(buffer, dtype=numpy_dtype, count=1)[0]

        elif dtype_id == DTYPE_T:
            data = buffer.decode('ascii')

        return dtype_class(data)

class String(DescriptorS):

    def __init__(self, data=''):
        data = str(data)

        super().__init__(
            data=data,
            dsc=mdsdsc_s_t(
                length=len(data.encode('ascii')),
                dtype_id=DTYPE_T,
            ),
        )

    def __repr__(self):
        return f'String("{self._data}")'

    def pack_data(self):
        return bytearray(self._data.encode('ascii'))
    
    @staticmethod
    def unpack_data(buffer):
        return String(buffer.decode('ascii'))

class Ident(DescriptorS):
    pass

class NID(DescriptorS):
    def __init__(self, data=0):
        data = numpy.uint32(data)

        super().__init__(
            data=data,
            dsc=mdsdsc_s_t(
                length=data.itemsize,
                dtype_id=DTYPE_NID,
            ),
        )

class Path(DescriptorS):
    pass

class UInt8(DescriptorS, Numeric):
    def __init__(self, data=0):
        data = numpy.uint8(data)

        super().__init__(
            data=data,
            dsc=mdsdsc_s_t(
                length=data.itemsize,
                dtype_id=DTYPE_BU,
            ),
        )
    
class UInt16(DescriptorS, Numeric):
    def __init__(self, data=0):
        data = numpy.uint16(data)

        super().__init__(
            data=data,
            dsc=mdsdsc_s_t(
                length=data.itemsize,
                dtype_id=DTYPE_WU,
            ),
        )

class UInt32(DescriptorS, Numeric):
    def __init__(self, data=0):
        data = numpy.uint32(data)

        super().__init__(
            data=data,
            dsc=mdsdsc_s_t(
                length=data.itemsize,
                dtype_id=DTYPE_LU,
            ),
        )

class UInt64(DescriptorS, Numeric):
    def __init__(self, data=0):
        data = numpy.uint64(data)

        super().__init__(
            data=data,
            dsc=mdsdsc_s_t(
                length=data.itemsize,
                dtype_id=DTYPE_QU,
            ),
        )

class Int8(DescriptorS, Numeric):
    def __init__(self, data=0):
        data = numpy.int8(data)

        super().__init__(
            data=data,
            dsc=mdsdsc_s_t(
                length=data.itemsize,
                dtype_id=DTYPE_B,
            ),
        )

class Int16(DescriptorS, Numeric):
    def __init__(self, data=0):
        data = numpy.int16(data)

        super().__init__(
            data=data,
            dsc=mdsdsc_s_t(
                length=data.itemsize,
                dtype_id=DTYPE_W,
            ),
        )

class Int32(DescriptorS, Numeric):
    def __init__(self, data=0):
        data = numpy.int32(data)

        super().__init__(
            data=data,
            dsc=mdsdsc_s_t(
                length=data.itemsize,
                dtype_id=DTYPE_L,
            ),
        )

class Int64(DescriptorS, Numeric):
    def __init__(self, data=0):
        data = numpy.int64(data)

        super().__init__(
            data=data,
            dsc=mdsdsc_s_t(
                length=data.itemsize,
                dtype_id=DTYPE_Q,
            ),
        )

class Float32(DescriptorS, Numeric):
    def __init__(self, data=0.0):
        data = numpy.float32(data)

        super().__init__(
            data=data,
            dsc=mdsdsc_s_t(
                length=data.itemsize,
                dtype_id=DTYPE_FS,
            ),
        )

class Float64(DescriptorS, Numeric):
    def __init__(self, data=0.0):
        data = numpy.float64(data)

        super().__init__(
            data=data,
            dsc=mdsdsc_s_t(
                length=data.itemsize,
                dtype_id=DTYPE_FT,
            ),
        )

###
### DescriptorA
###

class DescriptorA(Descriptor):

    def __new__(cls, *args, **kwargs):
        if cls is DescriptorA:
            raise Exception(f'DescriptorA cannot be instantiated directly')
        
        return object.__new__(cls)

    def __init__(self, data, dsc, dims=[]):
        
        self._dims = tuple(dims)

        if isinstance(data, numpy.ndarray): # TODO: StringArray
            self._dims = data.shape[::-1]
            dsc.length = data.itemsize
            dsc.arsize = data.size * data.itemsize

        dsc.offset = ctypes.sizeof(dsc)
        dsc.dimct = len(self._dims)
        dsc.aflags.redim = 1 # Indicate that this array can be redimensioned
        dsc.aflags.column = 1 # Opposite to what the comments claim, this indicates row-major
        dsc.aflags.coeff = (dsc.dimct > 1)

        if dsc.aflags.coeff:
            # a0
            dsc.offset += ctypes.sizeof(ctypes.c_uint32)

            # coeff
            dsc.offset += ctypes.sizeof(ctypes.c_uint32) * dsc.dimct

        super().__init__(data=data, dsc=dsc)

    def __eq__(self, other):
        if isinstance(other, Descriptor):
            other = other.data()

        # numpy.array(bool).all()
        return (self.data() == other).all()

    def __ne__(self, other):
        if isinstance(other, Descriptor):
            other = other.data()

        # numpy.array(bool).any()
        return (self.data() != other).any()
    
    @property
    def scale(self):
        return self._dsc.scale

    @property
    def digits(self):
        return self._dsc.digits

    @property
    def aflags(self):
        return self._dsc.aflags
    
    @property
    def dimct(self):
        return self._dsc.dimct
    
    @property
    def dims(self):
        return self._dims
    
    @property
    def arsize(self):
        return self._dsc.arsize
    
    def pack(self):
        return self.pack_header() + self.pack_data()
    
    def pack_header(self):
        buffer = bytearray(self._dsc)

        if self._dsc.aflags.coeff:
            a0_coeffs = [self._dsc.offset] + list(self._dims)
            a0_coeffs = numpy.array(a0_coeffs, dtype=numpy.int32)
            buffer += a0_coeffs.tobytes()

        return buffer
        
    def pack_data(self):
        return bytearray(self._data.tobytes())
    
    @staticmethod
    def unpack_data(dtype_id, buffer, dims=[]):
        dtype_class = DTYPE_CLASS_MAP[CLASS_A][dtype_id]
        numpy_dtype = NUMPY_DTYPE_MAP[dtype_id]

        data = numpy.frombuffer(buffer, dtype=numpy_dtype)
        
        if len(dims) > 0:
            data = data.reshape(dims[::-1])

        return dtype_class(data)

class StringArray(DescriptorA):
    def __init__(self, data=[]):

        data = numpy.array(data, dtype=str)
        shape = data.shape

        # Iterating over a flat array is considerably easier than using numpy.nditer
        data = data.flatten()

        # Ensure that all elements are the same size by padding them with trailing spaces
        maxlen = data.itemsize
        for i, s in enumerate(data):
            data[i] = s.ljust(maxlen)

        # Put our original shape back
        data = data.reshape(shape)
        
        # Force numpy to use ASCII (well, UTF-8) instead of UTF-32
        data = data.astype(bytes)

        super().__init__(
            data=data,
            dsc=mdsdsc_a_t(
                class_id=CLASS_A,
                dtype_id=DTYPE_T,
            ),
        )

    def __repr__(self):
        return f'StringArray({self._data.astype(str)})'

    def __eq__(self, other):
        if isinstance(other, Descriptor):
            other = other.data()

        # numpy.array(bool).all()
        return (self.data().astype(str) == other.astype(str)).all()

    def __ne__(self, other):
        if isinstance(other, Descriptor):
            other = other.data()

        # numpy.array(bool).any()
        return (self.data().astype(str) != other.astype(str)).any()

    def data(self):
        tmp = self._data.astype(str).flatten()

        for i, s in enumerate(tmp):
            tmp[i] = s.rstrip()

        return tmp.reshape(self._data.shape)
    
    def data_raw(self):
        return self._data.astype(str)

class UInt8Array(DescriptorA, Numeric):
    def __init__(self, data=[]):
        if isinstance(data, (bytes, bytearray, memoryview)):
            data = numpy.frombuffer(data, dtype=numpy.uint8)
        else:
            data = numpy.array(data, dtype=numpy.uint8)

        super().__init__(
            data=data,
            dsc=mdsdsc_a_t(
                class_id=CLASS_A,
                dtype_id=DTYPE_BU,
            ),
        )

    def deserialize(self):
        return Descriptor.unpack(bytearray(self.data().tobytes()))

class UInt16Array(DescriptorA, Numeric):
    def __init__(self, data=[]):
        data = numpy.array(data, dtype=numpy.uint16)

        super().__init__(
            data=data,
            dsc=mdsdsc_a_t(
                class_id=CLASS_A,
                dtype_id=DTYPE_WU,
            ),
        )

class UInt32Array(DescriptorA, Numeric):
    def __init__(self, data=[]):
        data = numpy.array(data, dtype=numpy.uint32)

        super().__init__(
            data=data,
            dsc=mdsdsc_a_t(
                class_id=CLASS_A,
                dtype_id=DTYPE_LU,
            ),
        )

class UInt64Array(DescriptorA, Numeric):
    def __init__(self, data=[]):
        data = numpy.array(data, dtype=numpy.uint64)

        super().__init__(
            data=data,
            dsc=mdsdsc_a_t(
                class_id=CLASS_A,
                dtype_id=DTYPE_QU,
            ),
        )

class Int8Array(DescriptorA, Numeric):
    def __init__(self, data=[]):
        if isinstance(data, (bytes, bytearray, memoryview)):
            data = numpy.frombuffer(data, dtype=numpy.int8)
        else:
            data = numpy.array(data, dtype=numpy.int8)

        super().__init__(
            data=data,
            dsc=mdsdsc_a_t(
                class_id=CLASS_A,
                dtype_id=DTYPE_B,
            ),
        )

    def deserialize(self):
        return Descriptor.unpack(bytearray(self.data().tobytes()))

class Int16Array(DescriptorA, Numeric):
    def __init__(self, data=[]):
        data = numpy.array(data, dtype=numpy.int16)

        super().__init__(
            data=data,
            dsc=mdsdsc_a_t(
                class_id=CLASS_A,
                dtype_id=DTYPE_W,
            ),
        )

class Int32Array(DescriptorA, Numeric):
    def __init__(self, data=[]):
        data = numpy.array(data, dtype=numpy.int32)

        super().__init__(
            data=data,
            dsc=mdsdsc_a_t(
                class_id=CLASS_A,
                dtype_id=DTYPE_L,
            ),
        )

class Int64Array(DescriptorA, Numeric):
    def __init__(self, data=[]):
        data = numpy.array(data, dtype=numpy.int64)

        super().__init__(
            data=data,
            dsc=mdsdsc_a_t(
                class_id=CLASS_A,
                dtype_id=DTYPE_Q,
            ),
        )

class Float32Array(DescriptorA, Numeric):
    def __init__(self, data=[]):
        data = numpy.array(data, dtype=numpy.float32)

        super().__init__(
            data=data,
            dsc=mdsdsc_a_t(
                class_id=CLASS_A,
                dtype_id=DTYPE_FS,
            ),
        )

class Float64Array(DescriptorA, Numeric):
    def __init__(self, data=[]):
        data = numpy.array(data, dtype=numpy.float64)

        super().__init__(
            data=data,
            dsc=mdsdsc_a_t(
                class_id=CLASS_A,
                dtype_id=DTYPE_FT,
            ),
        )
    
###
### DescriptorAPD
###

class DescriptorAPD(Descriptor):

    def __new__(cls, *args, **kwargs):
        if cls is DescriptorAPD:
            raise Exception(f'DescriptorAPD cannot be instantiated directly')
        
        return object.__new__(cls)

    def __init__(self, data, count, dsc):

        # TODO:
        
        dsc.class_id = CLASS_APD
        dsc.length = ctypes.sizeof(ctypes.c_uint32)
        dsc.arsize = count * dsc.length
        dsc.dimct = 1

        super().__init__(data=data, dsc=dsc)

    def data(self):
        return self

    @property
    def scale(self):
        return self._dsc.scale

    @property
    def digits(self):
        return self._dsc.digits

    @property
    def aflags(self):
        return self._dsc.aflags
    
    @property
    def dimct(self):
        return self._dsc.dimct
    
    @property
    def dims(self):
        return self._data.shape[::-1]
    
    @property
    def arsize(self):
        return self._dsc.arsize
    
    @property
    def descs(self):
        return list(self)

    def __repr__(self):
        return f'{self.__class__.__name__}({",".join(map(repr, self.descs))})'
    
    def pack(self):

        count = self._dsc.arsize // self._dsc.length
        offsets = numpy.zeros(count, dtype=numpy.uint32)

        data_buffer = bytearray()
        data_offset = ctypes.sizeof(self._dsc) + (offsets.itemsize * offsets.size)

        for i, value in enumerate(self.descs):

            if type(value) is Descriptor:
                offsets[i] = 0
                continue

            offsets[i] = data_offset + len(data_buffer)
            data_buffer += value.pack()

        return bytearray(bytes(self._dsc) + offsets.tobytes() + data_buffer)
    
class List(DescriptorAPD):
    
    def __init__(self, *items, descs=[]):

        data = []

        # If this has been called as List(list)
        if len(items) == 1 and isinstance(items[0], (list, tuple)):
            for item in items[0]:
                data.append(Descriptor.from_data(item))

        else:
            for item in items:
                data.append(Descriptor.from_data(item))

        data.extend(descs)

        super().__init__(
            data=data,
            count=len(data),
            dsc=mdsdsc_a_t(
                dtype_id=DTYPE_LIST,
            )
        )

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return self._data.__iter__()

    def __getitem__(self, index):
        return self._data[index]
    
    def __setitem__(self, index, value):
        self._data[index] = Descriptor.from_data(value)
        self._dsc.arsize = len(self._data) * self._dsc.length
    
    def append(self, value):
        self._data.append(Descriptor.from_data(value))
        self._dsc.arsize += self._dsc.length

    def data(self):
        return self._data

# Trying to subclass tuple causes issues
class Tuple(DescriptorAPD):
    
    def __init__(self, *items, descs=[]):

        data = []

        # If this has been called as Tuple(tuple)
        if len(items) == 1 and isinstance(items[0], (list, tuple)):
            for item in items[0]:
                data.append(Descriptor.from_data(item))

        else:
            for item in items:
                data.append(Descriptor.from_data(item))

        data.extend(descs)

        super().__init__(
            data=tuple(data),
            count=len(data),
            dsc=mdsdsc_a_t(
                dtype_id=DTYPE_TUPLE,
            )
        )

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return self._data.__iter__()

    def __getitem__(self, index):
        return self._data[index]

    def data(self):
        return tuple(self._data)

class Dictionary(DescriptorAPD):
    
    # dict or key, value, ...repeat
    def __init__(self, *pairs, descs=[]):

        # If this has been called as Dictionary(dict)
        if len(pairs) == 1 and isinstance(pairs[0], dict):
            pairs = list(pairs[0].items())

        # If the entire list contains key/value tuples
        elif all([ (isinstance(pair, tuple) and len(pair) == 2) for pair in pairs ]):
            pairs = list(pairs)
            
        else:
            from itertools import islice, izip
            pairs = izip(islice(pairs, None, None, 2), islice(pairs, 1, None, 2))

        data = {}
        for k, v in pairs:
            data[Descriptor.from_data(k)] = Descriptor.from_data(v)

        if (len(descs) % 2) != 0:
            raise Exception('Cannot create Dictionary, descs must be a list of key/value pairs')

        for i in range(0, len(descs), 2):
            data[descs[i]] = descs[i + 1]

        super().__init__(
            data=data,
            count=len(data) * 2,
            dsc=mdsdsc_a_t(
                dtype_id=DTYPE_DICTIONARY,
            )
        )

    def __repr__(self):
        return f'Dictionary({", ".join(list(map(repr, self.items())))})'
    
    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return self._data.__iter__()
    
    def __contains__(self, key):
        return self._data.__contains__(key)
    
    def __getitem__(self, key):
        return self._data.__getitem__(key)
    
    def __setitem__(self, key, value):
        self._data[Descriptor.from_data(key)] = Descriptor.from_data(value)
        self._dsc.arsize = (len(self._data) * 2) * self._dsc.length
    
    def keys(self):
        return self._data.keys()
    
    def values(self):
        return self._data.values()
    
    def items(self):
        return self._data.items()
    
    def get(self, key, default):
        return self._data.get(key, default)

    def data(self):
        return dict(self._data)
    
    @property
    def descs(self):
        descs = []
        for k, v in self.items():
            descs.append(k)
            descs.append(v)
        return descs

###
### DescriptorR
###

class DescriptorR(Descriptor):

    def __new__(cls, *args, **kwargs):
        if cls is DescriptorR:
            raise Exception(f'DescriptorR cannot be instantiated directly')
        
        return object.__new__(cls)
    
    def __init__(self, dsc, dscptrs, data=None):
        
        dsc.class_id = CLASS_R
        dsc.ndesc = len(dscptrs)
        
        self._dscptrs = [ Descriptor.from_data(dscptr) for dscptr in dscptrs ]

        if data is not None:
            dsc.length = data.itemsize

        super().__init__(data=data, dsc=dsc)

    def __repr__(self):
        return f'{self.__class__.__name__}({", ".join(map(repr, self._dscptrs))})'
    
    def __eq__(self, other):
        if type(self) != type(other):
            return False
        
        if self._data != other._data:
            return False
        
        if len(self._dscptrs) != len(other._dscptrs):
            return False
        
        for ours, theirs in zip(self._dscptrs, other._dscptrs):
            if ours != theirs:
                return False

        return True
    
    @property
    def ndesc(self):
        return self._dsc.ndesc
    
    @property
    def dscptrs(self):
        return self._dscptrs

    def data(self):
        return self
    
    def pack(self):
        offsets = numpy.zeros(self._dsc.ndesc, dtype=numpy.uint32)

        dscptrs_buffer = bytearray()
        dscptrs_offset = ctypes.sizeof(self._dsc) + (offsets.itemsize * offsets.size)

        data_buffer = bytearray()
        if self._data is not None:
            self._dsc.length = self._data.itemsize
            self._dsc.offset = dscptrs_offset
            dscptrs_offset += self._data.itemsize
            data_buffer = bytearray(self._data.tobytes())

        for i, dscptr in enumerate(self.dscptrs):

            if type(dscptr) is Descriptor:
                offsets[i] = 0
                continue

            offsets[i] = dscptrs_offset + len(dscptrs_buffer)
            dscptrs_buffer += dscptr.pack()

        return bytearray(bytes(self._dsc) + offsets.tobytes() + data_buffer + dscptrs_buffer)

class Signal(DescriptorR):
    
    def __init__(self, value=None, raw=None, *dimensions):
        super().__init__(
            dscptrs=[value, raw, *dimensions],
            dsc=mdsdsc_r_t(
                dtype_id=DTYPE_SIGNAL,
            )
        )

    @property
    def value(self):
        return self._dscptrs[0]
    
    @property
    def raw(self):
        return self._dscptrs[1]
    
    @property
    def dimensions(self):
        return self._dscptrs[2 : ]

    def data(self):
        if type(self.value) is not Descriptor:
            return self.value.data()
        return self.raw.data()
    
    def raw_of(self):
        return self._dscptrs[1]

    def dim_of(self, index=0):
        return self.dimensions[index]

class Dimension(DescriptorR):
    
    def __init__(self, window=None, axis=None):
        super().__init__(
            dscptrs=[window, axis],
            dsc=mdsdsc_r_t(
                dtype_id=DTYPE_DIMENSION,
            )
        )

    @property
    def window(self):
        return self._dscptrs[0]
    
    @property
    def axis(self):
        return self._dscptrs[1]

class Window(DescriptorR):
    
    def __init__(self, startidx=None, endingidx=None, value_at_idx0=None):
        super().__init__(
            dscptrs=[startidx, endingidx, value_at_idx0],
            dsc=mdsdsc_r_t(
                dtype_id=DTYPE_WINDOW,
            )
        )

    @property
    def startidx(self):
        return self._dscptrs[0]

    @property
    def endingidx(self):
        return self._dscptrs[1]

    @property
    def value_at_idx0(self):
        return self._dscptrs[2]

class Slope(DescriptorR):
    
    # slope, begin, ending, ...repeat
    def __init__(self, *segments):
        if (len(segments) % 3) != 0:
            raise Exception('len(segments) must be a multiple of 3')
        
        super().__init__(
            dscptrs=[*segments],
            dsc=mdsdsc_r_t(
                dtype_id=DTYPE_SLOPE,
            )
        )

    @property
    def segments(self):
        segments = []
        for i in range(0, len(self._dscptrs), 3):
            segments.append((self._dscptrs[i], self._dscptrs[i + 1], self._dscptrs[i + 2]))
        return segments

class Function(DescriptorR):
    
    def __init__(self, opcode = 0, *arguments):
        super().__init__(
            data=numpy.uint16(opcode),
            dscptrs=[*arguments],
            dsc=mdsdsc_r_t(
                dtype_id=DTYPE_FUNCTION,
            )
        )

    @property
    def opcode(self):
        return self._data

    @property
    def arguments(self):
        return self._dscptrs

    def __repr__(self):
        return f'Function({self._data}, {", ".join(map(repr, self._dscptrs))})'
    
    def data(self):
        raise Exception('Functions are not implemented')

class Conglom(DescriptorR):
    
    def __init__(self, image=None, model=None, name=None, qualifiers=None):
        super().__init__(
            dscptrs=[image, model, name, qualifiers],
            dsc=mdsdsc_r_t(
                dtype_id=DTYPE_CONGLOM,
            )
        )

    @property
    def image(self):
        return self._dscptrs[0]

    @property
    def model(self):
        return self._dscptrs[1]

    @property
    def name(self):
        return self._dscptrs[2]

    @property
    def qualifiers(self):
        return self._dscptrs[3]

class Range(DescriptorR):
    
    def __init__(self, begin=None, ending=None, deltaval=None):
        super().__init__(
            dscptrs=[begin, ending, deltaval],
            dsc=mdsdsc_r_t(
                dtype_id=DTYPE_RANGE,
            )
        )

    @property
    def begin(self):
        return self._dscptrs[0]

    @property
    def ending(self):
        return self._dscptrs[1]

    @property
    def deltaval(self):
        return self._dscptrs[2]
    
    def data(self):
        return range(self.begin.data(), self.ending.data(), self.deltaval.data())
    
    # TODO: iterator?
    
class Action(DescriptorR):

    def __init__(self, dispatch=None, task=None, errorlogs=None, completion_message=None, performance=None):
        super().__init__(
            dscptrs=[dispatch, task, errorlogs, completion_message, performance],
            dsc=mdsdsc_r_t(
                dtype_id=DTYPE_ACTION,
            )
        )
    
    @property
    def dispatch(self):
        return self._dscptrs[0]
    
    @property
    def task(self):
        return self._dscptrs[1]
    
    @property
    def errorlogs(self):
        return self._dscptrs[2]
    
    @property
    def completion_message(self):
        return self._dscptrs[3]
    
    @property
    def performance(self):
        return self._dscptrs[4]

class Dispatch(DescriptorR):
    
    def __init__(self, treesched = 0, ident=None, phase=None, when=None, completion=None):
        super().__init__(
            data=numpy.uint8(treesched),
            dscptrs=[ident, phase, when, completion],
            dsc=mdsdsc_r_t(
                dtype_id=DTYPE_DISPATCH,
            )
        )

    @property
    def treesched(self):
        return self._data

    @property
    def ident(self):
        return self._dscptrs[0]

    @property
    def phase(self):
        return self._dscptrs[1]

    @property
    def when(self):
        return self._dscptrs[2]

    @property
    def completion(self):
        return self._dscptrs[3]

class Program(DescriptorR):
    
    def __init__(self, time_out=None, program=None):
        super().__init__(
            dscptrs=[time_out, program],
            dsc=mdsdsc_r_t(
                dtype_id=DTYPE_PROGRAM,
            )
        )

    @property
    def time_out(self):
        return self._dscptrs[0]

    @property
    def program(self):
        return self._dscptrs[1]
    
    def data(self):
        raise Exception('Programs are not implemented')

class Routine(DescriptorR):
    
    def __init__(self, time_out=None, image=None, routine=None, *arguments):
        super().__init__(
            dscptrs=[time_out, image, routine, *arguments],
            dsc=mdsdsc_r_t(
                dtype_id=DTYPE_ROUTINE,
            )
        )

    @property
    def time_out(self):
        return self._dscptrs[0]

    @property
    def image(self):
        return self._dscptrs[1]

    @property
    def routine(self):
        return self._dscptrs[2]

    @property
    def arguments(self):
        return self._dscptrs[3 : ]
    
    def data(self):
        raise Exception('Routines are not implemented')

class Procedure(DescriptorR):
    
    def __init__(self, time_out=None, language=None, procedure=None, *arguments):
        super().__init__(
            dscptrs=[time_out, language, procedure, *arguments],
            dsc=mdsdsc_r_t(
                dtype_id=DTYPE_PROCEDURE,
            )
        )

    @property
    def time_out(self):
        return self._dscptrs[0]

    @property
    def language(self):
        return self._dscptrs[1]

    @property
    def procedure(self):
        return self._dscptrs[2]

    @property
    def arguments(self):
        return self._dscptrs[3 : ]
    
    def data(self):
        raise Exception('Procedures are not implemented')

class Method(DescriptorR):
    
    def __init__(self, time_out=None, method=None, device=None):
        super().__init__(
            dscptrs=[time_out, method, device],
            dsc=mdsdsc_r_t(
                dtype_id=DTYPE_METHOD,
            )
        )

    @property
    def time_out(self):
        return self._dscptrs[0]

    @property
    def method(self):
        return self._dscptrs[1]

    @property
    def device(self):
        return self._dscptrs[2]
    
    def data(self):
        raise Exception('Methods are not implemented')

class Dependency(DescriptorR):
    
    def __init__(self, treedep = 0, *arguments):
        super().__init__(
            data=numpy.uint8(treedep),
            dscptrs=[*arguments],
            dsc=mdsdsc_r_t(
                dtype_id=DTYPE_DEPENDENCY,
            )
        )

    @property
    def treedep(self):
        return self._data

    @property
    def arguments(self):
        return self._dscptrs
    
    def data(self):
        raise Exception('Dependencies are not implemented')

class Condition(DescriptorR):
    
    def __init__(self, treecond=0, condition=None):
        super().__init__(
            data=numpy.uint8(treecond),
            dscptrs=[condition],
            dsc=mdsdsc_r_t(
                dtype_id=DTYPE_CONDITION,
            )
        )

    @property
    def treecond(self):
        return self._data

    @property
    def condition(self):
        return self._dscptrs[0]

class WithUnits(DescriptorR):
    
    def __init__(self, value=None, units=None):
        super().__init__(
            dscptrs=[value, units],
            dsc=mdsdsc_r_t(
                dtype_id=DTYPE_WITH_UNITS,
            )
        )

    @property
    def value(self):
        return self._dscptrs[0]

    @property
    def units(self):
        return self._dscptrs[1]

    def data(self):
        return self.value.data()

class Call(DescriptorR):
    
    def __init__(self, return_dtype_id=DTYPE_L, image=None, routine=None, *arguments):
        super().__init__(
            data=numpy.uint8(return_dtype_id),
            dscptrs=[image, routine, *arguments],
            dsc=mdsdsc_r_t(
                dtype_id=DTYPE_CALL,
            )
        )

    @property
    def return_dtype_id(self):
        return self._data

    @property
    def image(self):
        return self._dscptrs[0]
    
    @property
    def routine(self):
        return self._dscptrs[1]
    
    @property
    def arguments(self):
        return self._dscptrs[2 : ]
    
    def data(self):
        raise Exception('Calls are not implemented')

class WithError(DescriptorR):
    
    def __init__(self, value=None, error=None):
        super().__init__(
            dscptrs=[value, error],
            dsc=mdsdsc_r_t(
                dtype_id=DTYPE_WITH_ERROR,
            )
        )

    @property
    def value(self):
        return self._dscptrs[0]

    @property
    def error(self):
        return self._dscptrs[1]
    
    def getException(self):
        return getExceptionFromError(self.error.data())

    def data(self):
        return self.value.data()

class Opaque(DescriptorR):
    
    def __init__(self, value=None, opaque_type=None):
        super().__init__(
            dscptrs=[value, opaque_type],
            dsc=mdsdsc_r_t(
                dtype_id=DTYPE_OPAQUE,
            )
        )

    @property
    def value(self):
        return self._dscptrs[0]

    @property
    def opaque_type(self):
        return self._dscptrs[1]
    
    def data(self):
        return self.value.data()

###
### Lookup Tables
###

CLASS_MAP = {
    CLASS_MISSING: Descriptor,
    CLASS_S: DescriptorS,
    CLASS_A: DescriptorA,
    CLASS_CA: DescriptorA,
    CLASS_APD: DescriptorA,
    CLASS_R: DescriptorR,
}

DTYPE_CLASS_MAP = {
    CLASS_S: {
        CLASS_MISSING: Descriptor,
        DTYPE_T: String,
        DTYPE_IDENT: Ident,
        DTYPE_PATH: Path,
        DTYPE_NID: NID,
        DTYPE_BU: UInt8,
        DTYPE_WU: UInt16,
        DTYPE_LU: UInt32,
        DTYPE_QU: UInt64,
        DTYPE_B: Int8,
        DTYPE_W: Int16,
        DTYPE_L: Int32,
        DTYPE_Q: Int64,
        DTYPE_FS: Float32,
        DTYPE_F: Float32,
        DTYPE_FT: Float64,
        DTYPE_D: Float64,
        DTYPE_G: Float64,
    },
    CLASS_A: {
        CLASS_MISSING: Descriptor,
        DTYPE_T: StringArray,
        DTYPE_BU: UInt8Array,
        DTYPE_WU: UInt16Array,
        DTYPE_LU: UInt32Array,
        DTYPE_QU: UInt64Array,
        DTYPE_B: Int8Array,
        DTYPE_W: Int16Array,
        DTYPE_L: Int32Array,
        DTYPE_Q: Int64Array,
        DTYPE_FS: Float32Array,
        DTYPE_F: Float32Array,
        DTYPE_FT: Float64Array,
        DTYPE_D: Float64Array,
        DTYPE_G: Float64Array,
    },
    CLASS_APD: {
        DTYPE_LIST: List,
        DTYPE_TUPLE: Tuple,
        DTYPE_DICTIONARY: Dictionary,
    },
    CLASS_R: {
        CLASS_MISSING: Descriptor,
        DTYPE_SIGNAL: Signal,
        DTYPE_DIMENSION: Dimension,
        DTYPE_WINDOW: Window,
        DTYPE_SLOPE: Slope,
        DTYPE_FUNCTION: Function,
        DTYPE_CONGLOM: Conglom,
        DTYPE_RANGE: Range,
        DTYPE_ACTION: Action,
        DTYPE_DISPATCH: Dispatch,
        DTYPE_PROGRAM: Program,
        DTYPE_ROUTINE: Routine,
        DTYPE_PROCEDURE: Procedure,
        DTYPE_METHOD: Method,
        DTYPE_DEPENDENCY: Dependency,
        DTYPE_CONDITION: Condition,
        DTYPE_WITH_UNITS: WithUnits,
        DTYPE_CALL: Call,
        DTYPE_WITH_ERROR: WithError,
        DTYPE_OPAQUE: Opaque,
    }
}

NUMPY_DTYPE_MAP = {
    DTYPE_BU: numpy.uint8,
    DTYPE_WU: numpy.uint16,
    DTYPE_LU: numpy.uint32,
    DTYPE_QU: numpy.uint64,
    DTYPE_B: numpy.int8,
    DTYPE_W: numpy.int16,
    DTYPE_L: numpy.int32,
    DTYPE_Q: numpy.int64,
    DTYPE_FS: numpy.float32,
    DTYPE_FT: numpy.float64,
    DTYPE_NID: numpy.uint32,
}