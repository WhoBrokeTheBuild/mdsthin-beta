
import ctypes

from .dtypedef import *
from .classdef import *

###
### mdsdsc_t
###

class mdsdsc_t(ctypes.LittleEndianStructure):
    """
    Descriptor base class
    """

    _pack_ = 1
    _fields_ = [
        ('length', ctypes.c_uint16),
        ('dtype_id', dtype_t),
        ('class_id', class_t),
        ('offset', ctypes.c_uint32), # pointer
    ]

    @property
    def class_str(self):
        return class_to_string(self.class_id)
    
    @property
    def dtype_str(self):
        return dtype_to_string(self.dtype_id)

###
### mdsdsc_s_t
###

class mdsdsc_s_t(mdsdsc_t):
    """
    Static fixed-length descriptor (CLASS_S)
    """

###
### mdsdsc_d_t
###

class mdsdsc_d_t(mdsdsc_t):
    """
    Dynamic string descriptor (CLASS_D)
    """

###
### mdsdsc_a_t
###

class aflags_t(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ('fill', ctypes.c_uint8, 3),
        ('binscale', ctypes.c_uint8, 1),
        ('redim', ctypes.c_uint8, 1),
        ('column', ctypes.c_uint8, 1),
        ('coeff', ctypes.c_uint8, 1),
        ('bounds', ctypes.c_uint8, 1),
    ]

class mdsdsc_a_t(mdsdsc_t):
    """
    Array descriptor (CLASS_A, CLASS_CA, CLASS_APD)
    """

    _pack_ = 1
    _fields_ = [
        ('scale', ctypes.c_int8),
        ('digits', ctypes.c_uint8),
        ('aflags', aflags_t),
        ('dimct', ctypes.c_uint8),
        ('arsize', ctypes.c_uint32),
    ]

###
### mdsdsc_r_t
###

class mdsdsc_r_t(mdsdsc_t):
    """
    Record descriptor (CLASS_R)
    """
    
    _pack_ = 1
    _fields_ = [
        ('ndesc', ctypes.c_uint32, 8),
        ('fill', ctypes.c_uint32, 24),
    ]
