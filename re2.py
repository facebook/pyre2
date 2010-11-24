#!/usr/bin/env python

# Copyright (c) 2010, David Reiss and Facebook, Inc. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# * Neither the name of Facebook nor the names of its contributors
#   may be used to endorse or promote products derived from this software
#   without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Define this first, since it is referenced by _re2.
class error(Exception):
    pass

import _re2, sys, unittest
from re import IGNORECASE

__all__ = [
    "error",
    "compile",
    "search",
    "match",
    "fullmatch",
    "IGNORECASE",
    ]

# Module-private compilation function, for future caching, other enhancements
_compile = _re2._compile

class Regex(object):
    def __init__(self, re):
        self.re = re
    def __getattr__(self, attr):
        return getattr(self.re, attr)
    def findall(self, string, pos = 0, endpos = sys.maxint):
        """Similar to the findall() function, using the compiled pattern, but
        also accepts optional pos and endpos parameters that limit the search
        region like for match(). """
        return [m.group() for m in self.finditer(string, pos, endpos)]
    def finditer(self, string, pos = 0, endpos = sys.maxint):
        """Similar to the finditer() function, using the compiled pattern, but
        also accepts optional pos and endpos parameters that limit the search
        region like for match()."""
        while 1:
            m = self.re.search(string, pos, endpos)
            if m is None:
                break
            yield m
            pos = m.end()

def compile(pattern, flags = None):
    "Compile a regular expression pattern, returning a pattern object."
    flags = flags or 0
    if flags & (~IGNORECASE):
      raise NotImplementedError('')
    return Regex(_compile(pattern, flags))

def search(pattern, string, flags = None):
    """Scan through string looking for a match to the pattern, returning
    a match object, or None if no match was found."""
    return compile(pattern, flags).search(string)

def match(pattern, string, flags = None):
    """Try to apply the pattern at the start of the string, returning
    a match object, or None if no match was found."""
    return compile(pattern, flags).match(string)

def fullmatch(pattern, string, flags = None):
    """Try to apply the pattern to the entire string, returning
    a match object, or None if no match was found."""
    return compile(pattern, flags).fullmatch(string)

def findall(pattern, string, flags = None):
    """Return all non-overlapping matches of pattern in string, as a list of
    strings."""
    return compile(pattern, flags).findall(string)

def finditer(pattern, string, flags = None):
    """Return an iterator yielding MatchObject instances over all
    non-overlapping matches for the RE pattern in string."""
    return compile(pattern, flags).finditer(string)

class Re2Test(unittest.TestCase):
  def test_case(self):
    self.assertEqual(findall('a', 'A', IGNORECASE), ['A'])
    self.assertEqual(findall('a', 'A'), [])
  def test_findall(self):
    self.assertEqual(findall('aa','aaaa'), ['aa','aa'])

if __name__ == '__main__':
  unittest.main()
