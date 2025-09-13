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
from BaseMod.camera.cameraModule import CameraModule
from BaseMod.camera.cameraUIConnectors import CameraViewUI, CameraSettingsUI, CameraUI
from BaseMod.camera.cameraEditor import CameraEditor
from BaseMod.properties.propertiesEditor import PropertiesEditor
from BaseMod.properties.propertiesUIConnectors import PropertiesUI
from BaseMod.light.lightModule import LightModule
from BaseMod.light.lightEditor import LightEditor
from BaseMod.light.lightUIConnectors import LightUI, LightViewUI
from BaseMod.LevelParts import GeoLevelPart, TileLevelPart, PropLevelPart, EffectLevelPart, CameraLevelPart, InfoLevelPart, LightLevelPart
from RWESharp.Modify import Mod, ModInfo
from RWESharp.Core import SettingElement, HotkeyElement, get_hotkeys_from_pattern, PATH_FILES_VIDEOS
from RWESharp.Ui import FunnyVideo
from PySide6.QtGui import QAction, QPixmap
import os

from widgets.Viewport import ViewPort


class BaseMod(Mod):
    def __init__(self, manager, path):
        super().__init__(manager, ModInfo(
            "Base Mod",
            "basemod",
            "timofey26",
            "1.0.0",
            "RWE# essentials\nincludes all editors, modules and other\nCan't and shouldn't be disabled"
        ), path)
        from BaseMod.geo.geoUIConnectors import GeoUI, GeoViewUI, GeoSettings
        from BaseMod.tiles.tileUIConnectors import TileViewUI, TileUI, TileSettings
        from BaseMod.props.propUIConnectors import PropsViewUI
        self.bmconfig = BaseModConfig(self)

        self.preferences = PreferencesUI(self)
        self.rpdark = RaspberryDark(self).add_myself()
        # TODO not to do that ^
        self.geoeditor = GeometryEditor(self)
        self.geoui = GeoUI(self)
        self.geoeditor.add_myself(self.geoui)
        self.geoview = GeoViewUI(self).add_myself()
        self.geosettings = GeoSettings(self)

        self.tileview = TileViewUI(self).add_myself()
        self.tileeditor = TileEditor(self)
        self.tileui = TileUI(self)
        self.tilesettings = TileSettings(self)
        self.tileeditor.add_myself(self.tileui)

        self.effecteditor = EffectEditor(self)
        self.effectui = EffectsUI(self)
        self.effecteditor.add_myself(self.effectui)

        self.propeditor = PropEditor(self)
        self.propui = PropsUI(self)
        self.propeditor.add_myself(self.propui)
        self.propsview = PropsViewUI(self).add_myself()

        self.cameraview = CameraViewUI(self).add_myself()
        self.cameraeditor = CameraEditor(self)
        self.cameraui = CameraUI(self)
        self.cameraeditor.add_myself(self.cameraui)
        self.camerasettings = CameraSettingsUI(self)

        self.lighteditor = LightEditor(self)
        self.lightui = LightUI(self)
        self.lighteditor.add_myself(self.lightui)
        self.lightviewui = LightViewUI(self).add_myself()

        self.propertieseditor = PropertiesEditor(self)
        self.propertiesui = PropertiesUI(self)
        self.propertieseditor.add_myself(self.propertiesui)

        self.sex = QAction("sex(earrape warning)")
        self.sex.triggered.connect(self.sexthing)
        self.bmconfig.funny.valueChanged.connect(self.funnychanged)

        self.gridui = GridView(self).add_myself()

        self.settingtree = SettingElement(self, self.modinfo.title, self.modinfo.id).add_myself()
        SettingElement(self, "Theme", "pref", self.preferences, self.settingtree)
        self.settingtree.add_child(SettingElement(self, "Geo", "geo", self.geosettings))
        self.settingtree.add_child(SettingElement(self, "Tiles", "tiles", self.tilesettings))
        self.settingtree.add_child(SettingElement(self, "Cameras", "cameras", self.camerasettings))

        self.editorsTree = HotkeyElement(self, "Editors", "editors").add_myself()
        geoelement = HotkeyElement(self, "Geometry Editor", "geoedit", parent=self.editorsTree)
        geoelement.add_children_configurables(*get_hotkeys_from_pattern(self, "KEYS_geo"), *get_hotkeys_from_pattern(self, "EDIT_geo"))
        tileelement = HotkeyElement(self, "Tile Editor", "tileedit", parent=self.editorsTree)
        tileelement.add_children_configurables(*get_hotkeys_from_pattern(self, "EDIT_tile"))

        effectelement = HotkeyElement(self, "Effect Editor", "effectedit", parent=self.editorsTree)
        effectelement.add_children_configurables(*get_hotkeys_from_pattern(self, "EDIT_effect"))

        propelement = HotkeyElement(self, "Prop Editor", "propedit", parent=self.editorsTree)
        propelement.add_children_configurables(*get_hotkeys_from_pattern(self, "EDIT_props"))

        self.visualsTree = HotkeyElement(self, "Visuals(Modules)", "visuals").add_myself()
        geoviewelement = HotkeyElement(self, "Geometry View", "geoview", parent=self.visualsTree)
        geoviewelement.add_children_configurables(*get_hotkeys_from_pattern(self, "VIEW_geo"))
        tileviewelement = HotkeyElement(self, "Tiles View", "tileview", parent=self.visualsTree)
        tileviewelement.add_children_configurables(*get_hotkeys_from_pattern(self, "VIEW_tile"))

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

        self.action_propeditor = QAction("Prop Editor")
        self.bmconfig.prop_editor.link_action(self.action_propeditor)
        self.action_propeditor.triggered.connect(lambda: self.manager.change_editor_name("props"))
        self.manager.editors_menu.addAction(self.action_propeditor)

        self.action_cameraeditor = QAction("Camera Editor")
        self.bmconfig.camera_editor.link_action(self.action_cameraeditor)
        self.action_cameraeditor.triggered.connect(lambda: self.manager.change_editor_name("cameras"))
        self.manager.editors_menu.addAction(self.action_cameraeditor)

        self.action_lighteditor = QAction("Light Editor")
        self.bmconfig.light_editor.link_action(self.action_lighteditor)
        self.action_lighteditor.triggered.connect(lambda: self.manager.change_editor_name("light"))
        self.manager.editors_menu.addAction(self.action_lighteditor)

        # scan recent levels
        self.recent = []
        self.bmconfig.recentfiles.valueChanged.connect(self.update_recent)
        self.update_recent()

    def update_recent(self):
        recent = self.bmconfig.recentfiles.value.split("\n")
        self.recent = []
        self.manager.window.ui.menuRecent.clear()
        for i in recent:
            if not os.path.exists(i):
                continue
            self.recent.append(i)
            openlevel = QAction(i, parent=self.manager.window.ui.menuRecent)
            openlevel.triggered.connect(self.open_recent(i))
            self.manager.window.ui.menuRecent.addAction(openlevel)

    def open_recent(self, i):
        def opn():
            self.manager.open_level_from_path(i)
        return opn

    def sexthing(self):
        self.vid = FunnyVideo(self.manager, False, os.path.join(PATH_FILES_VIDEOS, "sex.mp4").replace("\\", "/"), "SEX")

    def funnychanged(self, value):
        if value:
            self.manager.tool_menu.addAction(self.sex)
            return
        if self.sex in self.manager.tool_menu.actions():
            self.manager.tool_menu.removeAction(self.sex)

    def on_save(self, viewport):
        self.bmconfig.windowstate.update_value(self.manager.window.saveState())
        self.bmconfig.windowgeo.update_value(self.manager.window.saveGeometry())
        level = viewport.level
        if level.file is not None and os.path.exists(level.file):
            if level.file in self.recent:
                self.recent.remove(level.file)
            self.recent.insert(0, level.file)
        self.bmconfig.recentfiles.update_value_default("\n".join(self.recent))

    def level_opened(self, viewport: ViewPort):
        GeoModule(self).add_myself(viewport, "geo")
        TileModule(self).add_myself(viewport, "tiles")
        GridModule(self).add_myself(viewport, "grid")
        # # effects
        PropModule(self).add_myself(viewport, "props")
        CameraModule(self).add_myself(viewport, "cameras")
        LightModule(self).add_myself(viewport, "light")

    def mount_levelparts(self, level):
        InfoLevelPart(level)
        GeoLevelPart(level)
        TileLevelPart(level)
        PropLevelPart(level)
        EffectLevelPart(level)
        CameraLevelPart(level)
        LightLevelPart(level)
        if level.file is not None and os.path.exists(level.file):
            if level.file in self.recent:
                self.recent.remove(level.file)
            self.recent.insert(0, level.file)
        self.bmconfig.recentfiles.update_value_default("\n".join(self.recent))
        self.update_recent()
