
import argparse

from . import *

if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog='mdsthin.test')

    parser.add_argument(
        '--server',
        default=None,
        help='Server to connect to'
    )

    parser.add_argument(
        '--cmod',
        default=False,
        action='store_const', const=True,
        help='Run C-Mod specific test'
    )

    parser.add_argument(
        'unittest',
        nargs='*',
        help='Arguments to unittest.main()'
    )

    args, extra = parser.parse_known_args()

    run_mdsthin_tests(
        server=args.server,
        cmod_tests=args.cmod,
        # unittest arguments
        argv=[ parser.prog, *extra],
    )

