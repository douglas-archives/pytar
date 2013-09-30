#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import tarfile


def pytar_extract(tar_file_name):
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
        'success': {
            'status': 'success',
            'message': 'Successfully extracted.'
        },
    }

    if not os.path.exists(tar_file_name):
        return messages['path_does_not_exist']

    extract_path = os.path.dirname(tar_file_name)

    if os.path.isdir(tar_file_name):
        return messages['is_dir']
    else:
        is_a_valid_tarfile = tarfile.is_tarfile(tar_file_name)
        if not is_a_valid_tarfile:
            return messages['not_a_tar_file']
        else:
            tar_file = tarfile.open(tar_file_name)
            tar_file.extractall(extract_path)
            tar_file.close()
            return messages['success']
