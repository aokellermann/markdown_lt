#!/usr/bin/env python3
"""Setup script for markdown_lt."""

from setuptools import setup


def fread(path):
    """Reads a file."""
    with open(path, 'r') as file:
        return file.read()


setup(
    name='markdown_lt',
    version='0.1.0',
    url='https://github.com/aokellermann/markdown_lt',
    author='Antony Kellermann',
    author_email='aokellermann@gmail.com',
    description='LanguageTool for markdown files.',
    long_description=fread('README.md'),
    license='MIT',
    packages=['markdown_lt'],
    platforms='any',
)
