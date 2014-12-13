#!/usr/bin/env python

from distutils.core import setup, Extension

setup(
    name="fb-re2",
    version="0.1.2",
    url="https://github.com/facebook/pyre2",
    description="Python wrapper for Google's RE2",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
    ],
    author="David Reiss",
    author_email="dreiss@fb.com",
    maintainer="Siddharth Agarwal",
    maintainer_email="sid0@fb.com",
    py_modules = ["re2"],
    ext_modules = [Extension("_re2",
      sources = ["_re2.cc"],
      libraries = ["re2"],
      )],
    )
