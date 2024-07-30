from PySide6.QtCore import Slot, Qt, QCoreApplication
from PySide6.QtGui import QAction, QColor
from PySide6.QtWidgets import QMenu, QCheckBox

from BaseMod.baseMod import BaseMod
from BaseMod.geo.geometryEditor import GeoBlocks, stackables, stackables_all_layers
from BaseMod.geo.ui.geometry_ui import Ui_Geo
from BaseMod.geo.ui.geometry_vis_ui import Ui_GeoView
from BaseMod.geo.ui.geosettings_ui import Ui_Geometry
from BaseMod.geo.GeoConsts import *

from RWESharp.Configurable import IntConfigurable, BoolConfigurable, KeyConfigurable
from RWESharp.Core import SettingsViewer
from RWESharp.Ui import ViewUI, SettingUI, UI
from RWESharp.Utils import paint_svg_qicon

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
        self.editor = self.mod.geoeditor
        self.controls = self.editor.controls

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

        self.editor.drawl1.link_button(self.ui.ToolGeoApplyToL1, self.drawl1_key)
        self.editor.drawl2.link_button(self.ui.ToolGeoApplyToL2, self.drawl2_key)
        self.editor.drawl3.link_button(self.ui.ToolGeoApplyToL3, self.drawl3_key)

        self.editor.toolleft.link_combobox(self.ui.ToolGeoM1Select)
        self.editor.toolright.link_combobox(self.ui.ToolGeoM2Select)

        self.mod.bmconfig.icon_color.valueChanged.connect(self.change_color)
        self.change_color(self.mod.bmconfig.icon_color.value)

        self.controls.wall.link_button(self.ui.ToolGeoWall)
        self.controls.air.link_button(self.ui.ToolGeoAir)
        self.controls.slope.link_button(self.ui.ToolGeoSlope)
        self.controls.floor.link_button(self.ui.ToolGeoFloor)
        self.controls.glass.link_button(self.ui.ToolGeoGlass)

        self.controls.rock.link_button(self.ui.ToolGeoRock)
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
        self.editor.brushsize.link_spinbox(self.ui.Brushsize)
        self.editor.controls.brushsizeup.link_button(self.ui.BrushSizeUp)
        self.editor.controls.brushsizedown.link_button(self.ui.BrushSizeDown)

    def brushsize_minus(self):
        self.ui.Brushsize.stepDown()

    def brushsize_plus(self):
        self.ui.Brushsize.stepUp()

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
    def __init__(self, mod, parent=None):
        super().__init__(mod, parent)
        self.mod: BaseMod
        self.ui = Ui_GeoView()
        self.ui.setupUi(self)
        self.module = self.mod.geomodule

        self.drawlgeo_key = KeyConfigurable(mod, "VIEW_geo.drawlall_key", "Alt+G", "Show geometry")
        self.drawl1_key = KeyConfigurable(mod, "VIEW_geo.drawl1_key", "Alt+1", "Show 1st layer geometry")
        self.drawl2_key = KeyConfigurable(mod, "VIEW_geo.drawl2_key", "Alt+2", "Show 2nd layer geometry")
        self.drawl3_key = KeyConfigurable(mod, "VIEW_geo.drawl3_key", "Alt+3", "Show 3rd layer geometry")
        self.drawlbeams_key = KeyConfigurable(mod, "VIEW_geo.drawl3beamskey", "Alt+b", "Show beams")
        self.drawlpipes_key = KeyConfigurable(mod, "VIEW_geo.drawlpipes_key", "Alt+v", "Show connection pipes")
        self.drawlmisc_key = KeyConfigurable(mod, "VIEW_geo.drawlmisc_key", "Alt+c", "Show other/misc")



        # adding menu and stuff
        self.menu = QMenu("Geometry")
        self.menu_drawlall = QAction("Geo")

        self.menu.addAction(self.menu_drawlall)
        self.menu.addSeparator()
        self.menu_drawl1 = QAction("Layer 1")
        self.module.drawl1.link_button_action(self.ui.VGeoLayer1, self.menu_drawl1, self.drawl1_key)
        self.menu.addAction(self.menu_drawl1)
        self.menu_drawl2 = QAction("Layer 2")
        self.module.drawl2.link_button_action(self.ui.VGeoLayer2, self.menu_drawl2, self.drawl2_key)
        self.menu.addAction(self.menu_drawl2)
        self.menu_drawl3 = QAction("Layer 3")
        self.module.drawl3.link_button_action(self.ui.VGeoLayer3, self.menu_drawl3, self.drawl3_key)
        self.menu.addAction(self.menu_drawl3)
        self.menu.addSeparator()
        self.menu_drawlbeams = QAction("Beams")
        self.module.drawlbeams.link_button_action(self.ui.VGeoBeams, self.menu_drawlbeams, self.drawlbeams_key)
        self.menu.addAction(self.menu_drawlbeams)
        self.menu_drawlpipes = QAction("Paths")
        self.module.drawlpipes.link_button_action(self.ui.VGeoPipes, self.menu_drawlpipes, self.drawlpipes_key)
        self.menu.addAction(self.menu_drawlpipes)
        self.menu_drawlmisc = QAction("Misc")
        self.module.drawlmisc.link_button_action(self.ui.VGeoMisc, self.menu_drawlmisc, self.drawlmisc_key)
        self.menu.addAction(self.menu_drawlmisc)

        self.mod.manager.view_menu.addMenu(self.menu)
        self.ui.VGeoAll.checkStateChanged.connect(self.all_layers)
        self.module.drawoption.link_radio([self.ui.VGeoRWEstyle, self.ui.VGeoOldStyle])

        self.VQuickGeo = QCheckBox()
        self.VQuickGeo.setObjectName(u"VQuickGeo")
        self.VQuickGeo.setText(QCoreApplication.translate("MainWindow", u"Geometry", None))
        self.VQuickGeo.setChecked(True)
        # self.VQuickGeo.checkStateChanged.connect(self.toggle_geo)
        self.mod.add_quickview_option(self.VQuickGeo)

        self.module.drawgeo.link_button_action(self.VQuickGeo, self.menu_drawlall, self.drawlgeo_key)
        self.module.drawAll.link_button(self.ui.VGeoAll)

    @Slot(Qt.CheckState)
    def all_layers(self, state: Qt.CheckState):
        if state == Qt.CheckState.Checked:
            self.module.draw = False
            self.ui.VGeoLayer1.setChecked(True)
            self.ui.VGeoLayer2.setChecked(True)
            self.ui.VGeoLayer3.setChecked(True)
            self.ui.VGeoBeams.setChecked(True)
            self.ui.VGeoPipes.setChecked(True)
            self.ui.VGeoMisc.setChecked(True)
            self.module.draw = True
            self.module.render_module()


