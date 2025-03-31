import json

from PySide6.QtCore import Slot, Qt, QCoreApplication, Signal
from PySide6.QtGui import QAction, QColor
from PySide6.QtWidgets import QMenu, QCheckBox, QFileDialog, QPushButton

from BaseMod.baseMod import BaseMod
from BaseMod.geo.geometryEditor import GeoBlocks, stackables, stackables_all_layers
from BaseMod.geo.ui.geometry_ui import Ui_Geo
from BaseMod.geo.ui.geometry_vis_ui import Ui_GeoView
from BaseMod.geo.ui.geosettings_ui import Ui_Geometry
from BaseMod.geo.GeoConsts import *

from RWESharp.Configurable import KeyConfigurable, StringConfigurable
from RWESharp.Core import SettingsViewer, CONSTS, PATH_FILES_IMAGES
from RWESharp.Ui import ViewUI, SettingUI, UI
from RWESharp.Utils import paint_svg_qicon
from RWESharp.Configurable import BoolConfigurable, FloatConfigurable, IntConfigurable

import os

button_to_geo = {
    "ToolGeoWall": GeoBlocks.Wall,
    "ToolGeoAir": GeoBlocks.Air,
    "ToolGeoSlope": GeoBlocks.Slope,
    "ToolGeoBeam": GeoBlocks.Beam,
    "ToolGeoFloor": GeoBlocks.Floor,
    "ToolGeoCrack": GeoBlocks.Crack,
    "ToolGeoSpear": GeoBlocks.Spear,
    "ToolGeoRock": GeoBlocks.Rock,
    "ToolGeoGlass": GeoBlocks.Glass,
    "ToolGeoHive": GeoBlocks.Hive,
    "ToolGeoForbidChains": GeoBlocks.ForbidFlyChains,
    "ToolGeoWormGrass": GeoBlocks.WormGrass,
    "ToolGeoWaterfall": GeoBlocks.Waterfall,
    "ToolGeoShortcutEntrance": GeoBlocks.ShortcutEntrance,
    "ToolGeoShortcut": GeoBlocks.Shortcut,
    "ToolGeoDen": GeoBlocks.DragonDen,
    "ToolGeoEntrance": GeoBlocks.Entrance,
    "ToolGeoWraykAMoleHole": GeoBlocks.WhackAMoleHole,
    "ToolGeoGarbageWorm": GeoBlocks.GarbageWormHole,
    "ToolGeoScavHole": GeoBlocks.ScavengerDen,
    "ToolGeoClearStackabls": GeoBlocks.CleanUpper,
    "ToolGeoClearBlocks": GeoBlocks.CleanBlocks,
    "ToolGeoClearLayer": GeoBlocks.CleanLayer,
    "ToolGeoClearAll": GeoBlocks.CleanAll,
    "ToolGeoInvert": GeoBlocks.Inverse,
}


