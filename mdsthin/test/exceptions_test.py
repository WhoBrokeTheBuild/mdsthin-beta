
import numpy
import unittest

from ..exceptions import *

class ExceptionsTest(unittest.TestCase):

    def test_status(self):

        self.assertTrue(STATUS_OK(TreeSUCCESS.status))
        self.assertFalse(STATUS_NOT_OK(TreeSUCCESS.status))
        
        self.assertTrue(STATUS_NOT_OK(DevCAMERA_NOT_FOUND.status))
        self.assertFalse(STATUS_OK(DevCAMERA_NOT_FOUND.status))

        self.assertEqual(STATUS_FACILITY(TreeNODATA.status), 4049)
        self.assertEqual(STATUS_MESSAGE(TreeNODATA.status), 4124)
        self.assertEqual(STATUS_SEVERITY(TreeNODATA.status), 2)

    def test_get_exception(self):

        self.assertEqual(getException(65545), MDSplusSUCCESS)

        self.assertEqual(getException(265388200), TreeNOT_OPEN)

        unknown_exception = getException(1234) 
        self.assertEqual(type(unknown_exception), MdsException)
        self.assertEqual(str(unknown_exception), 'Unknown status: 1234')

    def test_get_exception_from_error(self):
        
        self.assertEqual(getExceptionFromError("%TREE-W-NOT_OPEN, Tree not currently open"), TreeNOT_OPEN)
        
        self.assertEqual(getExceptionFromError("%TREE-W-NOT_OPEN, This part doesn't matter"), TreeNOT_OPEN)
        
        unknown_exception = getExceptionFromError("This part definitely matters")
        self.assertEqual(type(unknown_exception), MdsException)
        self.assertEqual(str(unknown_exception), 'This part definitely matters')
