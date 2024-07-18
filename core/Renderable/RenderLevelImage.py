from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap, QPainter, QImage
from core.Renderable.RenderImage import RenderImage
from core.info import CELLSIZE


class RenderLevelImage(RenderImage):
    def __init__(self, mod, depth):
        super().__init__(mod, depth, QSize(mod.manager.level_width * CELLSIZE, mod.manager.level_height * CELLSIZE))

    def level_resized(self):
        # self.image = QPixmap(QSize(self.mod.manager.level_width * CELLSIZE, self.mod.manager.level_height * CELLSIZE))
        # self.painter = None
        # self.painter = QPainter(self.image)
        # self.painter.begin(self.image)
        self.renderedtexture.setPixmap(self.image)
        self.redraw()
