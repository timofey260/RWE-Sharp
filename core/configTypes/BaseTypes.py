from .ConfigBase import Configurable
from PySide6.QtCore import Slot, Signal, Qt
from PySide6.QtWidgets import QCheckBox
import json


class BoolConfigurable(Configurable):
    valueChanged = Signal(bool)

    def __init__(self, name: str, default: bool=False, description: str=""):
        super().__init__(name, default, description)

    def load_str_value(self, text: str) -> None:
        self.value = text == "1"
        self.valueChanged.emit(self.value)

    def save_str_value(self) -> str:
        return "1" if self.value else "0"

    @Slot(bool)
    @Slot(Qt.CheckState)
    def update_value(self, value: bool | Qt.CheckState):
        if isinstance(value, bool):
            super().update_value(value)
        else:
            super().update_value(value == Qt.CheckState.Checked.value)

    def connect_checkbox(self, checkbox: QCheckBox):
        checkbox.setChecked(self.value)
        checkbox.stateChanged.connect(self.update_value)


class StringConfigurable(Configurable):
    valueChanged = Signal(str)

    def __init__(self, name: str, default: str="", description: str=""):
        super().__init__(name, default, description)

    def load_str_value(self, text: str) -> None:
        self.value = text
        self.valueChanged.emit(self.value)

    def save_str_value(self) -> str:
        return self.value

    @Slot(str)
    def update_value(self, value: str):
        super().update_value(value)


class IntConfigurable(Configurable):
    valueChanged = Signal(int)

    def __init__(self, name: str, default: int=0, description: str=""):
        super().__init__(name, default, description)

    def load_str_value(self, text: str) -> None:
        self.value = int(text)
        self.valueChanged.emit(self.value)

    def save_str_value(self) -> str:
        return str(self.value)

    @Slot(int)
    def update_value(self, value: int):
        super().update_value(value)


class FloatConfigurable(Configurable):
    valueChanged = Signal(float)

    def __init__(self, name: str, default: float=0, description: str=""):
        super().__init__(name, default, description)

    def load_str_value(self, text: str) -> None:
        self.value = float(text)
        self.valueChanged.emit(self.value)

    def save_str_value(self) -> str:
        return str(self.value)

    @Slot(float)
    def update_value(self, value: float):
        super().update_value(value)


class DictConfigurable(Configurable):
    valueChanged = Signal(dict)

    def __init__(self, name: str, default: dict=None, description: str= ""):
        if default is None:
            default = {}
        super().__init__(name, default, description)

    def load_str_value(self, text: str) -> None:
        self.value = json.loads(text)
        self.valueChanged.emit(self.value)

    def save_str_value(self) -> str:
        return json.dumps(self.value)

    @Slot(dict)
    def update_value(self, value: dict):
        super().update_value(value)