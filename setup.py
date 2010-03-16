#!/usr/bin/env python

from distutils.core import setup, Extension

setup(
    name="re2",
    version="0.1.0",
    description="Python wrapper for Google's RE2",
    author="David Reiss",
    py_modules = ["re2"],
    ext_modules = [Extension("_re2",
      sources = ["_re2.cc"],
      libraries = ["re2"],
      )],
    )
