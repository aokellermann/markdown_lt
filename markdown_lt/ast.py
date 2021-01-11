import mistune


class AstRenderer:
    def __init__(self, plugins: list = None):
        self.ast_renderer = mistune.create_markdown(renderer='ast', plugins=plugins)

    def read(self, filepath: str):
        return self.ast_renderer.read(filepath)
