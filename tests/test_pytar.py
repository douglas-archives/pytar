#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pytar
----------------------------------

Tests for `pytar` module.
"""

from __future__ import unicode_literals

from pytar import pytar

from .utils import abspath, CURRENT_DIR, clean_extracted_files

import tarfile

import sys
if sys.version_info[:2] < (2, 7):
    import unittest2 as unittest
else:
    import unittest


class TestPytarExtract(unittest.TestCase):
    def test_should_extract_a_normal_tar_file(self):
        tar_file = abspath('tarfiles/files.tar')
        result = pytar.pytar_extract(tar_file)
        self.assertEqual('success', result['status'])
        self.addCleanup(clean_extracted_files)

    def test_should_extract_a_normal_tar_file_with_verbose_flag(self):
        tar_file = abspath('tarfiles/files.tar')
        result = pytar.pytar_extract(tar_file, verbose=True)
        self.assertEqual('success', result['status'])
        self.assertNotEqual('', result['verbose'])
        self.addCleanup(clean_extracted_files)

    def test_should_not_extract_a_corrupted_tar_file(self):
        tar_file = abspath('tarfiles/corrupted-tar-file.tar')
        result = pytar.pytar_extract(tar_file)
        self.assertEqual('fail', result['status'])

    def test_should_not_extract_a_directory(self):
        result = pytar.pytar_extract(CURRENT_DIR)
        self.assertEqual('fail', result['status'])

    def test_should_not_extract_an_inexistent_path(self):
        inexistent_tar_file = abspath('tarfiles/inexistent-tar-file.tar')
        result = pytar.pytar_extract(inexistent_tar_file)
        self.assertEqual('fail', result['status'])

    def test_should_not_extract_an_empty_tar_file(self):
        result = pytar.pytar_extract(abspath('tarfiles/empty-tar-file.tar'))
        self.assertEqual('fail', result['status'])


class TestPytarListing(unittest.TestCase):
    def test_should_output_the_verbose_list_of_members_from_a_tar_file(self):
        tar_file = tarfile.open(abspath('tarfiles/files.tar'))
        output = pytar.list_contents(tar_file)
        self.assertIn('tar.png', output)
        self.assertIn('hi.txt', output)


if __name__ == '__main__':
    unittest.main()
