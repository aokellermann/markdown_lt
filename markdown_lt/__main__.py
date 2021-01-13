#!/usr/bin/env python3
"""Executable for linting natural language in markdown files."""
import getopt
import sys

from markdown_lt import check, matches_to_string


def read_utf8(filepath: str) -> str:
    with open(filepath, 'rb') as file:
        return file.read().decode('utf-8')


def readlines_utf8(filepath: str) -> list:
    with open(filepath, 'rb') as file:
        return [word.decode('utf-8') for word in file.readlines()]


def print_usage():
    """Prints executable usage options."""

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


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print_usage()
        sys.exit(2)
    if len(sys.argv) == 2 and sys.argv[1] in ('-h', '--help'):
        print_usage()
        sys.exit(0)

    language = None
    mother_tongue = None
    wordlist = None
    enabled_only = False
    enabled_rules = None
    disabled_rules = None
    try:
        opts, _ = getopt.getopt(sys.argv[1:-1], "l:m:w:oe:d:",
                                ["language=", "mother-tongue=", "wordlist=", "enabled-only", "enable", "disable"])
        for opt, arg in opts:
            if opt in ("-l", "--language"):
                language = arg
            elif opt in ("-m", "--mother-tongue"):
                mother_tongue = arg
            elif opt in ("-w", "--wordlist"):
                wordlist = set(readlines_utf8(arg))
            elif opt in ("-o", "--enabled-only"):
                enabled_only = True
            elif opt in ("-e", "--enable"):
                enabled_rules = set(arg.split(','))
            elif opt in ("-d", "--disable"):
                disabled_rules = set(arg.split(','))
            else:
                raise RuntimeError("Invalid option/argument: {} {}".format(opt, arg))
    except Exception as err:
        print(err)
        sys.exit(2)

    matches = check(read_utf8(sys.argv[-1]), language, mother_tongue, wordlist, enabled_only, enabled_rules,
                    disabled_rules)
    print(matches_to_string(matches))

    sys.exit(len(matches) >= 1)
