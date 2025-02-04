import enum
from core.configTypes.ConfigBase import Configurable
from PySide6.QtGui import QKeySequence, QColor, QAction, QShortcut, QPen
from PySide6.QtWidgets import QAbstractButton, QComboBox, QKeySequenceEdit
from PySide6.QtCore import Signal, Qt, Slot
from widgets.ColorPicker import ColorPicker
from widgets.PenPicker import PenPicker


class KeyConfigurable(Configurable):
    valueChanged = Signal(QKeySequence)
    tooltipChanged = Signal(str)

    def __init__(self, mod, name, default: QKeySequence | str | QKeySequence.StandardKey, description="", shortdesc=""):
        if shortdesc == "":
            shortdesc = description
        self.shortdesc = shortdesc
        default = QKeySequence(default)
        self.buttons: list[QAbstractButton] = []
        super().__init__(mod, name, default, description)

    def save_str_value(self) -> str:
        return self.value.toString()

    def load_str_value(self, text: str) -> None:
        self.value = QKeySequence(text)
        self.valueChanged.emit(self.value)
        self.tooltipChanged.emit(f"{self.description}({self.value.toString()})")

    def update_value(self, value: QKeySequence):
        super().update_value(value)
        self.tooltipChanged.emit(f"{self.description}({self.value.toString()})")
        for i in self.buttons:
            i.setShortcut(self.value)

    def link_button(self, button: QAbstractButton):
        self.buttons.append(button)
        if len(self.description) > 0:
            self.tooltipChanged.connect(button.setToolTip)
            self.tooltipChanged.emit(f"{self.description}({self.value.toString()})")
        button.setShortcut(self.value)

    def link_action(self, action: QAction):
        action.setShortcut(self.value)
        if len(self.description) > 0:
            action.setToolTip(self.description)
        self.valueChanged.connect(action.setShortcut)

    def link_keysequenceedit(self, edit: QKeySequenceEdit):
        edit.setKeySequence(self.value)
        edit.keySequenceChanged.connect(self.update_value)
        self.valueChanged.connect(edit.setKeySequence)

    def link_shortcut(self, shortcut: QShortcut):
        shortcut.setKey(self.value)
        if len(self.description) > 0:
            shortcut.setWhatsThis(self.description)
        self.valueChanged.connect(shortcut.setKey)


class ColorConfigurable(Configurable):
    valueChanged = Signal(QColor)

    def __init__(self, mod, name, default: QColor | str, description=""):
        if isinstance(default, str):
            default = QColor.fromString(default)
        self.value = default
        super().__init__(mod, name, default, description)

    def save_str_value(self) -> str:
        return f"{self.value.red()} {self.value.green()} {self.value.blue()} {self.value.alpha()}"

    def load_str_value(self, text: str) -> None:
        self.value = QColor(*[int(i) for i in text.split()])
        self.valueChanged.emit(self.value)

    def update_value(self, value: QColor):
        super().update_value(value)

    def link_color_picker(self, colorpicker: ColorPicker):
        if len(self.description) > 0:
            colorpicker.setToolTip(self.description)
        colorpicker.set_color(self.value)
        colorpicker.colorPicked.connect(self.update_value)
        self.valueChanged.connect(colorpicker.set_color)


class PenConfigurable(Configurable):
    valueChanged = Signal(QPen)

    def __init__(self, mod, name, default: QPen | None, description=""):
        if default is None:
            default = QPen()
        self.value = default
        super().__init__(mod, name, default, description)

    def save_str_value(self) -> str:
        return (f"{self.value.widthF()} {self.value.style().value}"
                f"{self.value.color().red()} {self.value.color().green()} {self.value.color().blue()} "
                f"{self.value.color().alpha()}")

    def load_str_value(self, text: str) -> None:
        t = text.split()
        self.value = QPen()
        self.value.setWidthF(float(t[0]))
        c = QColor(int(t[2]), int(t[3]), int(t[4]), int(t[5]))
        self.value.setColor(c)
        self.value.setStyle(Qt.PenStyle(int(t[1])))
        self.valueChanged.emit(self.value)

    def update_value(self, value: QPen):
        super().update_value(value)

    def link_pen_picker(self, penpicker: PenPicker):
        if len(self.description) > 0:
            penpicker.setToolTip(self.description)
        penpicker.set_pen(self.value)
        penpicker.penChanged.connect(self.update_value)
        self.valueChanged.connect(penpicker.set_pen)


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
            self.value = self.default
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
        if len(self.description) > 0:
            combobox.setToolTip(self.description)
        if combobox.count() == 0:
            for i in self.enumtouse:
                combobox.addItem(i.name)
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
            self.value = self.default
        self.valueChanged[enum.Enum].emit(self.value)
        self.valueChanged[int].emit(self.value.value)

    def save_str_value(self) -> str:
        return str(self.value.value)
