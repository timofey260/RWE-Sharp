from .geometry_ui import Ui_Geo
from .geometry_vis_ui import Ui_GeoView
from PySide6.QtWidgets import QWidget, QMenu
from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QAction
from ..baseMod import BaseMod


button_to_geo = {
    "ToolGeoWall": "wall",
    "ToolGeoAir": "air",
    "ToolGeoSlope": "slope",
    "ToolGeoBeam": "beam",
    "ToolGeoFloor": "floor",
    "ToolGeoCrack": "crack",
    "ToolGeoSpear": "spear",
    "ToolGeoRock": "rock",
    "ToolGeoGlass": "glass",
    "ToolGeoHive": "hive",
    "ToolGeoForbidChains": "forbidchains",
    "ToolGeoWormGrass": "wormgrass",
    "ToolGeoShortcutEntrance": "shortcutentrance",
    "ToolGeoShortcut": "shortcut",
    "ToolGeoDen": "den",
    "ToolGeoEntrance": "entrance",
    "ToolGeoWraykAMoleHole": "wmh",
    "ToolGeoGarbageWorm": "worm",
    "ToolGeoScavHole": "scav",
    "ToolGeoClearUpperLayer": "cleanupper",
    "ToolGeoClearLayer": "cleanlayer",
    "ToolGeoClearAll": "cleanall",
}


class GeoUI(QWidget):
    def __init__(self, mod, parent=None):
        super().__init__(parent)
        self.mod: BaseMod = mod
        self.ui = Ui_Geo()
        self.ui.setupUi(self)

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
        self.ui.ToolGeoClearUpperLayer.clicked.connect(self.set_tool)
        self.ui.ToolGeoScavHole.clicked.connect(self.set_tool)
        self.ui.ToolGeoGarbageWorm.clicked.connect(self.set_tool)
        self.ui.ToolGeoWormGrass.clicked.connect(self.set_tool)
        self.ui.ToolGeoForbidChains.clicked.connect(self.set_tool)
        self.ui.ToolGeoCrack.clicked.connect(self.set_tool)
        self.ui.ToolGeoBeam.clicked.connect(self.set_tool)
        self.ui.ToolGeoFloor.clicked.connect(self.set_tool)
        self.ui.ToolGeoWraykAMoleHole.clicked.connect(self.set_tool)

    @Slot()
    def set_tool(self):
        name = self.sender().objectName()
        self.mod.geoconfig.selectedTool.update_value(button_to_geo.get(name, "none"))


class GeoViewUI(QWidget):
    def __init__(self, mod, parent=None):
        super().__init__(parent)
        self.mod: BaseMod = mod
        self.ui = Ui_GeoView()
        self.ui.setupUi(self)

        # adding menu and stuff
        self.menu = QMenu("Geometry")
        self.menu_drawl1 = QAction("Layer 1")
        self.mod.geoviewconfig.drawl1.link_button_action(self.ui.VGeoLayer1, self.menu_drawl1, self.mod.geoviewconfig.drawl1_key)
        self.menu.addAction(self.menu_drawl1)
        self.menu_drawl2 = QAction("Layer 2")
        self.mod.geoviewconfig.drawl2.link_button_action(self.ui.VGeoLayer2, self.menu_drawl2, self.mod.geoviewconfig.drawl2_key)
        self.menu.addAction(self.menu_drawl2)
        self.menu_drawl3 = QAction("Layer 3")
        self.mod.geoviewconfig.drawl3.link_button_action(self.ui.VGeoLayer3, self.menu_drawl3, self.mod.geoviewconfig.drawl3_key)
        self.menu.addAction(self.menu_drawl3)
        self.menu.addSeparator()
        self.menu_drawlbeams = QAction("Beams")
        self.mod.geoviewconfig.drawlbeams.link_button_action(self.ui.VGeoBeams, self.menu_drawlbeams, self.mod.geoviewconfig.drawlbeams_key)
        self.menu.addAction(self.menu_drawlbeams)
        self.menu_drawlpipes = QAction("Paths")
        self.mod.geoviewconfig.drawlpipes.link_button_action(self.ui.VGeoPipes, self.menu_drawlpipes, self.mod.geoviewconfig.drawlpipes_key)
        self.menu.addAction(self.menu_drawlpipes)
        self.menu_drawlmisc = QAction("Misc")
        self.mod.geoviewconfig.drawlmisc.link_button_action(self.ui.VGeoMisc, self.menu_drawlmisc, self.mod.geoviewconfig.drawlmisc_key)
        self.menu.addAction(self.menu_drawlmisc)
        self.mod.manager.view_menu.addMenu(self.menu)
        self.ui.VGeoAll.checkStateChanged.connect(self.all_layers)
        self.mod.geoviewconfig.drawAll.link_button(self.ui.VGeoAll)
        # self.mod.manager.window.ui.menuFile.addAction(self.bgeo)


    @Slot(Qt.CheckState)
    def all_layers(self, state: Qt.CheckState):
        if state == Qt.CheckState.Checked:
            # todo remove freezes
            self.mod.geomodule.draw = False
            self.ui.VGeoLayer1.setChecked(True)
            self.ui.VGeoLayer2.setChecked(True)
            self.ui.VGeoLayer3.setChecked(True)
            self.ui.VGeoBeams.setChecked(True)
            self.ui.VGeoPipes.setChecked(True)
            self.ui.VGeoMisc.setChecked(True)
            self.mod.geomodule.draw = True
            self.mod.geomodule.render_module()

    @Slot(Qt.CheckState)
    def toggle_geo(self, state: Qt.CheckState):
        v = state == Qt.CheckState.Checked
        self.mod.geoviewconfig.drawl1.update_value(v)
        self.mod.geoviewconfig.drawl2.update_value(v)
        self.mod.geoviewconfig.drawl3.update_value(v)