#!/usr/bin/env python3
"""CLI driver for linting natural language in markdown files."""

from markdown_lt import AstMatcher, AstRenderer, Linter


def check(md_text: str,
          language: str = None,
          mother_tongue: str = None,
          wordlist: set = None,
          wordlist_only_current_session: bool = True,
          enabled_only: bool = False,
          enabled_rules: set = None,
          disabled_rules: set = None) -> list:
    """Driver function. Takes in options and returns a list of matches."""

    ast_renderer = AstRenderer()
    language_tool = Linter(language, mother_tongue, wordlist, wordlist_only_current_session, enabled_only,
                           enabled_rules, disabled_rules)
    matcher = AstMatcher(language_tool)

    ast = ast_renderer.parse(md_text)
    matches = matcher.match(ast)
    return matches
