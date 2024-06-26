from BaseMod.tiles.ui.tileexplorer import Ui_TileExplorer
from PySide6.QtWidgets import QMainWindow, QTreeWidgetItem, QListWidgetItem, QListWidget
from PySide6.QtGui import QAction, QPixmap, QColor, QImage
from PySide6.QtCore import Slot, Signal, Qt, QSize, QPoint
from RWESharp.Core import ItemData, PATH_FILES_IMAGES_PALETTES
from RWESharp.Loaders import Tile, palette_to_colortable, return_tile_pixmap
from RWESharp.Configurable import BoolConfigurable, IntConfigurable, StringConfigurable
import os


class TileExplorer(QMainWindow):
    stateChanged = Signal(bool)
    tileSelected = Signal(list)

    def __init__(self, manager, parent=None):
        super().__init__(parent)
        self.manager = manager
        self.mod = manager.basemod
        self.category_colors = BoolConfigurable(self.mod, "TileExplorer.category_colors", False, "Color of categories")
        self.tile_cols = BoolConfigurable(self.mod, "TileExplorer.tile_collisions", True, "show tile collisions")
        self.tile_prev = BoolConfigurable(self.mod, "TileExplorer.tile_preview", True, "show tile preview")
        self.drawoption = IntConfigurable(self.mod, "TileExplorer.drawoption", 7, "show tile collisions")
        self.layer = IntConfigurable(self.mod, "TileExplorer.layer", 0, "layer")
        self.palette_path = StringConfigurable(self.mod, "TileExplorer.palettepath", os.path.join(PATH_FILES_IMAGES_PALETTES, "palette0.png"), "path to pallete")
        self.colortable = palette_to_colortable(QImage(self.palette_path.value))
        self.tiles: ItemData = manager.tiles
        self.ui = Ui_TileExplorer()
        self.ui.setupUi(self)
        self.state = False
        self.preview = self.ui.Preview
        self.preview.add_manager(manager, self)
        self.view_categories = self.ui.Categories
        self.view_tiles = self.ui.Tiles
        self.view_tile = self.ui.Properties
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
        self.tile_prev.link_button(self.ui.TogglePreview)
        self.tile_prev.valueChanged.connect(self.hide_preview)
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

    def update_palette(self):
        self.colortable = palette_to_colortable(QImage(self.palette_path.value))

    def change_draw_option(self):
        self.change_tiles()
        if len(self.selected_tiles) > 0:
            self.preview.preview_tile(self.selected_tiles[0])

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
        self.view_tiles.setSpacing(10)
        self.view_tiles.setUniformItemSizes(True)

    def tiles_grid_ununiform(self):
        self.view_tiles.setViewMode(QListWidget.ViewMode.IconMode)
        self.view_tiles.setIconSize(QSize(40, 40))
        self.view_tiles.setSpacing(10)
        self.view_tiles.setUniformItemSizes(False)

    def tiles_grid_small(self):
        self.view_tiles.setViewMode(QListWidget.ViewMode.IconMode)
        self.view_tiles.setIconSize(QSize(20, 20))
        self.view_tiles.setSpacing(5)
        self.view_tiles.setUniformItemSizes(True)

    def tiles_list(self):
        self.view_tiles.setViewMode(QListWidget.ViewMode.ListMode)
        self.view_tiles.setIconSize(QSize(20, 20))
        self.view_tiles.setSpacing(0)
        self.view_tiles.setUniformItemSizes(True)

    def load_tiles(self):
        filter = self.ui.SearchBar.text()
        self.view_categories.clear()
        self.view_categories.setAlternatingRowColors(True)
        for category, color in zip(range(len(self.tiles.categories)), self.tiles.colors):
            if filter != "" and filter.lower() not in self.tiles.categories[category].lower():
                continue
            color: QColor
            image = QPixmap(20, 20)
            image.fill(color)
            item = QListWidgetItem(image, self.tiles.categories[category])
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
            for i in self.tiles.all_items():
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
            for i in self.tiles.get_items(category):
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
            self.preview.preview_tile(self.selected_tiles[0])

    def link_action(self, action: QAction):
        action.setCheckable(True)
        action.setChecked(self.state)
        action.toggled.connect(self.change_visibility)
        self.stateChanged.connect(action.setChecked)

    @Slot(bool)
    def change_visibility(self, value: bool):
        if self.state == value:
            return
        self.state = value
        if value:
            self.stateChanged.emit(value)
            self.show()
            self.view_categories.editItem(self.view_categories.itemAt(0, 0))
            return
        self.stateChanged.emit(value)
        self.hide()

    def hideEvent(self, event):
        self.change_visibility(False)
        super().hideEvent(event)

    def showEvent(self, event):
        self.change_visibility(True)
        super().showEvent(event)
