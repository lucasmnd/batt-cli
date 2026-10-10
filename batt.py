import argparse
import include.subcommands as subcommands

from include.batt_lib import CapacityInterval

def main():
    # PARSE USER INPUT
    # top level parser
    parser = argparse.ArgumentParser(prog='batt')
    subparsers = parser.add_subparsers(required=True)

    # subparser for the status command
    # batt status
    parser_status = subparsers.add_parser('status')
    parser_status.set_defaults(func=subcommands.status)

    # subparser for the set command
    # batt set interval
    parser_set = subparsers.add_parser('set')
    parser_set.add_argument('interval', type=CapacityInterval)
    parser_set.set_defaults(func=subcommands.set)

    # process input
    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()