#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
utils
----------------------------------

Some functions for using on the tests.
"""

import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def abspath(relative_path):
    return os.path.join(CURRENT_DIR, relative_path)


def clean_extracted_files():
    os.remove(abspath('tarfiles/hi.txt'))
    os.remove(abspath('tarfiles/tar.png'))


def clean_extracted_files_another_dir():
    os.remove(abspath('tarfiles/dir-test-extract-path/hi.txt'))
    os.remove(abspath('tarfiles/dir-test-extract-path/tar.png'))
