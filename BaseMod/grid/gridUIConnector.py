from PySide6.QtWidgets import QWidget, QCheckBox
from PySide6.QtGui import QAction
from PySide6.QtCore import QCoreApplication


class GridView(QWidget):
    def __init__(self, mod, parent=None):
        super().__init__(parent)
        self.mod = mod

        self.VQuickGrid = QCheckBox()
        self.VQuickGrid.setObjectName(u"VQuickGrid")
        self.VQuickGrid.setText(QCoreApplication.translate("MainWindow", u"Grid", None))
        self.VQuickGrid.setChecked(True)

        self.mod.add_quickview_option(self.VQuickGrid)

        self.grid = QAction("grid")
        self.mod.gridconfig.enablegrid.link_button_action(self.VQuickGrid, self.grid, self.mod.gridconfig.enablegrid_key)
        self.mod.manager.view_menu.addAction(self.grid)
