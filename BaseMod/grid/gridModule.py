from BaseMod.grid.gridRenderTexture import GridRenderLevelImage
from PySide6.QtCore import Slot, QRect, Qt, QPoint
from PySide6.QtGui import QBrush, QColor, QPen
from RWESharp.Renderable import RenderRect
from RWESharp.Modify import Module
from RWESharp.Core import CELLSIZE
from widgets.Viewport import ViewPort


class GridModule(Module):
    def __init__(self, mod):
        super().__init__(mod)
        self.ui = mod.gridui

        self.gridtexture = GridRenderLevelImage(self, 0).add_myself(self)
        self.rect = RenderRect(self, 1000, QRect(QPoint(0, 0), QPoint(1, 1)),
                               Qt.GlobalColor.transparent, QBrush(self.ui.backgroundcolor.value)).add_myself(self)
        self.border = RenderRect(self, 0,
                                 QRect(QPoint(0, 0), QPoint(1, 1)),
                                 QPen(self.ui.bordercolor.value, 5, Qt.PenStyle.DashLine)).add_myself(self)

        self.ui.enablegrid.valueChanged.connect(self.check_change)
        self.ui.gridopacity.valueChanged.connect(self.check_change)
        self.ui.enableborder.valueChanged.connect(self.change_border)

        self.ui.backgroundcolor.valueChanged.connect(self.rect.drawrect.setBrush)
        self.ui.bordercolor.valueChanged.connect(lambda x: self.border.drawrect.setPen(QPen(x, 5, Qt.PenStyle.DashLine)))
        self.render_module()

    @Slot()
    def check_change(self):
        self.gridtexture.renderedtexture.setOpacity(self.ui.gridopacity.value if self.ui.enablegrid.value else 0)

    def change_border(self):
        self.border.drawrect.setOpacity(1 if self.ui.enableborder.value else 0)

    def render_module(self):
        self.check_change()
        self.change_border()
        self.gridtexture.draw_layer()

    def init_scene_items(self, viewport):
        super().init_scene_items(viewport)
        self.level_resized()

    def level_resized(self):
        self.rect.setRect(QRect(QPoint(0, 0), CELLSIZE * self.level.level_size))
        borders = self.level.extra_tiles
        topleft = QPoint(borders[0], borders[1])
        bottomright = self.level.level_size - QPoint(borders[2], borders[3])
        self.border.setRect(QRect(topleft * CELLSIZE, bottomright * CELLSIZE))
        super().level_resized()
