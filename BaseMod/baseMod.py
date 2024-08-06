from BaseMod.geo.geometryEditor import GeometryEditor
from BaseMod.geo.geometryModule import GeoModule
from BaseMod.tiles.tileModule import TileModule
from BaseMod.grid.gridModule import GridModule
from BaseMod.grid.gridUIConnector import GridView
from BaseMod.Palettes.RaspberryDark import RaspberryDark
from BaseMod.Configs import BaseModConfig
from BaseMod.tiles.tileEditor import TileEditor
from BaseMod.tiles.tileExplorer import TileExplorer
from BaseMod.effects.effectEditor import EffectEditor
from BaseMod.effects.effectsUIConnector import EffectsUI
from BaseMod.effects.effectExplorer import EffectExplorer
from RWESharp.Modify import Mod, ModInfo
from RWESharp.Core import SettingElement, HotkeyElement, get_hotkeys_from_pattern, PATH_FILES_VIDEOS
from RWESharp.Ui import FunnyVideo
from PySide6.QtGui import QAction
import os


class BaseMod(Mod):
    def __init__(self, manager, path):
        super().__init__(manager, ModInfo(
            "Base Mod",
            "basemod",
            "timofey26",
            "1.0.0",
            "RWE# essentials\nincludes all editors, modules and other\ndisable it at your own risk :3"
        ), path)
        from BaseMod.geo.geoUIConnectors import GeoUI, GeoViewUI, GeoSettings
        from BaseMod.tiles.tileUIConnectors import TileViewUI, TileUI, TileSettings

        self.geoeditor: GeometryEditor | None = None
        self.geomodule: GeoModule | None = None
        self.geoui: GeoUI | None = None
        self.geoview: GeoViewUI | None = None
        self.geosettings: GeoSettings | None = None

        self.tilemodule: TileModule | None = None
        self.tileview: TileViewUI | None = None
        self.tileeditor: TileEditor | None = None
        self.tileui: TileUI | None = None
        self.tilesettings: TileSettings | None = None

        self.effecteditor: EffectEditor | None = None
        self.effectui: EffectsUI | None = None
        self.effect_explorer: EffectExplorer | None = None
        self.effect_explorer_action: QAction | None = None

        self.gridmodule: GridModule | None = None
        self.gridui: GridView | None = None

        self.settingtree: SettingElement | None = None
        self.editorsTree: HotkeyElement | None = None
        self.bmconfig: BaseModConfig | None = None

        self.tile_explorer: TileExplorer | None = None
        self.tile_explorer_action: QAction | None = None

    def mod_init(self):
        from BaseMod.geo.geoUIConnectors import GeoUI, GeoViewUI, GeoSettings
        from BaseMod.tiles.tileUIConnectors import TileViewUI, TileUI, TileSettings

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

        self.tilemodule = TileModule(self).add_myself()
        self.tileeditor = TileEditor(self)
        self.tile_explorer = TileExplorer(self.manager, self.manager.window)
        self.tileview = TileViewUI(self).add_myself()
        self.tileui = TileUI(self)
        self.tilesettings = TileSettings(self)
        self.tileeditor.add_myself(self.tileui)

        self.effecteditor = EffectEditor(self)
        self.effect_explorer = EffectExplorer(self, self.manager.window)
        self.effectui = EffectsUI(self)
        self.effecteditor.add_myself(self.effectui)

        if self.bmconfig.funny.value:
            self.sex = QAction("sex")
            self.manager.tool_menu.addAction(self.sex)
            self.sex.triggered.connect(self.sexthing)

        self.tile_explorer_action = QAction("Tile Explorer")
        self.manager.window_menu.addAction(self.tile_explorer_action)
        self.tile_explorer.link_action(self.tile_explorer_action)
        self.tile_explorer.change_visibility(False)
        self.bmconfig.tileexplorer_key.link_action(self.tile_explorer_action)

        self.effect_explorer_action = QAction("Effect Explorer")
        self.manager.window_menu.addAction(self.effect_explorer_action)
        self.effect_explorer.link_action(self.effect_explorer_action)
        self.effect_explorer.change_visibility(False)
        self.bmconfig.effectexplorer_key.link_action(self.effect_explorer_action)

        self.gridui = GridView(self).add_myself()

        self.settingtree = SettingElement(self, self.modinfo.title, self.modinfo.name).add_myself()
        self.settingtree.add_child(SettingElement(self, "Geo", "geo", self.geosettings))
        self.settingtree.add_child(SettingElement(self, "Tiles", "tiles", self.tilesettings))

        self.editorsTree = HotkeyElement(self, "Editors", "editors").add_myself()
        geoelement = HotkeyElement(self, "Geometry Editor", "geoedit", parent=self.editorsTree)
        geoelement.add_children_configurables(*get_hotkeys_from_pattern(self, "KEYS_geo"), *get_hotkeys_from_pattern(self, "EDIT_geo"))
        tileelement = HotkeyElement(self, "Tile Editor", "tileedit", parent=self.editorsTree)
        tileelement.add_children_configurables(*get_hotkeys_from_pattern(self, "EDIT_tile"))
        self.visualsTree = HotkeyElement(self, "Visuals(Modules)", "visuals").add_myself()
        geoviewelement = HotkeyElement(self, "Geometry View", "geoview", parent=self.visualsTree)
        geoviewelement.add_children_configurables(*get_hotkeys_from_pattern(self, "VIEW_geo"))
        tileviewelement = HotkeyElement(self, "Tiles View", "tileview", parent=self.visualsTree)
        tileviewelement.add_children_configurables(*get_hotkeys_from_pattern(self, "VIEW_tile"))

        effectskeys = HotkeyElement(self, "Effect editor", "effectedit", parent=self.editorsTree)
        effectskeys.add_children_configurables(*get_hotkeys_from_pattern(self, "EDIT_effect"))

        self.action_geoeditor = QAction("Geometry Editor")
        self.bmconfig.geometry_editor.link_action(self.action_geoeditor)
        self.action_geoeditor.triggered.connect(lambda: self.manager.change_editor_name("geo"))
        self.manager.editors_menu.addAction(self.action_geoeditor)

        self.action_tileeditor = QAction("Tile Editor")
        self.bmconfig.tile_editor.link_action(self.action_tileeditor)
        self.action_tileeditor.triggered.connect(lambda: self.manager.change_editor_name("tiles"))
        self.manager.editors_menu.addAction(self.action_tileeditor)

        self.action_effecteditor = QAction("Effect Editor")
        self.bmconfig.effect_editor.link_action(self.action_effecteditor)
        self.action_effecteditor.triggered.connect(lambda: self.manager.change_editor_name("effects"))
        self.manager.editors_menu.addAction(self.action_effecteditor)

    def sexthing(self):
        self.vid = FunnyVideo(self.manager, False, os.path.join(PATH_FILES_VIDEOS, "sex.mp4").replace("\\", "/"), "SEX")