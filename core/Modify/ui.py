from PySide6.QtWidgets import QWidget


class UI(QWidget):
    def __init__(self, mod, parent=None):
        super().__init__(parent)
        self.mod = mod


class ViewUI(UI):
    def add_myself(self):
        self.mod.add_vis_ui(self)
        return self
