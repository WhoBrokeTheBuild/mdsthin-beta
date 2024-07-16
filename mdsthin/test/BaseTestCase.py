
import unittest

class BaseTestCase(unittest.TestCase):

    ASSERTION_COUNT = 0

    def assertEqual(self, first, second, msg=None):
        BaseTestCase.ASSERTION_COUNT += 1
        return unittest.TestCase.assertEqual(self, first, second, msg=msg)

    def assertTrue(self, expr, msg=None):
        BaseTestCase.ASSERTION_COUNT += 1
        return unittest.TestCase.assertTrue(self, expr, msg=msg)

    def assertAlmostEqual(self, first, second, places=None, msg=None, delta=None):
        BaseTestCase.ASSERTION_COUNT += 1
        return unittest.TestCase.assertAlmostEqual(self, first, second=second, places=places, msg=msg, delta=delta)

    def assertRaises(self, expected_exception, callable, *args):
        BaseTestCase.ASSERTION_COUNT += 1
        return unittest.TestCase.assertRaises(self, expected_exception, callable, *args)

    # def assertAllEqual(self, first, second, msg = None):
    #     comparison = first == second
    #     self.assertTrue(all(comparison.flatten()), msg=msg)
    