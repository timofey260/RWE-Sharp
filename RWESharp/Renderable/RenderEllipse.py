from RWESharp.Renderable.Renderable import Renderable
from PySide6.QtCore import QRect, Qt, QPointF, QRectF
from PySide6.QtWidgets import QGraphicsEllipseItem
from PySide6.QtGui import QColor, QPen, QBrush
from widgets import Viewport


class RenderEllipse(Renderable):
    def __init__(self, module, depth: int, rect: QRectF, pen=QPen(Qt.GlobalColor.red), brush=QBrush(Qt.GlobalColor.transparent), add_renderable: bool = True):
        super().__init__(module, depth, False)
        self.rect = QRectF()
        self.drawellipse = QGraphicsEllipseItem(self.rect)
        self.setRect(rect)
        self.pen = QPen(pen)
        self.brush = QBrush(brush)
        self.drawellipse.setZValue(self.depth)
        self.drawellipse.setPen(self.pen)
        self.drawellipse.setBrush(self.brush)
        if add_renderable:
            module.add_renderable(self)

    def init_graphics(self, viewport):
        super().init_graphics(viewport)
        viewport.workscene.addItem(self.drawellipse)
        self.setRect(self.rect)

    def remove_graphics(self, viewport):
        super().remove_graphics(viewport)
        viewport.workscene.removeItem(self.drawellipse)

    def move_event(self):
        super().move_event()
        self.drawellipse.setPos(self.actual_offset)

    def zoom_event(self):
        self.drawellipse.setScale(self.zoom * self.scale)

    def setRect(self, rect: QRect | QRectF):
        if isinstance(self.rect, QRect):
            self.rect = rect.toRectF()
        else:
            self.rect = rect
        self.drawellipse.setRect(rect)

    def setOpacity(self, opacity):
        super().setOpacity(opacity)
        self.drawellipse.setOpacity(self.opacity)

    def setPos(self, pos: QPointF):
        super().setPos(pos)
        self.drawellipse.setPos(self.actual_offset)
