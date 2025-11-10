from PySide6.QtCore import QCoreApplication, Qt
from PySide6.QtGui import QAction
from PySide6.QtGui import QColor, QPen
from PySide6.QtWidgets import QCheckBox

from BaseMod.grid.grid_ui import Ui_MiscView
from RWS.Configurable import BoolConfigurable, IntConfigurable, KeyConfigurable, ColorConfigurable, \
    PenConfigurable
from RWS.Ui import ViewUI


class GridView(ViewUI):
    def __init__(self, mod, parent=None):
        super().__init__(mod, parent)
        self.ui = Ui_MiscView()
        self.ui.setupUi(self)

        self.enablewater = BoolConfigurable(mod, "grid.enable_water", False, "Enable water")
        self.enablegrid = BoolConfigurable(mod, "grid.enable_grid", False, "Enable grid")
        self.enableborder = BoolConfigurable(mod, "grid.enable_border", True, "Enable grid")
        self.more_funny = self.mod.bmconfig.more_funny
        #self.gridopacity = FloatConfigurable(mod, "grid.grid_opacity", .5, "Opacity grid")
        self.enablegrid_key = KeyConfigurable(mod, "grid.enable_grid_key", "Ctrl+G", "Grid key")
        self.enablewater_key = KeyConfigurable(mod, "grid.enable_water_key", "Alt+W", "Grid key")
        self.backgroundcolor = ColorConfigurable(mod, "grid.bgcolor", QColor(150, 150, 150), "Background Color")
        self.watercolor = ColorConfigurable(mod, "grid.watercolor", QColor(85, 70, 255, 120), "Water Color")
        self.grid_size_X = IntConfigurable(mod, "grid.gridsizex", 1, "Grid scale X")
        self.grid_size_Y = IntConfigurable(mod, "grid.gridsizey", 1, "Grid scale Y")
        self.grid_offset_X = IntConfigurable(mod, "grid.gridoffsetx", 0, "Grid offset X")
        self.grid_offset_Y = IntConfigurable(mod, "grid.gridoffsety", 0, "Grid offset Y")

        self.gridpen = PenConfigurable(mod, "grid.gridpen", QPen(QColor(255, 255, 255, 70), 1), "Grid Pen")
        self.borderpen = PenConfigurable(mod, "grid.borderpen", QPen(QColor(255, 255, 255, 200), 5, Qt.PenStyle.DashLine), "Grid Pen")

        self.VQuickGrid = QCheckBox()
        self.VQuickGrid.setObjectName(u"VQuickGrid")
        self.VQuickGrid.setText(QCoreApplication.translate("MainWindow", u"Grid", None))
        self.mod.add_quickview_option(self.VQuickGrid)

        self.VQuickWater = QCheckBox()
        self.VQuickWater.setObjectName(u"VQuickWater")
        self.VQuickWater.setText(QCoreApplication.translate("MainWindow", u"Water", None))
        self.mod.add_quickview_option(self.VQuickWater)

        self.grid = QAction("Grid")
        self.enablegrid.link_button_action(self.VQuickGrid, self.grid, self.enablegrid_key)
        self.enablegrid.link_button(self.ui.ShowGrid)
        self.mod.manager.view_menu.addAction(self.grid)

        self.water = QAction("Water")
        self.enablewater.link_button_action(self.VQuickWater, self.water, self.enablewater_key)
        self.enablewater.link_button(self.ui.Water)
        self.mod.manager.view_menu.addAction(self.water)
        self.watercolor.link_color_picker(self.ui.WaterColor)

        self.enableborder.link_button(self.ui.ShowBorder)
        self.gridpen.link_pen_picker(self.ui.GridColor)
        self.borderpen.link_pen_picker(self.ui.BorderColor)

        self.grid_size_X.link_spinbox(self.ui.ScaleX)
        self.grid_size_Y.link_spinbox(self.ui.ScaleY)
        self.grid_offset_X.link_spinbox(self.ui.OffsetX)
        self.grid_offset_Y.link_spinbox(self.ui.OffsetY)
