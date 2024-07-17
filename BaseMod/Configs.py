from RWESharp.Configurable import KeyConfigurable, EnumFlagConfigurable, StringConfigurable, ColorConfigurable
from RWESharp.Core import HotkeyElement
from RWESharp.Core import get_hotkeys_from_pattern
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor


class BaseModConfig:
    def __init__(self, mod):
        self.movement_button = EnumFlagConfigurable(mod, "basemod.movement_button", Qt.MouseButton.MiddleButton,
                                                    Qt.MouseButton,
                                                    "button to move viewport")
        self.main_button = EnumFlagConfigurable(mod, "basemod.main_button", Qt.MouseButton.LeftButton, Qt.MouseButton,
                                                "Main button")
        self.sec_button = EnumFlagConfigurable(mod, "basemod.secondary_button", Qt.MouseButton.RightButton, Qt.MouseButton,
                                               "Secondary button")
        self.icon_color = ColorConfigurable(mod, "basemod.icon_theme", QColor(255, 255, 255, 255))

        self.undo_key = KeyConfigurable(mod, "basemod.undo", "Ctrl+z", "Key to undo")
        self.redo_key = KeyConfigurable(mod, "basemod.redo", "Ctrl+Shift+z", "Key to redo")
        self.save_key = KeyConfigurable(mod, "basemod.save", "Ctrl+s", "Key to save the level")
        self.palette = StringConfigurable(mod, "basemod.palette", "", "palette colors")

        edittab = HotkeyElement(mod, "Edit", "edit").add_myself()
        edittab.add_children_configurables(*get_hotkeys_from_pattern(mod, "basemod"))