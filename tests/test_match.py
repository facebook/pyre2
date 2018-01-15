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

    def test_match_bytes(self):
        ''' test that we can match things in the bytes type '''
        r = re2.compile('(\\x09)')
        m = r.match(b'\x09')
        self.assertIsNotNone(m)
        g = m.groups()
        self.assertTrue(isinstance(g, tuple))
        self.assertTrue(isinstance(g[0], bytes))
        self.assertEqual(b'\x09', g[0])

    def test_match_str(self):
        ''' test that we can match binary things in the str type '''
        r = re2.compile('(\\x09)')
        m = r.match('\x09')
        self.assertIsNotNone(m)
        g = m.groups()
        self.assertTrue(isinstance(g, tuple))
        self.assertTrue(isinstance(g[0], str))
        self.assertEqual('\x09', g[0])

    def test_match_bad_utf8_bytes(self):
        ''' Validate that we just return None on invalid utf-8 '''
        r = re2.compile('\\x80')
        m = r.match(b'\x80')
        self.assertIsNone(m)

    def test_span_type(self):
        ''' verify that start/end return the native literal integer type '''
        r = re2.compile('abc')
        m = r.match('abc')
        self.assertTrue(isinstance(m.start(), type(1)))
        self.assertTrue(isinstance(m.end(), type(1)))

    def test_set_unanchored(self):
        s = re2.Set(re2.UNANCHORED)
        s_with_default_anchoring = re2.Set()

        for re2_set in [s, s_with_default_anchoring]:
            re2_set.add('foo')
            re2_set.add('bar')
            re2_set.add('baz')
            re2_set.compile()

            self.assertEqual(re2_set.match('foo'), [0])
            self.assertEqual(re2_set.match('bar'), [1])
            self.assertEqual(re2_set.match('baz'), [2])
            self.assertEqual(re2_set.match('afoobaryo'), [0, 1])

            self.assertEqual(re2_set.match('ooba'), [])

    def test_set_anchor_both(self):
        s = re2.Set(re2.ANCHOR_BOTH)
        self.assertEqual(s.add('foo'), 0)
        self.assertEqual(s.add('bar'), 1)
        s.compile()

        self.assertEqual(s.match('foobar'), [])
        self.assertEqual(s.match('fooba'), [])
        self.assertEqual(s.match('oobar'), [])
        self.assertEqual(s.match('foo'), [0])
        self.assertEqual(s.match('bar'), [1])

    def test_set_anchor_start(self):
        s = re2.Set(re2.ANCHOR_START)
        self.assertEqual(s.add('foo'), 0)
        self.assertEqual(s.add('bar'), 1)
        s.compile()

        self.assertEqual(s.match('foobar'), [0])
        self.assertEqual(s.match('oobar'), [])
        self.assertEqual(s.match('foo'), [0])
        self.assertEqual(s.match('ofoobaro'), [])
        self.assertEqual(s.match('baro'), [1])

    def test_bad_anchoring(self):
        with self.assertRaisesRegexp(ValueError, 'anchoring must be one of.*'):
            re2.Set(None)

        with self.assertRaisesRegexp(ValueError, 'anchoring must be one of.*'):
            re2.Set(15)

        with self.assertRaisesRegexp(ValueError, 'anchoring must be one of.*'):
            re2.Set({})

    def test_match_without_compile(self):
        s = re2.Set()
        s.add('foo')

        with self.assertRaisesRegexp(RuntimeError, 'Can\'t match\(\) on an.*'):
            s.match('bar')

    def test_add_after_compile(self):
        s = re2.Set()
        s.add('foo')
        s.compile()

        with self.assertRaisesRegexp(RuntimeError,
            'Can\'t add\(\) on an already compiled Set'):
            s.add('bar')

    # Segfaults on Debain Jessie
    #def test_compile_on_empty(self):
    #    s = re2.Set()
    #    s.compile()
    #    self.assertEqual(s.match('nah'), [])

    def test_double_compile(self):
        s = re2.Set()
        s.add('foo')
        s.compile()
        s.compile()

    def test_add_with_bad_pattern(self):
        s = re2.Set()

        with self.assertRaisesRegexp(ValueError, 'missing \)'):
            s.add('(')

        with self.assertRaises(TypeError):
            s.add(3)
