from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPixmap, QColor, QAction
from PySide6.QtWidgets import QMainWindow, QTreeWidgetItem, QListWidgetItem, QTableWidgetItem

from BaseMod.Explorer import Explorer
from BaseMod.tiles.tilePin import TilePin
from RWS.Configurable import BoolConfigurable, IntConfigurable
from RWS.Core import CELLSIZE, SPRITESIZE, PATH_COLLECTIONS_TILES
from RWS.Loaders import Tile, Tiles


class TileExplorer(Explorer):
    def category_items(self, cat) -> list:
        return cat.tiles

    def preview_item(self, item):
        if item is None:
            self.tileimage.setOpacity(0)
            return
        self.preview_tile(item)
        self.ui.Properties.clear()
        self.ui.Properties.setRowCount(5)
        self.ui.Properties.setColumnCount(1)
        self.ui.Properties.setVerticalHeaderItem(0, QTableWidgetItem("Name"))
        self.ui.Properties.setItem(0, 0, QTableWidgetItem(item.name))
        self.ui.Properties.setVerticalHeaderItem(1, QTableWidgetItem("Description"))
        self.ui.Properties.setItem(1, 0, QTableWidgetItem(item.description))
        self.ui.Properties.setVerticalHeaderItem(2, QTableWidgetItem("Size"))
        self.ui.Properties.setItem(2, 0, QTableWidgetItem(f"{item.size.width()}x{item.size.height()}"))
        self.ui.Properties.setVerticalHeaderItem(3, QTableWidgetItem("b. tiles"))
        self.ui.Properties.setItem(3, 0, QTableWidgetItem(str(item.bfTiles)))
        self.ui.Properties.setVerticalHeaderItem(4, QTableWidgetItem("Tags"))
        self.ui.Properties.setItem(4, 0, QTableWidgetItem(", ".join(item.tags)))
        self.ui.Properties.adjustSize()
        self.ui.Properties.resizeColumnsToContents()
        # self.ui.Properties.resizeRowsToContents()
        # self.ui.Properties.verticalHeaderDefaultSectionSize = 25
        # self.ui.Properties.verticalHeaderStretchLastSection = True
        # self.ui.Properties.setAutoScroll(True)

    def itemtype(self) -> type:
        return Tile

    def get_categories(self) -> list:
        return self.tiles.categories

    def get_all_items(self) -> list:
        return self.tiles.all_tiles()

    def item_from_data(self, data) -> QListWidgetItem | None:
        filter = self.ui.SearchBar.text()
        if filter != "" and filter.lower() not in data.name.lower() and not self.simplemode:
            return None
        item = QListWidgetItem(data.name)
        item.setData(Qt.ItemDataRole.UserRole, data)
        item.setIcon(self.get_icon(data))
        return item

    def treeitem_from_data(self, data) -> QTreeWidgetItem | None:
        filter = self.ui.SearchBar.text()
        if filter != "" and filter.lower() not in data.name.lower():
            return None
        tileitem = QTreeWidgetItem([data.name])
        tileitem.setData(0, Qt.ItemDataRole.UserRole, data)
        tileitem.setIcon(0, self.get_icon(data))
        return tileitem

    def cat_from_data(self, cat) -> QTreeWidgetItem | None:
        filter = self.ui.SearchBar.text()
        if filter != "" and filter.lower() not in cat.name.lower() and not self.simplemode:
            return None
        color = cat.color
        color: QColor
        image = QPixmap(20, 20)
        image.fill(color)
        item = QTreeWidgetItem([cat.name])
        item.setIcon(0, image)
        item.setData(0, Qt.ItemDataRole.UserRole, cat)
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
            item.setForeground(0, biggestcolor)
        return item

    def __init__(self, editor, parent: QMainWindow):
        self.tiles: Tiles = editor.manager.tiles
        super().__init__(editor.mod, parent)
        self.tileview = self.mod.tileview

        self.tile_cols = BoolConfigurable(self.mod, "TileExplorer.tile_collisions", True, "show tile collisions")
        self.tile_preview = BoolConfigurable(self.mod, "TileExplorer.tile_preview", True, "show tile preview")
        # self.drawoption = IntConfigurable(self.mod, "TileExplorer.drawoption", 7, "show tile collisions")
        self.layer = IntConfigurable(self.mod, "TileExplorer.layer", 0, "layer")
        self.tile_cols.link_button(self.ui.ToggleCollisions)
        self.tile_cols.valueChanged.connect(self.hide_cols)
        self.tile_preview.link_button(self.ui.TogglePreview)
        self.tile_preview.valueChanged.connect(self.hide_preview)
        # self.drawoption.link_combobox(self.ui.RenderOption)
        # self.drawoption.valueChanged.connect(self.change_draw_option)
        self.layer.link_combobox(self.ui.LayerBox)
        self.layer.valueChanged.connect(self.change_draw_option)
        self.tileview.drawoption.valueChanged.connect(self.change_draw_option)
        self.tileview.drawoption.link_combobox(self.ui.RenderOption)
        self.tileview.render.connect(lambda : self.change_items())
        self.tileview.render.connect(lambda : self.preview_tile(self.selected[0]) if len(self.selected) > 0 else None)
        self.ui.SearchBar.textChanged.connect(self.search)
        self.ui.Pin.clicked.connect(self.pin_tile)
        self.itemselected.connect(editor.add_tile)

        self.pins = []

        self.tileimage = self.preview.workscene.addPixmap(QPixmap(1, 1))
        self.tilecolsimage = self.preview.workscene.addPixmap(QPixmap(1, 1))
        self.preview.items.append(self.tileimage)
        self.preview.items.append(self.tilecolsimage)
        self.ui.LItem.setText("Tile")
        self.ui.LItems.setText("Tiles")
        self.setWindowTitle("Tile Explorer")
        self.hide()

        self.tile_explorer_action = QAction("Tile Explorer")
        self.manager.window_menu.addAction(self.tile_explorer_action)
        self.link_action(self.tile_explorer_action)
        self.mod.bmconfig.tileexplorer_key.link_action(self.tile_explorer_action)

        self.tiles.tileschanged.connect(self.load_categories)

    @property
    def custom_categories_path(self):
        return PATH_COLLECTIONS_TILES

    def categories_modified(self):
        self.tiles.add_custom_tiles()

    def category_is_custom(self, cat) -> bool:
        return cat in self.tiles.custom_categories

    def category_name(self, cat) -> str:
        return cat.name

    def item_name(self, item) -> str:
        return item.name

    def category_at_index(self, index):
        return self.tiles.categories[index]

    def pin_tile(self):
        for i in self.selected:
            pin = TilePin(i, self, self.manager.window)
            pin.change_visibility(True)
            self.pins.append(pin)
            pin.setFocus()

    def unpin_tile(self, tile: Tile):
        for i in range(len(self.pins) - 1, -1, -1):
            if self.pins[i].tile == tile:
                self.remove_pin(self.pins[i])

    def unpin_all(self):
        for i in range(len(self.pins) - 1, -1, -1):
            self.remove_pin(self.pins[i])

    def remove_pin(self, pin):
        pin.deleteLater()
        self.pins.remove(pin)

    def preview_tile(self, tile):
        self.tileimage.setOpacity(1)
        self.tileimage.setPixmap(tile.return_tile_pixmap(self.synced_draw_option, self.layer.value, self.tileview.colortable))
        self.tilecolsimage.setPixmap(tile.collisions_image())
        self.tileimage.setData(2, (CELLSIZE / SPRITESIZE) if self.synced_draw_option == 0 else 1)

        self.tileimage.setData(1, QPoint(0, 0) if self.synced_draw_option == 0 else (-QPoint(tile.bfTiles, tile.bfTiles) * CELLSIZE))
        self.preview.set_pos(QPoint(0, 0))
        self.preview.set_zoom()
        self.preview.verticalScrollBar().setValue(0)
        self.preview.horizontalScrollBar().setValue(0)

    def change_draw_option(self):
        self.change_items()
        if len(self.selected) > 0:
            self.preview_tile(self.selected[0])
        if self.simplemode:
            self.load_categories()

    @property
    def synced_draw_option(self):
        return self.mod.tileview.drawoption.value

    def hide_cols(self, value):
        self.tilecolsimage.setOpacity(1 if value else 0)

    def hide_preview(self, value):
        self.tileimage.setOpacity(1 if value and len(self.selected) > 0 else 0)

    def get_icon(self, tile: Tile):
        return tile.return_tile_pixmap(self.synced_draw_option, self.layer.value, self.tileview.colortable)
