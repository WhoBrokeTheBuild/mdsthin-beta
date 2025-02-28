
import numpy
import unittest

from ..connection import *
from ..functions import *

class CModTest(unittest.TestCase):

    SERVER = ''

    @classmethod
    def setUpClass(cls):
        if cls.SERVER != '':
            cls.conn = Connection(cls.SERVER)
            cls.conn.openTree('cmod', 1090909009)

    def setUp(self):
        if self.SERVER == '':
            raise unittest.SkipTest("--server and --cmod were not specified")

    def test_open_close_tree(self):

        self.conn.openTree('cmod', -1)
        self.conn.closeTree('cmod', -1)

    def test_tstart(self):

        self.assertEqual(self.conn.get('TSTART'), -4.0)

        # TSTART is DTYPE_F, this tests convert_float
        self.assertEqual(self.conn.getObject('TSTART'), -4.0)

    def test_ip(self):

        first10 = numpy.array([ 0, 0, -2.0493028, 313.1422, 2.0493028, 0, 311.0929, -2.0493028, 309.0436, 311.0929 ], dtype=numpy.float32)

        data = self.conn.get('\\IP').data()

        self.assertTrue((data[ : 10] == first10).all())

    def test_checkcamac(self):

        self.assertRaises(TdiINVCLADTY, self.conn.get, 'ADMIN.CHECKCAMAC')

        compare = Action(Dispatch(2, 'ALCDATA_ANALYSIS', 'INIT', 999, ''), EXT_FUNCTION(None, 'CheckCamacServers'), '', None, None)

        data = self.conn.getObject('ADMIN.CHECKCAMAC')

        self.assertEqual(data, compare)