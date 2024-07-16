
import argparse

from ..connection import *

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(prog='mdsthin.mdstcl')

    parser.add_argument('server', help='Server to connect to')

    args = parser.parse_args()
    
    print('Connecting to:', args.server)
    c = Connection(args.server)
    c.mdstcl()
