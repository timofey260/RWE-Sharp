from core.Modify.Mod import Mod, ModInfo
from .geo.geometryEditor import GeometryEditor
from .geo.geometryModule import GeoModule
from .geo.geoConfig import GeoConfig, GeoViewConfig
from .tiles.tileModule import TileModule
from .tiles.tileConfig import TileViewConfig
from .globalConfig import Globalconfig
from .grid.gridModule import GridModule
from .grid.gridConfig import GridConfig
from .grid.gridUIConnector import GridView
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
        self.config: Globalconfig | None = None

        self.geoconfig: GeoConfig | None = None
        self.geoeditor: GeometryEditor | None = None
        self.geomodule: GeoModule | None = None
        self.geoui: GeoUI | None = None
        self.geoview: GeoViewUI | None = None
        self.geoviewconfig: GeoViewConfig | None = None

        self.tilemodule: TileModule | None = None
        self.tileview: TileViewUI | None = None
        self.tileviewconfig: TileViewConfig | None = None

        self.gridmodule: GridModule | None = None
        self.gridconfig: GridConfig | None = None
        self.gridui: GridView | None = None

    def pre_mod_init(self):
        self.config = Globalconfig(self).add_myself()
        self.geoconfig = GeoConfig(self).add_myself()
        self.geoviewconfig = GeoViewConfig(self).add_myself()
        self.tileviewconfig = TileViewConfig(self).add_myself()

        self.gridconfig = GridConfig(self).add_myself()

    def mod_init(self):
        from .geo.geoUIConnectors import GeoUI, GeoViewUI
        from .tiles.tileUIConnectors import TileViewUI

        self.geomodule = GeoModule(self).add_myself()
        self.geoui = GeoUI(self)
        self.geoview = GeoViewUI(self).add_myself()
        self.geoeditor = GeometryEditor(self).add_myself(self.geoui)

        self.tilemodule = TileModule(self).add_myself()
        self.tileview = TileViewUI(self).add_myself()

        self.gridmodule = GridModule(self).add_myself()
        self.gridui = GridView(self).add_myself()

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
