from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap, QColor
from core.Renderable.RenderImage import RenderImage
from core.info import CELLSIZE


class RenderLevelImage(RenderImage):
    def __init__(self, module, depth):
        super().__init__(module, depth, QSize(1, 1))

    def init_graphics(self, viewport):
        super().init_graphics(viewport)
        self.level_resized()

    def level_resized(self):
        self.painter.end()
        self.image = QPixmap(QSize(self.viewport.level.level_width * CELLSIZE, self.viewport.level.level_height * CELLSIZE))
        self.image.fill(QColor(0, 0, 0, 0))
        self.painter.begin(self.image)
        self.renderedtexture.setPixmap(self.image)
