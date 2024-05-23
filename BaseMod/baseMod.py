from core.Modify.Mod import Mod, ModInfo
from .geo.geometryEditor import GeometryEditor
from .geo.geometryModule import GeoModule
from .tiles.tileModule import TileModule
from .globalConfig import globalConfig
from PySide6.QtWidgets import QWidget, QCheckBox
from PySide6.QtCore import QCoreApplication, Slot, Qt


class BaseMod(Mod):
    def __init__(self, manager):
        super().__init__(manager, ModInfo(
            "Base Mod",
            "RWE# essentials\nincludes all editors, modules and other\ndisable it at your own risk :3",
            "basemod",
            "timofey26",
            "1.0.0"
        ))
        from .geo.geoUIConnectors import GeoUI, GeoViewUI

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
