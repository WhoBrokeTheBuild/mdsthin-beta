
OPCODE_MAP = {
    '$': 0,
    '$A0': 1,
    '$ALPHA': 2,
    '$AMU': 3,
    '$C': 4,
    '$CAL': 5,
    '$DEGREE': 6,
    '$EV': 7,
    '$FALSE': 8,
    '$FARADAY': 9,
    '$G': 10,
    '$GAS': 11,
    '$H': 12,
    '$HBAR': 13,
    '$I': 14,
    '$K': 15,
    '$ME': 16,
    '$MISSING': 17,
    '$MP': 18,
    '$N0': 19,
    '$NA': 20,
    '$P0': 21,
    '$PI': 22,
    '$QE': 23,
    '$RE': 24,
    '$ROPRAND': 25,
    '$RYDBERG': 26,
    '$T0': 27,
    '$TORR': 28,
    '$TRUE': 29,
    '$VALUE': 30,
    'ABORT': 31,
    'ABS': 32,
    'ABS1': 33,
    'ABSSQ': 34,
    'ACHAR': 35,
    'ACOS': 36,
    'ACOSD': 37,
    'ADD': 38,
    'ADJUSTL': 39,
    'ADJUSTR': 40,
    'AIMAG': 41,
    'AINT': 42,
    'ALL': 43,
    'ALLOCATED': 44,
    'AND': 45,
    'AND_NOT': 46,
    'ANINT': 47,
    'ANY': 48,
    'ARG': 49,
    'ARGD': 50,
    'ARG_OF': 51,
    'ARRAY': 52,
    'ASIN': 53,
    'ASIND': 54,
    'AS_IS': 55,
    'ATAN': 56,
    'ATAN2': 57,
    'ATAN2D': 58,
    'ATAND': 59,
    'ATANH': 60,
    'AXIS_OF': 61,
    'BACKSPACE': 62,
    'IBCLR': 63,
    'BEGIN_OF': 64,
    'IBITS': 65,
    'BREAK': 66,
    'BSEARCH': 67,
    'IBSET': 68,
    'BTEST': 69,
    'BUILD_ACTION': 70,
    'BUILD_CONDITION': 71,
    'BUILD_CONGLOM': 72,
    'BUILD_DEPENDENCY': 73,
    'BUILD_DIM': 74,
    'BUILD_DISPATCH': 75,
    'BUILD_EVENT': 76,
    'BUILD_FUNCTION': 77,
    'BUILD_METHOD': 78,
    'BUILD_PARAM': 79,
    'BUILD_PATH': 80,
    'BUILD_PROCEDURE': 81,
    'BUILD_PROGRAM': 82,
    'BUILD_RANGE': 83,
    'BUILD_ROUTINE': 84,
    'BUILD_SIGNAL': 85,
    'BUILD_SLOPE': 86,
    'BUILD_WINDOW': 87,
    'BUILD_WITH_UNITS': 88,
    'BUILTIN_OPCODE': 89,
    'BYTE': 90,
    'BYTE_UNSIGNED': 91,
    'CASE': 92,
    'CEILING': 93,
    'CHAR': 94,
    'CLASS': 95,
    'FCLOSE': 96,
    'CMPLX': 97,
    'COMMA': 98,
    'COMPILE': 99,
    'COMPLETION_OF': 100,
    'CONCAT': 101,
    'CONDITIONAL': 102,
    'CONJG': 103,
    'CONTINUE': 104,
    'CONVOLVE': 105,
    'COS': 106,
    'COSD': 107,
    'COSH': 108,
    'COUNT': 109,
    'CSHIFT': 110,
    'CVT': 111,
    'DATA': 112,
    'DATE_AND_TIME': 113,
    'DATE_TIME': 114,
    'DBLE': 115,
    'DEALLOCATE': 116,
    'DEBUG': 117,
    'DECODE': 118,
    'DECOMPILE': 119,
    'DECOMPRESS': 120,
    'DEFAULT': 121,
    'DERIVATIVE': 122,
    'DESCR': 123,
    'DIAGONAL': 124,
    'DIGITS': 125,
    'DIM': 126,
    'DIM_OF': 127,
    'DISPATCH_OF': 128,
    'DIVIDE': 129,
    'LBOUND': 130,
    'DO': 131,
    'DOT_PRODUCT': 132,
    'DPROD': 133,
    'DSCPTR': 134,
    'SHAPE': 135,
    'SIZE': 136,
    'KIND': 137,
    'UBOUND': 138,
    'D_COMPLEX': 139,
    'D_FLOAT': 140,
    'RANGE': 141,
    'PRECISION': 142,
    'ELBOUND': 143,
    'ELSE': 144,
    'ELSEWHERE': 145,
    'ENCODE': 146,
    'ENDFILE': 147,
    'END_OF': 148,
    'EOSHIFT': 149,
    'EPSILON': 150,
    'EQ': 151,
    'EQUALS': 152,
    'EQUALS_FIRST': 153,
    'EQV': 154,
    'ESHAPE': 155,
    'ESIZE': 156,
    'EUBOUND': 157,
    'EVALUATE': 158,
    'EXECUTE': 159,
    'EXP': 160,
    'EXPONENT': 161,
    'EXT_FUNCTION': 162,
    'FFT': 163,
    'FIRSTLOC': 164,
    'FIT': 165,
    'FIX_ROPRAND': 166,
    'FLOAT': 167,
    'FLOOR': 168,
    'FOR': 169,
    'FRACTION': 170,
    'FUN': 171,
    'F_COMPLEX': 172,
    'F_FLOAT': 173,
    'GE': 174,
    'GETNCI': 175,
    'GOTO': 176,
    'GT': 177,
    'G_COMPLEX': 178,
    'G_FLOAT': 179,
    'HELP_OF': 180,
    'HUGE': 181,
    'H_COMPLEX': 182,
    'H_FLOAT': 183,
    'IACHAR': 184,
    'IAND': 185,
    'IAND_NOT': 186,
    'ICHAR': 187,
    'IDENT_OF': 188,
    'IF': 189,
    'IF_ERROR': 190,
    'IMAGE_OF': 191,
    'IN': 192,
    'INAND': 193,
    'INAND_NOT': 194,
    'INDEX': 195,
    'INOR': 196,
    'INOR_NOT': 197,
    'INOT': 198,
    'INOUT': 199,
    'INQUIRE': 200,
    'INT': 201,
    'INTEGRAL': 202,
    'INTERPOL': 203,
    'INTERSECT': 204,
    'INT_UNSIGNED': 205,
    'INVERSE': 206,
    'IOR': 207,
    'IOR_NOT': 208,
    'IS_IN': 209,
    'IEOR': 210,
    'IEOR_NOT': 211,
    'LABEL': 212,
    'LAMINATE': 213,
    'LANGUAGE_OF': 214,
    'LASTLOC': 215,
    'LE': 216,
    'LEN': 217,
    'LEN_TRIM': 218,
    'LGE': 219,
    'LGT': 220,
    'LLE': 221,
    'LLT': 222,
    'LOG': 223,
    'LOG10': 224,
    'LOG2': 225,
    'LOGICAL': 226,
    'LONG': 227,
    'LONG_UNSIGNED': 228,
    'LT': 229,
    'MATMUL': 230,
    'MAT_ROT': 231,
    'MAT_ROT_INT': 232,
    'MAX': 233,
    'MAXEXPONENT': 234,
    'MAXLOC': 235,
    'MAXVAL': 236,
    'MEAN': 237,
    'MEDIAN': 238,
    'MERGE': 239,
    'METHOD_OF': 240,
    'MIN': 241,
    'MINEXPONENT': 242,
    'MINLOC': 243,
    'MINVAL': 244,
    'MOD': 245,
    'MODEL_OF': 246,
    'MULTIPLY': 247,
    'NAME_OF': 248,
    'NAND': 249,
    'NAND_NOT': 250,
    'NDESC': 251,
    'NE': 252,
    'NEAREST': 253,
    'NEQV': 254,
    'NINT': 255,
    'NOR': 256,
    'NOR_NOT': 257,
    'NOT': 258,
    'OBJECT_OF': 259,
    'OCTAWORD': 260,
    'OCTAWORD_UNSIGNED': 261,
    'ON_ERROR': 262,
    'OPCODE_BUILTIN': 263,
    'OPCODE_STRING': 264,
    'FOPEN': 265,
    'OPTIONAL': 266,
    'OR': 267,
    'OR_NOT': 268,
    'OUT': 269,
    'PACK': 270,
    'PHASE_OF': 271,
    'POST_DEC': 272,
    'POST_INC': 273,
    'POWER': 274,
    'PRESENT': 275,
    'PRE_DEC': 276,
    'PRE_INC': 277,
    'PRIVATE': 278,
    'PROCEDURE_OF': 279,
    'PRODUCT': 280,
    'PROGRAM_OF': 281,
    'PROJECT': 282,
    'PROMOTE': 283,
    'PUBLIC': 284,
    'QUADWORD': 285,
    'QUADWORD_UNSIGNED': 286,
    'QUALIFIERS_OF': 287,
    'RADIX': 288,
    'RAMP': 289,
    'RANDOM': 290,
    'RANDOM_SEED': 291,
    'DTYPE_RANGE': 292,
    'RANK': 293,
    'RAW_OF': 294,
    'READ': 295,
    'REAL': 296,
    'REBIN': 297,
    'REF': 298,
    'REPEAT': 299,
    'REPLICATE': 300,
    'RESHAPE': 301,
    'RETURN': 302,
    'REWIND': 303,
    'RMS': 304,
    'ROUTINE_OF': 305,
    'RRSPACING': 306,
    'SCALE': 307,
    'SCAN': 308,
    'FSEEK': 309,
    'SET_EXPONENT': 310,
    'SET_RANGE': 311,
    'ISHFT': 312,
    'ISHFTC': 313,
    'SHIFT_LEFT': 314,
    'SHIFT_RIGHT': 315,
    'SIGN': 316,
    'SIGNED': 317,
    'SIN': 318,
    'SIND': 319,
    'SINH': 320,
    'SIZEOF': 321,
    'SLOPE_OF': 322,
    'SMOOTH': 323,
    'SOLVE': 324,
    'SORTVAL': 325,
    'SPACING': 326,
    'SPAWN': 327,
    'SPREAD': 328,
    'SQRT': 329,
    'SQUARE': 330,
    'STATEMENT': 331,
    'STD_DEV': 332,
    'STRING': 333,
    'STRING_OPCODE': 334,
    'SUBSCRIPT': 335,
    'SUBTRACT': 336,
    'SUM': 337,
    'SWITCH': 338,
    'SYSTEM_CLOCK': 339,
    'TAN': 340,
    'TAND': 341,
    'TANH': 342,
    'TASK_OF': 343,
    'TEXT': 344,
    'TIME_OUT_OF': 345,
    'TINY': 346,
    'TRANSFER': 347,
    'TRANSPOSE_': 348,
    'TRIM': 349,
    'UNARY_MINUS': 350,
    'UNARY_PLUS': 351,
    'UNION': 352,
    'UNITS': 353,
    'UNITS_OF': 354,
    'UNPACK': 355,
    'UNSIGNED': 356,
    'VAL': 357,
    'VALIDATION_OF': 358,
    'VALUE_OF': 359,
    'VAR': 360,
    'VECTOR': 361,
    'VERIFY': 362,
    'WAIT': 363,
    'WHEN_OF': 364,
    'WHERE': 365,
    'WHILE': 366,
    'WINDOW_OF': 367,
    'WORD': 368,
    'WORD_UNSIGNED': 369,
    'WRITE': 370,
    'ZERO': 371,
    '$2PI': 372,
    '$NARG': 373,
    'ELEMENT': 374,
    'RC_DROOP': 375,
    'RESET_PRIVATE': 376,
    'RESET_PUBLIC': 377,
    'SHOW_PRIVATE': 378,
    'SHOW_PUBLIC': 379,
    'SHOW_VM': 380,
    'TRANSLATE': 381,
    'TRANSPOSE_MUL': 382,
    'UPCASE': 383,
    'USING': 384,
    'VALIDATION': 385,
    '$DEFAULT': 386,
    '$EXPT': 387,
    '$SHOT': 388,
    'GETDBI': 389,
    'CULL': 390,
    'EXTEND': 391,
    'I_TO_X': 392,
    'X_TO_I': 393,
    'MAP': 394,
    'COMPILE_DEPENDENCY': 395,
    'DECOMPILE_DEPENDENCY': 396,
    'BUILD_CALL': 397,
    'ERRORLOGS_OF': 398,
    'PERFORMANCE_OF': 399,
    'XD': 400,
    'CONDITION_OF': 401,
    'SORT': 402,
    '$THIS': 403,
    'DATA_WITH_UNITS': 404,
    '$ATM': 405,
    '$EPSILON0': 406,
    '$GN': 407,
    '$MU0': 408,
    'EXTRACT': 409,
    'FINITE': 410,
    'BIT_SIZE': 411,
    'MODULO': 412,
    'SELECTED_INT_KIND': 413,
    'SELECTED_REAL_KIND': 414,
    'DSQL': 415,
    'ISQL': 416,
    'FTELL': 417,
    'MAKE_ACTION': 418,
    'MAKE_CONDITION': 419,
    'MAKE_CONGLOM': 420,
    'MAKE_DEPENDENCY': 421,
    'MAKE_DIM': 422,
    'MAKE_DISPATCH': 423,
    'MAKE_FUNCTION': 424,
    'MAKE_METHOD': 425,
    'MAKE_PARAM': 426,
    'MAKE_PROCEDURE': 427,
    'MAKE_PROGRAM': 428,
    'MAKE_RANGE': 429,
    'MAKE_ROUTINE': 430,
    'MAKE_SIGNAL': 431,
    'MAKE_WINDOW': 432,
    'MAKE_WITH_UNITS': 433,
    'MAKE_CALL': 434,
    'CLASS_OF': 435,
    'DSCPTR_OF': 436,
    'KIND_OF': 437,
    'NDESC_OF': 438,
    'ACCUMULATE': 439,
    'MAKE_SLOPE': 440,
    'REM': 441,
    'COMPLETION_MESSAGE_OF': 442,
    'INTERRUPT_OF': 443,
    '$SHOTNAME': 444,
    'BUILD_WITH_ERROR': 445,
    'ERROR_OF': 446,
    'MAKE_WITH_ERROR': 447,
    'DO_TASK': 448,
    'ISQL_SET': 449,
    'FS_FLOAT': 450,
    'FS_COMPLEX': 451,
    'FT_FLOAT': 452,
    'FT_COMPLEX': 453,
    'BUILD_OPAQUE': 454,
    'MAKE_OPAQUE': 455,
    'DICT': 456,
    'TUPLE': 457,
    'LIST': 458,
    'SQUEEZE': 459,
    'FLATTEN': 460,
}

