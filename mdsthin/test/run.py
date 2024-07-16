
import atexit
import unittest

from . import *
from .BaseTestCase import BaseTestCase

def print_assertion_count():
    print(BaseTestCase.ASSERTION_COUNT, 'assertions')

def run_mdsthin_tests(server=None, cmod_tests=False, **kwargs):
        
    atexit.register(print_assertion_count)

    if server is not None:
        ConnectionTest.SERVER = server

        if cmod_tests:
            CModTest.SERVER = server
            
    unittest.main(**kwargs)
    