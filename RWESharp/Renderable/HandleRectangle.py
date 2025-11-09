from RWESharp.Renderable.Renderable import Renderable
from PySide6.QtWidgets import QGraphicsRectItem
from PySide6.QtCore import Qt, QPointF, QRectF, Signal, QObject, QRect, QPoint
from PySide6.QtGui import QColor, QPen
from RWESharp.info import CELLSIZE

class Rectangle(QGraphicsRectItem, QObject):
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
        self.enabled = True
        self.lastpos = QPointF()

    def mousePressEvent(self, event):
        insiderect = self.rect().adjusted(40, 40, -40, -40)
        outsiderect = self.rect()
        if insiderect.contains(event.pos()) or not self.enabled:
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

class NormalRectangle(Rectangle):
    rectChanged = Signal(QRectF)

    def mouseReleaseEvent(self, event, /):
        super().mouseReleaseEvent(event)
        self.rectChanged.emit(self.rect().adjusted(20, 20, -20, -20))

class GridRectangle(Rectangle):
    rectChanged = Signal(QRect)

    def mouseReleaseEvent(self, event, /):
        super().mouseReleaseEvent(event)
        newrect = self.getrect
        self.setRect(QRectF(newrect.x() * CELLSIZE, newrect.y() * CELLSIZE, newrect.width() * CELLSIZE,
                            newrect.height() * CELLSIZE).adjusted(-20, -20, 20, 20))
        self.rectChanged.emit(newrect)

    @property
    def getrect(self) -> QRect:
        fixedrect = self.rect().toRect().adjusted(20, 20, -20, -20)
        newrect = QRect(QPoint(fixedrect.left() // CELLSIZE, fixedrect.top() // CELLSIZE),
                        QPoint(fixedrect.right() // CELLSIZE, fixedrect.bottom() // CELLSIZE))
        return newrect

class HandleRectangle(Renderable):
    def __init__(self, module, rect: QRectF, add_renderable: bool = True):
        super().__init__(module, -100, False)
        self.rect = rect
        self.recth = NormalRectangle()
        self.recth.setRect(self.rect.adjusted(-20, -20, 20, 20))
        self.visrect = QGraphicsRectItem(self.rect)
        self.visrect.setPen(QColor(Qt.GlobalColor.blue))
        self.recth.rectMoved.connect(self.rect_moved)

        if add_renderable:
            self.module.add_renderable(self)

    def rect_moved(self):
        self.rect = self.recth.rect().adjusted(20, 20, -20, -20)
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

    def setRect(self, rect: QRectF):
        self.rect = rect
        self.recth.setRect(rect.adjusted(-20, -20, 20, 20))
        self.visrect.setRect(rect)

class GridHandleRectangle(Renderable):
    def __init__(self, module, rect: QRect, add_renderable: bool = True):
        super().__init__(module, -100, False)
        self.rect = rect
        self.recth = GridRectangle()
        rectupped = QRectF(rect.x() * CELLSIZE, rect.y() * CELLSIZE, rect.width() * CELLSIZE, rect.height() * CELLSIZE)
        self.recth.setRect(rectupped.adjusted(-20, -20, 20, 20))
        self.visrect = QGraphicsRectItem(rectupped)
        self.visrect.setPen(QColor(Qt.GlobalColor.blue))
        self.recth.rectMoved.connect(self.rect_moved)

        if add_renderable:
            self.module.add_renderable(self)

    def rect_moved(self):
        self.rect = self.getrect
        self.visrect.setRect(QRect(self.rect.x() * CELLSIZE, self.rect.y() * CELLSIZE, self.rect.width() * CELLSIZE, self.rect.height() * CELLSIZE))

    @property
    def getrect(self):
        fixedrect = self.recth.rect().toRect().adjusted(20, 20, -20, -20)
        return QRect(QPoint(fixedrect.left() // CELLSIZE, fixedrect.top() // CELLSIZE), QPoint(fixedrect.right() // CELLSIZE, fixedrect.bottom() // CELLSIZE))

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

    def setRect(self, rect: QRect):
        self.rect = rect
        newrect = QRectF(rect.x() * CELLSIZE, rect.y() * CELLSIZE, rect.width() * CELLSIZE, rect.height() * CELLSIZE)
        self.recth.setRect(newrect.adjusted(-20, -20, 20, 20))
        self.visrect.setRect(newrect)