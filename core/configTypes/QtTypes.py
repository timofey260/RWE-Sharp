import enum
from .ConfigBase import Configurable
from PySide6.QtGui import QKeySequence, QColor, QAction
from PySide6.QtWidgets import QAbstractButton, QComboBox
from PySide6.QtCore import Signal, Qt, Slot


class KeyConfigurable(Configurable):
    valueChanged = Signal(QKeySequence)

    def __init__(self, mod, name, default: QKeySequence | str, description=""):
        if isinstance(default, str):
            default = QKeySequence(default)
        self.buttons: list[QAbstractButton] = []
        super().__init__(mod, name, default, description)

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

    def connect_action(self, obj: QAction):
        obj.setShortcut(self.value)
        self.valueChanged.connect(obj.setShortcut)


class ColorConfigurable(Configurable):
    valueChanged = Signal(QColor)

    def __init__(self, mod, name, default: QColor, description=""):
        self.value = default
        super().__init__(mod, name, default, description)

    def save_str_value(self) -> str:
        return f"{self.value.red()} {self.value.green()} {self.value.blue()} {self.value.alpha()}"

    def load_str_value(self, text: str) -> None:
        self.value = QColor(*[int(i) for i in text.split()])
        self.valueChanged.emit(self.value)

    def update_value(self, value: QColor):
        super().update_value(value)


class EnumConfigurable(Configurable):
    valueChanged = Signal((enum.Enum, ), (int, ))

    def __init__(self, mod, name, default: enum.Enum, enumtouse, description=""):
        self.enumtouse = enumtouse
        super().__init__(mod, name, default, description)
        self.value: enum.Enum

    @Slot(enum.Enum)
    @Slot(int)
    def update_value(self, value: enum.Enum | int):
        if isinstance(value, int):
            value = self.enumtouse(value)
        if self.value == value:
            return
        self.value = value
        self.valueChanged[enum.Enum].emit(self.value)
        self.valueChanged[int].emit(self.value.value)

    def load_str_value(self, text: str) -> None:
        try:
            self.value = self.enumtouse(int(text))
        except ValueError:
            self.value = self.enumtouse(0)
        self.valueChanged[enum.Enum].emit(self.value)
        self.valueChanged[int].emit(self.value.value)

    def save_str_value(self) -> str:
        return str(self.value.value)

    def link_combobox(self, combobox: QComboBox):
        """
        Links combobox with configurable
        Just make sure your enum starts with 0
        :param combobox: Combobox to link
        """
        combobox.setCurrentIndex(self.value.value)
        combobox.currentIndexChanged.connect(self.update_value)
        self.valueChanged[int].connect(combobox.setCurrentIndex)


class EnumFlagConfigurable(Configurable):
    valueChanged = Signal((enum.Flag, ), (int, ))

    def __init__(self, mod, name, default: enum.Flag, enumtouse, description=""):
        self.enumtouse = enumtouse
        super().__init__(mod, name, default, description)

    @Slot(enum.Flag)
    @Slot(int)
    def update_value(self, value: enum.Flag | int):
        if isinstance(value, int):
            value = self.enumtouse(value)
        if self.value == value:
            return
        self.value = value
        self.valueChanged[enum.Flag].emit(self.value)
        self.valueChanged[int].emit(self.value.value)

    def load_str_value(self, text: str) -> None:
        try:
            self.value = self.enumtouse(int(text))
        except ValueError:
            self.value = self.enumtouse(1)
        self.valueChanged[enum.Enum].emit(self.value)
        self.valueChanged[int].emit(self.value.value)

    def save_str_value(self) -> str:
        return str(self.value.value)
