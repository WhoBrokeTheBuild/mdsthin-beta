
import atexit
import unittest

from . import *

def run_mdsthin_tests(server=None, cmod_tests=False, **kwargs):
        
    if server is not None:
        ConnectionTest.SERVER = server

        if cmod_tests:
            CModTest.SERVER = server
            
    unittest.main(**kwargs)
    