OPCODE_REPR_MAP = {
    0: lambda: '$',
    1: lambda: '$A0',
    2: lambda: '$ALPHA',
    3: lambda: '$AMU',
    4: lambda: '$C',
    5: lambda: '$CAL',
    6: lambda: '$DEGREE',
    7: lambda: '$EV',
    8: lambda: '$FALSE',
    9: lambda: '$FARADAY',
    10: lambda: '$G',
    11: lambda: '$GAS',
    12: lambda: '$H',
    13: lambda: '$HBAR',
    14: lambda: '$I',
    15: lambda: '$K',
    16: lambda: '$ME',
    17: lambda: '$MISSING',
    18: lambda: '$MP',
    19: lambda: '$N0',
    20: lambda: '$NA',
    21: lambda: '$P0',
    22: lambda: '$PI',
    23: lambda: '$QE',
    24: lambda: '$RE',
    25: lambda: '$ROPRAND',
    26: lambda: '$RYDBERG',
    27: lambda: '$T0',
    28: lambda: '$TORR',
    29: lambda: '$TRUE',
    30: lambda: '$VALUE',
    31: lambda *args: f'ABORT({", ".join(map(repr, args))})',
    32: lambda *args: f'ABS({", ".join(map(repr, args))})',
    33: lambda *args: f'ABS1({", ".join(map(repr, args))})',
    34: lambda *args: f'ABSSQ({", ".join(map(repr, args))})',
    35: lambda *args: f'ACHAR({", ".join(map(repr, args))})',
    36: lambda *args: f'ACOS({", ".join(map(repr, args))})',
    37: lambda *args: f'ACOSD({", ".join(map(repr, args))})',
    38: lambda a,b: f"({repr(a)} + {repr(b)})",
    39: lambda *args: f'ADJUSTL({", ".join(map(repr, args))})',
    40: lambda *args: f'ADJUSTR({", ".join(map(repr, args))})',
    41: lambda *args: f'AIMAG({", ".join(map(repr, args))})',
    42: lambda *args: f'AINT({", ".join(map(repr, args))})',
    43: lambda *args: f'ALL({", ".join(map(repr, args))})',
    44: lambda *args: f'ALLOCATED({", ".join(map(repr, args))})',
    45: lambda *args: f'AND({", ".join(map(repr, args))})',
    46: lambda *args: f'AND_NOT({", ".join(map(repr, args))})',
    47: lambda *args: f'ANINT({", ".join(map(repr, args))})',
    48: lambda *args: f'ANY({", ".join(map(repr, args))})',
    49: lambda *args: f'ARG({", ".join(map(repr, args))})',
    50: lambda *args: f'ARGD({", ".join(map(repr, args))})',
    51: lambda *args: f'ARG_OF({", ".join(map(repr, args))})',
    52: lambda *args: f'ARRAY({", ".join(map(repr, args))})',
    53: lambda *args: f'ASIN({", ".join(map(repr, args))})',
    54: lambda *args: f'ASIND({", ".join(map(repr, args))})',
    55: lambda *args: f'AS_IS({", ".join(map(repr, args))})',
    56: lambda *args: f'ATAN({", ".join(map(repr, args))})',
    57: lambda *args: f'ATAN2({", ".join(map(repr, args))})',
    58: lambda *args: f'ATAN2D({", ".join(map(repr, args))})',
    59: lambda *args: f'ATAND({", ".join(map(repr, args))})',
    60: lambda *args: f'ATANH({", ".join(map(repr, args))})',
    61: lambda *args: f'AXIS_OF({", ".join(map(repr, args))})',
    62: lambda *args: f'BACKSPACE({", ".join(map(repr, args))})',
    63: lambda *args: f'IBCLR({", ".join(map(repr, args))})',
    64: lambda *args: f'BEGIN_OF({", ".join(map(repr, args))})',
    65: lambda *args: f'IBITS({", ".join(map(repr, args))})',
    66: lambda: 'BREAK',
    67: lambda *args: f'BSEARCH({", ".join(map(repr, args))})',
    68: lambda *args: f'IBSET({", ".join(map(repr, args))})',
    69: lambda *args: f'BTEST({", ".join(map(repr, args))})',
    70: lambda *args: f'BUILD_ACTION({", ".join(map(repr, args))})',
    71: lambda *args: f'BUILD_CONDITION({", ".join(map(repr, args))})',
    72: lambda *args: f'BUILD_CONGLOM({", ".join(map(repr, args))})',
    73: lambda *args: f'BUILD_DEPENDENCY({", ".join(map(repr, args))})',
    74: lambda *args: f'BUILD_DIM({", ".join(map(repr, args))})',
    75: lambda *args: f'BUILD_DISPATCH({", ".join(map(repr, args))})',
    76: lambda *args: f'BUILD_EVENT({", ".join(map(repr, args))})',
    77: lambda *args: f'BUILD_FUNCTION({", ".join(map(repr, args))})',
    78: lambda *args: f'BUILD_METHOD({", ".join(map(repr, args))})',
    79: lambda *args: f'BUILD_PARAM({", ".join(map(repr, args))})',
    80: lambda *args: f'BUILD_PATH({", ".join(map(repr, args))})',
    81: lambda *args: f'BUILD_PROCEDURE({", ".join(map(repr, args))})',
    82: lambda *args: f'BUILD_PROGRAM({", ".join(map(repr, args))})',
    83: lambda *args: f'BUILD_RANGE({", ".join(map(repr, args))})',
    84: lambda *args: f'BUILD_ROUTINE({", ".join(map(repr, args))})',
    85: lambda *args: f'BUILD_SIGNAL({", ".join(map(repr, args))})',
    86: lambda *args: f'BUILD_SLOPE({", ".join(map(repr, args))})',
    87: lambda *args: f'BUILD_WINDOW({", ".join(map(repr, args))})',
    88: lambda *args: f'BUILD_WITH_UNITS({", ".join(map(repr, args))})',
    89: lambda *args: f'BUILTIN_OPCODE({", ".join(map(repr, args))})',
    90: lambda *args: f'BYTE({", ".join(map(repr, args))})',
    91: lambda *args: f'BYTE_UNSIGNED({", ".join(map(repr, args))})',
    92: lambda *args: f'CASE({", ".join(map(repr, args))})',
    93: lambda *args: f'CEILING({", ".join(map(repr, args))})',
    94: lambda *args: f'CHAR({", ".join(map(repr, args))})',
    95: lambda *args: f'CLASS({", ".join(map(repr, args))})',
    96: lambda *args: f'FCLOSE({", ".join(map(repr, args))})',
    97: lambda *args: f'CMPLX({", ".join(map(repr, args))})',
    98: lambda *args: f'COMMA({", ".join(map(repr, args))})',
    99: lambda *args: f'COMPILE({", ".join(map(repr, args))})',
    100: lambda *args: f'COMPLETION_OF({", ".join(map(repr, args))})',
    101: lambda *args: f'CONCAT({", ".join(map(repr, args))})',
    102: lambda *args: f'CONDITIONAL({", ".join(map(repr, args))})',
    103: lambda *args: f'CONJG({", ".join(map(repr, args))})',
    104: lambda: 'CONTINUE',
    105: lambda *args: f'CONVOLVE({", ".join(map(repr, args))})',
    106: lambda *args: f'COS({", ".join(map(repr, args))})',
    107: lambda *args: f'COSD({", ".join(map(repr, args))})',
    108: lambda *args: f'COSH({", ".join(map(repr, args))})',
    109: lambda *args: f'COUNT({", ".join(map(repr, args))})',
    110: lambda *args: f'CSHIFT({", ".join(map(repr, args))})',
    111: lambda *args: f'CVT({", ".join(map(repr, args))})',
    112: lambda *args: f'DATA({", ".join(map(repr, args))})',
    113: lambda *args: f'DATE_AND_TIME({", ".join(map(repr, args))})',
    114: lambda *args: f'DATE_TIME({", ".join(map(repr, args))})',
    115: lambda *args: f'DBLE({", ".join(map(repr, args))})',
    116: lambda *args: f'DEALLOCATE({", ".join(map(repr, args))})',
    117: lambda *args: f'DEBUG({", ".join(map(repr, args))})',
    118: lambda *args: f'DECODE({", ".join(map(repr, args))})',
    119: lambda *args: f'DECOMPILE({", ".join(map(repr, args))})',
    120: lambda *args: f'DECOMPRESS({", ".join(map(repr, args))})',
    121: lambda *args: f'DEFAULT({", ".join(map(repr, args))})',
    122: lambda *args: f'DERIVATIVE({", ".join(map(repr, args))})',
    123: lambda *args: f'DESCR({", ".join(map(repr, args))})',
    124: lambda *args: f'DIAGONAL({", ".join(map(repr, args))})',
    125: lambda *args: f'DIGITS({", ".join(map(repr, args))})',
    126: lambda *args: f'DIM({", ".join(map(repr, args))})',
    127: lambda *args: f'DIM_OF({", ".join(map(repr, args))})',
    128: lambda *args: f'DISPATCH_OF({", ".join(map(repr, args))})',
    129: lambda a,b: f"({repr(a)} / {repr(b)})",
    130: lambda *args: f'LBOUND({", ".join(map(repr, args))})',
    131: lambda *args: f'DO({", ".join(map(repr, args))})',
    132: lambda *args: f'DOT_PRODUCT({", ".join(map(repr, args))})',
    133: lambda *args: f'DPROD({", ".join(map(repr, args))})',
    134: lambda *args: f'DSCPTR({", ".join(map(repr, args))})',
    135: lambda *args: f'SHAPE({", ".join(map(repr, args))})',
    136: lambda *args: f'SIZE({", ".join(map(repr, args))})',
    137: lambda *args: f'KIND({", ".join(map(repr, args))})',
    138: lambda *args: f'UBOUND({", ".join(map(repr, args))})',
    139: lambda *args: f'D_COMPLEX({", ".join(map(repr, args))})',
    140: lambda *args: f'D_FLOAT({", ".join(map(repr, args))})',
    141: lambda *args: f'RANGE({", ".join(map(repr, args))})',
    142: lambda *args: f'PRECISION({", ".join(map(repr, args))})',
    143: lambda *args: f'ELBOUND({", ".join(map(repr, args))})',
    144: lambda: 'ELSE',
    145: lambda: 'ELSEWHERE',
    146: lambda *args: f'ENCODE({", ".join(map(repr, args))})',
    147: lambda *args: f'ENDFILE({", ".join(map(repr, args))})',
    148: lambda *args: f'END_OF({", ".join(map(repr, args))})',
    149: lambda *args: f'EOSHIFT({", ".join(map(repr, args))})',
    150: lambda *args: f'EPSILON({", ".join(map(repr, args))})',
    151: lambda *args: f'EQ({", ".join(map(repr, args))})',
    152: lambda *args: f'EQUALS({", ".join(map(repr, args))})',
    153: lambda *args: f'EQUALS_FIRST({", ".join(map(repr, args))})',
    154: lambda *args: f'EQV({", ".join(map(repr, args))})',
    155: lambda *args: f'ESHAPE({", ".join(map(repr, args))})',
    156: lambda *args: f'ESIZE({", ".join(map(repr, args))})',
    157: lambda *args: f'EUBOUND({", ".join(map(repr, args))})',
    158: lambda *args: f'EVALUATE({", ".join(map(repr, args))})',
    159: lambda *args: f'EXECUTE({", ".join(map(repr, args))})',
    160: lambda *args: f'EXP({", ".join(map(repr, args))})',
    161: lambda *args: f'EXPONENT({", ".join(map(repr, args))})',
    162: lambda _,func,*args: f"{func.data()}({', '.join(map(repr, args))})",
    163: lambda *args: f'FFT({", ".join(map(repr, args))})',
    164: lambda *args: f'FIRSTLOC({", ".join(map(repr, args))})',
    165: lambda *args: f'FIT({", ".join(map(repr, args))})',
    166: lambda *args: f'FIX_ROPRAND({", ".join(map(repr, args))})',
    167: lambda *args: f'FLOAT({", ".join(map(repr, args))})',
    168: lambda *args: f'FLOOR({", ".join(map(repr, args))})',
    169: lambda *args: f'FOR({", ".join(map(repr, args))})',
    170: lambda *args: f'FRACTION({", ".join(map(repr, args))})',
    171: lambda *args: f'FUN({", ".join(map(repr, args))})',
    172: lambda *args: f'F_COMPLEX({", ".join(map(repr, args))})',
    173: lambda *args: f'F_FLOAT({", ".join(map(repr, args))})',
    174: lambda *args: f'GE({", ".join(map(repr, args))})',
    175: lambda *args: f'GETNCI({", ".join(map(repr, args))})',
    176: lambda *args: f'GOTO({", ".join(map(repr, args))})',
    177: lambda *args: f'GT({", ".join(map(repr, args))})',
    178: lambda *args: f'G_COMPLEX({", ".join(map(repr, args))})',
    179: lambda *args: f'G_FLOAT({", ".join(map(repr, args))})',
    180: lambda *args: f'HELP_OF({", ".join(map(repr, args))})',
    181: lambda *args: f'HUGE({", ".join(map(repr, args))})',
    182: lambda *args: f'H_COMPLEX({", ".join(map(repr, args))})',
    183: lambda *args: f'H_FLOAT({", ".join(map(repr, args))})',
    184: lambda *args: f'IACHAR({", ".join(map(repr, args))})',
    185: lambda *args: f'IAND({", ".join(map(repr, args))})',
    186: lambda *args: f'IAND_NOT({", ".join(map(repr, args))})',
    187: lambda *args: f'ICHAR({", ".join(map(repr, args))})',
    188: lambda *args: f'IDENT_OF({", ".join(map(repr, args))})',
    189: lambda *args: f'IF({", ".join(map(repr, args))})',
    190: lambda *args: f'IF_ERROR({", ".join(map(repr, args))})',
    191: lambda *args: f'IMAGE_OF({", ".join(map(repr, args))})',
    192: lambda *args: f'IN({", ".join(map(repr, args))})',
    193: lambda *args: f'INAND({", ".join(map(repr, args))})',
    194: lambda *args: f'INAND_NOT({", ".join(map(repr, args))})',
    195: lambda *args: f'INDEX({", ".join(map(repr, args))})',
    196: lambda *args: f'INOR({", ".join(map(repr, args))})',
    197: lambda *args: f'INOR_NOT({", ".join(map(repr, args))})',
    198: lambda *args: f'INOT({", ".join(map(repr, args))})',
    199: lambda *args: f'INOUT({", ".join(map(repr, args))})',
    200: lambda *args: f'INQUIRE({", ".join(map(repr, args))})',
    201: lambda *args: f'INT({", ".join(map(repr, args))})',
    202: lambda *args: f'INTEGRAL({", ".join(map(repr, args))})',
    203: lambda *args: f'INTERPOL({", ".join(map(repr, args))})',
    204: lambda *args: f'INTERSECT({", ".join(map(repr, args))})',
    205: lambda *args: f'INT_UNSIGNED({", ".join(map(repr, args))})',
    206: lambda *args: f'INVERSE({", ".join(map(repr, args))})',
    207: lambda *args: f'IOR({", ".join(map(repr, args))})',
    208: lambda *args: f'IOR_NOT({", ".join(map(repr, args))})',
    209: lambda *args: f'IS_IN({", ".join(map(repr, args))})',
    210: lambda *args: f'IEOR({", ".join(map(repr, args))})',
    211: lambda *args: f'IEOR_NOT({", ".join(map(repr, args))})',
    212: lambda *args: f'LABEL({", ".join(map(repr, args))})',
    213: lambda *args: f'LAMINATE({", ".join(map(repr, args))})',
    214: lambda *args: f'LANGUAGE_OF({", ".join(map(repr, args))})',
    215: lambda *args: f'LASTLOC({", ".join(map(repr, args))})',
    216: lambda *args: f'LE({", ".join(map(repr, args))})',
    217: lambda *args: f'LEN({", ".join(map(repr, args))})',
    218: lambda *args: f'LEN_TRIM({", ".join(map(repr, args))})',
    219: lambda *args: f'LGE({", ".join(map(repr, args))})',
    220: lambda *args: f'LGT({", ".join(map(repr, args))})',
    221: lambda *args: f'LLE({", ".join(map(repr, args))})',
    222: lambda *args: f'LLT({", ".join(map(repr, args))})',
    223: lambda *args: f'LOG({", ".join(map(repr, args))})',
    224: lambda *args: f'LOG10({", ".join(map(repr, args))})',
    225: lambda *args: f'LOG2({", ".join(map(repr, args))})',
    226: lambda *args: f'LOGICAL({", ".join(map(repr, args))})',
    227: lambda *args: f'LONG({", ".join(map(repr, args))})',
    228: lambda *args: f'LONG_UNSIGNED({", ".join(map(repr, args))})',
    229: lambda *args: f'LT({", ".join(map(repr, args))})',
    230: lambda *args: f'MATMUL({", ".join(map(repr, args))})',
    231: lambda *args: f'MAT_ROT({", ".join(map(repr, args))})',
    232: lambda *args: f'MAT_ROT_INT({", ".join(map(repr, args))})',
    233: lambda *args: f'MAX({", ".join(map(repr, args))})',
    234: lambda *args: f'MAXEXPONENT({", ".join(map(repr, args))})',
    235: lambda *args: f'MAXLOC({", ".join(map(repr, args))})',
    236: lambda *args: f'MAXVAL({", ".join(map(repr, args))})',
    237: lambda *args: f'MEAN({", ".join(map(repr, args))})',
    238: lambda *args: f'MEDIAN({", ".join(map(repr, args))})',
    239: lambda *args: f'MERGE({", ".join(map(repr, args))})',
    240: lambda *args: f'METHOD_OF({", ".join(map(repr, args))})',
    241: lambda *args: f'MIN({", ".join(map(repr, args))})',
    242: lambda *args: f'MINEXPONENT({", ".join(map(repr, args))})',
    243: lambda *args: f'MINLOC({", ".join(map(repr, args))})',
    244: lambda *args: f'MINVAL({", ".join(map(repr, args))})',
    245: lambda *args: f'MOD({", ".join(map(repr, args))})',
    246: lambda *args: f'MODEL_OF({", ".join(map(repr, args))})',
    247: lambda a,b: f"({repr(a)} * {repr(b)})",
    248: lambda *args: f'NAME_OF({", ".join(map(repr, args))})',
    249: lambda *args: f'NAND({", ".join(map(repr, args))})',
    250: lambda *args: f'NAND_NOT({", ".join(map(repr, args))})',
    251: lambda *args: f'NDESC({", ".join(map(repr, args))})',
    252: lambda *args: f'NE({", ".join(map(repr, args))})',
    253: lambda *args: f'NEAREST({", ".join(map(repr, args))})',
    254: lambda *args: f'NEQV({", ".join(map(repr, args))})',
    255: lambda *args: f'NINT({", ".join(map(repr, args))})',
    256: lambda *args: f'NOR({", ".join(map(repr, args))})',
    257: lambda *args: f'NOR_NOT({", ".join(map(repr, args))})',
    258: lambda *args: f'NOT({", ".join(map(repr, args))})',
    259: lambda *args: f'OBJECT_OF({", ".join(map(repr, args))})',
    260: lambda *args: f'OCTAWORD({", ".join(map(repr, args))})',
    261: lambda *args: f'OCTAWORD_UNSIGNED({", ".join(map(repr, args))})',
    262: lambda *args: f'ON_ERROR({", ".join(map(repr, args))})',
    263: lambda *args: f'OPCODE_BUILTIN({", ".join(map(repr, args))})',
    264: lambda *args: f'OPCODE_STRING({", ".join(map(repr, args))})',
    265: lambda *args: f'FOPEN({", ".join(map(repr, args))})',
    266: lambda *args: f'OPTIONAL({", ".join(map(repr, args))})',
    267: lambda *args: f'OR({", ".join(map(repr, args))})',
    268: lambda *args: f'OR_NOT({", ".join(map(repr, args))})',
    269: lambda *args: f'OUT({", ".join(map(repr, args))})',
    270: lambda *args: f'PACK({", ".join(map(repr, args))})',
    271: lambda *args: f'PHASE_OF({", ".join(map(repr, args))})',
    272: lambda *args: f'POST_DEC({", ".join(map(repr, args))})',
    273: lambda *args: f'POST_INC({", ".join(map(repr, args))})',
    274: lambda *args: f'POWER({", ".join(map(repr, args))})',
    275: lambda *args: f'PRESENT({", ".join(map(repr, args))})',
    276: lambda *args: f'PRE_DEC({", ".join(map(repr, args))})',
    277: lambda *args: f'PRE_INC({", ".join(map(repr, args))})',
    278: lambda *args: f'PRIVATE({", ".join(map(repr, args))})',
    279: lambda *args: f'PROCEDURE_OF({", ".join(map(repr, args))})',
    280: lambda *args: f'PRODUCT({", ".join(map(repr, args))})',
    281: lambda *args: f'PROGRAM_OF({", ".join(map(repr, args))})',
    282: lambda *args: f'PROJECT({", ".join(map(repr, args))})',
    283: lambda *args: f'PROMOTE({", ".join(map(repr, args))})',
    284: lambda *args: f'PUBLIC({", ".join(map(repr, args))})',
    285: lambda *args: f'QUADWORD({", ".join(map(repr, args))})',
    286: lambda *args: f'QUADWORD_UNSIGNED({", ".join(map(repr, args))})',
    287: lambda *args: f'QUALIFIERS_OF({", ".join(map(repr, args))})',
    288: lambda *args: f'RADIX({", ".join(map(repr, args))})',
    289: lambda *args: f'RAMP({", ".join(map(repr, args))})',
    290: lambda *args: f'RANDOM({", ".join(map(repr, args))})',
    291: lambda *args: f'RANDOM_SEED({", ".join(map(repr, args))})',
    292: lambda *args: f'DTYPE_RANGE({", ".join(map(repr, args))})',
    293: lambda *args: f'RANK({", ".join(map(repr, args))})',
    294: lambda *args: f'RAW_OF({", ".join(map(repr, args))})',
    295: lambda *args: f'READ({", ".join(map(repr, args))})',
    296: lambda *args: f'REAL({", ".join(map(repr, args))})',
    297: lambda *args: f'REBIN({", ".join(map(repr, args))})',
    298: lambda *args: f'REF({", ".join(map(repr, args))})',
    299: lambda *args: f'REPEAT({", ".join(map(repr, args))})',
    300: lambda *args: f'REPLICATE({", ".join(map(repr, args))})',
    301: lambda *args: f'RESHAPE({", ".join(map(repr, args))})',
    302: lambda *args: f'RETURN({", ".join(map(repr, args))})',
    303: lambda *args: f'REWIND({", ".join(map(repr, args))})',
    304: lambda *args: f'RMS({", ".join(map(repr, args))})',
    305: lambda *args: f'ROUTINE_OF({", ".join(map(repr, args))})',
    306: lambda *args: f'RRSPACING({", ".join(map(repr, args))})',
    307: lambda *args: f'SCALE({", ".join(map(repr, args))})',
    308: lambda *args: f'SCAN({", ".join(map(repr, args))})',
    309: lambda *args: f'FSEEK({", ".join(map(repr, args))})',
    310: lambda *args: f'SET_EXPONENT({", ".join(map(repr, args))})',
    311: lambda *args: f'SET_RANGE({", ".join(map(repr, args))})',
    312: lambda *args: f'ISHFT({", ".join(map(repr, args))})',
    313: lambda *args: f'ISHFTC({", ".join(map(repr, args))})',
    314: lambda a,b: f"({repr(a)} << {repr(b)})",
    315: lambda a,b: f"({repr(a)} >> {repr(b)})",
    316: lambda *args: f'SIGN({", ".join(map(repr, args))})',
    317: lambda *args: f'SIGNED({", ".join(map(repr, args))})',
    318: lambda *args: f'SIN({", ".join(map(repr, args))})',
    319: lambda *args: f'SIND({", ".join(map(repr, args))})',
    320: lambda *args: f'SINH({", ".join(map(repr, args))})',
    321: lambda *args: f'SIZEOF({", ".join(map(repr, args))})',
    322: lambda *args: f'SLOPE_OF({", ".join(map(repr, args))})',
    323: lambda *args: f'SMOOTH({", ".join(map(repr, args))})',
    324: lambda *args: f'SOLVE({", ".join(map(repr, args))})',
    325: lambda *args: f'SORTVAL({", ".join(map(repr, args))})',
    326: lambda *args: f'SPACING({", ".join(map(repr, args))})',
    327: lambda *args: f'SPAWN({", ".join(map(repr, args))})',
    328: lambda *args: f'SPREAD({", ".join(map(repr, args))})',
    329: lambda *args: f'SQRT({", ".join(map(repr, args))})',
    330: lambda *args: f'SQUARE({", ".join(map(repr, args))})',
    331: lambda *args: f'STATEMENT({", ".join(map(repr, args))})',
    332: lambda *args: f'STD_DEV({", ".join(map(repr, args))})',
    333: lambda *args: f'STRING({", ".join(map(repr, args))})',
    334: lambda *args: f'STRING_OPCODE({", ".join(map(repr, args))})',
    335: lambda *args: f'SUBSCRIPT({", ".join(map(repr, args))})',
    336: lambda a,b: f"({repr(a)} - {repr(b)})",
    337: lambda *args: f'SUM({", ".join(map(repr, args))})',
    338: lambda *args: f'SWITCH({", ".join(map(repr, args))})',
    339: lambda *args: f'SYSTEM_CLOCK({", ".join(map(repr, args))})',
    340: lambda *args: f'TAN({", ".join(map(repr, args))})',
    341: lambda *args: f'TAND({", ".join(map(repr, args))})',
    342: lambda *args: f'TANH({", ".join(map(repr, args))})',
    343: lambda *args: f'TASK_OF({", ".join(map(repr, args))})',
    344: lambda *args: f'TEXT({", ".join(map(repr, args))})',
    345: lambda *args: f'TIME_OUT_OF({", ".join(map(repr, args))})',
    346: lambda *args: f'TINY({", ".join(map(repr, args))})',
    347: lambda *args: f'TRANSFER({", ".join(map(repr, args))})',
    348: lambda *args: f'TRANSPOSE_({", ".join(map(repr, args))})',
    349: lambda *args: f'TRIM({", ".join(map(repr, args))})',
    350: lambda *args: f'UNARY_MINUS({", ".join(map(repr, args))})',
    351: lambda *args: f'UNARY_PLUS({", ".join(map(repr, args))})',
    352: lambda *args: f'UNION({", ".join(map(repr, args))})',
    353: lambda *args: f'UNITS({", ".join(map(repr, args))})',
    354: lambda *args: f'UNITS_OF({", ".join(map(repr, args))})',
    355: lambda *args: f'UNPACK({", ".join(map(repr, args))})',
    356: lambda *args: f'UNSIGNED({", ".join(map(repr, args))})',
    357: lambda *args: f'VAL({", ".join(map(repr, args))})',
    358: lambda *args: f'VALIDATION_OF({", ".join(map(repr, args))})',
    359: lambda *args: f'VALUE_OF({", ".join(map(repr, args))})',
    360: lambda *args: f'VAR({", ".join(map(repr, args))})',
    361: lambda *args: f'VECTOR({", ".join(map(repr, args))})',
    362: lambda *args: f'VERIFY({", ".join(map(repr, args))})',
    363: lambda *args: f'WAIT({", ".join(map(repr, args))})',
    364: lambda *args: f'WHEN_OF({", ".join(map(repr, args))})',
    365: lambda *args: f'WHERE({", ".join(map(repr, args))})',
    366: lambda *args: f'WHILE({", ".join(map(repr, args))})',
    367: lambda *args: f'WINDOW_OF({", ".join(map(repr, args))})',
    368: lambda *args: f'WORD({", ".join(map(repr, args))})',
    369: lambda *args: f'WORD_UNSIGNED({", ".join(map(repr, args))})',
    370: lambda *args: f'WRITE({", ".join(map(repr, args))})',
    371: lambda *args: f'ZERO({", ".join(map(repr, args))})',
    372: lambda: '$2PI',
    373: lambda: '$NARG',
    374: lambda *args: f'ELEMENT({", ".join(map(repr, args))})',
    375: lambda *args: f'RC_DROOP({", ".join(map(repr, args))})',
    376: lambda: 'RESET_PRIVATE',
    377: lambda: 'RESET_PUBLIC',
    378: lambda *args: f'SHOW_PRIVATE({", ".join(map(repr, args))})',
    379: lambda *args: f'SHOW_PUBLIC({", ".join(map(repr, args))})',
    380: lambda *args: f'SHOW_VM({", ".join(map(repr, args))})',
    381: lambda *args: f'TRANSLATE({", ".join(map(repr, args))})',
    382: lambda *args: f'TRANSPOSE_MUL({", ".join(map(repr, args))})',
    383: lambda *args: f'UPCASE({", ".join(map(repr, args))})',
    384: lambda *args: f'USING({", ".join(map(repr, args))})',
    385: lambda *args: f'VALIDATION({", ".join(map(repr, args))})',
    386: lambda: '$DEFAULT',
    387: lambda: '$EXPT',
    388: lambda: '$SHOT',
    389: lambda *args: f'GETDBI({", ".join(map(repr, args))})',
    390: lambda *args: f'CULL({", ".join(map(repr, args))})',
    391: lambda *args: f'EXTEND({", ".join(map(repr, args))})',
    392: lambda *args: f'I_TO_X({", ".join(map(repr, args))})',
    393: lambda *args: f'X_TO_I({", ".join(map(repr, args))})',
    394: lambda *args: f'MAP({", ".join(map(repr, args))})',
    395: lambda *args: f'COMPILE_DEPENDENCY({", ".join(map(repr, args))})',
    396: lambda *args: f'DECOMPILE_DEPENDENCY({", ".join(map(repr, args))})',
    397: lambda *args: f'BUILD_CALL({", ".join(map(repr, args))})',
    398: lambda *args: f'ERRORLOGS_OF({", ".join(map(repr, args))})',
    399: lambda *args: f'PERFORMANCE_OF({", ".join(map(repr, args))})',
    400: lambda *args: f'XD({", ".join(map(repr, args))})',
    401: lambda *args: f'CONDITION_OF({", ".join(map(repr, args))})',
    402: lambda *args: f'SORT({", ".join(map(repr, args))})',
    403: lambda: '$THIS',
    404: lambda *args: f'DATA_WITH_UNITS({", ".join(map(repr, args))})',
    405: lambda: '$ATM',
    406: lambda: '$EPSILON0',
    407: lambda: '$GN',
    408: lambda: '$MU0',
    409: lambda *args: f'EXTRACT({", ".join(map(repr, args))})',
    410: lambda *args: f'FINITE({", ".join(map(repr, args))})',
    411: lambda *args: f'BIT_SIZE({", ".join(map(repr, args))})',
    412: lambda a,b: f"({repr(a)} % {repr(b)})",
    413: lambda *args: f'SELECTED_INT_KIND({", ".join(map(repr, args))})',
    414: lambda *args: f'SELECTED_REAL_KIND({", ".join(map(repr, args))})',
    415: lambda *args: f'DSQL({", ".join(map(repr, args))})',
    416: lambda *args: f'ISQL({", ".join(map(repr, args))})',
    417: lambda *args: f'FTELL({", ".join(map(repr, args))})',
    418: lambda *args: f'MAKE_ACTION({", ".join(map(repr, args))})',
    419: lambda *args: f'MAKE_CONDITION({", ".join(map(repr, args))})',
    420: lambda *args: f'MAKE_CONGLOM({", ".join(map(repr, args))})',
    421: lambda *args: f'MAKE_DEPENDENCY({", ".join(map(repr, args))})',
    422: lambda *args: f'MAKE_DIM({", ".join(map(repr, args))})',
    423: lambda *args: f'MAKE_DISPATCH({", ".join(map(repr, args))})',
    424: lambda *args: f'MAKE_FUNCTION({", ".join(map(repr, args))})',
    425: lambda *args: f'MAKE_METHOD({", ".join(map(repr, args))})',
    426: lambda *args: f'MAKE_PARAM({", ".join(map(repr, args))})',
    427: lambda *args: f'MAKE_PROCEDURE({", ".join(map(repr, args))})',
    428: lambda *args: f'MAKE_PROGRAM({", ".join(map(repr, args))})',
    429: lambda *args: f'MAKE_RANGE({", ".join(map(repr, args))})',
    430: lambda *args: f'MAKE_ROUTINE({", ".join(map(repr, args))})',
    431: lambda *args: f'MAKE_SIGNAL({", ".join(map(repr, args))})',
    432: lambda *args: f'MAKE_WINDOW({", ".join(map(repr, args))})',
    433: lambda *args: f'MAKE_WITH_UNITS({", ".join(map(repr, args))})',
    434: lambda *args: f'MAKE_CALL({", ".join(map(repr, args))})',
    435: lambda *args: f'CLASS_OF({", ".join(map(repr, args))})',
    436: lambda *args: f'DSCPTR_OF({", ".join(map(repr, args))})',
    437: lambda *args: f'KIND_OF({", ".join(map(repr, args))})',
    438: lambda *args: f'NDESC_OF({", ".join(map(repr, args))})',
    439: lambda *args: f'ACCUMULATE({", ".join(map(repr, args))})',
    440: lambda *args: f'MAKE_SLOPE({", ".join(map(repr, args))})',
    441: lambda *args: f'REM({", ".join(map(repr, args))})',
    442: lambda *args: f'COMPLETION_MESSAGE_OF({", ".join(map(repr, args))})',
    443: lambda *args: f'INTERRUPT_OF({", ".join(map(repr, args))})',
    444: lambda: '$SHOTNAME',
    445: lambda *args: f'BUILD_WITH_ERROR({", ".join(map(repr, args))})',
    446: lambda *args: f'ERROR_OF({", ".join(map(repr, args))})',
    447: lambda *args: f'MAKE_WITH_ERROR({", ".join(map(repr, args))})',
    448: lambda *args: f'DO_TASK({", ".join(map(repr, args))})',
    449: lambda *args: f'ISQL_SET({", ".join(map(repr, args))})',
    450: lambda *args: f'FS_FLOAT({", ".join(map(repr, args))})',
    451: lambda *args: f'FS_COMPLEX({", ".join(map(repr, args))})',
    452: lambda *args: f'FT_FLOAT({", ".join(map(repr, args))})',
    453: lambda *args: f'FT_COMPLEX({", ".join(map(repr, args))})',
    454: lambda *args: f'BUILD_OPAQUE({", ".join(map(repr, args))})',
    455: lambda *args: f'MAKE_OPAQUE({", ".join(map(repr, args))})',
    456: lambda *args: f'DICT({", ".join(map(repr, args))})',
    457: lambda *args: f'TUPLE({", ".join(map(repr, args))})',
    458: lambda *args: f'LIST({", ".join(map(repr, args))})',
    459: lambda *args: f'SQUEEZE({", ".join(map(repr, args))})',
    460: lambda *args: f'FLATTEN({", ".join(map(repr, args))})',
}
