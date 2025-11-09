from PySide6.QtCore import QLine
from PySide6.QtGui import QColor

from RWESharp2.Core import CELLSIZE
from RWESharp2.Renderable import RenderLevelImage


class GridRenderLevelImage(RenderLevelImage):
    def __init__(self, module, depth, add_renderable: bool = True):
        super().__init__(module, depth, add_renderable=False)
        module.ui.gridpen.valueChanged.connect(self.draw_layer)
        module.ui.grid_size_X.valueChanged.connect(self.draw_layer)
        module.ui.grid_size_Y.valueChanged.connect(self.draw_layer)
        module.ui.grid_offset_X.valueChanged.connect(self.draw_layer)
        module.ui.grid_offset_Y.valueChanged.connect(self.draw_layer)
        if add_renderable:
            self.module.add_renderable(self)

    def draw_layer(self) -> None:
        self.painter.setPen(self.module.ui.gridpen.value)
        self.image.fill(QColor(0, 0, 0, 0))
        self.painter.drawLines([QLine(i, 0, i, self.image.height()) for i in range(CELLSIZE * self.module.ui.grid_offset_X.value, self.image.width(), CELLSIZE * self.module.ui.grid_size_X.value)])
        self.painter.drawLines([QLine(0, i, self.image.width(), i) for i in range(CELLSIZE * self.module.ui.grid_offset_Y.value, self.image.height(), CELLSIZE * self.module.ui.grid_size_Y.value)])
        self.redraw()

    def level_resized(self, rect):
        super().level_resized(rect)
        self.draw_layer()
