from RWESharp.Renderable.Renderable import Renderable
from PySide6.QtCore import QRectF, Qt, QPointF, QRect
from PySide6.QtWidgets import QGraphicsRectItem
from PySide6.QtGui import QColor, QPen, QBrush
from widgets import Viewport


class RenderRect(Renderable):
    def __init__(self, module, depth, rect: QRectF | QRect, pen=QPen(Qt.GlobalColor.red), brush=QBrush(Qt.GlobalColor.transparent), add_renderable: bool = True):
        super().__init__(module, depth, False)
        self.rect = QRectF()
        self.drawrect = QGraphicsRectItem(self.rect)
        self.setRect(rect)
        self.pen = QPen(pen)
        self.brush = QBrush(brush)
        self.drawrect.setPen(self.pen)
        self.drawrect.setBrush(self.brush)
        self.drawrect.setZValue(self.depth)
        if add_renderable:
            self.module.add_renderable(self)

    def init_graphics(self, viewport):
        super().init_graphics(viewport)
        viewport.workscene.addItem(self.drawrect)
        self.setRect(self.rect)

    def remove_graphics(self, viewport):
        super().remove_graphics(viewport)
        viewport.workscene.removeItem(self.drawrect)
        # self.drawrect.removeFromIndex()

    def move_event(self):
        super().move_event()
        self.drawrect.setPos(self.actual_offset)

    def zoom_event(self):
        self.drawrect.setScale(self.zoom * self.scale)

    def setRect(self, rect: QRect | QRectF):
        if isinstance(self.rect, QRect):
            self.rect = rect.toRectF()
        else:
            self.rect = rect
        self.drawrect.setRect(rect)

    def setPos(self, pos: QPointF):
        super().setPos(pos)
        self.drawrect.setPos(self.actual_offset)

    def setOpacity(self, opacity):
        super().setOpacity(opacity)
        self.drawrect.setOpacity(self.opacity)
