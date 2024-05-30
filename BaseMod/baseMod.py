from core.Modify.Mod import Mod, ModInfo
from .geo.geometryEditor import GeometryEditor
from .geo.geometryModule import GeoModule
from .geo.geoConfig import GeoConfig, GeoViewConfig

from .tiles.tileModule import TileModule
from .tiles.tileConfig import TileViewConfig

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
        from .tiles.tileUIConnectors import TileViewUI
        self.config: globalConfig

        self.geoconfig: GeoConfig | None = None
        self.geoeditor: GeometryEditor | None = None
        self.geomodule: GeoModule | None = None
        self.geoui: GeoUI | None = None
        self.geoview: GeoViewUI | None = None
        self.geoviewconfig: GeoViewConfig | None = None

        self.tilemodule: TileModule | None = None
        self.tileview: TileViewUI | None = None
        self.tileviewconfig: TileViewConfig | None = None

    def pre_mod_init(self):
        self.config = globalConfig(self)
        self.geoconfig = GeoConfig(self)
        self.geoviewconfig = GeoViewConfig(self)
        self.tileviewconfig = TileViewConfig(self)
        self.add_config_module(self.config)
        self.add_config_module(self.geoconfig)
        self.add_config_module(self.geoviewconfig)
        self.add_config_module(self.tileviewconfig)

    def mod_init(self):
        from .geo.geoUIConnectors import GeoUI, GeoViewUI
        from .tiles.tileUIConnectors import TileViewUI

        self.geomodule = GeoModule(self)
        self.geoui = GeoUI(self)
        self.geoview = GeoViewUI(self)
        self.geoeditor = GeometryEditor(self)

        self.tilemodule = TileModule(self)
        self.tileview = TileViewUI(self)

        self.add_editor(self.geoeditor, self.geoui)
        self.add_module(self.geomodule)
        self.add_vis_ui(self.geoview)

        self.add_module(self.tilemodule)
        self.add_vis_ui(self.tileview)

        self.init_options()

    def init_options(self):
        self.VQuickGeo = QCheckBox()
        self.VQuickGeo.setObjectName(u"VQuickGeo")
        self.VQuickGeo.setText(QCoreApplication.translate("MainWindow", u"Geometry", None))
        self.VQuickGeo.setChecked(True)
        self.VQuickGeo.checkStateChanged.connect(self.geoview.toggle_geo)
        self.add_quickview_option(self.VQuickGeo)

        self.VQuickTiles = QCheckBox()
        self.VQuickTiles.setObjectName(u"VQuickTiles")
        self.VQuickTiles.setText(QCoreApplication.translate("MainWindow", u"Tiles", None))
        self.VQuickTiles.setChecked(True)
        self.VQuickTiles.checkStateChanged.connect(self.tileview.toggle_tiles)
        self.add_quickview_option(self.VQuickTiles)