class GeoUI(UI):
    def __init__(self, mod, parent=None):
        super().__init__(mod, parent)
        self.mod: BaseMod
        self.ui = Ui_Geo()
        self.ui.setupUi(self)
        self.controls = None
        self.editor = None

        self.drawl1_key = KeyConfigurable(mod, "EDIT_geo.drawl1_key", "Ctrl+1", "Edit only on layer 1")
        self.drawl2_key = KeyConfigurable(mod, "EDIT_geo.drawl2_key", "Ctrl+2", "Edit only on layer 2")
        self.drawl3_key = KeyConfigurable(mod, "EDIT_geo.drawl3_key", "Ctrl+3", "Edit only on layer 3")

        self.ui.ToolGeoWall.clicked.connect(self.set_tool)
        self.ui.ToolGeoAir.clicked.connect(self.set_tool)
        self.ui.ToolGeoSlope.clicked.connect(self.set_tool)
        self.ui.ToolGeoGlass.clicked.connect(self.set_tool)
        self.ui.ToolGeoDen.clicked.connect(self.set_tool)
        self.ui.ToolGeoEntrance.clicked.connect(self.set_tool)
        self.ui.ToolGeoShortcut.clicked.connect(self.set_tool)
        self.ui.ToolGeoShortcutEntrance.clicked.connect(self.set_tool)
        self.ui.ToolGeoSpear.clicked.connect(self.set_tool)
        self.ui.ToolGeoRock.clicked.connect(self.set_tool)
        self.ui.ToolGeoHive.clicked.connect(self.set_tool)
        self.ui.ToolGeoClearAll.clicked.connect(self.set_tool)
        self.ui.ToolGeoClearLayer.clicked.connect(self.set_tool)
        self.ui.ToolGeoClearStackabls.clicked.connect(self.set_tool)
        self.ui.ToolGeoClearBlocks.clicked.connect(self.set_tool)
        self.ui.ToolGeoScavHole.clicked.connect(self.set_tool)
        self.ui.ToolGeoGarbageWorm.clicked.connect(self.set_tool)
        self.ui.ToolGeoWormGrass.clicked.connect(self.set_tool)
        self.ui.ToolGeoForbidChains.clicked.connect(self.set_tool)
        self.ui.ToolGeoCrack.clicked.connect(self.set_tool)
        self.ui.ToolGeoBeam.clicked.connect(self.set_tool)
        self.ui.ToolGeoFloor.clicked.connect(self.set_tool)
        self.ui.ToolGeoWraykAMoleHole.clicked.connect(self.set_tool)
        self.ui.ToolGeoInvert.clicked.connect(self.set_tool)

        self.mod.bmconfig.icon_color.valueChanged.connect(self.change_color)
        self.change_color(self.mod.bmconfig.icon_color.value)

        self.ui.BrushSizeUp.clicked.connect(self.ui.Brushsize.stepUp)
        self.ui.BrushSizeDown.clicked.connect(self.ui.Brushsize.stepDown)

    def editor_linked(self, editor):
        self.editor = editor
        self.controls = self.editor.controls

        self.controls.rotate.link_button(self.ui.RotateRight)
        self.controls.rotate_back.link_button(self.ui.RotateLeft)

        self.controls.nextlayer.link_button(self.ui.NextLayer)
        self.controls.prevlayer.link_button(self.ui.PreviousLayer)

        self.controls.wall.link_button(self.ui.ToolGeoWall)
        self.controls.air.link_button(self.ui.ToolGeoAir)
        self.controls.slope.link_button(self.ui.ToolGeoSlope)
        self.controls.floor.link_button(self.ui.ToolGeoFloor)
        self.controls.glass.link_button(self.ui.ToolGeoGlass)

        self.controls.rock.link_button(self.ui.ToolGeoRock)
        self.controls.beam.link_button(self.ui.ToolGeoBeam)
        self.controls.spear.link_button(self.ui.ToolGeoSpear)
        self.controls.shortcut.link_button(self.ui.ToolGeoShortcut)
        self.controls.shortcut_entrance.link_button(self.ui.ToolGeoShortcutEntrance)
        self.controls.dragon_den.link_button(self.ui.ToolGeoDen)
        self.controls.fly_chains.link_button(self.ui.ToolGeoForbidChains)
        self.controls.fly_hive.link_button(self.ui.ToolGeoHive)
        self.controls.scav_hole.link_button(self.ui.ToolGeoScavHole)
        self.controls.garbage_worm_den.link_button(self.ui.ToolGeoGarbageWorm)
        self.controls.whack_a_mole_hole.link_button(self.ui.ToolGeoWraykAMoleHole)
        self.controls.worm_grass.link_button(self.ui.ToolGeoWormGrass)
        self.controls.entrance.link_button(self.ui.ToolGeoEntrance)
        self.controls.waterfall.link_button(self.ui.ToolGeoWaterfall)

        self.controls.clear_all.link_button(self.ui.ToolGeoClearAll)
        self.controls.clear_upper.link_button(self.ui.ToolGeoClearStackabls)
        self.controls.clear_blocks.link_button(self.ui.ToolGeoClearBlocks)
        self.controls.clear_layer.link_button(self.ui.ToolGeoClearLayer)
        self.controls.inverse.link_button(self.ui.ToolGeoInvert)
        self.controls.mirror.link_button(self.ui.ToolGeoMirror)

        self.ui.RotateRight.clicked.connect(self.editor.rotate)
        self.ui.RotateLeft.clicked.connect(self.editor.rotate_back)

        self.ui.NextLayer.clicked.connect(self.editor.next_layer)
        self.ui.PreviousLayer.clicked.connect(self.editor.prev_layer)

        self.editor.brushsize.link_spinbox(self.ui.Brushsize)
        self.editor.controls.brushsizeup.link_button(self.ui.BrushSizeUp)
        self.editor.controls.brushsizedown.link_button(self.ui.BrushSizeDown)

        self.editor.drawl1.link_button(self.ui.ToolGeoApplyToL1, self.drawl1_key)
        self.editor.drawl2.link_button(self.ui.ToolGeoApplyToL2, self.drawl2_key)
        self.editor.drawl3.link_button(self.ui.ToolGeoApplyToL3, self.drawl3_key)

        self.editor.toolleft.link_combobox(self.ui.ToolGeoM1Select)
        self.editor.toolright.link_combobox(self.ui.ToolGeoM2Select)

    def change_color(self, color: QColor):
        items = [IMG_PEN, IMG_BRUSH, IMG_BUCKET, IMG_LINE, IMG_RECT, IMG_RECT_HOLLOW, IMG_CIRCLE, IMG_CIRCLE_HOLLOW]
        for i in range(8):
            self.ui.ToolGeoM1Select.setItemIcon(i, paint_svg_qicon(items[i], color))
            self.ui.ToolGeoM2Select.setItemIcon(i, paint_svg_qicon(items[i], color))

    @Slot()
    def set_tool(self):
        name = self.sender().objectName()
        block = button_to_geo.get(name, GeoBlocks.Wall)
        self.editor.block.update_value(block)

        self.ui.ToolGeoApplyToL1.setEnabled(True)
        self.ui.ToolGeoApplyToL2.setEnabled(True)
        self.ui.ToolGeoApplyToL3.setEnabled(True)
        if block in stackables and block not in stackables_all_layers:
            self.ui.ToolGeoApplyToL2.setEnabled(False)
            self.ui.ToolGeoApplyToL3.setEnabled(False)


