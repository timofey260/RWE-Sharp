from abc import abstractmethod
import os

from PySide6.QtCore import Signal, Qt, QSize, QTimer
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QTreeWidgetItem, QListWidgetItem, QListWidget
from PySide6.QtWidgets import QDialog, QMessageBox, QDialogButtonBox
from BaseMod.ui.createcategory_ui import Ui_CreateCategory
from BaseMod.ui.itemaction_ui import Ui_ItemAction

from BaseMod.ui.explorer_ui import Ui_Explorer
from RWS.Configurable import BoolConfigurable
from RWS.Widgets import ViewDockWidget
from RWS.Utils import paint_svg_qicon


class Explorer(ViewDockWidget):
    itemselected = Signal(list)

    def __init__(self, mod, parent=None):
        super().__init__(parent)
        parent.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self)
        self.manager = mod.manager
        self.mod = mod
        self.category_colors = BoolConfigurable(self.mod, "TileExplorer.category_colors", False, "Color of categories")
        self.ui = Ui_Explorer()
        self.ui.setupUi(self)
        self.preview = self.ui.Preview
        self.preview.add_manager(self.manager)
        self.view_categories = self.ui.Categories
        self.view_items = self.ui.Items

        self.view_categories.setAlternatingRowColors(True)
        self.view_categories.setEditTriggers(QListWidget.EditTrigger.DoubleClicked)
        self.view_categories.itemSelectionChanged.connect(self.change_items)
        self.view_categories.setDragDropMode(QListWidget.DragDropMode.NoDragDrop)
        self.view_items.itemSelectionChanged.connect(self.change_item)
        self.view_items.setDragDropMode(QListWidget.DragDropMode.NoDragDrop)  # todo change in future
        self.view_items.setSelectionMode(QListWidget.SelectionMode.ExtendedSelection)
        self.view_items.setIconSize(QSize(20, 20))

        #self.ui.Favourite.clicked.connect()

        self.simplemode = False
        self.load_categories()
        self.items_grid()
        self.change_items()
        self.selected = []

        self.ui.TilesListView.clicked.connect(self.items_list)
        self.ui.TilesGridViewBig.clicked.connect(self.items_grid)
        self.ui.TilesGridViewSmall.clicked.connect(self.items_grid_small)
        self.ui.TilesIconView.clicked.connect(self.items_grid_ununiform)
        self.view_items.setResizeMode(QListWidget.ResizeMode.Adjust)

        self.category = 0
        self.item = 0

        self.ui.CatNext.clicked.connect(self.cat_next)
        self.ui.CatPrev.clicked.connect(self.cat_prev)
        self.ui.TileNext.clicked.connect(self.item_next)
        self.ui.TilePrev.clicked.connect(self.item_prev)
        self.setFloating(True)

        self.mod.bmconfig.icon_color.valueChanged.connect(self.changecolor)
        self.changecolor(self.mod.bmconfig.icon_color.value)
        self.ui.splitter.splitterMoved.connect(self.splitter_moved)
        self.ui.SearchBar.textChanged.connect(self.search)

        self.ui.CatsAddCC.clicked.connect(self.add_category)
        self.ui.CatsRemoveCC.clicked.connect(self.remove_category)
        self.ui.Favourite.clicked.connect(self.item_action)

    def resizeEvent(self,  event):
        if hasattr(self, 'ui') and self.ui:
            width,  height = self.width(), self.height()
            aspect_ratio = width / height if height else 1
            self.ui.splitter_3.setOrientation(Qt.Orientation.Horizontal if aspect_ratio > 1.6 else Qt.Orientation.Vertical)
            self.ui.splitter_2.setOrientation(Qt.Orientation.Vertical if 1.6 < aspect_ratio < 2 else Qt.Orientation.Horizontal)
        super().resizeEvent(event)

    def splitter_moved(self, pos, index):
        if self.ui.splitter.sizes()[1] == 0 and not self.simplemode:
            self.simplemode = True
            self.load_categories()
            self.view_items.clear()
        elif self.ui.splitter.sizes()[1] != 0 and self.simplemode:
            self.simplemode = False
            self.load_categories()
            self.change_items()

    def changecolor(self, color: QColor):
        self.ui.TilesListView.setIcon(paint_svg_qicon(u":/grids/grid/list.svg", color))
        self.ui.TilesGridViewBig.setIcon(paint_svg_qicon(u":/grids/grid/mediumgrid.svg", color))
        self.ui.TilesGridViewSmall.setIcon(paint_svg_qicon(u":/grids/grid/smallgrid.svg", color))
        self.ui.TilesIconView.setIcon(paint_svg_qicon(u":/grids/grid/smallgrid2.svg", color))
        self.ui.Pin.setIcon(paint_svg_qicon(u":/special/special/pin.svg", color))

        self.ui.CatsAddCC.setIcon(paint_svg_qicon(u":/special/special/add_category.svg", color))
        self.ui.CatsRemoveCC.setIcon(paint_svg_qicon(u":/special/special/remove_category.svg", color))
        self.ui.Favourite.setIcon(paint_svg_qicon(u":/special/special/add.svg", color))

        self.ui.CatPrev.setIcon(paint_svg_qicon(u":/misc/misc/arrow_left.svg", color))
        self.ui.CatNext.setIcon(paint_svg_qicon(u":/misc/misc/arrow_right.svg", color))
        self.ui.TilePrev.setIcon(paint_svg_qicon(u":/misc/misc/arrow_up.svg", color))
        self.ui.TileNext.setIcon(paint_svg_qicon(u":/misc/misc/arrow_down.svg", color))

    def cat_next(self):
        if self.simplemode:
            self.view_categories.topLevelItem(self.category).setExpanded(False)

        self.category = (self.categoryindex + 1) % self.view_categories.topLevelItemCount()
        self.view_categories.setCurrentItem(self.view_categories.topLevelItem(self.category))
        if self.simplemode:
            cat = self.view_categories.topLevelItem(self.category)
            self.item = self.itemindex % cat.childCount()
            self.view_categories.setCurrentItem(cat.child(self.item))
            cat.setExpanded(True)
            return
        self.item = self.itemindex % self.view_items.count()
        self.view_items.setCurrentRow(self.item)

    def cat_prev(self):
        if self.simplemode:
            self.view_categories.topLevelItem(self.category).setExpanded(False)
        self.category = (self.categoryindex - 1) % self.view_categories.topLevelItemCount()
        self.view_categories.setCurrentItem(self.view_categories.topLevelItem(self.category))
        if self.simplemode:
            cat = self.view_categories.topLevelItem(self.category)
            self.item = self.itemindex % cat.childCount()
            self.view_categories.setCurrentItem(cat.child(self.item))
            cat.setExpanded(True)
            return
        self.item = self.itemindex % self.view_items.count()
        self.view_items.setCurrentRow(self.item)

    def item_next(self):
        if self.simplemode:
            if self.view_categories.topLevelItem(self.category).childCount() == 0:
                return
            self.item = (self.itemindex + 1) % self.view_categories.topLevelItem(self.category).childCount()
            self.view_categories.setCurrentItem(self.view_categories.topLevelItem(self.category).child(self.item))
            return
        if self.view_items.count() == 0:
            return
        self.item = (self.itemindex + 1) % self.view_items.count()
        self.view_items.setCurrentRow(self.item)

    def item_prev(self):
        if self.simplemode:
            if self.view_categories.topLevelItem(self.category).childCount() == 0:
                return
            self.item = (self.itemindex - 1) % self.view_categories.topLevelItem(self.category).childCount()
            self.view_categories.setCurrentItem(self.view_categories.topLevelItem(self.category).child(self.item))
            return
        if self.view_items.count() == 0:
            return
        self.item = (self.itemindex - 1) % self.view_items.count()
        self.view_items.setCurrentRow(self.item)

    def items_grid(self):
        self.view_items.setViewMode(QListWidget.ViewMode.IconMode)
        self.view_items.setIconSize(QSize(40, 40))
        self.view_items.setSpacing(20)
        self.view_items.setUniformItemSizes(True)
        self.view_items.setAlternatingRowColors(False)

    def items_grid_ununiform(self):
        self.view_items.setViewMode(QListWidget.ViewMode.IconMode)
        self.view_items.setIconSize(QSize(40, 40))
        self.view_items.setSpacing(10)
        self.view_items.setUniformItemSizes(False)
        self.view_items.setAlternatingRowColors(False)

    def items_grid_small(self):
        self.view_items.setViewMode(QListWidget.ViewMode.IconMode)
        self.view_items.setIconSize(QSize(20, 20))
        self.view_items.setSpacing(5)
        self.view_items.setUniformItemSizes(True)
        self.view_items.setAlternatingRowColors(False)

    def items_list(self):
        self.view_items.setViewMode(QListWidget.ViewMode.ListMode)
        self.view_items.setIconSize(QSize(20, 20))
        self.view_items.setSpacing(0)
        self.view_items.setUniformItemSizes(True)
        self.view_items.setAlternatingRowColors(True)

    def load_categories(self):
        filter = self.ui.SearchBar.text()
        self.view_categories.clear()
        self.view_categories.collapseAll()
        for category in self.get_categories():
            item = self.cat_from_data(category)
            if item is None:
                continue
            if not self.simplemode:
                self.view_categories.addTopLevelItem(item)
                continue
            for i in self.category_items(category):
                tileitem = self.treeitem_from_data(i)
                if item is None:
                    continue
                item.addChild(tileitem)
            if filter == "" or item.childCount() > 0:
                self.view_categories.addTopLevelItem(item)
        if filter != "":
            self.view_categories.expandAll()

    def change_items(self):
        if self.simplemode:
            self.change_item()
            return
        filter = self.ui.SearchBar.text()
        if len(self.view_categories.selectedItems()) == 0 and filter == "":
            return
        self.view_items.clear()
        if filter != "":
            for i in self.get_all_items():
                if filter.lower() not in i.name.lower():
                    continue
                item = self.item_from_data(i)
                self.view_items.addItem(item)
            return
        categories = []
        for i in self.view_categories.selectedItems():
            categories.append(i.data(0, Qt.ItemDataRole.UserRole))
        for category in categories:
            for i in self.category_items(category):
                item = self.item_from_data(i)
                self.view_items.addItem(item)

    def change_item(self):
        if self.simplemode:
            selection = list(filter(lambda x: isinstance(x, self.itemtype()), list(
                map(lambda x: x.data(0, Qt.ItemDataRole.UserRole), self.view_categories.selectedItems()))))
            if len(selection) == 0:
                return
            self.selected = selection
        else:
            selection = list(map(lambda x: x.data(Qt.ItemDataRole.UserRole), self.view_items.selectedItems()))
            if len(selection) == 0:
                return
            self.selected = selection
        self.itemselected.emit(self.selected)
        self.preview_item(None)

        if len(self.selected) == 1:
            self.preview_item(self.selected[0])
            # self.preview.preview_tile(self.selected_tiles[0], self.synced_draw_option, self.layer.value, self.colortable)

    def search(self, text: str):
        self.load_categories()
        self.change_items()

    def add_category(self):
        while True:
            d = QDialog()
            ui = Ui_CreateCategory()
            ui.setupUi(d)
            ui.CategoryName.setText("Custom Category")
            ui.CategoryColor.set_color(QColor(160, 20, 20))

            value = d.exec()
            print(value, QDialogButtonBox.StandardButton.Cancel)
            if value == 0:
                return
            filepath = os.path.join(self.custom_categories_path, ui.CategoryName.text())
            color = ui.CategoryColor.color
            if os.path.exists(filepath):
                message = QMessageBox(QMessageBox.Icon.Warning, "Category Exists", "This category already exists!\nWould you like to override it?")
                message.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Cancel)
                message.setDefaultButton(QMessageBox.StandardButton.Cancel)
                value2 = message.exec()
                if value2 == QMessageBox.StandardButton.No:
                    return
                if value2 == QMessageBox.StandardButton.Cancel:
                    continue
            break
        with open(filepath, "w") as f:
            f.write(f"{color.red()} {color.green()} {color.blue()}")
        self.categories_modified()

    def remove_category(self):
        if not self.category_is_custom(self.categoryindex):
            return
        message = QMessageBox(QMessageBox.Icon.Warning, "Delete Custom Category", "Are you sure?")
        message.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
        message.setDefaultButton(QMessageBox.StandardButton.Cancel)

        value = message.exec()
        if value == QMessageBox.StandardButton.Cancel:
            return
        filepath = os.path.join(self.custom_categories_path, self.category_name(self.categoryindex))
        if os.path.exists(filepath):
            os.remove(filepath)
            self.categories_modified()

    def item_action(self):
        print(self.selected)

    def focussearch(self):
        self.raise_()
        self.activateWindow()
        QTimer.singleShot(0, self.ui.SearchBar.setFocus)

    @property
    def categoryindex(self):
        if len(self.view_categories.selectedItems()) == 0:
            return self.category
        item = self.view_categories.selectedItems()[0]
        if self.view_categories.indexOfTopLevelItem(item) == -1:
            return self.view_categories.indexFromItem(item.parent()).row()
        return self.view_categories.indexFromItem(item).row()

    @property
    def itemindex(self):
        if len(self.view_categories.selectedItems()) == 0 or len(self.view_items.selectedItems()) == 0:
            return self.item
        if self.simplemode:
            if self.view_categories.indexFromItem(self.view_categories.selectedItems()[0]).column() == 1:
                return self.view_categories.indexFromItem(self.view_categories.selectedItems()[0]).row()
            return 0
        return self.view_items.row(self.view_items.selectedItems()[0])

    @abstractmethod
    def get_categories(self) -> list:
        pass

    @abstractmethod
    def get_all_items(self) -> list:
        pass

    @abstractmethod
    def item_from_data(self, data) -> QListWidgetItem | None:
        pass

    @abstractmethod
    def treeitem_from_data(self, data) -> QTreeWidgetItem | None:
        pass

    @abstractmethod
    def cat_from_data(self, cat) -> QTreeWidgetItem | None:
        pass

    @abstractmethod
    def itemtype(self) -> type:
        pass

    @abstractmethod
    def preview_item(self, item):
        pass

    @abstractmethod
    def category_items(self, cat) -> list:
        pass

    @abstractmethod
    def categories_modified(self) -> None:
        pass

    @property
    @abstractmethod
    def custom_categories_path(self) -> str:
        return ""

    @abstractmethod
    def category_is_custom(self, index: int) -> bool:
        return False

    @abstractmethod
    def category_name(self, index) -> str:
        return ""