from BaseMod.tiles.ui.tileexplorer import Ui_TileExplorer
from PySide6.QtWidgets import QMainWindow, QTreeWidgetItem, QListWidgetItem, QListWidget
from PySide6.QtGui import QAction, QPixmap, QColor
from PySide6.QtCore import Slot, Signal, Qt, QSize
from RWESharp.Core import ItemData
from RWESharp.Loaders import Tile
from RWESharp.Configurable import BoolConfigurable


class TileExplorer(QMainWindow):
    stateChanged = Signal(bool)

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
        self.load_tiles()

    def load_tiles(self):
        self.view_categories.clear()
        self.view_categories.setAlternatingRowColors(True)
        for category, color in zip(range(len(self.tiles.categories)), self.tiles.colors):
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
        if len(self.view_categories.selectedItems()) == 0:
            return
        self.view_tiles.clear()
        categories = []
        for i in self.view_categories.selectedItems():
            categories.append(i.data(Qt.ItemDataRole.UserRole))
        for category in categories:
            for i in self.tiles.get_items(category):
                i: Tile
                item = QListWidgetItem(i.name)
                item.setData(Qt.ItemDataRole.UserRole, i)
                item.setIcon(i.image2)
                self.view_tiles.addItem(item)
        self.view_tiles.setUniformItemSizes(True)

    @Slot()
    def change_tile(self):
        selection = self.view_tiles.selectedItems()
        if len(selection) == 1:
            self.preview.tileimage.setPixmap(selection[0].data(Qt.ItemDataRole.UserRole).image2)

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
