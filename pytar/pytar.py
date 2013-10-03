#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import sys
import tarfile
from datetime import datetime

PY3 = sys.version > '3'


def list_contents(tar_file):
    """
    Listing contents from a tar file. This implementation is based on
    Python core code, (tarfile.list).
    """
    members = tar_file.getmembers()
    output = ''
    for tarinfo in members:
        line = ''
        line += tarfile.filemode(tarinfo.mode) + ' '
        owner = '{0}/{1}'.format(
            tarinfo.uname or tarinfo.uid,
            tarinfo.gname or tarinfo.gid
        )
        line += owner

        if tarinfo.ischr() or tarinfo.isblk():
            dev = '{0},{1}'.format(tarinfo.devmajor, tarinfo.devminor)
            line += dev.center(10) + ' '
        else:
            line += '{0:10}'.format(tarinfo.size) + ' '

        line += str(datetime.fromtimestamp(tarinfo.mtime)) + ' '

        line += '{0}{1}{2}'.format(
            tarinfo.name if PY3 else tarinfo.name.decode('utf-8'),
            ('/' if tarinfo.isdir() else ''),
            ' '
        )

        if tarinfo.issym():
            line += '-> {0}'.format(tarinfo.linkname)
        if tarinfo.islnk():
            line += 'link to {0}'.format(tarinfo.linkname)

        output += '{0}\n'.format(line)

    return output or 'Nothing to output.'


def pytar_extract(tar_file_name, verbose=False):
    is_a_valid_tarfile = False
    messages = {
        'path_does_not_exist': {
            'status': 'fail',
            'message': 'ERROR: This path does not exist.'
        },
        'is_dir': {
            'status': 'fail',
            'message': 'ERROR: This is a directory not a tar file.'
        },
        'not_a_tar_file': {
            'status': 'fail',
            'message': 'ERROR: This may not be a tar file or may be corrupted.'
        },
        'empty_tar_file': {
            'status': 'fail',
            'message': 'This is an empty tar file.'
        },
        'success': {
            'status': 'success',
            'message': 'Successfully extracted.',
            'verbose': ''
        },
    }

    if not os.path.exists(tar_file_name):
        return messages['path_does_not_exist']

    if os.path.isdir(tar_file_name):
        return messages['is_dir']

    extract_path = os.path.dirname(tar_file_name)

    is_a_valid_tarfile = tarfile.is_tarfile(tar_file_name)
    if not is_a_valid_tarfile:
        return messages['not_a_tar_file']

    tar_file = tarfile.open(tar_file_name)
    members = tar_file.getmembers()

    if not members:
        return messages['empty_tar_file']

    tar_file.extractall(extract_path, members)

    if verbose:
        messages['success']['verbose'] = list_contents(tar_file)

    tar_file.close()
    return messages['success']
