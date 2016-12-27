#!/usr/bin/env python3

import argparse
import db
import sys


def main():
    """
    The main function
    :return: The proper exit code.
    """
    parser = argparse.ArgumentParser(description='Examine the database.')
    parser.add_argument('--print', action='store_true',
                        help='Print each of the database entries')

    args = parser.parse_args()
    if not args.print:
        parser.print_help()
        return 255

    db.Db().print()


if __name__ == '__main__':
    sys.exit(main())
