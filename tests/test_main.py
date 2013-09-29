#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_main
----------------------------------

Tests for `main` module.
"""

import unittest

from pytar.main import main
from pytar.main import parse_pytar_args

from utils import abspath


class TestArgParsing(unittest.TestCase):

    def test_parse_pytar_args_action_extract_tarfile(self):
        args = parse_pytar_args(['extract', 'tarfile.tar'])
        self.assertEqual(args.action, 'extract')
        self.assertEqual(args.target, 'tarfile.tar')


class TestMain(unittest.TestCase):

    def test_main_should_not_return_None(self):
        result = main(['extract', abspath('tarfiles/corrupted-tar-file.tar')])
        self.assertIsNotNone(result)

    def test_main_should_return_None(self):
        action = 'unkown_action'
        result = main([action, abspath('tarfiles/corrupted-tar-file.tar')])
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
