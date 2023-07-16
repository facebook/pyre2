#!/usr/bin/env python
# Copyright (c) Facebook, Inc. and its affiliates.

from setuptools import setup, Extension

setup(
    name="fb-re2",
    version="1.0.7",
    url="https://github.com/facebook/pyre2",
    description="Python wrapper for Google's RE2",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 5 - Production/Stable",
    ],
    author="David Reiss",
    author_email="dreiss@fb.com",
    maintainer="Siddharth Agarwal",
    maintainer_email="sid0@fb.com",
    py_modules = ["re2"],
    test_suite = "tests",
    ext_modules = [Extension("_re2",
      sources = ["_re2.cc"],
      libraries = ["re2"],
      extra_compile_args=['-std=c++17'],
      )],
    )
