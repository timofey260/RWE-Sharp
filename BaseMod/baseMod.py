from BaseMod.geo.geometryEditor import GeometryEditor
from BaseMod.geo.geometryModule import GeoModule
from BaseMod.tiles.tileModule import TileModule
from BaseMod.grid.gridModule import GridModule
from BaseMod.grid.gridUIConnector import GridView
from BaseMod.Palettes.RaspberryDark import RaspberryDark
from BaseMod.Configs import BaseModConfig
from BaseMod.tiles.tileEditor import TileEditor
from BaseMod.tiles.tileExplorer import TileExplorer
from RWESharp.Modify import Mod, ModInfo
from RWESharp.Core import SettingElement
from PySide6.QtGui import QAction


class BaseMod(Mod):
    def __init__(self, manager):
        super().__init__(manager, ModInfo(
            "Base Mod",
            "timofey26.basemod",
            "timofey26",
            "1.0.0",
            "RWE# essentials\nincludes all editors, modules and other\ndisable it at your own risk :3"
        ))
        from BaseMod.geo.geoUIConnectors import GeoUI, GeoViewUI, GeoSettings
        from BaseMod.tiles.tileUIConnectors import TileViewUI, TileUI

        self.geoeditor: GeometryEditor | None = None
        self.geomodule: GeoModule | None = None
        self.geoui: GeoUI | None = None
        self.geoview: GeoViewUI | None = None
        self.geosettings: GeoSettings | None = None

        self.tilemodule: TileModule | None = None
        self.tileview: TileViewUI | None = None
        self.tileeditor: TileViewUI | None = None
        self.tileui: TileUI | None = None

        self.gridmodule: GridModule | None = None
        self.gridui: GridView | None = None

        self.settingtree: SettingElement | None = None
        self.bmconfig: BaseModConfig | None = None

        self.tile_explorer: TileExplorer | None = None
        self.tile_explorer_action: QAction | None = None

    def mod_init(self):
        from BaseMod.geo.geoUIConnectors import GeoUI, GeoViewUI, GeoSettings
        from BaseMod.tiles.tileUIConnectors import TileViewUI, TileUI

        RaspberryDark(self).add_myself()

        self.bmconfig = BaseModConfig(self)
        self.bmconfig.palette.valueChanged.connect(self.manager.change_pallete)

        self.gridmodule = GridModule(self).add_myself()

        self.geomodule = GeoModule(self).add_myself()
        self.geoeditor = GeometryEditor(self)
        self.geoui = GeoUI(self)
        self.geoview = GeoViewUI(self).add_myself()
        self.geoeditor.add_myself(self.geoui)
        self.geosettings = GeoSettings(self)

        self.tile_explorer = TileExplorer(self.manager)
        self.tilemodule = TileModule(self).add_myself()
        self.tileview = TileViewUI(self).add_myself()
        self.tileeditor = TileEditor(self)
        self.tileui = TileUI(self)
        self.tileeditor.add_myself(self.tileui)

        self.tile_explorer_action = QAction("Tile Explorer")
        self.manager.window_menu.addAction(self.tile_explorer_action)
        self.tile_explorer.link_action(self.tile_explorer_action)

        self.gridui = GridView(self).add_myself()

        self.settingtree = SettingElement(self, self.modinfo.title, self.modinfo.name)
        self.settingtree.add_child(SettingElement(self, "Geo", "geo", self.geosettings))
        self.settingtree.add_myself()

