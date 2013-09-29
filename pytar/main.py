#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import argparse
import sys

import pytar

CREATE, EXTRACT = 'create', 'extract'


def parse_pytar_args(args):
    """ Parse the command-line arguments to pytar. """
    parser = argparse.ArgumentParser(
        description='''Extract a tar file or create a tar file from a
                       directory.'''
    )
    parser.add_argument(
        'action',
        help='''Type "extract" for extracting a tar file or "create" for
                create a tar file from directories and/or files.''',
        choices=[CREATE, EXTRACT]
    )
    parser.add_argument(
        'target',
        help='''Target for directories and/or files in general (depends
                on the action).'''
    )
    parser.add_argument(
        '-v', '--verbose',
        help='Print the files to be extracted',
        action='store_true', default=False
    )
    return parser.parse_args(args)


def main():
    args = parse_pytar_args(sys.argv[1:])

    if args.action == EXTRACT:
        extraction = pytar.pytar_extract(args.target)
        print(extraction.get('message'))


if __name__ == '__main__':
    main()
