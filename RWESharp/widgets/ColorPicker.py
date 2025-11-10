from PySide6.QtWidgets import QToolButton, QColorDialog
from PySide6.QtGui import QColor
from PySide6.QtCore import Signal
from RWESharp.utils import color_lerp


class ColorPicker(QToolButton):
    colorPicked = Signal(QColor)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.color = QColor(0, 0, 0, 255)
        self.set_style()
        self.pressed.connect(self.pick)

    def pick(self):
        c = QColorDialog.getColor(self.color, options=QColorDialog.ColorDialogOption.ShowAlphaChannel)
        if not c.isValid():
            return
        self.color = c
        self.colorPicked.emit(c)
        self.set_style()

    def set_color(self, color: QColor):
        self.color = color
        self.colorPicked.emit(color)
        self.set_style()

    def set_style(self):
        self.setStyleSheet(f"background-color: {self.colorname.name()}")
        e = self.isEnabled()
        self.setDisabled(True)  # yeah for some reason this works
        self.setEnabled(True)
        self.setEnabled(e)

    @property
    def colorname(self):
        return color_lerp(QColor(0, 0, 0), self.color, self.color.alphaF())
