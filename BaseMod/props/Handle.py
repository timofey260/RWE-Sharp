from RWESharp.Renderable import Renderable

from PySide6.QtWidgets import QGraphicsRectItem, QGraphicsSceneMouseEvent
from PySide6.QtGui import QPen, QBrush, QColor
from PySide6.QtCore import Qt


class HandleItem(QGraphicsRectItem):
    def __init__(self, handle):
        super().__init__(-5, -5, 10, 10)
        self.handle = handle
        self.setPen(QPen(QColor(0, 0, 0), 2))
        self.setBrush(QBrush(QColor(255, 255, 255)))
        self.setAcceptTouchEvents(True)
        self.setAcceptHoverEvents(True)
        self.setAcceptedMouseButtons(Qt.MouseButton.LeftButton)

    def mouseMoveEvent(self, event):
        #super().mouseMoveEvent(event)
        self.handle.setPos(self.handle.offset + (event.pos() - event.lastPos()) * (1 / self.handle.zoom))

    def mousePressEvent(self, event):
        event.accept()
        print(self.scene().mouseGrabberItem())
        #super().mousePressEvent(event)
        print("mpress")

    def mouseReleaseEvent(self, event):
        #super().mouseReleaseEvent(event)
        print("mrel")


class Handle(Renderable):
    def __init__(self, mod):
        super().__init__(mod, -100)
        self.handle: QGraphicsRectItem | None = None

    def init_graphics(self):
        self.handle = HandleItem(self)
        self.viewport.workscene.addItem(self.handle)
        self.handle.setZValue(self.depth)
        self.handle.setPos(self.actual_offset)

    def remove_graphics(self):
        self.handle.removeFromIndex()
        self.handle = None

    def zoom_event(self, zoom):
        self.handle.setPos(self.actual_offset)

    def move_event(self, pos):
        super().move_event(pos)
        self.handle.setPos(self.actual_offset)

    def setPos(self, pos):
        super().setPos(pos)
        if self.handle is not None:
            self.handle.setPos(self.actual_offset)
