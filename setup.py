#!/usr/bin/env python

from setuptools import setup

setup(
    name         = 'zygote',
    version      = '0.1',
    author       = 'Evan Klitzke',
    author_email = 'evan@eklitzke.org',
    description  = 'A tornado HTTP worker management tool',
    license      = 'Apache License 2.0',
    packages     = ['zygote'],
    entry_points = {'console_scripts': 'zygote = zygote.main:main'},
    install_requires = ['setuptools', 'tornado']
)

