def matches_to_string(matches: list):
    """Returns a human readable string of matches."""
    return "Found {} matches{}".format(
        len(matches), "." if not matches else ":\n{}".format("\n\n".join([str(match) for match in matches])))
