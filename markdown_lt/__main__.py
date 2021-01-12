#!/usr/bin/env python3
"""Executable for linting natural language in markdown files."""

import sys

from markdown_lt import run

if __name__ == '__main__':
    run(sys.argv)
