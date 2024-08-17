from PySide6.QtGui import QPalette


class Palette:
    def __init__(self, name, mod):
        self.palette: QPalette | None = None
        self.name = name
        self.mod = mod
        self.style: str | None = None

    def add_myself(self):
        self.mod.add_palette(self)
        return self
