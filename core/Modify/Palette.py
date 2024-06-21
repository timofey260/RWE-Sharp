from PySide6.QtGui import QPalette


class Palette:
    def __init__(self, name, mod):
        self.palette = QPalette()
        self.name = name
        self.mod = mod

    def add_myself(self):
        self.mod.add_palette(self)
        return self
