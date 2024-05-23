from .ConfigBase import ConfigObject
from PySide6.QtCore import Slot


class BoolConfigObject(ConfigObject):
    def __init__(self, name: str, default: bool, description: str=""):
        super().__init__(name, default, description)

    def load_str_value(self, text: str) -> None:
        self.value = text == "1"
        self.valueChanged.emit(self.value)

    def save_str_value(self) -> str:
        return "1" if self.value else "0"

    @Slot(bool)
    def update_value(self, value: bool):
        super().update_value(value)


class StringConfigObject(ConfigObject):
    def __init__(self, name: str, default: str, description: str=""):
        super().__init__(name, default, description)

    def load_str_value(self, text: str) -> None:
        self.value = text
        self.valueChanged.emit(self.value)

    def save_str_value(self) -> str:
        return self.value

    @Slot(str)
    def update_value(self, value: str):
        super().update_value(value)


class IntConfigObject(ConfigObject):
    def __init__(self, name: str, default: int, description: str=""):
        super().__init__(name, default, description)

    def load_str_value(self, text: str) -> None:
        self.value = int(text)
        self.valueChanged.emit(self.value)

    def save_str_value(self) -> str:
        return str(self.value)

    @Slot(int)
    def update_value(self, value: int):
        super().update_value(value)


class FloatConfigObject(ConfigObject):
    def __init__(self, name: str, default: float, description: str=""):
        super().__init__(name, default, description)

    def load_str_value(self, text: str) -> None:
        self.value = float(text)
        self.valueChanged.emit(self.value)

    def save_str_value(self) -> str:
        return str(self.value)

    @Slot(float)
    def update_value(self, value: float):
        super().update_value(value)