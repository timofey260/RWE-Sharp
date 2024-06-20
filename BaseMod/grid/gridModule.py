from core.Modify.baseModule import Module
from BaseMod.grid.gridRenderTexture import GridRenderTexture
from core.Renderable.RenderRect import RenderRect
from PySide6.QtCore import Slot, QRect, Qt, QPoint
from PySide6.QtGui import QBrush, QColor, QPen
from core.configTypes.BaseTypes import BoolConfigurable, FloatConfigurable
from core.configTypes.QtTypes import KeyConfigurable, ColorConfigurable
from core.info import CELLSIZE


class GridModule(Module):
    def __init__(self, mod):
        super().__init__(mod)
        self.enablegrid = BoolConfigurable(mod, "grid.enable_grid", False, "Enable grid")
        self.gridopacity = FloatConfigurable(mod, "grid.grid_opacity", .5, "Opacity grid")
        self.enablegrid_key = KeyConfigurable(mod, "grid.enable_grid_key", "Alt+G", "Grid key")
        self.backgroundcolor = ColorConfigurable(mod, "grid.bgcolor", QColor(150, 150, 150), "color of the background")
        self.bordercolor = ColorConfigurable(mod, "grid.bordercolor", QColor(255, 255, 255, 255), "color of the border")
        self.gridtexture = GridRenderTexture(self, 0).add_myself()
        self.rect = RenderRect(self, 1000, QRect(QPoint(0, 0), CELLSIZE * self.manager.level.level_size),
                               Qt.GlobalColor.transparent, QBrush(self.backgroundcolor.value)).add_myself()
        borders = self.manager.level.extra_tiles
        topleft = QPoint(borders[0], borders[1])
        bottomright = self.manager.level.level_size - QPoint(borders[2], borders[3])
        self.border = RenderRect(self, 0,
                                 QRect(self.viewport.editor_to_viewport(topleft),
                                       self.viewport.editor_to_viewport(bottomright)),
                                 QPen(self.bordercolor.value, 5, Qt.PenStyle.DashLine)).add_myself()

        self.enablegrid.valueChanged.connect(self.check_change)
        self.gridopacity.valueChanged.connect(self.check_change)

    @Slot()
    def check_change(self):
        self.gridtexture.renderedtexture.setOpacity(self.gridopacity.value if self.enablegrid.value else 0)

    def render_module(self):
        self.check_change()
        self.gridtexture.draw_layer()
