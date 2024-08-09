from PySide6.QtWidgets import QCheckBox
from PySide6.QtGui import QAction
from PySide6.QtCore import QCoreApplication
from RWESharp.Ui import ViewUI
from BaseMod.grid.grid_ui import Ui_GridView


class GridView(ViewUI):
    def __init__(self, mod, parent=None):
        super().__init__(mod, parent)
        self.ui = Ui_GridView()
        self.ui.setupUi(self)

        self.module = mod.gridmodule
        self.VQuickGrid = QCheckBox()
        self.VQuickGrid.setObjectName(u"VQuickGrid")
        self.VQuickGrid.setText(QCoreApplication.translate("MainWindow", u"Grid", None))
        self.VQuickGrid.setChecked(True)

        self.mod.add_quickview_option(self.VQuickGrid)

        self.grid = QAction("Grid")
        self.module.enablegrid.link_button_action(self.VQuickGrid, self.grid, self.module.enablegrid_key)
        self.module.enablegrid.link_button(self.ui.ShowGrid)
        self.module.enableborder.link_button(self.ui.ShowBorder)
        self.mod.manager.view_menu.addAction(self.grid)
