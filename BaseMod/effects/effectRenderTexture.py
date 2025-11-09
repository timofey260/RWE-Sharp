import numpy as np
from PySide6.QtCore import QPoint, QRect, QSize
from PySide6.QtGui import QColor

from RWESharp2.Core import CELLSIZE
from RWESharp2.Renderable import RenderLevelImage
from RWESharp2.Utils import color_lerp


class EffectRenderLevelImage(RenderLevelImage):
    def __init__(self, editor, depth, effect_index, add_renderable: bool = True):
        super().__init__(editor, depth, add_renderable=False)
        self.index = effect_index
        self.editor = editor
        self.painter.setPen(QColor(0, 0, 0, 0))
        # self.painter.setCompositionMode(self.painter.CompositionMode.CompositionMode_Source)
        if add_renderable:
            self.module.add_renderable(self)

    def change_index(self, index):
        self.index = index
        self.draw_layer()

    def draw_layer(self) -> None:
        self.image.fill(QColor(0, 0, 0, 0))
        if self.manager.selected_viewport is None or len(self.manager.selected_viewport.level.l_effects) == 0:
            return
        with np.nditer(self.module.level.l_effects[self.index]["mtrx"], flags=['multi_index'], op_flags=['readonly']) as it:
            for _ in it:
                self.draw_pixel(QPoint(it.multi_index[0], it.multi_index[1]))

        # for xi, x in enumerate(self.manager.selected_viewport.level.l_effects_effect_data(self.index)["mtrx"]):
        #     for yi, y in enumerate(x):
        #         self.draw_pixel(QPoint(xi, yi))
        self.redraw()

    def level_resized(self, rect):
        super().level_resized(rect)
        self.draw_layer()

    def draw_pixel(self, point: QPoint, clear=False):
        drawpoint = point * CELLSIZE
        val = self.manager.selected_viewport.level.l_effects[self.index, point.x(), point.y()]
        color = color_lerp(self.editor.coloroff.value, self.editor.coloron.value, val / 100)
        self.painter.setBrush(color)
        self.painter.setPen(QColor(0, 0, 0, 0))
        rect = QRect(drawpoint, QSize(CELLSIZE, CELLSIZE))
        if clear:
            self.painter.setCompositionMode(self.painter.CompositionMode.CompositionMode_Clear)
            self.painter.fillRect(rect, QColor(0, 0, 0, 0))
            self.painter.setCompositionMode(self.painter.CompositionMode.CompositionMode_SourceOver)
        self.painter.drawRect(rect)

