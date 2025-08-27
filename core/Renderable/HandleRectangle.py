from core.Renderable.Renderable import Renderable
from PySide6.QtWidgets import QGraphicsRectItem
from PySide6.QtCore import Qt, QPointF, QRectF, Signal, QObject
from PySide6.QtGui import QColor, QPen
from core.info import CELLSIZE

class Rectangle(QGraphicsRectItem, QObject):
    rectChanged = Signal(QRectF)
    rectMoved = Signal(QRectF)

    def __init__(self):
        QGraphicsRectItem.__init__(self)
        QObject.__init__(self)
        self.setAcceptTouchEvents(True)
        # self.setAcceptHoverEvents(True)
        self.setAcceptedMouseButtons(Qt.MouseButton.LeftButton)
        self.setRect(0, 0, 300, 300)
        self.setPos(0, 0)
        self.setScale(.5)
        self.setPen(QPen(Qt.PenStyle.NoPen))
        self.moveborder = [False] * 4
        self.lastpos = QPointF()

    def mousePressEvent(self, event):
        insiderect = self.rect().adjusted(40, 40, -40, -40)
        outsiderect = self.rect()
        if insiderect.contains(event.pos()):
            event.ignore()
            return
        event.accept()
        self.lastpos = event.pos()
        leftrect = QRectF(outsiderect.topLeft(), QPointF(insiderect.left(), outsiderect.bottom()))
        toprect = QRectF(outsiderect.topLeft(), QPointF(outsiderect.right(), insiderect.top()))
        rightrect = QRectF(QPointF(insiderect.right(), outsiderect.top()), outsiderect.bottomRight())
        bottomrect = QRectF(QPointF(outsiderect.left(), insiderect.bottom()), outsiderect.bottomRight())
        self.moveborder = [leftrect.contains(event.pos()), toprect.contains(event.pos()), rightrect.contains(event.pos()), bottomrect.contains(event.pos())]
        if self.moveborder[0] and self.moveborder[1]:  # highly very unoptimal but it just works
            self.moveborder[2] = False
            self.moveborder[3] = False
        elif self.moveborder[2] and self.moveborder[3]:
            self.moveborder[0] = False
            self.moveborder[1] = False
        elif self.moveborder[1] and self.moveborder[2]:
            self.moveborder[3] = False
            self.moveborder[0] = False
        elif self.moveborder[3] and self.moveborder[0]:
            self.moveborder[1] = False
            self.moveborder[2] = False

        if (self.moveborder[0] and self.moveborder[1]) or (self.moveborder[2] and self.moveborder[3]):
            self.setCursor(Qt.CursorShape.SizeFDiagCursor)
        elif (self.moveborder[1] and self.moveborder[2]) or (self.moveborder[3] and self.moveborder[0]):
            self.setCursor(Qt.CursorShape.SizeBDiagCursor)
        elif self.moveborder[0] or self.moveborder[2]:
            self.setCursor(Qt.CursorShape.SizeHorCursor)
        elif self.moveborder[1] or self.moveborder[3]:
            self.setCursor(Qt.CursorShape.SizeVerCursor)

    def mouseReleaseEvent(self, event, /):
        event.accept()
        self.unsetCursor()
        self.moveborder = [False] * 4
        self.rectChanged.emit(self.rect())

    def mouseMoveEvent(self, event, /):
        move = event.pos() - self.lastpos
        newrect = self.rect().adjusted(move.x() if self.moveborder[0] else 0,
                                       move.y() if self.moveborder[1] else 0,
                                       move.x() if self.moveborder[2] else 0,
                                       move.y() if self.moveborder[3] else 0)
        newrect.setWidth(max(newrect.width(), CELLSIZE * 4))
        newrect.setHeight(max(newrect.height(), CELLSIZE * 4))

        self.rectMoved.emit(newrect)
        self.setRect(newrect)
        self.lastpos = event.pos()

class HandleRectangle(Renderable):
    def __init__(self, module, rect: QRectF, add_renderable: bool = True):
        super().__init__(module, -100, False)
        self.rect = rect
        self.recth = Rectangle()
        self.recth.setRect(self.rect.adjusted(-20, -20, 20, 20))
        self.visrect = QGraphicsRectItem(self.rect)
        self.visrect.setPen(QColor(Qt.GlobalColor.blue))
        self.recth.rectMoved.connect(self.rect_moved)

        if add_renderable:
            self.module.add_renderable(self)

    def rect_moved(self):
        self.visrect.setRect(self.recth.rect().adjusted(20, 20, -20, -20))

    def init_graphics(self, viewport):
        super().init_graphics(viewport)
        viewport.workscene.addItem(self.recth)
        viewport.workscene.addItem(self.visrect)

    def remove_graphics(self, viewport):
        super().remove_graphics(viewport)
        viewport.workscene.removeItem(self.recth)
        viewport.workscene.removeItem(self.visrect)

    def zoom_event(self):
        super().zoom_event()
        self.recth.setScale(self.zoom)
        self.visrect.setScale(self.zoom)

    def move_event(self):
        super().move_event()
        self.recth.setPos(self.actual_offset)
        self.visrect.setPos(self.actual_offset)