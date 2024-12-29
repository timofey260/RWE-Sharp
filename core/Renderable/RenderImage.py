from core.info import CELLSIZE
from core.Renderable.Renderable import Renderable
from PySide6.QtCore import QSize, QPointF
from PySide6.QtGui import QPixmap, QColor, QPainter
from PySide6.QtWidgets import QGraphicsPixmapItem


class RenderImage(Renderable):
    def __init__(self, module, depth, imagesize: QSize):
        super().__init__(module, depth)
        self.image = QPixmap(imagesize)
        self.image.fill(QColor(0, 0, 0, 0))
        self.painter = QPainter(self.image)
        self.renderedtexture = QGraphicsPixmapItem(self.image)
        self.renderedtexture.setZValue(self.depth)

    def redraw(self) -> None:
        """
        Redraws pixmap on screen
        :return: None
        """
        self.renderedtexture.setPixmap(self.image)

    def draw_layer(self) -> None:
        """
        called when layer should be drawn on screen
        called on booting of rwe#
        :return: None
        """

    def init_graphics(self, viewport):
        super().init_graphics(viewport)
        viewport.workscene.addItem(self.renderedtexture)
        self.draw_layer()

    def remove_graphics(self, viewport):
        super().remove_graphics(viewport)
        viewport.workscene.removeItem(self.renderedtexture)

    def move_event(self, pos):
        super().move_event(pos)
        self.renderedtexture.setPos(self.actual_offset)

    def zoom_event(self, zoom):
        self.renderedtexture.setScale(zoom * self.scale)

    def setPos(self, pos: QPointF):
        super().setPos(pos)
        self.renderedtexture.setPos(self.actual_offset)
