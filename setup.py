#!/usr/bin/env python3
"""Setup script for markdown_lt."""

from setuptools import setup

import markdown_lt
from markdown_lt.utils import read_utf8

setup(name='markdown_lt',
      version=markdown_lt.__version__,
      url='https://github.com/aokellermann/markdown_lt',
      author='Antony Kellermann',
      author_email='aokellermann@gmail.com',
      description='LanguageTool for markdown files.',
      long_description=read_utf8('README.md'),
      license='MIT',
      packages=['markdown_lt'],
      platforms='any',
      scripts=['bin/markdown_lt'])
