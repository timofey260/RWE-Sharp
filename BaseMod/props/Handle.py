from RWESharp.Renderable import Renderable

from PySide6.QtWidgets import QGraphicsRectItem, QGraphicsSceneMouseEvent
from PySide6.QtGui import QPen, QBrush, QColor
from PySide6.QtCore import Qt, Signal, QPointF, QObject


class HandleItem(QGraphicsRectItem, QObject):
    posChanged = Signal(QPointF)

    def __init__(self, handle):
        QGraphicsRectItem.__init__(self, -5, -5, 10, 10)
        QObject.__init__(self)
        self.handle = handle
        self.setPen(QPen(QColor(0, 0, 0), 2))
        self.setBrush(QBrush(QColor(255, 255, 255)))
        self.setAcceptTouchEvents(True)
        self.setAcceptHoverEvents(True)
        self.setAcceptedMouseButtons(Qt.MouseButton.LeftButton)

    def mouseMoveEvent(self, event):
        #super().mouseMoveEvent(event)
        self.handle.setPos(self.handle.offset + (event.pos() - event.lastPos()) * (1 / self.handle.zoom))
        self.posChanged.emit(self.handle.offset)

    def mousePressEvent(self, event):
        event.accept()
        print(self.scene().mouseGrabberItem())

    def mouseReleaseEvent(self, event):
        print()


class Handle(Renderable):
    def __init__(self, module):
        super().__init__(module, -100)
        self.handle = HandleItem(self)
        self.handle.setZValue(self.depth)
        self.handle.setPos(self.offset)

    def init_graphics(self, viewport):
        super().init_graphics(viewport)
        self.viewport.workscene.addItem(self.handle)

    def remove_graphics(self, viewport):
        super().remove_graphics(viewport)
        viewport.workscene.removeItem(self.handle)

    def zoom_event(self, zoom):
        self.handle.setPos(self.actual_offset)

    def move_event(self, pos):
        super().move_event(pos)
        self.handle.setPos(self.actual_offset)

    def setPos(self, pos):
        super().setPos(pos)
        if self.handle is not None:
            self.handle.setPos(self.actual_offset)

    @property
    def posChanged(self):
        return self.handle.posChanged
