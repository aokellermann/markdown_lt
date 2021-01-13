"""Provides an AST generator for markdown files."""

import mistune


# pylint: disable=R0903
class AstRenderer:
    """AST renderer for markdown files."""
    def __init__(self, plugins: list = None):
        self.ast_renderer = mistune.create_markdown(renderer='ast', plugins=plugins)

    def parse(self, md_text: str):
        """Returns an AST from a markdown file path."""
        return self.ast_renderer.parse(md_text)
