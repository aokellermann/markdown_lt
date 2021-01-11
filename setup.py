#!/usr/bin/env python3

import markdown_lt
from setuptools import setup


def fread(filepath):
    with open(filepath, 'r') as f:
        return f.read()


setup(
    name='markdown_lt',
    version=markdown_lt.__version__,
    url='https://github.com/aokellermann/markdown_lt',
    author='Antony Kellermann',
    author_email='aokellermann@gmail.com',
    description='LanguageTool for markdown files.',
    long_description=fread('README.md'),
    license='MIT',
    packages=[
        'markdown_lt'
    ],
    platforms='any',
)
