from BaseMod.grid.gridRenderTexture import GridRenderLevelImage
from PySide6.QtCore import Slot, QRect, Qt, QPoint
from PySide6.QtGui import QBrush, QColor, QPen
from RWESharp.Renderable import RenderRect
from RWESharp.Modify import Module
from RWESharp.Configurable import BoolConfigurable, FloatConfigurable, IntConfigurable, KeyConfigurable, ColorConfigurable
from RWESharp.Core import CELLSIZE


class GridModule(Module):
    def __init__(self, mod):
        super().__init__(mod)
        self.enablegrid = BoolConfigurable(mod, "grid.enable_grid", False, "Enable grid")
        self.gridopacity = FloatConfigurable(mod, "grid.grid_opacity", .5, "Opacity grid")
        self.enablegrid_key = KeyConfigurable(mod, "grid.enable_grid_key", "Ctrl+G", "Grid key")
        self.backgroundcolor = ColorConfigurable(mod, "grid.bgcolor", QColor(150, 150, 150), "color of the background")
        self.bordercolor = ColorConfigurable(mod, "grid.bordercolor", QColor(255, 255, 255, 255), "color of the border")
        self.grid_size_X = IntConfigurable(mod, "grid.gridsizex", 1, "Grid scale X")
        self.grid_size_Y = IntConfigurable(mod, "grid.gridsizey", 1, "Grid scale Y")
        self.grid_offset_X = IntConfigurable(mod, "grid.gridoffsetx", 0, "Grid offset X")
        self.grid_offset_Y = IntConfigurable(mod, "grid.gridoffsety", 0, "Grid offset Y")

        self.gridtexture = GridRenderLevelImage(self, 0).add_myself(self)
        self.rect = RenderRect(self.mod, 1000, QRect(QPoint(0, 0), CELLSIZE * self.manager.level.level_size),
                               Qt.GlobalColor.transparent, QBrush(self.backgroundcolor.value)).add_myself(self)
        borders = self.manager.level.extra_tiles
        topleft = QPoint(borders[0], borders[1])
        bottomright = self.manager.level.level_size - QPoint(borders[2], borders[3])
        self.border = RenderRect(self.mod, 0,
                                 QRect(self.viewport.editor_to_viewport(topleft),
                                       self.viewport.editor_to_viewport(bottomright)),
                                 QPen(self.bordercolor.value, 5, Qt.PenStyle.DashLine)).add_myself(self)

        self.enablegrid.valueChanged.connect(self.check_change)
        self.gridopacity.valueChanged.connect(self.check_change)

    @Slot()
    def check_change(self):
        self.gridtexture.renderedtexture.setOpacity(self.gridopacity.value if self.enablegrid.value else 0)

    def render_module(self):
        self.check_change()
        self.gridtexture.draw_layer()

    def level_resized(self):
        self.rect.setRect(QRect(QPoint(0, 0), CELLSIZE * self.manager.level.level_size))
        borders = self.manager.level.extra_tiles
        topleft = QPoint(borders[0], borders[1])
        bottomright = self.manager.level.level_size - QPoint(borders[2], borders[3])
        self.border.setRect(QRect(self.viewport.editor_to_viewport(topleft), self.viewport.editor_to_viewport(bottomright)))
        super().level_resized()
