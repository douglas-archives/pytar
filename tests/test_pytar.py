#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pytar
----------------------------------

Tests for `pytar` module.
"""

import unittest
import os

from pytar import pytar

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def abspath(relative_path):
    return os.path.join(CURRENT_DIR, relative_path)


class TestPytar(unittest.TestCase):
    def test_should_extract_a_normal_tar_file(self):
        tar_file = abspath('tarfiles/files.tar')
        result = pytar.pytar_extract(tar_file)
        self.assertEqual('success', result['status'])

    def test_should_not_extract_a_corrupted_tar_file(self):
        tar_file = abspath('tarfiles/corrupted-tar-file.tar')
        result = pytar.pytar_extract(tar_file)
        self.assertEqual('fail', result['status'])

    def test_should_not_extract_a_directory(self):
        result = pytar.pytar_extract(CURRENT_DIR)
        self.assertEqual('fail', result['status'])


if __name__ == '__main__':
    unittest.main()
