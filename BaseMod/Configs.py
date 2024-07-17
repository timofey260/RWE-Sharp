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
        self.save_as_key = KeyConfigurable(mod, "basemod.saveas", "Ctrl+Shift+s", "Key to save the level")
        self.open_key = KeyConfigurable(mod, "basemod.open", "Ctrl+o", "Key to open the level")
        self.new_key = KeyConfigurable(mod, "basemod.new", "Ctrl+n", "Key to create new level")
        self.close_key = KeyConfigurable(mod, "basemod.close", "Ctrl+q", "Key to close RWE#")

        self.hotkey_key = KeyConfigurable(mod, "basemod.hotkeys", "Ctrl+Shift+`", "Key to open hotkey menu")
        self.settings_key = KeyConfigurable(mod, "basemod.settings", "Ctrl+`", "Key to open settings menu")
        self.view_key = KeyConfigurable(mod, "basemod.view", "Ctrl+Shift+v", "Key to open view tab")
        self.edit_key = KeyConfigurable(mod, "basemod.edit", "Ctrl+Shift+e", "Key to open edit tab")
        self.prefabs_key = KeyConfigurable(mod, "basemod.prefabs", "Ctrl+Shift+p", "Key to open prefabs tab")
        self.explorer_key = KeyConfigurable(mod, "basemod.explorer", "Ctrl+shift+r", "Key to open settings menu")
        self.palette = StringConfigurable(mod, "basemod.palette", "", "palette colors")

        edittab = HotkeyElement(mod, "Edit", "edit").add_myself()
        edittab.add_children_configurables(*get_hotkeys_from_pattern(mod, "basemod"))