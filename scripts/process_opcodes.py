
import os
import sys
import csv

if len(sys.argv) < 2:
    print('process_opcodes.py PATH_TO_MDSPLUS_SOURCE')

mdsplus_source_path = sys.argv[1]
opcodes_filename = os.path.join(mdsplus_source_path, 'tdishr', 'opcodes.csv')

root_path = os.path.dirname(os.path.dirname(__file__))
source_path = os.path.join(root_path, 'mdsthin')
functions_filename = os.path.join(source_path, 'functions.py')
opcbuiltins_filename = os.path.join(source_path, 'internals/opcbuiltins.py')

opcodes = []
with open(opcodes_filename, newline='') as input_file:

    reader = csv.DictReader(input_file)
    opcodes = [ opc for opc in reader ]

with open(functions_filename, 'wt') as output_file:

    output_file.write('\n')
    output_file.write('from .descriptors import Function\n')
    output_file.write('\n')

    for opc in opcodes:
        func_name = opc['builtin'].replace('$', 'd')
        
        if int(opc['m1']) == 0 and int(opc['m2']) == 0:
            output_file.write(f"def {func_name}():\n")
            output_file.write(f"    return Function({opc['opcode']})\n")
        else:
            output_file.write(f"def {func_name}(*args):\n")
            output_file.write(f"    return Function({opc['opcode']}, *args)\n")

        output_file.write('\n')

SPECIAL_OPCODES = {
    'ADD': 'lambda a,b: f"({repr(a)} + {repr(b)})"',
    'SUBTRACT': 'lambda a,b: f"({repr(a)} - {repr(b)})"',
    'MULTIPLY': 'lambda a,b: f"({repr(a)} * {repr(b)})"',
    'DIVIDE': 'lambda a,b: f"({repr(a)} / {repr(b)})"',
    'MODULO': 'lambda a,b: f"({repr(a)} % {repr(b)})"',
    'SHIFT_LEFT': 'lambda a,b: f"({repr(a)} << {repr(b)})"',
    'SHIFT_RIGHT': 'lambda a,b: f"({repr(a)} >> {repr(b)})"',
    'EXT_FUNCTION': 'lambda _,func,*args: f"{func.data()}({\', \'.join(map(repr, args))})"',
}

with open(opcbuiltins_filename, 'wt') as output_file:

    output_file.write('\n')
    output_file.write('OPCODE_MAP = {\n')

    for opc in opcodes:
        output_file.write(f"    '{opc['builtin']}': {opc['opcode']},\n")

    output_file.write('}\n')
    output_file.write('\n')
    output_file.write('OPCODE_REPR_MAP = {\n')

    for opc in opcodes:
        if opc['builtin'] in SPECIAL_OPCODES:
            lambda_func = SPECIAL_OPCODES[opc['builtin']]
        elif int(opc['m1']) == 0 and int(opc['m2']) == 0:
            lambda_func = f"lambda: '{opc['builtin']}'"
        else:
            lambda_func = f"lambda *args: f'{opc['builtin']}({{\", \".join(map(repr, args))}})'"

        output_file.write(f"    {opc['opcode']}: {lambda_func},\n")

    output_file.write('}\n')