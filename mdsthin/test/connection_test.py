
import unittest

from ..connection import *
from ..functions import *

class ConnectionTest(unittest.TestCase):

    SERVER = ''

    @classmethod
    def setUpClass(cls):
        if cls.SERVER != '':
            cls.conn = Connection(cls.SERVER)

    def setUp(self):
        if self.SERVER == '':
            raise unittest.SkipTest("--server was not specified")
    
    def test_tdi_types(self):

        tests = [
            { 'type': Int32,   'exp': '42',        'value': 42, },
            { 'type': UInt8,   'exp': '42BU',      'value': 42, },
            { 'type': UInt16,  'exp': '42WU',      'value': 42, },
            { 'type': UInt32,  'exp': '42LU',      'value': 42, },
            { 'type': UInt64,  'exp': '42QU',      'value': 42, },
            { 'type': Int8,    'exp': '42B',       'value': 42, },
            { 'type': Int16,   'exp': '42W',       'value': 42, },
            { 'type': Int32,   'exp': '42L',       'value': 42, },
            { 'type': Int64,   'exp': '42Q',       'value': 42, },
            { 'type': Float32, 'exp': '3.14159',   'value': 3.14159, },
            { 'type': Float32, 'exp': '3.14159F0', 'value': 3.14159, },
            { 'type': Float64, 'exp': '3.14159D0', 'value': 3.14159, },
            { 'type': Float64, 'exp': '3.14159G0', 'value': 3.14159, },
            # { 'type': Float128, 'exp': '3.14159H0', },

            { 'type': Float32, 'exp': 'F_FLOAT(3.14159)', 'value': 3.14159, },
            # { 'type': Float64, 'exp': 'D_FLOAT(3.14159)', 'value': 3.14159, },
            { 'type': Float64, 'exp': 'G_FLOAT(3.14159)', 'value': 3.14159, },

            { 'type': Int32Array, 'exp': '[ [2, 4], [6, 8] ]',     'value': numpy.array([ [2, 4], [6, 8] ], dtype=numpy.int32) },
            { 'type': Int8Array,  'exp': '[ [2B, 4B], [6B, 8B] ]', 'value': numpy.array([ [2, 4], [6, 8] ], dtype=numpy.int8) },
            { 'type': Int16Array, 'exp': '[ [2W, 4W], [6W, 8W] ]', 'value': numpy.array([ [2, 4], [6, 8] ], dtype=numpy.int16) },
            { 'type': Int32Array, 'exp': '[ [2L, 4L], [6L, 8L] ]', 'value': numpy.array([ [2, 4], [6, 8] ], dtype=numpy.int32) },
            { 'type': Int64Array, 'exp': '[ [2Q, 4Q], [6Q, 8Q] ]', 'value': numpy.array([ [2, 4], [6, 8] ], dtype=numpy.int64) },
        ]

        for info in tests:
            name = f"get('{info['exp']}')"
            with self.subTest(name):

                data = self.conn.get(info['exp'])
                self.assertEqual(type(data), info['type'])

                if type(info['value']) is float:
                    self.assertAlmostEqual(data.data(), info['value'], places=5)
                else:
                    self.assertEqual(data, info['value'])

        for info in tests:
            name = f"getObject('{info['exp']}')"
            with self.subTest(name):

                data = self.conn.getObject(info['exp'])
                self.assertEqual(type(data), info['type'])

                if type(info['value']) is float:
                    self.assertAlmostEqual(data.data(), info['value'], places=5)
                else:
                    self.assertEqual(data, info['value'])

    def test_getmany(self):

        expected_result = Descriptor({
            String('a'): Descriptor({ String('value'): Int32(42) }),
            String('b'): Descriptor({ String('value'): String('Hello, World!') }),
            String('c'): Descriptor({ String('error'): String('%TREE-W-NOT_OPEN, Tree not currently open') }),
        })

        gm = self.conn.getMany()
        gm.append('a', '42')
        gm.append('b', '"Hello, World!"')
        gm.append('c', 'asdf')
        result = gm.execute()

        self.assertEqual(result, expected_result)
        self.assertEqual(gm.get('a'), 42)
        self.assertEqual(gm.get('b'), 'Hello, World!')
        self.assertRaises(TreeNOT_OPEN, gm.get, 'c')

    def test_root_whoami(self):

        root_conn = Connection(self.SERVER, username='root')

        whoami = root_conn.get('whoami()').data()
        self.assertEqual(whoami, 'nobody', msg='Claiming to be root should map you to nobody.')

    def test_empty_get(self):

        result = self.conn.get('')
        self.assertEqual(type(result), Descriptor)
        self.assertEqual(result.data(), None)

