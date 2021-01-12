#!/usr/bin/env python3
"""Executable for linting natural language in markdown files."""

import getopt
import os
import sys

from markdown_lt import AstMatcher, AstRenderer, Linter


def print_usage(exit_code: int):
    """Prints exectuable usage options."""

    print("Usage: python -m markdown_lt [OPTION]... FILE")
    print(" FILE\t\t\t\tmarkdown file to check")
    print(" Available options:")
    print("  -h, --help\t\t\tprint usage information")
    print("  -l, --language LANG\t\tthe language code of the text")
    print("  -m, --mother-tongue LANG\tthe language code of your mother tongue")
    print("  -w, --wordlist DICT\t\ta newline separated file of valid words")
    print("  -o, --enabled-only\t\tdisable all rules except those specified in -e")
    print("  -e, --enable RULES\t\tcomma-separated list of rule IDs to enable")
    print("  -d, --disable RULES\t\tcomma-separated list of rule IDs to disable")
    print(" Exit code:")
    print("  0\t\t\t\tno errors")
    print("  1\t\t\t\tlanguage errors")
    print("  2\t\t\t\tuser error")
    sys.exit(exit_code)


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print_usage(2)
    if len(sys.argv) == 2 and sys.argv[1] in ['-h', '--help']:
        print_usage(0)

    LANGUAGE = None
    MOTHER_TONGUE = None
    WORDLIST = None
    ENABLED_ONLY = False
    ENABLED_RULES = set()
    DISABLED_RULES = set()
    FILEPATH = None
    try:
        opts, args = getopt.getopt(sys.argv[1:(len(sys.argv) - 1)], "l:m:w:oe:d:",
                                   ["language=", "mother-tongue=", "wordlist=", "enabled-only", "enable", "disable"])
        for opt, arg in opts:
            if opt in ("-l", "--language"):
                LANGUAGE = arg
            elif opt in ("-m", "--mother-tongue"):
                MOTHER_TONGUE = arg
            elif opt in ("-w", "--wordlist"):
                WORDLIST = open(arg).readlines()
            elif opt in ("-o", "--enabled-only"):
                ENABLED_ONLY = True
            elif opt in ("-e", "--enable"):
                ENABLED_RULES = set(arg.split(','))
            elif opt in ("-d", "--disable"):
                DISABLED_RULES = set(arg.split(','))
            else:
                raise RuntimeError("Invalid option/argument: {} {}".format(opt, arg))
        FILEPATH = os.path.abspath(sys.argv[-1])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    ast_renderer = AstRenderer()
    language_tool = Linter(LANGUAGE, MOTHER_TONGUE, WORDLIST, ENABLED_ONLY, ENABLED_RULES, DISABLED_RULES)
    matcher = AstMatcher(language_tool)

    ast = ast_renderer.read(FILEPATH)
    matches = matcher.match(ast)
    print("Found {} matches:\n".format(len(matches)))

    for match in matches:
        print("{}\n".format(match))

    sys.exit(int(len(matches) >= 1))
