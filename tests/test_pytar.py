#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pytar
----------------------------------

Tests for `pytar` module.
"""

from __future__ import unicode_literals

from pytar import pytar

from .utils import (abspath, CURRENT_DIR, clean_extracted_files,
                    clean_extracted_files_another_dir)

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

    def test_should_extract_to_another_directory(self):
        path = abspath('tarfiles/dir-test-extract-path/')
        result = pytar.pytar_extract(abspath('tarfiles/files.tar'), path)
        self.assertEqual('success', result['status'])
        self.addCleanup(clean_extracted_files_another_dir)

    def test_should_not_extract_to_an_inexistent_directory(self):
        path = abspath('tarfiles/inexistent-dir/')
        result = pytar.pytar_extract(abspath('tarfiles/files.tar'), path)
        self.assertEqual('fail', result['status'])


class TestPytarListing(unittest.TestCase):

    def setUp(self):
        tar_file = tarfile.open(
            abspath('tarfiles/tar-with-links-and-other-types.tar')
        )
        self.output_file_types = pytar.list_contents(tar_file)

    def test_should_output_the_verbose_list_of_members_from_a_tar_file(self):
        tar_file = tarfile.open(abspath('tarfiles/files.tar'))
        output = pytar.list_contents(tar_file)
        self.assertIn('tar.png', output)
        self.assertIn('hi.txt', output)

    def test_should_output_the_symbolic_link(self):
        self.assertIn('ustar/symtype -> regtype', self.output_file_types)

    def test_should_output_the_hard_link(self):
        self.assertIn('ustar/lnktype link to ustar/regtype',
                      self.output_file_types)

    def test_should_output_devmajor_devminor_when_character_device(self):
        self.assertIn('1,3', self.output_file_types)

    def test_should_output_devmajor_devminor_when_block_device(self):
        self.assertIn('3,0', self.output_file_types)


class TestPytarUnicode(unittest.TestCase):

    def test_should_read_and_list_unicode_file_names_inside_the_tar(self):
        tar_file = tarfile.open(abspath('tarfiles/test-unicode.tar'))
        output = pytar.list_contents(tar_file)
        self.assertIn('ãéçõïûã°+@', output)
        self.assertIn('umlauts-ÄÖÜäöüß', output)
        self.assertIn('ಫೈಲ್', output)
        self.assertIn('файл', output)


if __name__ == '__main__':
    unittest.main()
