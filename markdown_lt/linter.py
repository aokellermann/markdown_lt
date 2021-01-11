import language_tool_python


class Linter:
    def __init__(self, language: str, mother_tongue: str, wordlist: list[str], enabled_only: bool,
                 enabled_rules: set[str], disabled_rules: set[str]):
        self.linter = language_tool_python.LanguageTool(language, None, None, wordlist)
        if enabled_only:
            self.linter.enabled_rules_only = True
        if enabled_rules:
            self.linter.enabled_rules = enabled_rules
        if disabled_rules:
            self.linter.disabled_rules = disabled_rules

    def check(self, text: str):
        return self.linter.check(text)
