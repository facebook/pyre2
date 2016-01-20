=====
pyre2
=====

.. contents::

Summary
=======

pyre2 is a Python extension that wraps
`Google's RE2 regular expression library
<https://github.com/google/re2/>`_.
It implements many of the features of Python's built-in
``re`` module with compatible interfaces.


New Features
============

* ``Regexp`` objects have a ``fullmatch`` method that works like ``match``,
  but anchors the match at both the start and the end.
* ``Regexp`` objects have
  ``test_search``, ``test_match``, and ``test_fullmatch``
  methods that work like ``search``, ``match``, and ``fullmatch``,
  but only return ``True`` or ``False`` to indicate
  whether the match was successful.
  These methods should be faster than the full versions,
  especially for patterns with capturing groups.


Missing Features
================

* No substitution methods.
* No flags.
* No ``split``, ``findall``, or ``finditer``.
* No top-level convenience functions like ``search`` and ``match``.
  (Just use compile.)
* No compile cache.
  (If you care enough about performance to use RE2,
  you probably care enough to cache your own patterns.)
* No ``lastindex`` or ``lastgroup`` on ``Match`` objects.


Current Status
==============

pyre2 has only received basic testing,
and I am by no means a Python extension expert,
so it is quite possible that it contains bugs.
I'd guess the most likely are reference leaks in error cases.

RE2 doesn't build with fPIC, so I had to build it with

::

  make CFLAGS='-fPIC -c -Wall -Wno-sign-compare -O3 -g -I.'

I also had to add it to my compiler search path when building the module
with a command like

::

  env CPPFLAGS='-I/path/to/re2' LDFLAGS='-L/path/to/re2/obj' ./setup.py build


Contact
=======

You can file bug reports on GitHub, or email the author:
David Reiss <dreiss@facebook.com>.
