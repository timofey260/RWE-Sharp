from core.Renderable.RenderTexture import RenderTexture
from core.info import CELLSIZE
from PySide6.QtCore import QLine
from PySide6.QtGui import QColor


class GridRenderTexture(RenderTexture):
    def __init__(self, module, level):
        super().__init__(module, level)
        self.painter.setPen(QColor(0, 0, 0, 255))

    def draw_layer(self) -> None:
        self.painter.drawLines([QLine(i, 0, i, self.image.height()) for i in range(0, self.image.width(), CELLSIZE)])
        self.painter.drawLines([QLine(0, i, self.image.width(), i) for i in range(0, self.image.height(), CELLSIZE)])
        self.redraw()
