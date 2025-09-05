from core.configTypes.ConfigBase import Configurable
from PySide6.QtCore import Slot, Signal, Qt
from PySide6.QtWidgets import QRadioButton, QAbstractButton, QSlider, QSpinBox, QComboBox, QDoubleSpinBox
from PySide6.QtGui import QAction
import json


class BoolConfigurable(Configurable):
    from core.configTypes.QtTypes import KeyConfigurable
    valueChanged = Signal(bool)

    def __init__(self, mod, name: str, default: bool = False, description: str = ""):
        super().__init__(mod, name, default, description)

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

    def link_button(self, button: QAbstractButton, key: KeyConfigurable = None) -> None:
        """
        Makes link between Button and Configurable, where value gets synced
        :param button: button to link
        :param key: optional key to link to button
        :return: None
        """
        button.setChecked(self.value)
        if len(self.description) > 0:
            button.setToolTip(self.description)
        button.toggled.connect(self.update_value)
        self.valueChanged.connect(button.setChecked)
        if key is not None:
            key.link_button(button)

    def link_action(self, action: QAction, key: KeyConfigurable = None) -> None:
        """
        Makes link between Action and Configurable, where state is synced
        :param action: action to link
        :param key: optional key to link to action
        :return: None
        """
        action.setCheckable(True)
        action.setChecked(self.value)
        if len(self.description) > 0:
            action.setToolTip(self.description)
        action.triggered.connect(self.update_value)
        self.valueChanged.connect(action.setChecked)
        if key is not None:
            action.setShortcut(key.value)
            key.valueChanged.connect(action.setShortcut)

    def link_button_action(self, button: QAbstractButton, action: QAction, key: KeyConfigurable = None) -> None:
        """
        Links both Button and Action to a Configurable and syncs the state
        :param button: Button to link
        :param action: action to link
        :param key: optional key to link to action(for it to be used globally)
        :return: None
        """
        self.link_button(button)
        if len(key.description) > 0:
            key.tooltipChanged.connect(button.setToolTip)
            key.tooltipChanged.emit(f"{key.description}({key.value.toString()})")
        self.link_action(action, key)


class StringConfigurable(Configurable):
    valueChanged = Signal(str)

    def __init__(self, mod, name: str, default: str = "", description: str = ""):
        super().__init__(mod, name, default, description)

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

    def __init__(self, mod, name: str, default: int = 0, description: str = ""):
        self.radiolist: list[QRadioButton] = []
        super().__init__(mod, name, default, description)

    def load_str_value(self, text: str) -> None:
        self.value = int(text)
        self.valueChanged.emit(self.value)

    def save_str_value(self) -> str:
        return str(self.value)

    @Slot(int)
    @Slot()
    def update_value(self, value: int | None):
        if value is not None:
            value = int(value)
        if isinstance(self.sender(), QRadioButton) and self.sender() in self.radiolist:
            value = self.radiolist.index(self.sender())
        if self.value == value:
            return
        elif value is not None:
            super().update_value(value)
        if len(self.radiolist) > value > 0 and len(self.radiolist) > 0:
            self.radiolist[value].setChecked(True)

    def link_radio(self, buttons: list[QRadioButton]) -> None:
        """
        Links list of radio buttons to Configurable
        Configurable value becomes index of pressed radio button
        radio buttons will also be synced to current value
        :param buttons: Buttons to press
        :return: None
        """
        self.radiolist = buttons
        self.radiolist[self.value].setChecked(True)
        if len(self.description) > 0:
            for i in buttons:
                i.setToolTip(self.description)
        for i in self.radiolist:
            i.clicked.connect(self.update_value)

    def link_slider(self, slider: QSlider, releaseonly=False):
        """
        Links slider to Configurable
        :param slider: slider
        :param releaseonly: should configurable update only when slider is released
        :return: None
        """
        slider.setValue(self.value)
        if len(self.description) > 0:
            slider.setToolTip(self.description)
        if releaseonly:
            slider.sliderReleased.connect(lambda: self.update_value(slider.value()))
        else:
            slider.valueChanged.connect(self.update_value)
        self.valueChanged.connect(slider.setValue)

    def link_spinbox(self, spin: QSpinBox, releaseonly=False):
        """
        Links spin box to Configurable
        :param spin: Spinbox
        :param releaseonly: should configurable update only when slider/spinbox is released
        :return: None
        """
        spin.setValue(self.value)
        if len(self.description) > 0:
            spin.setToolTip(self.description)
        if releaseonly:
            spin.editingFinished.connect(lambda: self.update_value(spin.value()))
        else:
            spin.valueChanged.connect(self.update_value)
        self.valueChanged.connect(spin.setValue)

    def link_slider_spinbox(self, slider: QSlider, spinbox: QSpinBox, releaseonly=False):
        """
        Links both slider and spinbox to a Configurable
        :param slider: slider to link
        :param spinbox: spinbox to link
        :param releaseonly: should configurable update only when slider/spinbox is released
        """
        self.link_slider(slider, releaseonly)
        self.link_spinbox(spinbox, releaseonly)

    def link_combobox(self, combobox: QComboBox):
        """
        Links combobox with configurable
        :param combobox: Combobox to link
        """
        if len(self.description) > 0:
            combobox.setToolTip(self.description)
        combobox.setCurrentIndex(self.value)
        combobox.currentIndexChanged.connect(self.update_value)
        self.valueChanged.connect(combobox.setCurrentIndex)


class FloatConfigurable(Configurable):
    valueChanged = Signal(float)

    def __init__(self, mod, name: str, default: float = 0, description: str = ""):
        super().__init__(mod, name, default, description)

    def load_str_value(self, text: str) -> None:
        self.value = float(text)
        self.valueChanged.emit(self.value)

    def save_str_value(self) -> str:
        return str(self.value)

    @Slot(float)
    def update_value(self, value: float):
        super().update_value(value)

    def link_doublespinbox(self, spin: QDoubleSpinBox, releaseonly=False):
        """
        Links spin box to Configurable
        :param spin: Double spinbox
        :param releaseonly: should configurable update only when slider/spinbox is released
        :return: None
        """
        spin.setValue(self.value)
        if len(self.description) > 0:
            spin.setToolTip(self.description)
        if releaseonly:
            spin.editingFinished.connect(lambda: self.update_value(spin.value()))
        else:
            spin.valueChanged.connect(self.update_value)
        self.valueChanged.connect(spin.setValue)


class DictConfigurable(Configurable):
    valueChanged = Signal(dict)

    def __init__(self, mod, name: str, default: dict = None, description: str = ""):
        if default is None:
            default = {}
        super().__init__(mod, name, default, description)

    def load_str_value(self, text: str) -> None:
        self.value = json.loads(text)
        self.valueChanged.emit(self.value)

    def save_str_value(self) -> str:
        return json.dumps(self.value)

    @Slot(dict)
    def update_value(self, value: dict):
        super().update_value(value)
