from BaseMod.themes.paletteui import Ui_Paletteui
from BaseMod.themes.RaspberryDark import RaspberryDark
from PySide6.QtWidgets import QTreeWidgetItem, QColorDialog, QFileDialog
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtCore import Qt
from RWESharp.Ui import ThemeUI
from RWESharp.Core import PATH
from RWESharp.Configurable import ColorConfigurable


class RPDarkUI(ThemeUI):
    def setup_ui(self, viewer):
        self.ui = Ui_Paletteui()
        self.ui.setupUi(viewer)
        self.theme: RaspberryDark
        self.ui.treeWidget.itemDoubleClicked.connect(self.clicked)
        self.ui.Import.clicked.connect(self.import_action)
        self.ui.Export.clicked.connect(self.export_action)
        self.ui.Palette.clear()
        self.ui.Palette.addItems(["RaspberryDark", "MintDark", "MoonlightDark"])
        self.ui.Style.clear()
        self.ui.Style.addItems(["Sharp", "Circular"])
        self.theme.styleindex.link_combobox(self.ui.Style)
        self.theme.stylepalette.link_combobox(self.ui.Palette)
        self.theme.stylepalette.valueChanged.connect(self.fill_tree)
        self.fill_tree()

    def fill_tree(self):
        self.ui.treeWidget.clear()
        for i in self.theme.colors:
            item = QTreeWidgetItem([i.description])
            icon = QPixmap(10, 10)
            icon.fill(i.value)
            item.setIcon(0, icon)
            item.setData(0, Qt.ItemDataRole.UserRole, i)
            self.ui.treeWidget.addTopLevelItem(item)
            # i.valueChanged.connect(self.updateitem)

    def updateitem(self):
        if self.theme.multiple:
            return
        self.fill_tree()  # well it won't be that bad

    def clicked(self, item: QTreeWidgetItem, column):
        conf = item.data(0, Qt.ItemDataRole.UserRole)
        dialog = QColorDialog(conf.value, self.mod.manager.window)
        dialog.open()
        # dialog.show()
        dialog.colorSelected.connect(lambda x: [conf.update_value(x), self.fill_tree()])

    def import_action(self):
        file, _ = QFileDialog.getOpenFileName(self.mod.manager.window, "Select a file", PATH)
        self.theme.multiple = True
        self.theme.open_palette(file)
        self.theme.multiple = False
        self.fill_tree()
        self.theme.theme_reenable()

    def export_action(self):
        file, _ = QFileDialog.getSaveFileName(self.mod.manager.window, "Saving themes palette", PATH)
        with open(file, "w") as f:
            for i in self.theme.colors:
                f.write(f"{i.value.name()}\n")
