from PySide6.QtWidgets import QCheckBox
from PySide6.QtGui import QAction
from PySide6.QtCore import QCoreApplication
from core.Modify.ui import ViewUI


class GridView(ViewUI):
    def __init__(self, mod, parent=None):
        super().__init__(mod, parent)
        self.module = mod.gridmodule
        self.VQuickGrid = QCheckBox()
        self.VQuickGrid.setObjectName(u"VQuickGrid")
        self.VQuickGrid.setText(QCoreApplication.translate("MainWindow", u"Grid", None))
        self.VQuickGrid.setChecked(True)

        self.mod.add_quickview_option(self.VQuickGrid)

        self.grid = QAction("Grid")
        self.module.enablegrid.link_button_action(self.VQuickGrid, self.grid, self.module.enablegrid_key)
        self.mod.manager.view_menu.addAction(self.grid)
