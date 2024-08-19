from BaseMod.palettes.paletteui import Ui_Paletteui
from BaseMod.palettes.RaspberryDark import RaspberryDark
from PySide6.QtWidgets import QTreeWidgetItem, QColorDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from RWESharp.Ui import ThemeUI


class RPDarkUI(ThemeUI):
    def setup_ui(self, viewer):
        self.ui = Ui_Paletteui()
        self.ui.setupUi(viewer)
        self.theme: RaspberryDark
        self.theme.styleindex.link_combobox(self.ui.Style)
        self.theme.stylepalette.link_combobox(self.ui.Palette)
        self.ui.treeWidget.itemClicked.connect(self.clicked)
        self.fill_tree()

    def fill_tree(self):
        self.ui.treeWidget.clear()
        for i in self.theme.colors:
            item = QTreeWidgetItem([i.description])
            icon = QPixmap(10, 10)
            icon.fill(i.value)
            item.setIcon(0, icon)
            item.setData(0, Qt.ItemDataRole.UserRole, i)
            i.valueChanged.connect(self.fill_tree)
            self.ui.treeWidget.addTopLevelItem(item)

    def clicked(self, item: QTreeWidgetItem, column):
        conf = item.data(0, Qt.ItemDataRole.UserRole)
        dialog = QColorDialog(conf.value, self.mod.manager.window)
        dialog.open()
        # dialog.show()
        dialog.colorSelected.connect(lambda x: conf.update_value(x))