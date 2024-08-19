from RWESharp.Configurable import KeyConfigurable, EnumFlagConfigurable, StringConfigurable, ColorConfigurable, BoolConfigurable
from RWESharp.Core import HotkeyElement, get_hotkeys_from_pattern, ISWIN
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QKeySequence


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

        self.undo_key = KeyConfigurable(mod, "basemod.undo", QKeySequence.StandardKey.Undo, "Undo")
        self.redo_key = KeyConfigurable(mod, "basemod.redo", QKeySequence.StandardKey.Redo, "Redo")
        self.save_key = KeyConfigurable(mod, "basemod.save", QKeySequence.StandardKey.Save, "Save the level")
        self.save_as_key = KeyConfigurable(mod, "basemod.saveas", QKeySequence.StandardKey.SaveAs, "Save level but different")
        self.open_key = KeyConfigurable(mod, "basemod.open", QKeySequence.StandardKey.Open, "Open the level")
        self.new_key = KeyConfigurable(mod, "basemod.new", QKeySequence.StandardKey.New, "New level")
        self.close_key = KeyConfigurable(mod, "basemod.close", QKeySequence.StandardKey.Close, "Close RWE#")
        self.render_key = KeyConfigurable(mod, "basemod.render", "Ctrl+r", "Render")
        self.opendrizzle_key = KeyConfigurable(mod, "basemod.opendrizzle", "Ctrl+Shift+d", "Open Drizzle")

        self.about_key = KeyConfigurable(mod, "basemod.about", QKeySequence.StandardKey.HelpContents, "About menu")

        self.settings_key = KeyConfigurable(mod, "basemod.settings", "Ctrl+`", "Open settings menu")
        self.hotkey_key = KeyConfigurable(mod, "basemod.hotkeys", "Ctrl+Shift+`", "Open hotkey menu")
        self.view_key = KeyConfigurable(mod, "basemod.view", "Ctrl+Shift+v", "Open view tab")
        self.edit_key = KeyConfigurable(mod, "basemod.edit", "Ctrl+Shift+t", "Open edit tab")
        self.prefabs_key = KeyConfigurable(mod, "basemod.prefabs", "Ctrl+Shift+p", "Open prefabs tab")
        self.tileexplorer_key = KeyConfigurable(mod, "basemod.tileexplorer", "Ctrl+shift+r", "Open settings menu")
        self.effectexplorer_key = KeyConfigurable(mod, "basemod.effectexplorer", "Ctrl+shift+e", "Open settings menu")
        self.theme = StringConfigurable(mod, "basemod.palette", "timofey26.basemod.Raspberry Dark", "palette colors")  # "timofey26.basemod.Raspberry Dark"
        self.theme.valueChanged.connect(mod.manager.change_theme)

        self.geometry_editor = KeyConfigurable(mod, "basemod.geo", "1", "Open Geometry editor")
        self.tile_editor = KeyConfigurable(mod, "basemod.tiles", "2", "Open Tile editor")
        self.effect_editor = KeyConfigurable(mod, "basemod.effect", "3", "Open Effect editor")

        self.funny_vid = BoolConfigurable(mod, "basemod.funnyvid", True, "Funny video when you close rwe#")
        self.funny = BoolConfigurable(mod, "basemod.funny", True, "Adds funny")

        edittab = HotkeyElement(mod, "Edit", "edit").add_myself()
        edittab.add_children_configurables(*get_hotkeys_from_pattern(mod, "basemod"))
