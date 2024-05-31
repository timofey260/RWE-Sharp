from .ConfigBase import Configurable
from PySide6.QtCore import Slot, Signal, Qt
from PySide6.QtWidgets import QRadioButton, QAbstractButton
from PySide6.QtGui import QAction
import json
from .QtTypes import KeyConfigurable


class BoolConfigurable(Configurable):
    valueChanged = Signal(bool)

    def __init__(self, config, name: str, default: bool=False, description: str=""):
        super().__init__(config, name, default, description)

    def load_str_value(self, text: str) -> None:
        self.value = text == "1"
        self.valueChanged.emit(self.value)

    def save_str_value(self) -> str:
        return "1" if self.value else "0"

    @Slot(bool)
    @Slot(Qt.CheckState)
    @Slot()
    def update_value(self, value: bool | Qt.CheckState | None = None) -> None:
        if isinstance(value, bool):
            return super().update_value(value)
        elif isinstance(value, Qt.CheckState):
            return super().update_value(value == Qt.CheckState.Checked.value)
        super().update_value(not self.value)

    @Slot()
    def flip(self):
        self.update_value(not self.value)

    def link_button(self, button: QAbstractButton, key: KeyConfigurable=None) -> None:
        """
        Makes link between Button and Configurable, where value gets synced
        :param button: button to link
        :param key: optional key to link to button
        :return: None
        """
        button.setChecked(self.value)
        button.toggled.connect(self.update_value)
        self.valueChanged.connect(button.setChecked)
        if key is not None:
            key.connect_button(button)

    def link_action(self, action: QAction, key: KeyConfigurable=None) -> None:
        """
        Makes link between Action and Configurable, where state is synced
        :param action: action to link
        :param key: optional key to link to action
        :return: None
        """
        action.setCheckable(True)
        action.setChecked(self.value)
        action.triggered.connect(self.update_value)
        self.valueChanged.connect(action.setChecked)
        if key is not None:
            action.setShortcut(key.value)
            key.valueChanged.connect(action.setShortcut)

    def link_button_action(self, button: QAbstractButton, action: QAction, key: KeyConfigurable=None) -> None:
        """
        Links both Button and Action to a Configurable and syncs the state
        :param button: Button to link
        :param action: action to link
        :param key: optional key to link to action(for it to be used globally)
        :return: None
        """
        self.link_button(button)
        self.link_action(action, key)



class StringConfigurable(Configurable):
    valueChanged = Signal(str)

    def __init__(self, config, name: str, default: str="", description: str=""):
        super().__init__(config, name, default, description)

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

    def __init__(self, config, name: str, default: int=0, description: str=""):
        super().__init__(config, name, default, description)
        self.radiolist = []

    def load_str_value(self, text: str) -> None:
        self.value = int(text)
        self.valueChanged.emit(self.value)

    def save_str_value(self) -> str:
        return str(self.value)

    @Slot(int)
    @Slot()
    def update_value(self, value: int | None):
        if isinstance(self.sender(), QRadioButton) and self.sender() in self.radiolist:
            super().update_value(self.radiolist.index(self.sender()))
        elif value is not None:
            super().update_value(value)

    def link_radio(self, buttons: list[QRadioButton]) -> None:
        """
        Links list of radio buttons to Configurable
        Configurable value becomes index of pressed radio
        :param buttons: Buttons to press
        :return: None
        """
        self.radiolist = buttons
        self.radiolist[self.value].setChecked(True)
        for i in self.radiolist:
            i.clicked.connect(self.update_value)


class FloatConfigurable(Configurable):
    valueChanged = Signal(float)

    def __init__(self, config, name: str, default: float=0, description: str=""):
        super().__init__(config, name, default, description)

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

    def __init__(self, config, name: str, default: dict=None, description: str= ""):
        if default is None:
            default = {}
        super().__init__(config, name, default, description)

    def load_str_value(self, text: str) -> None:
        self.value = json.loads(text)
        self.valueChanged.emit(self.value)

    def save_str_value(self) -> str:
        return json.dumps(self.value)

    @Slot(dict)
    def update_value(self, value: dict):
        super().update_value(value)