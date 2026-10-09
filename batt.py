import argparse
import include.subcommands as subcommands

def main():
    # PARSE USER INPUT
    # top level parser
    parser = argparse.ArgumentParser(prog='batt')
    subparsers = parser.add_subparsers(required=True)

    # subparser for the status command
    parser_status = subparsers.add_parser('status')
    parser_status.set_defaults(func=subcommands.status)
    
    # process input
    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()