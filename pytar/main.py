#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import argparse
import sys

from .pytar import pytar_extract

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
        'extract_path',
        help='''Extraction path. By default will extract alongside the
                tar file.''',
        nargs='?',
        default=None
    )
    parser.add_argument(
        '-v', '--verbose',
        help='Print the files to be extracted',
        action='store_true', default=False
    )
    return parser.parse_args(args)


def main(sys_argv=[]):
    sys_argv = sys_argv or sys.argv
    try:
        args = parse_pytar_args(sys_argv[1:])
    except SystemExit:
        print('Need a help? Type: pytar -h')
        return None

    if args.action == EXTRACT:
        extraction_result = pytar_extract(
            args.target,
            args.extract_path,
            args.verbose
        )
        if args.verbose:
            return '{0}\n{1}'.format(extraction_result.get('verbose'),
                                     extraction_result.get('message'))
        else:
            return extraction_result.get('message')

if __name__ == '__main__':  # pragma: no cover
    sys.exit(main(sys.argv))
