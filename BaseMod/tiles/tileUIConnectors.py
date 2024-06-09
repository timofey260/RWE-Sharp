from BaseMod.tiles.tiles_vis_ui import Ui_TilesView
from PySide6.QtWidgets import QFileDialog, QMenu, QCheckBox
from PySide6.QtCore import Slot, Qt, QCoreApplication
from PySide6.QtGui import QAction
from BaseMod.baseMod import BaseMod
from core.info import PATH_FILES_IMAGES_PALETTES
from core.Modify.ui import ViewUI


class TileViewUI(ViewUI):
    def __init__(self, mod, parent=None):
        super().__init__(mod, parent)
        self.mod: BaseMod
        self.ui = Ui_TilesView()
        self.ui.setupUi(self)
        self.module = self.mod.tilemodule

        self.menu = QMenu("Tiles")

        self.menu_drawl1 = QAction("Layer 1")
        self.module.drawl1.link_button_action(self.ui.VTilesLayer1, self.menu_drawl1, self.module.drawl1_key)
        self.menu.addAction(self.menu_drawl1)
        self.menu_drawl2 = QAction("Layer 2")
        self.module.drawl2.link_button_action(self.ui.VTilesLayer2, self.menu_drawl2, self.module.drawl2_key)
        self.menu.addAction(self.menu_drawl2)
        self.menu_drawl3 = QAction("Layer 3")
        self.module.drawl3.link_button_action(self.ui.VTilesLayer3, self.menu_drawl3, self.module.drawl3_key)
        self.menu.addAction(self.menu_drawl3)
        self.ui.VTilesAllTiles.checkStateChanged.connect(self.all_layers)
        self.mod.manager.view_menu.addMenu(self.menu)
        self.module.drawoption.link_radio(
            [
                self.ui.VTilesClassic,
                self.ui.VTilesImage,
                self.ui.VTilesHenry,
                self.ui.VTilesUnrendered,
                self.ui.VTilesRendered,
                self.ui.VTilesRendered_shade,
                self.ui.VTilesRendered_rain
            ])
        self.ui.PaletteSelectButton.clicked.connect(self.change_palette)

        self.VQuickTiles = QCheckBox()
        self.VQuickTiles.setObjectName(u"VQuickTiles")
        self.VQuickTiles.setText(QCoreApplication.translate("MainWindow", u"Tiles", None))
        self.VQuickTiles.setChecked(True)
        self.VQuickTiles.checkStateChanged.connect(self.toggle_tiles)
        self.mod.add_quickview_option(self.VQuickTiles)

    @Slot()
    def change_palette(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select a Palette", PATH_FILES_IMAGES_PALETTES)
        self.module.palettepath.update_value(file)
        self.module.drawoption.update_value(4)

    @Slot(Qt.CheckState)
    def all_layers(self, state: Qt.CheckState):
        if state == Qt.CheckState.Checked:
            self.ui.VTilesLayer1.setChecked(True)
            self.ui.VTilesLayer2.setChecked(True)
            self.ui.VTilesLayer3.setChecked(True)
            self.ui.VTilesHeads.setChecked(True)
            self.ui.VTilesMaterials.setChecked(True)

    @Slot(Qt.CheckState)
    def toggle_tiles(self, state: Qt.CheckState):
        v = state == Qt.CheckState.Checked
        self.module.drawl1.update_value(v)
        self.module.drawl2.update_value(v)
        self.module.drawl3.update_value(v)