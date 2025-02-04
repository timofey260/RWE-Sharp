from PySide6.QtWidgets import QCheckBox
from PySide6.QtGui import QAction
from PySide6.QtCore import QCoreApplication, Qt
from RWESharp.Ui import ViewUI
from BaseMod.grid.grid_ui import Ui_GridView
from RWESharp.Configurable import BoolConfigurable, FloatConfigurable, IntConfigurable, KeyConfigurable, ColorConfigurable, PenConfigurable
from PySide6.QtGui import QColor, QPen


class GridView(ViewUI):
    def __init__(self, mod, parent=None):
        super().__init__(mod, parent)
        self.ui = Ui_GridView()
        self.ui.setupUi(self)

        self.enablegrid = BoolConfigurable(mod, "grid.enable_grid", False, "Enable grid")
        self.enableborder = BoolConfigurable(mod, "grid.enable_border", True, "Enable grid")
        self.gridopacity = FloatConfigurable(mod, "grid.grid_opacity", .5, "Opacity grid")
        self.enablegrid_key = KeyConfigurable(mod, "grid.enable_grid_key", "Ctrl+G", "Grid key")
        self.backgroundcolor = ColorConfigurable(mod, "grid.bgcolor", QColor(150, 150, 150), "color of the background")
        self.grid_size_X = IntConfigurable(mod, "grid.gridsizex", 1, "Grid scale X")
        self.grid_size_Y = IntConfigurable(mod, "grid.gridsizey", 1, "Grid scale Y")
        self.grid_offset_X = IntConfigurable(mod, "grid.gridoffsetx", 0, "Grid offset X")
        self.grid_offset_Y = IntConfigurable(mod, "grid.gridoffsety", 0, "Grid offset Y")

        self.gridpen = PenConfigurable(mod, "grid.gridpen", QPen(QColor(255, 255, 255, 70), 1), "Grid Pen")
        self.borderpen = PenConfigurable(mod, "grid.borderpen", QPen(QColor(255, 255, 255, 200), 5, Qt.PenStyle.DashLine), "Grid Pen")

        self.VQuickGrid = QCheckBox()
        self.VQuickGrid.setObjectName(u"VQuickGrid")
        self.VQuickGrid.setText(QCoreApplication.translate("MainWindow", u"Grid", None))
        self.VQuickGrid.setChecked(True)

        self.mod.add_quickview_option(self.VQuickGrid)

        self.grid = QAction("Grid")
        self.enablegrid.link_button_action(self.VQuickGrid, self.grid, self.enablegrid_key)
        self.enablegrid.link_button(self.ui.ShowGrid)
        self.enableborder.link_button(self.ui.ShowBorder)
        self.mod.manager.view_menu.addAction(self.grid)

        self.gridpen.link_pen_picker(self.ui.GridColor)
        self.borderpen.link_pen_picker(self.ui.BorderColor)