class GeoViewUI(ViewUI):
    render = Signal()

    def __init__(self, mod, parent=None):
        super().__init__(mod, parent)
        self.mod: BaseMod
        self.ui = Ui_GeoView()
        self.ui.setupUi(self)

        self.drawgeo = BoolConfigurable(mod, "VIEW_geo.drawgeo", True, "Draw geometry")
        self.drawAll = BoolConfigurable(mod, "VIEW_geo.drawall", False, "Draw all layers")
        self.drawl1 = BoolConfigurable(mod, "VIEW_geo.drawl1", True, "Draw layer 1")
        self.drawl2 = BoolConfigurable(mod, "VIEW_geo.drawl2", True, "Draw layer 2")
        self.drawl3 = BoolConfigurable(mod, "VIEW_geo.drawl3", True, "Draw layer 3")
        self.opacityl1 = FloatConfigurable(mod, "VIEW_geo.opacityl1", .9, "Opacity of the first layer")
        self.opacityl2 = FloatConfigurable(mod, "VIEW_geo.opacityl2", .5, "Opacity of the second layer")
        self.opacityl3 = FloatConfigurable(mod, "VIEW_geo.opacityl3", .2, "Opacity of the third layer")
        self.opacityrgb = FloatConfigurable(mod, "VIEW_geo.opacityrgb", .5,
                                            "Opacity of all layers on old rendering option")

        self.drawlbeams = BoolConfigurable(mod, "VIEW_geo.drawlbeams", True, "Draw Beams")
        self.drawlpipes = BoolConfigurable(mod, "VIEW_geo.drawlpipes", True, "Draw pipes")
        self.drawlmisc = BoolConfigurable(mod, "VIEW_geo.drawlmisc", True, "Draw rocks, spears etc")

        self.drawoption = IntConfigurable(mod, "VIEW_geo.drawOption", 0, "method of drawing")
        self.opacityshift = BoolConfigurable(mod, "VIEW_geo.opacityShift", True,
                                             "Does not change opacity of hidden layers")

        self.drawlgeo_key = KeyConfigurable(mod, "VIEW_geo.drawlall_key", "Alt+G", "Show geometry")
        self.drawl1_key = KeyConfigurable(mod, "VIEW_geo.drawl1_key", "Alt+1", "Show 1st layer geometry")
        self.drawl2_key = KeyConfigurable(mod, "VIEW_geo.drawl2_key", "Alt+2", "Show 2nd layer geometry")
        self.drawl3_key = KeyConfigurable(mod, "VIEW_geo.drawl3_key", "Alt+3", "Show 3rd layer geometry")
        self.drawlbeams_key = KeyConfigurable(mod, "VIEW_geo.drawl3beamskey", "Alt+z", "Show beams")
        self.drawlpipes_key = KeyConfigurable(mod, "VIEW_geo.drawlpipes_key", "Alt+x", "Show connection pipes")
        self.drawlmisc_key = KeyConfigurable(mod, "VIEW_geo.drawlmisc_key", "Alt+v", "Show other/misc")

        self.imagepath = StringConfigurable(mod, "VIEW_geo.imagepath", os.path.join(PATH_FILES_IMAGES, CONSTS.get("geo_image_config", {}).get("image")), "Geo Image path")
        self.imagepath.valueChanged.connect(mod.geoeditor.update_geo_texture)

        self.draw = True

        # adding menu and stuff
        self.menu = QMenu("Geometry")
        self.menu_drawlall = QAction("Geo")

        self.menu.addAction(self.menu_drawlall)
        self.menu.addSeparator()
        self.menu_drawl1 = QAction("Layer 1")
        self.drawl1.link_button_action(self.ui.VGeoLayer1, self.menu_drawl1, self.drawl1_key)
        self.menu.addAction(self.menu_drawl1)
        self.menu_drawl2 = QAction("Layer 2")
        self.drawl2.link_button_action(self.ui.VGeoLayer2, self.menu_drawl2, self.drawl2_key)
        self.menu.addAction(self.menu_drawl2)
        self.menu_drawl3 = QAction("Layer 3")
        self.drawl3.link_button_action(self.ui.VGeoLayer3, self.menu_drawl3, self.drawl3_key)
        self.menu.addAction(self.menu_drawl3)
        self.menu.addSeparator()
        self.menu_drawlbeams = QAction("Beams")
        self.drawlbeams.link_button_action(self.ui.VGeoBeams, self.menu_drawlbeams, self.drawlbeams_key)
        self.menu.addAction(self.menu_drawlbeams)
        self.menu_drawlpipes = QAction("Paths")
        self.drawlpipes.link_button_action(self.ui.VGeoPipes, self.menu_drawlpipes, self.drawlpipes_key)
        self.menu.addAction(self.menu_drawlpipes)
        self.menu_drawlmisc = QAction("Misc")
        self.drawlmisc.link_button_action(self.ui.VGeoMisc, self.menu_drawlmisc, self.drawlmisc_key)
        self.menu.addAction(self.menu_drawlmisc)

        self.mod.manager.view_menu.addMenu(self.menu)
        self.ui.VGeoAll.checkStateChanged.connect(self.all_layers)
        self.drawoption.link_radio([self.ui.VGeoRWEstyle, self.ui.VGeoOldStyle])

        self.VQuickGeo = QCheckBox()
        self.VQuickGeo.setObjectName(u"VQuickGeo")
        self.VQuickGeo.setText(QCoreApplication.translate("MainWindow", u"Geometry", None))
        self.VQuickGeo.setChecked(True)
        self.mod.add_quickview_option(self.VQuickGeo)

        self.drawgeo.link_button_action(self.VQuickGeo, self.menu_drawlall, self.drawlgeo_key)
        self.drawAll.link_button(self.ui.VGeoAll)

        self.drawgeo.valueChanged.connect(self.hide_geo)

    @Slot()
    def hide_geo(self):
        self.draw = False
        self.drawl1.update_value(self.drawgeo.value)
        self.drawl2.update_value(self.drawgeo.value)
        self.drawl3.update_value(self.drawgeo.value)
        self.draw = True

    @Slot(Qt.CheckState)
    def all_layers(self, state: Qt.CheckState):
        if state == Qt.CheckState.Checked:
            self.draw = False
            self.ui.VGeoLayer1.setChecked(True)
            self.ui.VGeoLayer2.setChecked(True)
            self.ui.VGeoLayer3.setChecked(True)
            self.ui.VGeoBeams.setChecked(True)
            self.ui.VGeoPipes.setChecked(True)
            self.ui.VGeoMisc.setChecked(True)
            self.draw = True
            self.render.emit()

    def showlayer(self, currentlayer):
        self.drawl1.update_value(currentlayer == 0)
        self.drawl2.update_value(currentlayer <= 1)
        self.drawl3.update_value(True)


