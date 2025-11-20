from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QAction
from PySide6.QtWidgets import QTreeWidgetItem, QListWidgetItem, QTableWidgetItem

from BaseMod.Explorer import Explorer
from RWS.Loaders import Prop


class PropExplorer(Explorer):
    def category_items(self, cat) -> list:
        return cat.props

    def get_categories(self) -> list:
        return self.props.categories

    def get_all_items(self) -> list:
        return self.props.all_props()

    def item_from_data(self, data) -> QListWidgetItem | None:
        filter = self.ui.SearchBar.text()
        if filter != "" and filter.lower() not in data.name.lower() and not self.simplemode:
            return None
        item = QListWidgetItem(data.name)
        item.setData(Qt.ItemDataRole.UserRole, data)
        item.setIcon(self.getimage(data.images[0]))
        return item

    def treeitem_from_data(self, data) -> QTreeWidgetItem | None:
        filter = self.ui.SearchBar.text()
        if filter != "" and filter.lower() not in data.name.lower():
            return None
        tileitem = QTreeWidgetItem([data.name])
        tileitem.setData(0, Qt.ItemDataRole.UserRole, data)
        tileitem.setIcon(0, self.getimage(data.images[0]))
        return tileitem

    def cat_from_data(self, cat) -> QTreeWidgetItem | None:
        filter = self.ui.SearchBar.text()
        if filter != "" and filter.lower() not in cat.name.lower() and not self.simplemode:
            return None
        color = cat.color
        image = QPixmap(20, 20)
        image.fill(color)
        item = QTreeWidgetItem([cat.name])
        item.setIcon(0, image)
        item.setData(0, Qt.ItemDataRole.UserRole, cat)
        return item

    def itemtype(self) -> type:
        return Prop

    def preview_item(self, item: Prop):
        if item is None:
            self.previewprop.setOpacity(0)
            return
        self.previewprop.setOpacity(1)
        self.previewprop.setPixmap(self.getimage(item.images[0]))
        self.ui.Properties.clear()
        self.ui.Properties.setRowCount(4)
        self.ui.Properties.setColumnCount(1)
        self.ui.Properties.setVerticalHeaderItem(0, QTableWidgetItem("Name"))
        self.ui.Properties.setItem(0, 0, QTableWidgetItem(item.name))
        self.ui.Properties.setVerticalHeaderItem(1, QTableWidgetItem("Description"))
        self.ui.Properties.setItem(1, 0, QTableWidgetItem(item.description))
        self.ui.Properties.setVerticalHeaderItem(2, QTableWidgetItem("Size"))
        self.ui.Properties.setItem(2, 0, QTableWidgetItem(f"{item.size.width()}x{item.size.height()}"))
        self.ui.Properties.setVerticalHeaderItem(3, QTableWidgetItem("Tags"))
        self.ui.Properties.setItem(3, 0, QTableWidgetItem(", ".join(item.tags)))
        self.ui.Properties.adjustSize()
        self.ui.Properties.resizeColumnsToContents()

    def __init__(self, editor, parent=None):
        self.props = editor.manager.props
        super().__init__(editor.mod, parent)
        self.previewprop = self.preview.workscene.addPixmap(QPixmap(1, 1))
        self.preview.items.append(self.previewprop)
        self.ui.LItem.setText("Prop")
        self.ui.LItems.setText("Props")
        self.setWindowTitle("Prop Explorer")
        self.hide()

        self.prop_explorer_action = QAction("Prop Explorer")
        self.manager.window_menu.addAction(self.prop_explorer_action)
        self.link_action(self.prop_explorer_action)
        self.mod.bmconfig.propexplorer_key.link_action(self.prop_explorer_action)
        self.itemselected.connect(editor.setprop)

        self.props.propschanged.connect(self.load_categories)

        self.ui.LayerBox.setVisible(False)
        self.ui.RenderOption.setVisible(False)

    def getimage(self, image):
        if isinstance(image, QPixmap):
            return image
        return QPixmap.fromImage(image)
