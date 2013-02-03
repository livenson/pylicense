pylicense
=========

Simple library/executable for extracting license information from the python eggs.

:license: BSD
:copyright: 2013 by Ilja Livenson

Example of usage
================

Assyming pylicense is installed as an egg with pylicense script sitting in the PATH:

   .. code-block:: shell
    $ pylicense eggs/ 
    BeautifulSoup 3.2.0, BSD
    coverage 3.5.2, BSD
    grokcore.annotation 1.2, ZPL
    grokcore.component 2.4, ZPL
    grokcore.security 1.5, ZPL
    ipython 0.13, BSD
    martian 0.14, ZPL
    mock 1.0b1, UNKNOWN
    netaddr 0.7.6, BSD License
    nose 1.1.2, GNU LGPL

