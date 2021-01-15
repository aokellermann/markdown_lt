"""Provides utilities for markdown_lt."""


def read_utf8(filepath: str) -> str:
    """Returns a utf-8 encoded string of a file."""
    with open(filepath, 'rb') as file:
        return file.read().decode('utf-8')


def readlines_utf8(filepath: str) -> list:
    """Returns a list of utf-8 encoded strings of a file."""
    with open(filepath, 'rb') as file:
        return [word.decode('utf-8').strip('\n ') for word in file.readlines()]


def match_to_string(match) -> str:
    """Returns a human readable string of a match."""
    s = "{} [{}]".format(match.message, match.ruleId)
    if match.replacements:
        s += '\nSuggestion: {}'.format('; '.join(match.replacements))
    s += '\n{}\n{}'.format(match.context, ' ' * match.offsetInContext + '^' * match.errorLength)
    return s


def matches_to_string(matches: list) -> str:
    """Returns a human readable string of matches."""
    return "Found {} matches{}".format(
        len(matches),
        "." if not matches else ":\n{}".format("\n\n".join([match_to_string(match) for match in matches])))
