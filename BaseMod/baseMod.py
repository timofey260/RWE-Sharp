from core.Modify.Mod import Mod, ModInfo
from .geo.geometryEditor import GeometryEditor
from .geo.geometry_ui import Ui_Geo
from .geo.geometry_vis_ui import Ui_GeoView
from .geo.geometryModule import GeoModule
from .tiles.tileModule import TileModule
from .globalConfig import globalConfig
from PySide6.QtWidgets import QWidget, QCheckBox
from PySide6.QtCore import QCoreApplication, Slot, Qt


class GeoUI(QWidget):
    def __init__(self, mod, parent=None):
        super().__init__(parent)
        self.mod: BaseMod = mod
        self.ui = Ui_Geo()
        self.ui.setupUi(self)


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



class BaseMod(Mod):
    def __init__(self, manager):
        super().__init__(manager, ModInfo(
            "Base Mod",
            "RWE# essentials\nincludes all editors, modules and other\ndisable it at your own risk :3",
            "basemod",
            "1.0.0",
            "timofey26"
        ))

        self.config = globalConfig(self)

        self.geoEditor = GeometryEditor(self)
        self.geomodule = GeoModule(self)
        self.geoui = GeoUI(self)
        self.geoview = GeoViewUI(self)

        self.tilemodule = TileModule(self)

        self.add_editor(self.geoEditor, self.geoui)
        self.add_module(self.geomodule)
        self.add_vis_ui(self.geoview)

        self.add_module(self.tilemodule)

        self.add_config_module(self.config)

        self.init_options()

    def init_options(self):
        self.VQuickGeo = QCheckBox()
        self.VQuickGeo.setObjectName(u"VQuickGeo")
        self.VQuickGeo.setText(QCoreApplication.translate("MainWindow", u"Geometry", None))
        self.VQuickGeo.setChecked(True)
        self.VQuickGeo.checkStateChanged.connect(self.geoview.toggle_geo)
        self.add_quickview_option(self.VQuickGeo)
