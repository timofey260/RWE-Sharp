from core.Renderable.Renderable import Renderable
from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap, QColor, QPainter
from PySide6.QtWidgets import QGraphicsPixmapItem


class RenderImage(Renderable):
    def __init__(self, mod, depth, imagesize: QSize):
        super().__init__(mod, depth)
        self.image = QPixmap(imagesize)
        self.image.fill(QColor(0, 0, 0, 0))
        self.painter = QPainter(self.image)
        self.renderedtexture: QGraphicsPixmapItem | None = None

    def redraw(self) -> None:
        """
        Redraws pixmap on screen
        :return: None
        """
        if self.renderedtexture is not None:
            self.renderedtexture.setPixmap(self.image)

    def draw_layer(self) -> None:
        """
        called when layer should be drawn on screen
        called on booting of rwe#
        :return: None
        """

    def init_graphics(self, viewport):
        self.renderedtexture = viewport.workscene.addPixmap(self.image)
        self.renderedtexture.setZValue(self.depth)
        self.draw_layer()

    def remove_graphics(self):
        self.renderedtexture.removeFromIndex()

    def move_event(self, pos):
        self.renderedtexture.setPos(pos)

    def zoom_event(self, zoom):
        self.renderedtexture.setScale(zoom)
    