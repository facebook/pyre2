import unittest
import re2

class TestMatch(unittest.TestCase):
    def test_const_match(self):
        m = re2.match('abc', 'abc')
        self.assertIsNotNone(m)
        self.assertEqual(m.start(), 0)
        self.assertEqual(m.end(), 3)
        self.assertEqual(m.span(), (0, 3))
        self.assertEqual(m.groups(), tuple())
        self.assertEqual(m.groupdict(), {})

    def test_group_match(self):
        m = re2.match('ab([cde]fg)', 'abdfghij')
        self.assertIsNotNone(m)
        self.assertEqual(m.start(), 0)
        self.assertEqual(m.end(), 5)
        self.assertEqual(m.span(), (0, 5))
        self.assertEqual(m.groups(), ('dfg',))
        self.assertEqual(m.groupdict(), {})

    def test_compiled_match(self):
        r = re2.compile('ab([cde]fg)')
        m = r.match('abdfghij')
        self.assertIsNotNone(m)
        self.assertEqual(m.start(), 0)
        self.assertEqual(m.end(), 5)
        self.assertEqual(m.span(), (0, 5))
        self.assertEqual(m.groups(), ('dfg',))
        self.assertEqual(m.groupdict(), {})

    def test_match_raise(self):
        '''test that using the API incorrectly fails'''
        r = re2.compile('ab([cde]fg)')
        self.assertRaises(TypeError, lambda: re2.match(r, 'abdfghij'))
