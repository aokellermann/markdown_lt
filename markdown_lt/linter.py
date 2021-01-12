"""Provides a linter for natural languages."""

import language_tool_python


# pylint: disable=R0903
class Linter:
    """Linter for natural languages."""

    # pylint: disable=R0913
    def __init__(self, language: str, mother_tongue: str, wordlist: list, enabled_only: bool, enabled_rules: set,
                 disabled_rules: set):
        self.linter = language_tool_python.LanguageTool(language, mother_tongue, None, wordlist)
        if enabled_only:
            self.linter.enabled_rules_only = True
        if enabled_rules:
            self.linter.enabled_rules = enabled_rules
        if disabled_rules:
            self.linter.disabled_rules = disabled_rules

    def check(self, text: str):
        """Lints a string of text and returns possible issues."""
        return self.linter.check(text)
