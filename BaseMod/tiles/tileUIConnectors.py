from PySide6.QtCore import Slot, Qt, QCoreApplication
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QFileDialog, QMenu, QCheckBox

from BaseMod.baseMod import BaseMod
from BaseMod.tiles.ui.tiles_ui import Ui_Tiles
from BaseMod.tiles.ui.tiles_vis_ui import Ui_TilesView
from RWESharp.Configurable import KeyConfigurable
from RWESharp.Core import PATH_FILES_IMAGES_PALETTES
from RWESharp.Ui import ViewUI, UI


class TileViewUI(ViewUI):
    def __init__(self, mod, parent=None):
        super().__init__(mod, parent)
        self.mod: BaseMod
        self.ui = Ui_TilesView()
        self.ui.setupUi(self)
        self.module = self.mod.tilemodule

        self.drawltiles_key = KeyConfigurable(mod, "VIEW_tile.drawltiles_key", "Alt+t", "Hide all tiles")
        self.drawl1_key = KeyConfigurable(mod, "VIEW_tile.drawl1_key", "Alt+Shift+1", "Show layer 1 tiles")
        self.drawl2_key = KeyConfigurable(mod, "VIEW_tile.drawl2_key", "Alt+Shift+2", "Show layer 2 tiles")
        self.drawl3_key = KeyConfigurable(mod, "VIEW_tile.drawl3_key", "Alt+Shift+3", "Show layer 3 tiles")
        self.menu = QMenu("Tiles")
        self.menu_drawtiles = QAction("Tiles")
        self.menu.addAction(self.menu_drawtiles)
        self.menu.addSeparator()

        self.menu_drawl1 = QAction("Layer 1")
        self.module.drawl1.link_button_action(self.ui.VTilesLayer1, self.menu_drawl1, self.drawl1_key)
        self.menu.addAction(self.menu_drawl1)
        self.menu_drawl2 = QAction("Layer 2")
        self.module.drawl2.link_button_action(self.ui.VTilesLayer2, self.menu_drawl2, self.drawl2_key)
        self.menu.addAction(self.menu_drawl2)
        self.menu_drawl3 = QAction("Layer 3")
        self.module.drawl3.link_button_action(self.ui.VTilesLayer3, self.menu_drawl3, self.drawl3_key)
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
        # self.VQuickTiles.checkStateChanged.connect(self.toggle_tiles)
        self.mod.add_quickview_option(self.VQuickTiles)
        self.module.drawtiles.link_button_action(self.VQuickTiles, self.menu_drawtiles, self.drawltiles_key)

    @Slot()
    def change_palette(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select a Palette", PATH_FILES_IMAGES_PALETTES)
        self.module.palettepath.update_value(file)
        self.module.drawoption.update_value(4)
        self.module.render_module()

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


class TileUI(UI):
    def __init__(self, mod, parent=None):
        super().__init__(mod, parent)
        self.ui = Ui_Tiles()
        self.ui.setupUi(self)
        mod: BaseMod

        self.explorer = mod.tile_explorer
        self.editor = mod.tileeditor
        self.editor.previewoption.link_combobox(self.ui.RenderOption)
        self.editor.show_collisions.link_button(self.ui.ToggleCollisions)
        self.editor.vis_layer.link_spinbox(self.ui.Layer)
        self.editor.toolleft.link_combobox(self.ui.ToolTilesM1Select)
        self.editor.toolright.link_combobox(self.ui.ToolTilesM2Select)
        self.editor.deleteleft.link_button(self.ui.DeleteM1)
        self.editor.deleteright.link_button(self.ui.DeleteM2)
        self.editor.force_place.link_button(self.ui.ForcePlace)
        self.editor.force_geo.link_button(self.ui.ForceGeo)

        self.tile_prev_key = KeyConfigurable(mod, "EDIT_tile.tile_prev", "w", "Previous Tile")
        self.cat_prev_key = KeyConfigurable(mod, "EDIT_tile.cat_prev", "a", "Previous Category")
        self.tile_next_key = KeyConfigurable(mod, "EDIT_tile.tile_next", "s", "Next Tile")
        self.cat_next_key = KeyConfigurable(mod, "EDIT_tile.cat_next", "d", "Next Category")

        self.tile_next_key.link_button(self.ui.TileNext)
        self.tile_prev_key.link_button(self.ui.TilePrev)
        self.cat_next_key.link_button(self.ui.CatNext)
        self.cat_prev_key.link_button(self.ui.CatPrev)

        self.ui.CatNext.clicked.connect(self.explorer.cat_next)
        self.ui.CatPrev.clicked.connect(self.explorer.cat_prev)
        self.ui.TileNext.clicked.connect(self.explorer.tile_next)
        self.ui.TilePrev.clicked.connect(self.explorer.tile_prev)
