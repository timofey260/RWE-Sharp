from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap, QColor
from core.Renderable.RenderImage import RenderImage
from core.info import CELLSIZE


class RenderLevelImage(RenderImage):
    def __init__(self, module, depth, add_renderable: bool = True):
        super().__init__(module, depth, QSize(1, 1), add_renderable=add_renderable)

    def init_graphics(self, viewport):
        super().init_graphics(viewport)
        self.level_resized(self.level.level_rect)

    def level_resized(self, rect):
        self.painter.end()
        self.image = QPixmap(QSize(rect.width() * CELLSIZE, rect.height() * CELLSIZE))
        self.image.fill(QColor(0, 0, 0, 0))
        self.painter.begin(self.image)
        self.renderedtexture.setPixmap(self.image)
