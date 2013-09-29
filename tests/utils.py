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