"""Provides a lint matcher for ASTs."""


class AstMatcher:
    """Lint matcher for ASTs."""
    def __init__(self, language_tool):
        self.language_tool = language_tool

    def match(self, ast: list) -> list:
        """Returns lint matches for an AST."""
        return self._match_list(ast)

    def _match(self, string: str) -> list:
        return self.language_tool.check(string)

    def _match_list(self, children: list) -> list:
        matches = []
        for child in children:
            if isinstance(child, dict):
                matches += self._match_dict(child)
            elif isinstance(child, list):
                matches += self._match_list(child)
        return matches

    def _match_dict(self, node: dict) -> list:
        matches = []
        node_type = node["type"]

        if node_type not in ('block_code', 'codespan', 'block_html'):
            if 'text' in node:
                matches += self._match(node['text'])
            if 'alt' in node:
                matches += self._match(node['alt'])

        if 'children' in node:
            children = node['children']
            if isinstance(children, dict):
                matches += self._match_dict(children)
            elif isinstance(children, list):
                matches += self._match_list(children)
        return matches
