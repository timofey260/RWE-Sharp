from RWESharp.Renderable import RenderLevelImage
from RWESharp.Core import CELLSIZE
from RWESharp.Utils import color_lerp
from PySide6.QtGui import QColor
from PySide6.QtCore import QPoint, QRect, QSize


class EffectRenderLevelImage(RenderLevelImage):
    def __init__(self, editor, depth, effect_index):
        super().__init__(editor.mod, depth)
        self.index = effect_index
        self.editor = editor

    def change_index(self, index):
        self.index = index
        self.draw_layer()

    def draw_layer(self) -> None:
        self.image.fill(QColor(0, 0, 0, 0))
        if self.manager.level.effect_len == 0:
            return
        for xi, x in enumerate(self.manager.level.effect_data(self.index)["mtrx"]):
            for yi, y in enumerate(x):
                self.draw_pixel(QPoint(xi, yi))
        self.redraw()

    def draw_pixel(self, point: QPoint):
        drawpoint = point * CELLSIZE
        val = self.manager.level.effect_data_pixel(self.index, point)
        color = color_lerp(self.editor.coloroff.value, self.editor.coloron.value, val / 100)
        self.painter.setPen(QColor(0, 0, 0, 0))
        self.painter.setBrush(color)
        self.painter.drawRect(QRect(drawpoint, QSize(CELLSIZE, CELLSIZE)))

