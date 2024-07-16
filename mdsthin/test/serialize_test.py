
import numpy
import unittest

from .BaseTestCase import *
from ..descriptors import *

class SerializeTest(BaseTestCase):

    def test_pack_unpack(self):

        INTEGER_ARRAY = [ 1, 1, 2, 4, 6, 10 ]
        FLOAT_ARRAY = [ -2.0, -1.0, 0.0, 1.0, 2.0, 3.0 ]

        INTEGER_MATRIX = [ [2, 4], [6, 8], [16, 32] ]
        FLOAT_MATRIX = [ [1.0, 1.5], [2.0, 2.5], [3.0, 3.5] ]

        tests = [
            # size = sizeof(mdsdsc_s_t) + sizeof(TYPE)
            { 'data': UInt8(42),        'size': 8 + 1 },
            { 'data': UInt16(42),       'size': 8 + 2 },
            { 'data': UInt32(42),       'size': 8 + 4 },
            { 'data': UInt64(42),       'size': 8 + 8 },
            { 'data': Int8(42),         'size': 8 + 1 },
            { 'data': Int16(42),        'size': 8 + 2 },
            { 'data': Int32(42),        'size': 8 + 4 },
            { 'data': Int64(42),        'size': 8 + 8 },
            { 'data': Float32(3.14159), 'size': 8 + 4 },
            { 'data': Float64(3.14159), 'size': 8 + 8 },

            # size = sizeof(mdsdsc_a_t) + (sizeof(TYPE) * len(DATA.flatten()))
            { 'data': UInt8Array(INTEGER_ARRAY),  'size': 16 + 6 },
            { 'data': UInt16Array(INTEGER_ARRAY), 'size': 16 + (6 * 2) },
            { 'data': UInt32Array(INTEGER_ARRAY), 'size': 16 + (6 * 4) },
            { 'data': UInt64Array(INTEGER_ARRAY), 'size': 16 + (6 * 8) },
            { 'data': Int8Array(INTEGER_ARRAY),   'size': 16 + 6 },
            { 'data': Int16Array(INTEGER_ARRAY),  'size': 16 + (6 * 2) },
            { 'data': Int32Array(INTEGER_ARRAY),  'size': 16 + (6 * 4) },
            { 'data': Int64Array(INTEGER_ARRAY),  'size': 16 + (6 * 8) },
            { 'data': Float32Array(FLOAT_ARRAY),  'size': 16 + (6 * 4) },
            { 'data': Float64Array(FLOAT_ARRAY),  'size': 16 + (6 * 8) },

            # size = sizeof(mdsdsc_a_t) + (sizeof(uint32) * (len(DATA.shape) + 1)) + (sizeof(TYPE) * len(DATA.flatten()))
            { 'data': UInt8Array(INTEGER_MATRIX),  'size': 16 + 12 + 6 },
            { 'data': UInt16Array(INTEGER_MATRIX), 'size': 16 + 12 + (6 * 2) },
            { 'data': UInt32Array(INTEGER_MATRIX), 'size': 16 + 12 + (6 * 4) },
            { 'data': UInt64Array(INTEGER_MATRIX), 'size': 16 + 12 + (6 * 8) },
            { 'data': Int8Array(INTEGER_MATRIX),   'size': 16 + 12 + 6 },
            { 'data': Int16Array(INTEGER_MATRIX),  'size': 16 + 12 + (6 * 2) },
            { 'data': Int32Array(INTEGER_MATRIX),  'size': 16 + 12 + (6 * 4) },
            { 'data': Int64Array(INTEGER_MATRIX),  'size': 16 + 12 + (6 * 8) },
            { 'data': Float32Array(FLOAT_MATRIX),  'size': 16 + 12 + (6 * 4) },
            { 'data': Float64Array(FLOAT_MATRIX),  'size': 16 + 12 + (6 * 8) },

            # size = sizeof(mdsdsc_s_t) + len(data)
            { 'data': String('Hello, World!'), 'size': 8 + 13 },

            # size = sizeof(mdsdsc_a_t) + pad_data_to_same_length(data)
            { 'data': StringArray([ 'one', 'three', 'seventeen' ]), 'size': 16 + 27 },
            { 'data': StringArray([ ['a', 'b'], ['one', 'three'], ['', 'seventeen'] ]), 'size': 16 + 12 + 54 },
        ]

        for info in tests:
            name = repr(info['data'])
            with self.subTest(name):
                
                buffer = info['data'].pack()
                self.assertEqual(len(buffer), info['size'])

                data_out = Descriptor.unpack(buffer)
                self.assertEqual(data_out, info['data'])


    def test_pack_buffers(self):

        # Packed with MDSplus.Data(...).serialize().data().tobytes()
        tests = [
            { 'data': String('Hello, World!'), 'buffer': b'\r\x00\x0e\x01\x08\x00\x00\x00Hello, World!' },

            { 'data': UInt8(42),  'buffer': b'\x01\x00\x02\x01\x08\x00\x00\x00*' },
            { 'data': UInt16(42), 'buffer': b'\x02\x00\x03\x01\x08\x00\x00\x00*\x00' },
            { 'data': UInt32(42), 'buffer': b'\x04\x00\x04\x01\x08\x00\x00\x00*\x00\x00\x00' },
            { 'data': UInt64(42), 'buffer': b'\x08\x00\x05\x01\x08\x00\x00\x00*\x00\x00\x00\x00\x00\x00\x00' },

            { 'data': Int8(42),  'buffer': b'\x01\x00\x06\x01\x08\x00\x00\x00*' },
            { 'data': Int16(42), 'buffer': b'\x02\x00\x07\x01\x08\x00\x00\x00*\x00' },
            { 'data': Int32(42), 'buffer': b'\x04\x00\x08\x01\x08\x00\x00\x00*\x00\x00\x00' },
            { 'data': Int64(42), 'buffer': b'\x08\x00\t\x01\x08\x00\x00\x00*\x00\x00\x00\x00\x00\x00\x00' },
        ]

        for info in tests:
            name = repr(info['data'])
            with self.subTest(name):
                
                data = Descriptor.unpack(info['buffer'])
                self.assertEqual(type(data), type(info['data']))
                self.assertEqual(data, info['data'])

                buffer = data.pack()
                self.assertEqual(buffer, info['buffer'])
