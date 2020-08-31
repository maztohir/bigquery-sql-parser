========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/bigquery-sql-parser/badge/?style=flat
    :target: https://readthedocs.org/projects/bigquery-sql-parser
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/maztohir/bigquery-sql-parser.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/maztohir/bigquery-sql-parser

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/maztohir/bigquery-sql-parser?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/maztohir/bigquery-sql-parser

.. |requires| image:: https://requires.io/github/maztohir/bigquery-sql-parser/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/maztohir/bigquery-sql-parser/requirements/?branch=master

.. |codecov| image:: https://codecov.io/gh/maztohir/bigquery-sql-parser/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/maztohir/bigquery-sql-parser

.. |version| image:: https://img.shields.io/pypi/v/bigquery-sql-parser.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/bigquery-sql-parser

.. |wheel| image:: https://img.shields.io/pypi/wheel/bigquery-sql-parser.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/bigquery-sql-parser

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/bigquery-sql-parser.svg
    :alt: Supported versions
    :target: https://pypi.org/project/bigquery-sql-parser

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/bigquery-sql-parser.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/bigquery-sql-parser

.. |commits-since| image:: https://img.shields.io/github/commits-since/maztohir/bigquery-sql-parser/v0.0.2.svg
    :alt: Commits since latest release
    :target: https://github.com/maztohir/bigquery-sql-parser/compare/v0.0.2...master



.. end-badges

Work out of the box to understand and modify your bigquery sql programatically

* Free software: MIT license

Installation
============

::

    pip install bigquery-sql-parser

You can also install the in-development version with::

    pip install https://github.com/maztohir/bigquery-sql-parser/archive/master.zip


Documentation
=============


https://bigquery-sql-parser.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
