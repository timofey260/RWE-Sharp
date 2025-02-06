from RWESharp.Renderable import Renderable
from RWESharp.Utils import closest_line
from PySide6.QtWidgets import QGraphicsRectItem, QGraphicsSceneMouseEvent
from PySide6.QtGui import QPen, QBrush, QColor, QGuiApplication
from PySide6.QtCore import Qt, Signal, QPointF, QObject


class HandleItem(QGraphicsRectItem, QObject):
    posChanged = Signal(QPointF)
    mouseReleased = Signal(QPointF)
    mousePressed = Signal(QPointF)

    def __init__(self, handle):
        QGraphicsRectItem.__init__(self, -5, -5, 10, 10)
        QObject.__init__(self)
        self.handle = handle
        self.setPen(QPen(QColor(0, 0, 0), 2))
        self.setBrush(QBrush(QColor(255, 255, 255)))
        self.setAcceptTouchEvents(True)
        self.setAcceptHoverEvents(True)
        self.setAcceptedMouseButtons(Qt.MouseButton.LeftButton)
        self.reserved_pos = QPointF()

    def mouseMoveEvent(self, event):
        #super().mouseMoveEvent(event)
        p = event.pos() * (1 / self.handle.zoom)
        sh = QGuiApplication.keyboardModifiers() & Qt.KeyboardModifier.ShiftModifier
        if sh:
            p = closest_line(self.handle.offset + p, self.reserved_pos).p2()
            self.handle.setPos(p)
            self.posChanged.emit(self.handle.offset)
            return
        self.handle.setPos(self.handle.offset + p)
        self.posChanged.emit(self.handle.offset)

    def mousePressEvent(self, event):
        event.accept()
        self.reserved_pos = self.handle.offset
        self.mousePressed.emit(self.handle.offset)

    def mouseReleaseEvent(self, event):
        self.mouseReleased.emit(self.handle.offset)


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

    def zoom_event(self):
        self.handle.setPos(self.actual_offset)
        self.handle.setScale(self.scale)

    def move_event(self):
        super().move_event()
        self.handle.setPos(self.actual_offset)

    def setPos(self, pos):
        super().setPos(pos)
        if self.handle is not None:
            self.handle.setPos(self.actual_offset)

    @property
    def posChanged(self) -> Signal:
        return self.handle.posChanged

    @property
    def mousePressed(self) -> Signal:
        return self.handle.mousePressed

    @property
    def mouseReleased(self) -> Signal:
        return self.handle.mouseReleased
