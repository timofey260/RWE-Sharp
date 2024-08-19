from PySide6.QtCore import Slot, Qt, QCoreApplication
from PySide6.QtGui import QAction, QColor
from PySide6.QtWidgets import QFileDialog, QMenu, QCheckBox

from BaseMod.baseMod import BaseMod
from BaseMod.tiles.tileModule import TileModule
from BaseMod.tiles.ui.tiles_ui import Ui_Tiles
from BaseMod.tiles.ui.tiles_vis_ui import Ui_TilesView
from BaseMod.tiles.ui.tilesettings_ui import Ui_TileSettings
from BaseMod.geo.GeoConsts import *

from RWESharp.Configurable import KeyConfigurable, IntConfigurable, BoolConfigurable
from RWESharp.Core import PATH_FILES_IMAGES_PALETTES
from RWESharp.Ui import ViewUI, UI, SettingUI
from RWESharp.Utils import paint_svg_qicon
from widgets.SettingsViewer import SettingsViewer


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

        self.explorer = mod.tileeditor.explorer
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
        self.force_geo_key = KeyConfigurable(mod, "EDIT_tiles.fgkey", "g", "Force geometry")
        self.force_place_key = KeyConfigurable(mod, "EDIT_tiles.fpkey", "f", "Force place")

        self.tile_next_key.link_button(self.ui.TileNext)
        self.tile_prev_key.link_button(self.ui.TilePrev)
        self.cat_next_key.link_button(self.ui.CatNext)
        self.cat_prev_key.link_button(self.ui.CatPrev)
        self.force_geo_key.link_button(self.ui.ForceGeo)
        self.force_place_key.link_button(self.ui.ForcePlace)

        self.ui.CatNext.clicked.connect(self.explorer.cat_next)
        self.ui.CatPrev.clicked.connect(self.explorer.cat_prev)
        self.ui.TileNext.clicked.connect(self.explorer.tile_next)
        self.ui.TilePrev.clicked.connect(self.explorer.tile_prev)
        self.ui.PalleteSelect.clicked.connect(self.change_palette)
        mod.bmconfig.icon_color.valueChanged.connect(self.change_color)
        self.change_color(mod.bmconfig.icon_color.value)
        self.ui.OpenExplorer.clicked.connect(self.open_explorer)

    def change_color(self, color: QColor):
        items = [IMG_PEN, IMG_BRUSH, IMG_BUCKET, IMG_LINE, IMG_RECT, IMG_RECT_HOLLOW, IMG_CIRCLE, IMG_CIRCLE_HOLLOW]
        for i in range(8):
            self.ui.ToolTilesM1Select.setItemIcon(i, paint_svg_qicon(items[i], color))
            self.ui.ToolTilesM2Select.setItemIcon(i, paint_svg_qicon(items[i], color))

    def change_palette(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select a Palette", PATH_FILES_IMAGES_PALETTES)
        self.editor.palette_image.update_value(file)
        self.editor.tile_item.set_tile(self.editor.tile_item.tile, self.editor.colortable, 4)

    def open_explorer(self):
        self.mod.tileeditor.explorer.change_visibility(True)


class TileSettings(SettingUI):
    def __init__(self, mod):
        super().__init__(mod)
        self.module: TileModule = self.mod.tilemodule
        self.rl1 = IntConfigurable(self, "rl1", 0, "Opacity of rendered layer 1")
        self.nl1 = IntConfigurable(self, "nl1", 0, "Opacity of not rendered layer 1")
        self.rl2 = IntConfigurable(self, "rl2", 0, "Opacity of rendered layer 2")
        self.nl2 = IntConfigurable(self, "nl2", 0, "Opacity of not rendered layer 2")
        self.rl3 = IntConfigurable(self, "rl3", 0, "Opacity of rendered layer 3")
        self.nl3 = IntConfigurable(self, "nl3", 0, "Opacity of not rendered layer 3")
        self.opshift = BoolConfigurable(self, "opshift", False,
                                        "Opacity shift\nOnly change opacity of shown layers\n"
                                        "For example, if layer 1 is hidden, layer 2 will have opacity of layer 1 and "
                                        "layer 3 will have opacity of layer 2")

        self.drawoption = IntConfigurable(None, "drawoption", 0, "Draw option")

        self.showl1 = BoolConfigurable(None, "sl1", True, "Show First layer")
        self.showl2 = BoolConfigurable(None, "sl2", True, "Show Second layer")
        self.showl3 = BoolConfigurable(None, "sl3", True, "Show Third layer")
        self.reset_values()

    def init_ui(self, viewer: SettingsViewer):
        self.ui = Ui_TileSettings()
        self.ui.setupUi(viewer)
        self.ui.TilePreview.add_manager(self.mod.manager, self)

        self.rl1.link_slider_spinbox(self.ui.L1opr, self.ui.L1opr_2)
        self.rl2.link_slider_spinbox(self.ui.L2opr, self.ui.L2opr_2)
        self.rl3.link_slider_spinbox(self.ui.L3opr, self.ui.L3opr_2)

        self.nl1.link_slider_spinbox(self.ui.L1opn, self.ui.L1opn_2)
        self.nl2.link_slider_spinbox(self.ui.L2opn, self.ui.L2opn_2)
        self.nl3.link_slider_spinbox(self.ui.L3opn, self.ui.L3opn_2)

        self.showl1.link_button(self.ui.L1show)
        self.showl2.link_button(self.ui.L2show)
        self.showl3.link_button(self.ui.L3show)

        self.drawoption.link_combobox(self.ui.RenderOption)
        self.drawoption.valueChanged.connect(self.ui.TilePreview.update_option)

        self.opshift.link_button(self.ui.Opacityshift)

        for i in [self.rl1, self.rl2, self.rl3, self.nl1, self.nl2, self.nl3, self.opshift, self.showl1, self.showl2, self.showl3]:
            i.valueChanged.connect(self.ui.TilePreview.update_preview)

    def reset_values(self):
        self.rl1.update_value_default(int(self.module.drawl1rendered.value * 255))
        self.nl1.update_value_default(int(self.module.drawl1notrendered.value * 255))
        self.rl2.update_value_default(int(self.module.drawl2rendered.value * 255))
        self.nl2.update_value_default(int(self.module.drawl2notrendered.value * 255))
        self.rl3.update_value_default(int(self.module.drawl3rendered.value * 255))
        self.nl3.update_value_default(int(self.module.drawl3notrendered.value * 255))
        self.opshift.update_value_default(self.module.opacityshift.value)

    def apply_values(self):
        self.module.drawl1rendered.update_value(self.rl1.value / 255)
        self.module.drawl2rendered.update_value(self.rl2.value / 255)
        self.module.drawl3rendered.update_value(self.rl3.value / 255)
        self.module.drawl1notrendered.update_value(self.nl1.value / 255)
        self.module.drawl2notrendered.update_value(self.nl2.value / 255)
        self.module.drawl3notrendered.update_value(self.nl3.value / 255)
        self.module.opacityshift.update_value(self.opshift.value)
        self.reset_values()

    def reset_values_default(self):
        self.rl1.update_value_default(int(self.module.drawl1rendered.default * 255))
        self.nl1.update_value_default(int(self.module.drawl1notrendered.default * 255))
        self.rl2.update_value_default(int(self.module.drawl2rendered.default * 255))
        self.nl2.update_value_default(int(self.module.drawl2notrendered.default * 255))
        self.rl3.update_value_default(int(self.module.drawl3rendered.default * 255))
        self.nl3.update_value_default(int(self.module.drawl3notrendered.default * 255))
        self.opshift.update_value_default(self.module.opacityshift.default)
