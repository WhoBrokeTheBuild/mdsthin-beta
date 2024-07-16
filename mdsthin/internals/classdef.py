
import ctypes

###
### class_t
###

class_t = ctypes.c_ubyte

CLASS_MISSING = 0
"""Invalid class"""

CLASS_S = 1
"""`S`tatic fixed-length descriptor"""

CLASS_D = 2
"""`D`ynamic string descriptor"""

CLASS_V = 3
"""(deprecated) VMS `V`ariable buffer descriptor"""

CLASS_A = 4
"""`A`rray descriptor"""

CLASS_P = 5
"""(deprecated?) Procedure descriptor"""

CLASS_PI = 6
"""(deprecated?) Procedure incarnation descriptor"""

CLASS_J = 7
"""(deprecated) VMS debugger label descriptor"""

CLASS_JI = 8
"""(deprecated) VMS debugger label incarnation descriptor"""

CLASS_SD = 9
"""(deprecated?) Decimal string descriptor"""

CLASS_NCA = 10
"""(deprecated?) `N`on`c`ontiguous `A`rray descriptor"""

CLASS_VS = 11
"""(deprecated?) `V`arying `S`tring descriptor"""

CLASS_VSA = 12
"""(deprecated?) `V`arying `S`tring `A`rray descriptor"""

CLASS_UBS = 13
"""(deprecated?) `U`naligned `B`it `S`tring descriptor"""

CLASS_UBA = 14
"""(deprecated?) `U`naligned `B`it `A`rray descriptor"""

CLASS_SB = 15
"""(deprecated?) `S`tring with `B`ounds descriptor"""

CLASS_UBSB = 16
"""(deprecated?) `U`naligned `B`it `S`tring with `B`ounds descriptor"""

CLASS_XD = 192
"""E`x`tended `D`ynamic descriptor"""

CLASS_XS = 193
"""E`x`tended `S`tatic descriptor"""

CLASS_R = 194
"""`R`ecord descriptor"""

CLASS_CA = 195
"""`C`ompressed `A`rray descriptor"""

CLASS_APD = 196
"""`A`rray of `P`ointers to `D`ata descriptor"""

ARRAY_CLASSES = [
    CLASS_A,
    CLASS_CA,
    CLASS_APD,
]

def class_is_array(class_id) -> bool:
    if type(class_id) is class_t:
        class_id = class_id.value

    return class_id in ARRAY_CLASSES

def class_to_string(class_id) -> str:
    VALUES = {
        CLASS_MISSING: 'CLASS_MISSING',
        CLASS_S: 'CLASS_S',
        CLASS_D: 'CLASS_D',
        CLASS_V: 'CLASS_V',
        CLASS_A: 'CLASS_A',
        CLASS_P: 'CLASS_P',
        CLASS_PI: 'CLASS_PI',
        CLASS_J: 'CLASS_J',
        CLASS_JI: 'CLASS_JI',
        CLASS_SD: 'CLASS_SD',
        CLASS_NCA: 'CLASS_NCA',
        CLASS_VS: 'CLASS_VS',
        CLASS_VSA: 'CLASS_VSA',
        CLASS_UBS: 'CLASS_UBS',
        CLASS_UBA: 'CLASS_UBA',
        CLASS_SB: 'CLASS_SB',
        CLASS_UBSB: 'CLASS_UBSB',
        CLASS_XD: 'CLASS_XD',
        CLASS_XS: 'CLASS_XS',
        CLASS_R: 'CLASS_R',
        CLASS_CA: 'CLASS_CA',
        CLASS_APD: 'CLASS_APD',
    }

    if type(class_id) is class_t:
        class_id = class_id.value

    if class_id in VALUES:
        return VALUES[class_id]

    return f'CLASS_UNKNOWN({class_id})'
