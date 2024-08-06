import os

from PySide6.QtCore import Slot, Signal, Qt, QSize, QPoint
from PySide6.QtGui import QAction, QPixmap, QColor, QImage
from PySide6.QtWidgets import QMainWindow, QListWidgetItem, QListWidget, QFileDialog

from BaseMod.tiles.ui.tileexplorer import Ui_TileExplorer
from RWESharp.Configurable import BoolConfigurable, IntConfigurable, StringConfigurable
from RWESharp.Core import PATH_FILES_IMAGES_PALETTES, ViewDockWidget
from RWESharp.Loaders import Tile, palette_to_colortable, return_tile_pixmap, Tiles
from RWESharp.Utils import paint_svg_qicon


class TileExplorer(ViewDockWidget):
    tileSelected = Signal(list)

    def __init__(self, manager, parent: QMainWindow):
        super().__init__(parent)
        self.manager = manager
        self.mod = manager.basemod
        parent.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self)

        self.category_colors = BoolConfigurable(self.mod, "TileExplorer.category_colors", False, "Color of categories")
        self.tile_cols = BoolConfigurable(self.mod, "TileExplorer.tile_collisions", True, "show tile collisions")
        self.tile_preview = BoolConfigurable(self.mod, "TileExplorer.tile_preview", True, "show tile preview")
        self.drawoption = IntConfigurable(self.mod, "TileExplorer.drawoption", 7, "show tile collisions")
        self.layer = IntConfigurable(self.mod, "TileExplorer.layer", 0, "layer")
        self.palette_path = StringConfigurable(self.mod, "TileExplorer.palettepath", os.path.join(PATH_FILES_IMAGES_PALETTES, "palette0.png"), "path to pallete")
        if not os.path.exists(self.palette_path.value):
            self.palette_path.reset_value()
        self.colortable = palette_to_colortable(QImage(self.palette_path.value))
        self.tiles: Tiles = manager.tiles
        self.ui = Ui_TileExplorer()
        self.ui.setupUi(self)
        self.state = False
        self.preview = self.ui.Preview
        self.preview.add_manager(manager)
        self.view_categories = self.ui.Categories
        self.view_tiles = self.ui.Tiles
        self.view_tile = self.ui.Properties
        self.view_categories.setAlternatingRowColors(True)
        self.view_categories.setEditTriggers(QListWidget.EditTrigger.DoubleClicked)
        self.view_categories.itemSelectionChanged.connect(self.change_tiles)
        self.view_tiles.itemSelectionChanged.connect(self.change_tile)
        self.view_tiles.setDragDropMode(QListWidget.DragDropMode.NoDragDrop)  # todo change in future
        self.view_tiles.setSelectionMode(QListWidget.SelectionMode.ExtendedSelection)
        self.view_categories.setDragDropMode(QListWidget.DragDropMode.NoDragDrop)
        self.view_tiles.setIconSize(QSize(20, 20))

        self.ui.TilesListView.clicked.connect(self.tiles_list)
        self.ui.TilesGridViewBig.clicked.connect(self.tiles_grid)
        self.ui.TilesGridViewSmall.clicked.connect(self.tiles_grid_small)
        self.ui.TilesIconView.clicked.connect(self.tiles_grid_ununiform)
        self.view_tiles.setResizeMode(QListWidget.ResizeMode.Adjust)

        self.ui.SearchBar.textChanged.connect(self.search)
        self.tile_cols.link_button(self.ui.ToggleCollisions)
        self.tile_cols.valueChanged.connect(self.hide_cols)
        self.tile_preview.link_button(self.ui.TogglePreview)
        self.tile_preview.valueChanged.connect(self.hide_preview)
        self.drawoption.link_combobox(self.ui.RenderOption)
        self.drawoption.valueChanged.connect(self.change_draw_option)
        self.layer.link_combobox(self.ui.LayerBox)
        self.layer.valueChanged.connect(self.change_draw_option)
        self.mod.tilemodule.drawoption.valueChanged.connect(self.change_draw_option)
        self.tileSelected.connect(self.mod.tileeditor.add_tile)
        self.palette_path.valueChanged.connect(self.update_palette)
        self.selected_tiles: list[Tile] = []
        self.load_tiles()
        self.tiles_grid()
        self.change_tiles()

        self.category = 0
        self.tile = 0

        self.ui.CatNext.clicked.connect(self.cat_next)
        self.ui.CatPrev.clicked.connect(self.cat_prev)
        self.ui.TileNext.clicked.connect(self.tile_next)
        self.ui.TilePrev.clicked.connect(self.tile_prev)
        self.setFloating(True)

        self.mod.bmconfig.icon_color.valueChanged.connect(self.changecolor)
        self.changecolor(self.mod.bmconfig.icon_color.value)

    def changecolor(self, color: QColor):
        self.ui.TilesListView.setIcon(paint_svg_qicon(u":/grids/grid/list.svg", color))
        self.ui.TilesGridViewBig.setIcon(paint_svg_qicon(u":/grids/grid/mediumgrid.svg", color))
        self.ui.TilesGridViewSmall.setIcon(paint_svg_qicon(u":/grids/grid/smallgrid.svg", color))
        self.ui.TilesIconView.setIcon(paint_svg_qicon(u":/grids/grid/smallgrid2.svg", color))
        self.ui.Pin.setIcon(paint_svg_qicon(u":/special/special/pin.svg", color))

    def change_palette(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select a Palette", PATH_FILES_IMAGES_PALETTES)
        self.palette_path.update_value(file)
        self.drawoption.update_value(4)
        self.preview.preview_tile(self.preview.tile, self.synced_draw_option, self.layer.value, self.colortable)

    @property
    def categoryindex(self):
        return self.view_categories.row(self.view_categories.selectedItems()[0]) if len(self.view_categories.selectedItems()) > 0 else self.category

    @property
    def tileindex(self):
        return self.view_tiles.row(self.view_tiles.selectedItems()[0]) if len(self.view_tiles.selectedItems()) > 0 else self.tile

    def cat_next(self):
        self.category = (self.categoryindex + 1) % self.view_categories.count()
        self.view_categories.setCurrentRow(self.category)
        self.tile = self.tileindex % self.view_tiles.count()
        self.view_tiles.setCurrentRow(self.tile)

    def cat_prev(self):
        self.category = (self.categoryindex - 1) % self.view_categories.count()
        self.view_categories.setCurrentRow(self.category)
        self.tile = self.tileindex % self.view_tiles.count()
        self.view_tiles.setCurrentRow(self.tile)

    def tile_next(self):
        self.tile = (self.tileindex + 1) % self.view_tiles.count()
        self.view_tiles.setCurrentRow(self.tile)

    def tile_prev(self):
        self.tile = (self.tileindex - 1) % self.view_tiles.count()
        self.view_tiles.setCurrentRow(self.tile)

    def update_palette(self):
        self.colortable = palette_to_colortable(QImage(self.palette_path.value))

    def change_draw_option(self):
        self.change_tiles()
        if len(self.selected_tiles) > 0:
            self.preview.preview_tile(self.selected_tiles[0], self.synced_draw_option, self.layer.value, self.colortable)

    @property
    def synced_draw_option(self):
        return self.drawoption.value if self.drawoption.value != 7 else self.mod.tilemodule.drawoption.value

    def hide_cols(self, value):
        self.preview.tilecolsimage.setOpacity(1 if value else 0)

    def hide_preview(self, value):
        self.preview.tileimage.setOpacity(1 if value and len(self.selected_tiles) > 0 else 0)

    def search(self, text: str):
        self.load_tiles()
        self.change_tiles()

    def tiles_grid(self):
        self.view_tiles.setViewMode(QListWidget.ViewMode.IconMode)
        self.view_tiles.setIconSize(QSize(40, 40))
        self.view_tiles.setSpacing(20)
        self.view_tiles.setUniformItemSizes(True)
        self.view_tiles.setAlternatingRowColors(False)

    def tiles_grid_ununiform(self):
        self.view_tiles.setViewMode(QListWidget.ViewMode.IconMode)
        self.view_tiles.setIconSize(QSize(40, 40))
        self.view_tiles.setSpacing(10)
        self.view_tiles.setUniformItemSizes(False)
        self.view_tiles.setAlternatingRowColors(False)

    def tiles_grid_small(self):
        self.view_tiles.setViewMode(QListWidget.ViewMode.IconMode)
        self.view_tiles.setIconSize(QSize(20, 20))
        self.view_tiles.setSpacing(5)
        self.view_tiles.setUniformItemSizes(True)
        self.view_tiles.setAlternatingRowColors(False)

    def tiles_list(self):
        self.view_tiles.setViewMode(QListWidget.ViewMode.ListMode)
        self.view_tiles.setIconSize(QSize(20, 20))
        self.view_tiles.setSpacing(0)
        self.view_tiles.setUniformItemSizes(True)
        self.view_tiles.setAlternatingRowColors(True)

    def load_tiles(self):
        filter = self.ui.SearchBar.text()
        self.view_categories.clear()
        for category in self.tiles.categories:
            color = category.color
            if filter != "" and filter.lower() not in category.name.lower():
                continue
            color: QColor
            image = QPixmap(20, 20)
            image.fill(color)
            item = QListWidgetItem(image, category.name)
            item.setData(Qt.ItemDataRole.UserRole, category)
            if self.category_colors.value:
                biggestratio = 0
                biggestcolor = Qt.GlobalColor.white
                for i in Qt.GlobalColor:
                    ratio = (color.lightnessF() + 0.05)
                    ratio2 = (QColor(i).lightnessF() + 0.05)
                    diff = max(ratio, ratio2) - min(ratio, ratio2)
                    if diff > biggestratio:
                        biggestratio = diff
                        biggestcolor = i
                item.setForeground(biggestcolor)
            # self.view_categories.setIconSize(QSize(2000, 2000))
            self.view_categories.addItem(item)

    @Slot()
    def change_tiles(self):
        filter = self.ui.SearchBar.text()
        if len(self.view_categories.selectedItems()) == 0 and filter == "":
            return
        self.view_tiles.clear()
        if filter != "":
            for i in self.tiles.all_tiles():
                i: Tile
                if filter.lower() not in i.name.lower():
                    continue
                item = QListWidgetItem(i.name)
                item.setData(Qt.ItemDataRole.UserRole, i)
                item.setIcon(self.get_icon(i))
                self.view_tiles.addItem(item)
            return
        categories = []
        for i in self.view_categories.selectedItems():
            categories.append(i.data(Qt.ItemDataRole.UserRole))
        for category in categories:
            for i in category.tiles:
                item = QListWidgetItem(i.name)
                item.setData(Qt.ItemDataRole.UserRole, i)
                item.setIcon(self.get_icon(i))
                self.view_tiles.addItem(item)

    def get_icon(self, tile: Tile):
        return return_tile_pixmap(tile, self.synced_draw_option, self.layer.value, self.colortable)

    @Slot()
    def change_tile(self):
        selection = self.view_tiles.selectedItems()
        if len(selection) == 0:
            return
        self.selected_tiles = []
        for i in selection:
            self.selected_tiles.append(i.data(Qt.ItemDataRole.UserRole))
        self.tileSelected.emit(self.selected_tiles)
        self.preview.tileimage.setOpacity(0)
        if len(self.selected_tiles) == 1:
            self.preview.preview_tile(self.selected_tiles[0], self.synced_draw_option, self.layer.value, self.colortable)
