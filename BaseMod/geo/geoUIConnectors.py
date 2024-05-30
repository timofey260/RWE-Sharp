from .geometry_ui import Ui_Geo
from .geometry_vis_ui import Ui_GeoView
from PySide6.QtWidgets import QWidget
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
        self.mod.geoviewconfig.drawl1.connect_checkbox(self.ui.VGeoLayer1)
        self.mod.geoviewconfig.drawl2.connect_checkbox(self.ui.VGeoLayer2, self.mod.geoviewconfig.drawl2_key)
        self.mod.geoviewconfig.drawl3.connect_checkbox(self.ui.VGeoLayer3, self.mod.geoviewconfig.drawl3_key)
        self.mod.geoviewconfig.drawlbeams.connect_checkbox(self.ui.VGeoBeams, self.mod.geoviewconfig.drawlbeams_key)
        self.mod.geoviewconfig.drawlpipes.connect_checkbox(self.ui.VGeoPipes, self.mod.geoviewconfig.drawlpipes_key)
        self.mod.geoviewconfig.drawlmisc.connect_checkbox(self.ui.VGeoMisc, self.mod.geoviewconfig.drawlmisc_key)
        self.ui.VGeoAll.checkStateChanged.connect(self.all_layers)
        self.mod.geoviewconfig.drawAll.connect_checkbox(self.ui.VGeoAll)
        self.bgeo = QAction("geo")
        self.bgeo.setShortcut(self.mod.geoviewconfig.drawl1_key.value)
        self.bgeo.triggered.connect(self.mod.geoviewconfig.drawl1.flip)
        self.mod.manager.view_menu.addAction("geo")
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