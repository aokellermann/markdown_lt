"""Provides utilities for markdown_lt."""


def read_utf8(filepath: str) -> str:
    """Returns a utf-8 encoded string of a file."""
    with open(filepath, 'rb') as file:
        return file.read().decode('utf-8')


def readlines_utf8(filepath: str) -> list:
    """Returns a list of utf-8 encoded strings of a file."""
    with open(filepath, 'rb') as file:
        return [word.decode('utf-8') for word in file.readlines()]


def matches_to_string(matches: list):
    """Returns a human readable string of matches."""
    return "Found {} matches{}".format(
        len(matches), "." if not matches else ":\n{}".format("\n\n".join([str(match) for match in matches])))
