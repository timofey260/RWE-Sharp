from .ConfigBase import Configurable
from PySide6.QtGui import QKeySequence, QColor
from PySide6.QtWidgets import QAbstractButton
from PySide6.QtCore import Signal


class KeyConfigurable(Configurable):
    valueChanged = Signal(QKeySequence)
    def __init__(self, name, default: QKeySequence, description=""):
        super().__init__(name, default, description)
        self.buttons: list[QAbstractButton] = []

    def save_str_value(self) -> str:
        return self.value.toString()

    def load_str_value(self, text: str) -> None:
        self.value = QKeySequence(text)
        self.valueChanged.emit(self.value)

    def update_value(self, value: QKeySequence):
        super().update_value(value)
        for i in self.buttons:
            i.setShortcut(self.value)

    def connect_button(self, obj: QAbstractButton):
        self.buttons.append(obj)
        obj.setShortcut(self.value)


class ColorConfigurable(Configurable):
    valueChanged = Signal(QColor)
    def __init__(self, name, default: QColor, description=""):
        super().__init__(name, default, description)
        self.value = default

    def save_str_value(self) -> str:
        return str(self.value)

    def load_str_value(self, text: str) -> None:
        self.value = QColor.fromString(text)
        self.valueChanged.emit(self.value)

    def update_value(self, value: QColor):
        super().update_value(value)


