# Copyright (c) Facebook, Inc. and its affiliates.
import unittest
import re2

class TestCompile(unittest.TestCase):
    def test_raise(self):
        with self.assertRaisesRegexp(
            re2.error,
            'no argument for repetition operator: \\*'
        ):
            re2.compile('*')
