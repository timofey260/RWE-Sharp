from core.Modify.Mod import Mod, ModInfo
from BaseMod.geo.geometryEditor import GeometryEditor
from BaseMod.geo.geometryModule import GeoModule
from BaseMod.tiles.tileModule import TileModule
from BaseMod.grid.gridModule import GridModule
from BaseMod.grid.gridUIConnector import GridView
from PySide6.QtCore import Qt
from core.configTypes.QtTypes import KeyConfigurable, QtEnumConfigurable


class BaseMod(Mod):
    def __init__(self, manager):
        super().__init__(manager, ModInfo(
            "Base Mod",
            "RWE# essentials\nincludes all editors, modules and other\ndisable it at your own risk :3",
            "basemod",
            "timofey26",
            "1.0.0"
        ))
        from .geo.geoUIConnectors import GeoUI, GeoViewUI
        from .tiles.tileUIConnectors import TileViewUI

        self.geoeditor: GeometryEditor | None = None
        self.geomodule: GeoModule | None = None
        self.geoui: GeoUI | None = None
        self.geoview: GeoViewUI | None = None

        self.tilemodule: TileModule | None = None
        self.tileview: TileViewUI | None = None

        self.gridmodule: GridModule | None = None
        self.gridui: GridView | None = None

        self.movement_button: QtEnumConfigurable | None = None
        self.main_button: QtEnumConfigurable | None = None
        self.sec_button: QtEnumConfigurable | None = None

        self.undo_key: KeyConfigurable | None = None
        self.redo_key: KeyConfigurable | None = None
        self.save_key: KeyConfigurable | None = None

    def pre_mod_init(self):
        pass

    def mod_init(self):
        from .geo.geoUIConnectors import GeoUI, GeoViewUI
        from .tiles.tileUIConnectors import TileViewUI

        self.geomodule = GeoModule(self).add_myself()
        self.geoeditor = GeometryEditor(self)
        self.geoui = GeoUI(self)
        self.geoview = GeoViewUI(self).add_myself()
        self.geoeditor.add_myself(self.geoui)

        self.tilemodule = TileModule(self).add_myself()
        self.tileview = TileViewUI(self).add_myself()

        self.gridmodule = GridModule(self).add_myself()
        self.gridui = GridView(self).add_myself()

        self.movement_button = QtEnumConfigurable(self, "movement_button", Qt.MouseButton.MiddleButton, Qt.MouseButton,
                                                  "button to move viewport")
        self.main_button = QtEnumConfigurable(self, "main_button", Qt.MouseButton.LeftButton, Qt.MouseButton,
                                              "Main button")
        self.sec_button = QtEnumConfigurable(self, "secondary_button", Qt.MouseButton.RightButton, Qt.MouseButton,
                                             "Secondary button")

        self.undo_key = KeyConfigurable(self, "undo", "Ctrl+z", "Key to undo")
        self.redo_key = KeyConfigurable(self, "redo", "Ctrl+Shift+z", "Key to redo")
        self.save_key = KeyConfigurable(self, "save", "Ctrl+s", "Key to save the level")
