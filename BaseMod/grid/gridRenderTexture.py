from RWESharp.Renderable import RenderLevelImage
from RWESharp.Core import CELLSIZE
from PySide6.QtCore import QLine
from PySide6.QtGui import QColor


class GridRenderLevelImage(RenderLevelImage):
    def __init__(self, module, depth):
        super().__init__(module, depth)
        module.ui.gridpen.valueChanged.connect(self.draw_layer)

    def draw_layer(self) -> None:
        self.painter.setPen(self.module.ui.gridpen.value)
        self.image.fill(QColor(0, 0, 0, 0))
        self.painter.drawLines([QLine(i, 0, i, self.image.height()) for i in range(0, self.image.width(), CELLSIZE)])
        self.painter.drawLines([QLine(0, i, self.image.width(), i) for i in range(0, self.image.height(), CELLSIZE)])
        self.redraw()

    def level_resized(self):
        super().level_resized()
        self.draw_layer()
        self.redraw()
