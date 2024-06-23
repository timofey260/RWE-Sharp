from RWESharp.Configurable import KeyConfigurable, EnumFlagConfigurable, StringConfigurable
from PySide6.QtCore import Qt


class BaseModConfig:
    def __init__(self, mod):
        self.movement_button = EnumFlagConfigurable(mod, "movement_button", Qt.MouseButton.MiddleButton,
                                                    Qt.MouseButton,
                                                    "button to move viewport")
        self.main_button = EnumFlagConfigurable(mod, "main_button", Qt.MouseButton.LeftButton, Qt.MouseButton,
                                                "Main button")
        self.sec_button = EnumFlagConfigurable(mod, "secondary_button", Qt.MouseButton.RightButton, Qt.MouseButton,
                                               "Secondary button")

        self.undo_key = KeyConfigurable(mod, "undo", "Ctrl+z", "Key to undo")
        self.redo_key = KeyConfigurable(mod, "redo", "Ctrl+Shift+z", "Key to redo")
        self.save_key = KeyConfigurable(mod, "save", "Ctrl+s", "Key to save the level")
        self.palette = StringConfigurable(mod, "palette", "", "palette colors")