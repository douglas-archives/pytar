#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import argparse
import sys
import os
import tarfile

CREATE, EXTRACT = 'create', 'extract'


def pytar_create(tar_file_name):
    pass


def pytar_extract(tar_file_name):
    is_a_valid_tarfile = False
    extract_path = os.path.dirname(tar_file_name)
    messages = {
        'is_dir': {
            'status': 'fail',
            'message': 'ERROR: This is a directory not a tar file.'
        },
        'not_a_tar_file': {
            'status': 'fail',
            'message': 'ERROR: This may not be a tar file or may be corrupted.'
        },
        'success': {
            'status': 'success',
            'message': 'Successfully extracted.'
        },
    }

    if os.path.isdir(tar_file_name):
        return messages['is_dir']
    else:
        is_a_valid_tarfile = tarfile.is_tarfile(tar_file_name)
        if not is_a_valid_tarfile:
            return messages['not_a_tar_file']
        else:
            with tarfile.open(tar_file_name) as tar_file:
                tar_file.extractall(extract_path)
                return messages['success']


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
        extraction = pytar_extract(args.target)
        print(extraction.get('message'))


if __name__ == '__main__':
    main()