#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_main
----------------------------------

Tests for `main` module.
"""

from pytar.main import main
from pytar.main import parse_pytar_args

from .utils import abspath, clean_extracted_files

import sys
if sys.version_info[:2] < (2, 7):
    import unittest2 as unittest
else:
    import unittest


class TestArgParsing(unittest.TestCase):

    def test_parse_pytar_args_action_extract_tarfile(self):
        args = parse_pytar_args(['extract', 'tarfile.tar'])
        self.assertEqual(args.action, 'extract')
        self.assertEqual(args.target, 'tarfile.tar')


class TestMain(unittest.TestCase):

    def test_main_should_not_return_None(self):
        corrupted_tar_file = abspath('tarfiles/corrupted-tar-file.tar')
        result = main(['', 'extract', corrupted_tar_file])
        self.assertIsNotNone(result)

    def test_main_should_return_message_and_contents_using_verbose_flag(self):
        corrupted_tar_file = abspath('tarfiles/files.tar')
        result = main(['', 'extract', corrupted_tar_file, '--verbose'])
        self.assertIn('tar.png', result)
        self.assertIn('hi.txt', result)
        self.addCleanup(clean_extracted_files)

    def test_main_should_return_None(self):
        action = 'unkown_action'
        result = main(['', action, abspath('tarfiles/corrupted-tar-file.tar')])
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
