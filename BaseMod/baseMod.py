from BaseMod.geo.geometryEditor import GeometryEditor
from BaseMod.geo.geometryModule import GeoModule
from BaseMod.tiles.tileModule import TileModule
from BaseMod.grid.gridModule import GridModule
from BaseMod.grid.gridUIConnector import GridView
from BaseMod.Palettes.RaspberryDark import RaspberryDark
from PySide6.QtCore import Qt
from RWESharp.Modify import Mod, ModInfo
from RWESharp.Configurable import StringConfigurable, KeyConfigurable, EnumFlagConfigurable
from RWESharp.Core import SettingElement
from BaseMod.Configs import BaseModConfig


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
        from BaseMod.tiles.tileUIConnectors import TileViewUI

        self.geoeditor: GeometryEditor | None = None
        self.geomodule: GeoModule | None = None
        self.geoui: GeoUI | None = None
        self.geoview: GeoViewUI | None = None
        self.geosettings: GeoSettings | None = None

        self.tilemodule: TileModule | None = None
        self.tileview: TileViewUI | None = None

        self.gridmodule: GridModule | None = None
        self.gridui: GridView | None = None

        self.palette: StringConfigurable | None = None

        self.settingtree: SettingElement | None = None
        self.bmconfig: BaseModConfig | None = None

    def mod_init(self):
        from BaseMod.geo.geoUIConnectors import GeoUI, GeoViewUI, GeoSettings
        from BaseMod.tiles.tileUIConnectors import TileViewUI

        RaspberryDark(self).add_myself()
        self.palette = StringConfigurable(self, "palette", "", "palette colors")
        self.palette.valueChanged.connect(self.manager.change_pallete)

        self.gridmodule = GridModule(self).add_myself()

        self.geomodule = GeoModule(self).add_myself()
        self.geoeditor = GeometryEditor(self)
        self.geoui = GeoUI(self)
        self.geoview = GeoViewUI(self).add_myself()
        self.geoeditor.add_myself(self.geoui)
        self.geosettings = GeoSettings(self)

        self.tilemodule = TileModule(self).add_myself()
        self.tileview = TileViewUI(self).add_myself()

        self.gridui = GridView(self).add_myself()

        self.settingtree = SettingElement(self, self.modinfo.title, self.modinfo.name)
        self.settingtree.add_child(SettingElement(self, "Geo", "geo", self.geosettings))
        self.settingtree.add_myself()

        self.bmconfig = BaseModConfig(self)
