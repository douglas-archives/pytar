#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import tarfile


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
