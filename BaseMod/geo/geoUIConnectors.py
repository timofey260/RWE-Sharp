from .geometry_ui import Ui_Geo
from .geometry_vis_ui import Ui_GeoView
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot, Qt
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
        print(button_to_geo.get(name, "none"))
        self.mod.config.geo_selectedTool.update_value(button_to_geo.get(name, "none"))


class GeoViewUI(QWidget):
    def __init__(self, mod, parent=None):
        super().__init__(parent)
        self.mod: BaseMod = mod
        self.ui = Ui_GeoView()
        self.ui.setupUi(self)
        self.ui.VGeoLayer1.checkStateChanged.connect(self.mod.geomodule.check_l1_change)
        self.ui.VGeoLayer2.checkStateChanged.connect(self.mod.geomodule.check_l2_change)
        self.ui.VGeoLayer3.checkStateChanged.connect(self.mod.geomodule.check_l3_change)
        self.ui.VGeoBeams.checkStateChanged.connect(self.mod.geomodule.check_beams_change)
        self.ui.VGeoPipes.checkStateChanged.connect(self.mod.geomodule.check_pipes_change)
        self.ui.VGeoMisc.checkStateChanged.connect(self.mod.geomodule.check_misc_change)
        self.ui.VGeoAll.checkStateChanged.connect(self.all_layers)

    @Slot(Qt.CheckState)
    def all_layers(self, state: Qt.CheckState):
        if state == Qt.CheckState.Checked:
            self.ui.VGeoLayer1.setChecked(True)
            self.ui.VGeoLayer2.setChecked(True)
            self.ui.VGeoLayer3.setChecked(True)
            self.ui.VGeoBeams.setChecked(True)
            self.ui.VGeoPipes.setChecked(True)
            self.ui.VGeoMisc.setChecked(True)

    @Slot(Qt.CheckState)
    def toggle_geo(self, state: Qt.CheckState):
        if state == Qt.CheckState.Unchecked:
            self.mod.geomodule.check_l1_change(state)
            self.mod.geomodule.check_l2_change(state)
            self.mod.geomodule.check_l3_change(state)
        else:
            self.mod.geomodule.check_l1_change(self.ui.VGeoLayer1.checkState())
            self.mod.geomodule.check_l2_change(self.ui.VGeoLayer2.checkState())
            self.mod.geomodule.check_l3_change(self.ui.VGeoLayer3.checkState())