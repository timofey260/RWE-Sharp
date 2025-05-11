from PySide6.QtCore import Slot, Qt, QCoreApplication, Signal
from PySide6.QtGui import QAction, QColor, QImage
from PySide6.QtWidgets import QFileDialog, QMenu, QCheckBox

from BaseMod.baseMod import BaseMod
from BaseMod.tiles.ui.tiles_ui import Ui_Tiles
from BaseMod.tiles.ui.tiles_vis_ui import Ui_TilesView
from BaseMod.tiles.ui.tilesettings_ui import Ui_TileSettings
from BaseMod.geo.GeoConsts import *

from RWESharp.Configurable import BoolConfigurable, IntConfigurable, StringConfigurable, FloatConfigurable, KeyConfigurable
from RWESharp.Core import PATH_FILES_IMAGES_PALETTES
from RWESharp.Ui import ViewUI, UI, SettingUI
from RWESharp.Utils import paint_svg_qicon
from RWESharp.Loaders import palette_to_colortable
from widgets.SettingsViewer import SettingsViewer
import os


class TileViewUI(ViewUI):
    render = Signal()

    def __init__(self, mod, parent=None):
        super().__init__(mod, parent)
        self.mod: BaseMod
        self.ui = Ui_TilesView()
        self.ui.setupUi(self)

        self.drawtiles = BoolConfigurable(mod, "VIEW_tile.drawtiles", True, "Draw tiles")
        self.drawl1 = BoolConfigurable(mod, "VIEW_tile.drawl1", True, "Draw layer 1")
        self.drawl2 = BoolConfigurable(mod, "VIEW_tile.drawl2", True, "Draw layer 2")
        self.drawl3 = BoolConfigurable(mod, "VIEW_tile.drawl3", True, "Draw layer 3")
        self.drawlheads = BoolConfigurable(mod, "VIEW_tile.drawlheads", True, "Draw tile heads")
        self.drawlmats = BoolConfigurable(mod, "VIEW_tile.drawlmats", True, "Draw materials")

        self.drawoption = IntConfigurable(mod, "VIEW_tile.drawoption", 0, "Option how to draw tiles")
        self.palettepath = StringConfigurable(mod, "VIEW_tile.palettepath",
                                              os.path.join(PATH_FILES_IMAGES_PALETTES, "palette0.png"),
                                              "Path to themes")

        self.drawpnotrendered = FloatConfigurable(mod, "VIEW_tile.drawpnotrend", .9,
                                                   "Primary layer draw opacity(classic and henry)")
        self.drawsnotrendered = FloatConfigurable(mod, "VIEW_tile.drawsnotrend", .196,
                                                   "Secondary layer draw opacity(classic and henry)")

        self.drawprendered = FloatConfigurable(mod, "VIEW_tile.drawprend", 1, "Primary layer draw opacity(rendered)")
        self.drawsrendered = FloatConfigurable(mod, "VIEW_tile.drawsrend", 1, "Secondary layer draw opacity(rendered)")

        self.renderall = BoolConfigurable(mod, "VIEW_tile.renderall", True, "Render layers behind current")

        self.matborder = BoolConfigurable(mod, "VIEW_tile.matborder", True,
                                          "Material Border")

        if not os.path.exists(self.palettepath.value):
            self.palettepath.reset_value()

        self.palettepath.valueChanged.connect(self.change_colortable)
        self.colortable = None

        self.drawtiles.valueChanged.connect(self.hide_tiles)

        self.drawltiles_key = KeyConfigurable(mod, "VIEW_tile.drawltiles_key", "Alt+t", "Hide all tiles")
        self.drawl1_key = KeyConfigurable(mod, "VIEW_tile.drawl1_key", "Alt+Shift+1", "Show layer 1 tiles")
        self.drawl2_key = KeyConfigurable(mod, "VIEW_tile.drawl2_key", "Alt+Shift+2", "Show layer 2 tiles")
        self.drawl3_key = KeyConfigurable(mod, "VIEW_tile.drawl3_key", "Alt+Shift+3", "Show layer 3 tiles")
        self.menu = QMenu("Tiles")
        self.menu_drawtiles = QAction("Tiles")
        self.menu.addAction(self.menu_drawtiles)
        self.menu.addSeparator()

        self.menu_drawl1 = QAction("Layer 1")
        self.drawl1.link_button_action(self.ui.VTilesLayer1, self.menu_drawl1, self.drawl1_key)
        self.menu.addAction(self.menu_drawl1)
        self.menu_drawl2 = QAction("Layer 2")
        self.drawl2.link_button_action(self.ui.VTilesLayer2, self.menu_drawl2, self.drawl2_key)
        self.menu.addAction(self.menu_drawl2)
        self.menu_drawl3 = QAction("Layer 3")
        self.drawl3.link_button_action(self.ui.VTilesLayer3, self.menu_drawl3, self.drawl3_key)
        self.menu.addAction(self.menu_drawl3)

        self.menu_drawl1 = QAction("Materials")
        self.drawl1.link_button_action(self.ui.VTilesLayer1, self.menu_drawl1, self.drawl1_key)
        self.menu.addAction(self.menu_drawl1)
        self.menu_drawl2 = QAction("Layer 2")
        self.drawl2.link_button_action(self.ui.VTilesLayer2, self.menu_drawl2, self.drawl2_key)
        self.menu.addAction(self.menu_drawl2)
        self.menu_drawl3 = QAction("Layer 3")
        self.drawl3.link_button_action(self.ui.VTilesLayer3, self.menu_drawl3, self.drawl3_key)
        self.menu.addAction(self.menu_drawl3)
        self.ui.VTilesAllTiles.checkStateChanged.connect(self.all_layers)
        self.mod.manager.view_menu.addMenu(self.menu)
        self.drawoption.link_radio(
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
        self.drawtiles.link_button_action(self.VQuickTiles, self.menu_drawtiles, self.drawltiles_key)
        self.change_colortable()

    @Slot()
    def change_palette(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select a Palette", PATH_FILES_IMAGES_PALETTES)
        self.palettepath.update_value(file)
        self.drawoption.update_value(4)
        self.render.emit()

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
        self.drawl1.update_value(v)
        self.drawl2.update_value(v)
        self.drawl3.update_value(v)

    def hide_tiles(self):
        self.drawl1.update_value(self.drawtiles.value)
        self.drawl2.update_value(self.drawtiles.value)
        self.drawl3.update_value(self.drawtiles.value)

    def showlayer(self, currentlayer):
        self.drawl1.update_value(currentlayer == 0)
        self.drawl2.update_value(currentlayer <= 1)
        self.drawl3.update_value(True)

    def change_colortable(self):
        self.colortable = palette_to_colortable(QImage(self.palettepath.value))


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
        self.editor.strictmode.link_combobox(self.ui.StrictMode)

        self.tile_prev_key = KeyConfigurable(mod, "EDIT_tile.tile_prev", "w", "Previous Tile")
        self.cat_prev_key = KeyConfigurable(mod, "EDIT_tile.cat_prev", "a", "Previous Category")
        self.tile_next_key = KeyConfigurable(mod, "EDIT_tile.tile_next", "s", "Next Tile")
        self.cat_next_key = KeyConfigurable(mod, "EDIT_tile.cat_next", "d", "Next Category")
        self.force_geo_key = KeyConfigurable(mod, "EDIT_tiles.fgkey", "g", "Force geometry")
        self.force_place_key = KeyConfigurable(mod, "EDIT_tiles.fpkey", "f", "Force place")
        self.find_key = KeyConfigurable(mod, "EDIT_tile.find_key", "Ctrl+e", "Find tile")

        self.explorer_key = KeyConfigurable(mod, "EDIT_tile.explorer_key", "Ctrl+f", "Show Tile Explorer")

        self.explorer_key.link_button(self.ui.OpenExplorer)

        self.tile_next_key.link_button(self.ui.TileNext)
        self.tile_prev_key.link_button(self.ui.TilePrev)
        self.cat_next_key.link_button(self.ui.CatNext)
        self.cat_prev_key.link_button(self.ui.CatPrev)
        self.find_key.link_button(self.ui.FindTE)
        self.force_geo_key.link_button(self.ui.ForceGeo)
        self.force_place_key.link_button(self.ui.ForcePlace)

        self.ui.CatNext.clicked.connect(self.explorer.cat_next)
        self.ui.CatPrev.clicked.connect(self.explorer.cat_prev)
        self.ui.TileNext.clicked.connect(self.explorer.item_next)
        self.ui.TilePrev.clicked.connect(self.explorer.item_prev)
        self.ui.PalleteSelect.clicked.connect(self.change_palette)
        self.ui.FindTE.clicked.connect(self.explorer.focussearch)
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
        self.editor.explorer.change_visibility(True)
        self.editor.explorer.focussearch()


class TileSettings(SettingUI):
    def __init__(self, mod):
        super().__init__(mod)
        self.tileviewui = self.mod.tileview
        l1 = lambda x: int(x * 255)
        l2 = lambda x: x / 255
        self.rp = SettingUI.ManageableSetting(IntConfigurable(None, "rp", 0, "Opacity of rendered primary layer"), self.tileviewui.drawprendered, l1, l2).add_myself(self)
        self.np = SettingUI.ManageableSetting(IntConfigurable(None, "np", 0, "Opacity of not rendered primary layer"), self.tileviewui.drawpnotrendered, l1, l2).add_myself(self)
        self.rs = SettingUI.ManageableSetting(IntConfigurable(None, "rs", 0, "Opacity of rendered secondary layer"), self.tileviewui.drawsrendered, l1, l2).add_myself(self)
        self.ns = SettingUI.ManageableSetting(IntConfigurable(None, "ns", 0, "Opacity of not rendered secondary layer"), self.tileviewui.drawsnotrendered, l1, l2).add_myself(self)

        self.renderall = SettingUI.ManageableSetting(BoolConfigurable(None, "renderall", False,
                                        "Draw layers behind current one"), self.tileviewui.renderall).add_myself(self)

        self.matborder = SettingUI.ManageableSetting(BoolConfigurable(None, "matborder", True,
                                                                    "Add black border to materials"),
                                                   self.tileviewui.matborder).add_myself(self)

        self.drawoption = IntConfigurable(None, "drawoption", 0, "Draw option")
        self.reset_values()

    def init_ui(self, viewer: SettingsViewer):
        self.ui = Ui_TileSettings()
        self.ui.setupUi(viewer)
        self.ui.TilePreview.add_manager(self.mod.manager, self)

        self.rp.setting.link_slider_spinbox(self.ui.Popr, self.ui.Popr_2)
        self.rs.setting.link_slider_spinbox(self.ui.Sopr, self.ui.Sopr_2)

        self.np.setting.link_slider_spinbox(self.ui.Popn, self.ui.Popn_2)
        self.ns.setting.link_slider_spinbox(self.ui.Sopn, self.ui.Sopn_2)

        self.drawoption.link_combobox(self.ui.RenderOption)
        self.drawoption.valueChanged.connect(self.ui.TilePreview.update_option)

        self.matborder.setting.link_button(self.ui.MatBorder)

        self.renderall.setting.link_button(self.ui.Rall)

        for i in [self.rp, self.rs, self.np, self.ns, self.renderall]:
            i.setting.valueChanged.connect(self.ui.TilePreview.update_preview)
        self.ui.LayerSlider.valueChanged.connect(self.ui.TilePreview.update_preview)
