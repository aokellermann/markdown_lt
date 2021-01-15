"""Provides a linter for natural languages."""

from language_tool_python import LanguageTool


class Linter:
    """Linter for natural languages."""
    def __init__(self, language: str, mother_tongue: str, wordlist: set, wordlist_only_current_session: bool,
                 enabled_only: bool, enabled_rules: set, disabled_rules: set):
        self.linter = LanguageTool(language, mother_tongue, None, list(filter(lambda word: word, wordlist)))
        if wordlist_only_current_session:
            self.linter.new_spellings_only_current_session = True
        if enabled_only:
            self.linter.enabled_rules_only = True
        if enabled_rules:
            self.linter.enabled_rules = enabled_rules
        if disabled_rules:
            self.linter.disabled_rules = disabled_rules

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.linter.close()

    def check(self, text: str):
        """Lints a string of text and returns possible issues."""
        return self.linter.check(text)
