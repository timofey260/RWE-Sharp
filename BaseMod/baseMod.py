from BaseMod.geo.geometryEditor import GeometryEditor
from BaseMod.geo.geometryModule import GeoModule
from BaseMod.tiles.tileModule import TileModule
from BaseMod.grid.gridModule import GridModule
from BaseMod.grid.gridUIConnector import GridView
from BaseMod.themes.RaspberryDark import RaspberryDark
from BaseMod.Configs import BaseModConfig
from BaseMod.tiles.tileEditor import TileEditor
from BaseMod.props.propModule import PropModule
from BaseMod.props.propEditor import PropEditor
from BaseMod.props.propUIConnectors import PropsUI
from BaseMod.effects.effectEditor import EffectEditor
from BaseMod.effects.effectsUIConnectors import EffectsUI
from BaseMod.themes.preferencesuiconnector import PreferencesUI
from RWESharp.Modify import Mod, ModInfo
from RWESharp.Core import SettingElement, HotkeyElement, get_hotkeys_from_pattern, PATH_FILES_VIDEOS
from RWESharp.Ui import FunnyVideo
from PySide6.QtGui import QAction
from RWESharp.Core import Manager
import os

from widgets.Viewport import ViewPort


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
        # ThemeManager(self).add_myself()
        self.rpdark = RaspberryDark(self).add_myself()
        #TODO not to do that ^
        self.bmconfig = BaseModConfig(self)

        self.geoeditor = GeometryEditor(self)
        self.geoui = GeoUI(self)
        self.geoeditor.add_myself(self.geoui)
        self.geoview = GeoViewUI(self).add_myself()
        # #self.geosettings = GeoSettings(self)

        #self.tileeditor = TileEditor(self)
        # self.tileview = TileViewUI(self).add_myself()
        #self.tileui = TileUI(self)
        # self.tilesettings = TileSettings(self) # todo
        #self.tileeditor.add_myself(self.tileui)
        #
        # self.effecteditor = EffectEditor(self)
        # self.effectui = EffectsUI(self)
        # self.effecteditor.add_myself(self.effectui)
        #
        # self.propeditor = PropEditor(self)
        # self.propui = PropsUI(self)
        # self.propeditor.add_myself(self.propui)

        if self.bmconfig.funny.value:
            self.sex = QAction("sex")
            self.manager.tool_menu.addAction(self.sex)
            self.sex.triggered.connect(self.sexthing)
        return
        # self.gridui = GridView(self).add_myself()

        self.settingtree = SettingElement(self, self.modinfo.title, self.modinfo.name).add_myself()
        SettingElement(self, "Theme", "pref", PreferencesUI(self), self.settingtree)
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

    def on_save(self, viewport):
        self.bmconfig.windowstate.update_value(self.manager.window.saveState())
        self.bmconfig.windowgeo.update_value(self.manager.window.saveGeometry())

    def level_opened(self, viewport: ViewPort):
        GeoModule(self).add_myself(viewport, "geo")
        TileModule(self).add_myself(viewport, "tiles")
        GridModule(self).add_myself(viewport, "grid")
        # # effects
        PropModule(self).add_myself(viewport)
