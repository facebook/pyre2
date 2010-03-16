#!/usr/bin/env python

# Define this first, since it is referenced by _re2.
class error(Exception):
  pass

import _re2

compile = _re2._compile
