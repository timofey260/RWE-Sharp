from BaseMod.palettes.paletteui import Ui_Paletteui
from BaseMod.palettes.RaspberryDark import RaspberryDark
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
        self.theme.styleindex.link_combobox(self.ui.Style)
        self.theme.stylepalette.link_combobox(self.ui.Palette)
        self.ui.treeWidget.itemDoubleClicked.connect(self.clicked)
        self.ui.Import.clicked.connect(self.import_action)
        self.ui.Export.clicked.connect(self.export_action)
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
            i.valueChanged.connect(self.updateitem)

    def updateitem(self):
        if self.theme.multiple:
            return
        self.fill_tree()  # well it won't be that bad
        return

    def clicked(self, item: QTreeWidgetItem, column):
        conf = item.data(0, Qt.ItemDataRole.UserRole)
        dialog = QColorDialog(conf.value, self.mod.manager.window)
        dialog.open()
        # dialog.show()
        dialog.colorSelected.connect(lambda x: conf.update_value(x))

    def import_action(self):
        file, _ = QFileDialog.getOpenFileName(self.mod.manager.window, "Select a file", PATH)
        self.theme.multiple = True
        with open(file) as f:
            for i, v in enumerate(f.readlines()):
                # index = v.find(":")
                self.theme.colors[i].update_value(QColor.fromString(v.replace("\n", "")))
                # self.updateitem(self.ui.treeWidget.itemAt(0, i), self.theme.colors[i].value)
        self.theme.multiple = False
        self.fill_tree()
        self.theme.theme_reenable()

    def export_action(self):
        file, _ = QFileDialog.getSaveFileName(self.mod.manager.window, "Saving theme palette", PATH)
        with open(file, "w") as f:
            for i in self.theme.colors:
                f.write(f"{i.value.name()}\n")
