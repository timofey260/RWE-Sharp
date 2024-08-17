from core.Application import Application


class Palette:
    def __init__(self, name, mod):
        self.name = name
        self.mod = mod

    def add_myself(self):
        self.mod.add_palette(self)
        return self

    def palette_enable(self):
        pass

    def palette_disable(self):
        pass

    @property
    def app(self) -> Application:
        return self.mod.manager.application
