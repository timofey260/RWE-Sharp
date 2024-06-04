from PySide6.QtCore import Signal, QObject


class Configurable(QObject):
    valueChanged: Signal | None = None
    """
    Activated when value is changed
    """

    def __init__(self, config, name: str, default: ..., description: str=""):
        """
        Abstract object for creating custom config parameters and storing them
        :param config: config to link
        :param name: name of object. should not contain spaces or any special characters
        :param default: default value of variable
        :param description: description in config menu
        """
        super().__init__()
        self.name = name
        self.default = default
        self.value = default
        self.description = description
        if config is not None:
            config.values[name] = self

    def load_str_value(self, text: str) -> None:
        self.valueChanged.emit(self.value)

    def save_str_value(self) -> str:
        ...

    def update_value(self, value: ...):
        if self.value == value:
            return
        self.value = value
        self.valueChanged.emit(self.value)

    def reset_value(self):
        self.update_value(self.default)