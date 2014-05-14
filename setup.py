#!/usr/bin/env python
import plumber
try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension


setup(
    name="picles.plumber",
    version='.'.join(plumber.__version__),
    description="Simple data transformation pipeline.",
    author="Gustavo Fonseca & contributors",
    author_email="gustavo@gfonseca.net",
    license="BSD",
    url="https://github.com/picleslivre/plumber/",
    py_modules=["plumber"],
    package_data={'': ['README.md', 'LICENSE']},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
    tests_require=["mocker"],
    test_suite='tests',
)
