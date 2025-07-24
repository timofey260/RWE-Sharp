from core.Renderable.Renderable import Renderable
from PySide6.QtCore import Qt, QPointF
from PySide6.QtWidgets import QGraphicsPolygonItem
from PySide6.QtGui import QColor, QPen, QBrush, QPolygonF
from widgets import Viewport


class RenderPoly(Renderable):
    def __init__(self, module, depth, poly: QPolygonF, pen=QPen(Qt.GlobalColor.red), brush=QBrush(Qt.GlobalColor.transparent), add_renderable: bool = True):
        super().__init__(module, depth, False)
        self.poly = poly
        self.drawpoly = QGraphicsPolygonItem(self.poly)
        self.pen = QPen(pen)
        self.brush = QBrush(brush)
        self.drawpoly.setZValue(self.depth)
        self.drawpoly.setPen(self.pen)
        self.drawpoly.setBrush(self.brush)
        if add_renderable:
            self.module.add_renderable(self)

    def init_graphics(self, viewport):
        super().init_graphics(viewport)
        viewport.workscene.addItem(self.drawpoly)
        self.setPoly(self.poly)

    def remove_graphics(self, viewport):
        super().remove_graphics(viewport)
        viewport.workscene.removeItem(self.drawpoly)

    def move_event(self):
        super().move_event()
        self.drawpoly.setPos(self.actual_offset)

    def zoom_event(self):
        self.drawpoly.setScale(self.zoom * self.scale)

    def setPoly(self, poly: QPolygonF):
        self.poly = poly
        self.drawpoly.setPolygon(poly)

    def setPos(self, pos: QPointF):
        super().setPos(pos)
        self.drawpoly.setPos(self.actual_offset)

    def setOpacity(self, opacity):
        super().setOpacity(opacity)
        self.drawpoly.setOpacity(self.opacity)
