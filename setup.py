#!/usr/bin/env python3
"""Setup script for markdown_lt."""

from setuptools import setup

from markdown_lt.utils import read_utf8, readlines_utf8


def get_version() -> str:
    """Gets the version of this module without importing."""
    lines = readlines_utf8('__init__.py')
    for line in lines:
        if line.startswith('__version__'):
            return line.split('\'')[1]
    raise RuntimeError("Couldn't find version!")


setup(name='markdown_lt',
      version=get_version(),
      url='https://github.com/aokellermann/markdown_lt',
      author='Antony Kellermann',
      author_email='aokellermann@gmail.com',
      description='LanguageTool for markdown files.',
      long_description=read_utf8('README.md'),
      long_description_content_type='text/markdown',
      license='MIT',
      packages=['markdown_lt'],
      platforms='any',
      scripts=['bin/markdown_lt'])
