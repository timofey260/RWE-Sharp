from PySide6.QtWidgets import QToolButton, QColorDialog
from PySide6.QtGui import QColor
from PySide6.QtCore import Signal


class ColorPicker(QToolButton):
    colorPicked = Signal(QColor)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.color = QColor(0, 0, 0, 255)
        self.set_style()
        self.pressed.connect(self.pick)

    def pick(self):
        c = QColorDialog.getColor(self.color)
        self.color = c
        self.colorPicked.emit(c)
        self.set_style()

    def set_color(self, color: QColor):
        self.color = color
        self.colorPicked.emit(color)
        self.set_style()

    def set_style(self):
        self.setStyleSheet(f"background-color: {self.color.name()}")
        self.setDisabled(True)  # yeah for some reason this works
        self.setEnabled(True)