class GeoSettings(SettingUI):
    def __init__(self, mod):
        super().__init__(mod)
        self.mod: BaseMod
        self.module = self.mod.geomodule
        self.l1op = IntConfigurable(self, "l1op", int(self.module.opacityl1.default * 255), "Opacity of layer 1")
        self.l2op = IntConfigurable(self, "l2op", int(self.module.opacityl2.default * 255), "Opacity of layer 2")
        self.l3op = IntConfigurable(self, "l3op", int(self.module.opacityl3.default * 255), "Opacity of layer 3")
        self.rgbop = IntConfigurable(self, "rgbop", int(self.module.opacityrgb.default * 255),
                                     "Opacity of all layers on Leditor render option")
        self.opshift = BoolConfigurable(self, "opshift", self.module.opacityshift.default,
                                        "Opacity shift\nOnly change opacity of shown layers\n"
                                        "For example, if layer 1 is hidden, layer 2 will have opacity of layer 1 and "
                                        "layer 3 will have opacity of layer 2")

    def init_ui(self, viewer: SettingsViewer):
        self.ui = Ui_Geometry()
        self.ui.setupUi(viewer)

        self.l1op.link_slider(self.ui.L1op)
        self.l2op.link_slider(self.ui.L2op)
        self.l3op.link_slider(self.ui.L3op)
        self.rgbop.link_slider(self.ui.RGBop)
        self.l1op.link_spinbox(self.ui.L1op2)
        self.l2op.link_slider(self.ui.L2op2)
        self.l3op.link_slider(self.ui.L3op2)
        self.rgbop.link_slider(self.ui.RGBop2)

        self.opshift.link_button(self.ui.OPshift)

        self.ui.graphicsView.add_manager(self.mod.manager, self)
        self.ui.L1show.setChecked(True)
        self.ui.L2show.setChecked(True)
        self.ui.L3show.setChecked(True)
        self.ui.RWEpreview.setChecked(True)

    def apply_values(self):
        self.module.opacityl1.update_value(self.l1op.value / 255)
        self.module.opacityl2.update_value(self.l2op.value / 255)
        self.module.opacityl3.update_value(self.l3op.value / 255)
        self.module.opacityrgb.update_value(self.rgbop.value / 255)
        self.module.opacityshift.update_value(self.opshift.value)
        self.reset_values()

    def reset_values(self):
        self.l1op.update_value_default(int(self.module.opacityl1.value * 255))
        self.l2op.update_value_default(int(self.module.opacityl2.value * 255))
        self.l3op.update_value_default(int(self.module.opacityl3.value * 255))
        self.rgbop.update_value_default(int(self.module.opacityrgb.value * 255))
        self.opshift.update_value_default(self.module.opacityshift.value)

    def reset_values_default(self):
        self.l1op.update_value(int(self.module.opacityl1.default * 255))
        self.l2op.update_value(int(self.module.opacityl2.default * 255))
        self.l3op.update_value(int(self.module.opacityl3.default * 255))
        self.rgbop.update_value(int(self.module.opacityrgb.default * 255))
        self.opshift.update_value(self.module.opacityshift.default)