class GeoSettings(SettingUI):
    def __init__(self, mod):
        super().__init__(mod)
        self.mod: BaseMod
        self.geoviewui = self.mod.geoview
        l1 = lambda x: int(x * 255)
        l2 = lambda x: x / 255
        self.l1op = SettingUI.ManageableSetting(
            IntConfigurable(None, "l1op", 0, "Opacity of layer 1"),
            self.geoviewui.opacityl1, l1, l2).add_myself(self)
        self.l2op = SettingUI.ManageableSetting(
            IntConfigurable(None, "l2op", 0, "Opacity of layer 2"),
            self.geoviewui.opacityl2, l1, l2).add_myself(self)
        self.l3op = SettingUI.ManageableSetting(
            IntConfigurable(None, "l3op", 0, "Opacity of layer 3"),
            self.geoviewui.opacityl3, l1, l2).add_myself(self)
        self.rgbop = SettingUI.ManageableSetting(
            IntConfigurable(None, "rgbop", 0, "Opacity of all layers on Leditor render option"),
            self.geoviewui.opacityrgb, l1, l2).add_myself(self)
        self.opshift = SettingUI.ManageableSetting(
            BoolConfigurable(None, "opshift", False,
                             "Opacity shift\nOnly change opacity of shown layers\n"
                             "For example, if layer 1 is hidden, layer 2 will have opacity of layer 1 and "
                             "layer 3 will have opacity of layer 2"),
            self.geoviewui.opacityshift).add_myself(self)
        self.imagepath = SettingUI.ManageableSetting(
            StringConfigurable(None, "imgpath", "", "Image Path"), self.geoviewui.imagepath).add_myself(self)
        self.reset_values()
        self.mod.geoeditor.update_geo_texture()

    def init_ui(self, viewer: SettingsViewer):
        self.ui = Ui_Geometry()
        self.ui.setupUi(viewer)
        self.ui.ChangeImage.clicked.connect(self.change_spritesheet)

        self.l1op.setting.link_slider_spinbox(self.ui.L1op, self.ui.L1op2)
        self.l2op.setting.link_slider_spinbox(self.ui.L2op, self.ui.L2op2)
        self.l3op.setting.link_slider_spinbox(self.ui.L3op, self.ui.L3op2)
        self.rgbop.setting.link_slider_spinbox(self.ui.RGBop, self.ui.RGBop2)

        self.opshift.setting.link_button(self.ui.OPshift)
        self.imagepath.setting.valueChanged.connect(self.ui.graphicsView.update_pixmaps)

        self.ui.graphicsView.add_manager(self.mod.manager, self)
        self.ui.L1show.setChecked(True)
        self.ui.L2show.setChecked(True)
        self.ui.L3show.setChecked(True)
        self.ui.RWEpreview.setChecked(True)

    def change_spritesheet(self):
        file_path, _ = QFileDialog.getOpenFileName(self.ui.ChangeImage, "Select Geometry Image", PATH_FILES_IMAGES, "Images (*.png; *.jpg)")
        if file_path:
            self.imagepath.setting.update_value(file_path)
            # with open("files/Consts.json", "r+") as f:
            #     data = json.load(f)
            #     data["geo_image_config"]["image"] = file_path
            #     f.seek(0)
            #     json.dump(data, f, indent=4)
            #     f.truncate()

        # hey timo do that thing you said youre gonna do
        # oki
