from BaseMod.tiles.ui.tileexplorer import Ui_TileExplorer
from PySide6.QtWidgets import QMainWindow, QTreeWidgetItem, QListWidgetItem, QListWidget
from PySide6.QtGui import QAction, QPixmap, QColor
from PySide6.QtCore import Slot, Signal, Qt, QSize
from RWESharp.Core import ItemData
from RWESharp.Loaders import Tile
from RWESharp.Configurable import BoolConfigurable


class TileExplorer(QMainWindow):
    stateChanged = Signal(bool)
    tileSelected = Signal(list)

    def __init__(self, manager, parent=None):
        super().__init__(parent)
        self.manager = manager
        self.mod = manager.basemod
        self.category_colors = BoolConfigurable(self.mod, "TileExplorer.Category_colors", False, "Color of categories")
        self.tiles: ItemData = manager.tiles
        self.ui = Ui_TileExplorer()
        self.ui.setupUi(self)
        self.state = False
        self.preview = self.ui.Preview
        self.preview.add_manager(manager)
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
        self.selected_tiles: list[Tile] = []
        self.load_tiles()
        self.tiles_grid()

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
                item.setIcon(i.image2)
                self.view_tiles.addItem(item)
            return
        categories = []
        for i in self.view_categories.selectedItems():
            categories.append(i.data(Qt.ItemDataRole.UserRole))
        for category in categories:
            for i in self.tiles.get_items(category):
                item = QListWidgetItem(i.name)
                item.setData(Qt.ItemDataRole.UserRole, i)
                item.setIcon(i.image2)
                self.view_tiles.addItem(item)

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
        if len(selection) == 1:
            self.preview.tileimage.setOpacity(1)
            self.preview.tileimage.setPixmap(selection[0].data(Qt.ItemDataRole.UserRole).image2)
            self.preview.topleft.setPos(0, 0)
            self.preview.tileimage.setPos(0, 0)
            self.preview.verticalScrollBar().setValue(0)
            self.preview.horizontalScrollBar().setValue(0)

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
