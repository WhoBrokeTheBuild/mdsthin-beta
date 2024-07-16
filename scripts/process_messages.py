
import os
import sys
import glob

from xml.etree import ElementTree

if len(sys.argv) < 2:
    print('process_messages.py PATH_TO_MDSPLUS_SOURCE')

mdsplus_source_path = sys.argv[1]
xml_filename_list = glob.glob(os.path.join(mdsplus_source_path, '**', '*_messages.xml'))

root_path = os.path.dirname(os.path.dirname(__file__))
source_path = os.path.join(root_path, 'mdsthin')
output_filename = os.path.join(source_path, 'exceptions.py')

SEVERITY_MAP = {
    'warning': 0,
    'success': 1,
    'error': 2,
    'info': 3,
    'fatal': 4,
    'internal': 7
}

SEVERITY_CODES = ['W', 'S', 'E', 'I', 'F', '?', '?', '?']

SKIP_FACILITY_LIST = [ 'Ss', 'Mdsdcl', 'Cam' ]

output_file = open(output_filename, 'wt')
output_file.write('''
EXCEPTION_MAP = {}
EXCEPTION_PREFIX_MAP = {}

def STATUS_OK(status):
    return (status & 1)

def STATUS_NOT_OK(status):
    return not (status & 1)

def STATUS_FACILITY(status):
    return (status >> 16)

def STATUS_MESSAGE(status):
    return (status >> 3) & 0b1111111111111

def STATUS_SEVERITY(status):
    return (status & 0b111)

def getException(status):
    return EXCEPTION_MAP.get(status, MdsException(f'Unknown status: {status}'))

def getExceptionFromError(error):
    if error.startswith('%'):
        prefix = error.split(',', maxsplit=1)[0]
        return EXCEPTION_PREFIX_MAP.get(prefix, MdsException(error))

    return MdsException(error)

class MdsException(Exception):
    pass

''')

for xml_filename in xml_filename_list:
    with open(xml_filename, 'rt') as xml_file:
        try:
            root = ElementTree.parse(xml_filename).getroot()
            for facility in root.iter('facility'):
                facility_name = facility.get('name')
                facility_value = int(facility.get('value'))

                if facility_name in SKIP_FACILITY_LIST:
                    continue

                output_file.write(f'class {facility_name}Exception(MdsException):\n')
                output_file.write(f'    pass\n')
                output_file.write('\n')

                for status in facility.iter('status'):
                    status_name = status.get('name')
                    status_value = int(status.get('value'))

                    if status_name.startswith('CAM_') or status_name == 'CAMACERR':
                        continue

                    deprecated = status.get('deprecated', None)
                    severity = SEVERITY_MAP[status.get('severity').lower()]

                    message = status.get('text', None)
                    if message is None:
                        continue

                    message = message.replace('  ', ' ')
                    message = message[0].upper() + message[ 1 : ]
                    if message[-1] == '.':
                        message = message[ : -1 ]

                    message_name = facility_name + status_name
                    message_value = (facility_value << 16) + (status_value << 3) + severity
                    message_prefix = f'%{facility_name.upper()}-{SEVERITY_CODES[severity]}-{status_name.upper()}'

                    output_file.write(f'class {message_name}({facility_name}Exception):\n')
                    output_file.write(f'    status = {message_value}\n')
                    output_file.write(f'    prefix = "{message_prefix}"\n')
                    output_file.write(f'    def __init__(self):\n')
                    output_file.write(f'        Exception.__init__(self, "{message_prefix}, {message}")\n')
                    output_file.write('\n')
                    output_file.write(f'EXCEPTION_MAP[{message_name}.status] = {message_name}\n')
                    output_file.write(f'EXCEPTION_PREFIX_MAP[{message_name}.prefix] = {message_name}\n')
                    output_file.write('\n')

        except Exception as e:
            print(e)