#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_main
----------------------------------

Tests for `main` module.
"""

import unittest

from pytar.main import parse_pytar_args


class TestArgParsing(unittest.TestCase):

    def test_parse_pytar_args_action_extract_tarfile(self):
        args = parse_pytar_args(['extract', 'tarfile.tar'])
        self.assertEqual(args.action, 'extract')
        self.assertEqual(args.target, 'tarfile.tar')

    def test_parse_pytar_args_action_extract_tarfile_verbose(self):
        args = parse_pytar_args(['extract', 'tarfile.tar', '--verbose'])
        self.assertTrue(args.verbose)

if __name__ == '__main__':
    unittest.main()
