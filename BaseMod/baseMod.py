from core.Modify.Mod import Mod
from .geo.GeometryEditor import GeometryEditor
from .geo.geometry_ui import Ui_Geo
from .geo.geometry_vis_ui import Ui_GeoView
from .geo.geometryModule import GeoModule
from PySide6.QtWidgets import QWidget, QCheckBox
from PySide6.QtCore import QCoreApplication


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


class BaseMod(Mod):
    def __init__(self, manager):
        super().__init__(manager)
        self.geoEditor = GeometryEditor(self.manager)
        self.geomodule = GeoModule(self.manager)
        self.geoui = GeoUI(self)
        self.geoview = GeoViewUI(self)

        self.add_editor(self.geoEditor, self.geoui)
        self.add_module(self.geomodule)
        self.add_vis_ui(self.geoview)

        self.init_options()

    def init_options(self):
        self.VQuickGeo = QCheckBox()
        self.VQuickGeo.setObjectName(u"VQuickGeo")
        self.VQuickGeo.setText(QCoreApplication.translate("MainWindow", u"Geometry", None))
        self.VQuickGeo.setChecked(True)
        self.add_quickview_option(self.VQuickGeo)
