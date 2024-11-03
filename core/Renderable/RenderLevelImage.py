from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap, QColor
from core.Renderable.RenderImage import RenderImage
from core.info import CELLSIZE


class RenderLevelImage(RenderImage):
    def __init__(self, mod, depth):
        super().__init__(mod, depth, QSize(mod.manager.level_width * CELLSIZE, mod.manager.level_height * CELLSIZE))

    def level_resized(self):
        self.painter.end()
        self.image = QPixmap(QSize(self.mod.manager.level_width * CELLSIZE, self.mod.manager.level_height * CELLSIZE))
        self.image.fill(QColor(0, 0, 0, 0))
        self.painter.begin(self.image)
        if self.renderedtexture is None:
            return
        self.renderedtexture.setPixmap(self.image)
