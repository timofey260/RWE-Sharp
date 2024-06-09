from PySide6.QtGui import QColor, QBrush
from PySide6.QtCore import Qt, QPoint, QRect, Slot, QPointF
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QApplication, QGraphicsRectItem, QGraphicsEllipseItem
from core.info import CELLSIZE
from core.configTypes.QtTypes import ColorConfigurable, QtEnumConfigurable, KeyConfigurable


class ViewPort(QGraphicsView):
    '''
    Viewport for visualizing level and editors

    :param parent: widget parent
    '''
    def __init__(self, parent):
        super().__init__(parent)
        self.manager = None
        self.workscene: QGraphicsScene = QGraphicsScene(self)
        self.setScene(self.workscene)
        self.zoom = 1
        self.rect: QGraphicsRectItem = self.workscene.addRect(QRect(0, 0, 1, 1))
        self.origin = self.workscene.addEllipse(0, 0, 1, 1, QColor(0, 0, 0, 0))
        self.managedfields: list[QGraphicsPixmapItem] = []
        self.verticalScrollBar().sliderReleased.connect(self.redraw)
        self.horizontalScrollBar().sliderReleased.connect(self.redraw)
        self._lmb = False
        self._rmb = False
        self._mmb = False
        self.mpos = QPoint()
        self.backgroundcolor = ColorConfigurable(None, "bgcolor", QColor(150, 150, 150), "color of the background")

    @Slot()
    def redraw(self):
        self.repaint()

    def add_texture(self, pixmap) -> QGraphicsPixmapItem:
        newpixmap = self.workscene.addPixmap(pixmap)
        self.managedfields.append(newpixmap)
        return newpixmap

    def add_managed_fields(self, manager):
        self.manager = manager
        self.backgroundcolor.link_mod(manager.basemod)
        self.rect.setBrush(self.backgroundcolor.value)
        if len(self.managedfields) > 0:
            self.rect.setRect(self.managedfields[0].sceneBoundingRect())
        # self.setBackgroundBrush(QBrush(QColor(30, 30, 30), Qt.BrushStyle.SolidPattern))

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        if event.buttons() & self.manager.basemod.main_button.value:
            self._lmb = True
        if event.buttons() & self.manager.basemod.sec_button.value:
            self._rmb = True
        if event.buttons() & self.manager.basemod.movement_button.value:
            self._mmb = True
        self.manager.editor.mouse_press_event(event)

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        if event.button() & self.manager.basemod.main_button.value:
            self._lmb = False
        if event.button() & self.manager.basemod.sec_button.value:
            self._rmb = False
        if event.button() & self.manager.basemod.movement_button.value:
            self._mmb = False
        self.manager.editor.mouse_release_event(event)

    @property
    def mouse_left(self) -> bool:
        return self._lmb

    @property
    def mouse_right(self) -> bool:
        return self._rmb

    @property
    def mouse_middle(self):
        return self._mmb

    def wheelEvent(self, event):
        mods = QApplication.keyboardModifiers()
        #print(self.map.scale() + (event.angleDelta().y() / 80))
        if mods == mods.ShiftModifier:
            event.setModifiers(Qt.KeyboardModifier.NoModifier)
            self.verticalScrollBar().wheelEvent(event)
            return
        elif mods == mods.ControlModifier:
            event.setModifiers(Qt.KeyboardModifier.NoModifier)
            self.horizontalScrollBar().wheelEvent(event)
            return
        pointbefore = self.viewport_to_editor_float(self.mpos.toPointF())
        self.zoom = max(0.1, self.zoom + (event.angleDelta().y() * (-1 if event.inverted() else 1) / 800))
        offset = (self.viewport_to_editor_float(self.mpos.toPointF()) - pointbefore) * CELLSIZE * self.zoom
        for i in self.managedfields:
            i.setScale(self.zoom)
            i.setX(i.x() + offset.x())
            i.setY(i.y() + offset.y())
        self.rect.setRect(self.managedfields[0].sceneBoundingRect())
        self.manager.editor.mouse_wheel_event(event)
        self.manager.editor.mouse_move_event(event)
        #self.verticalScrollBar().size
        #self.horizontalScrollBar().adjustSize()

    def mouseMoveEvent(self, event):
        offset = event.pos() - self.mpos
        if self.mouse_middle:
            # self.origin.setX(self.origin.x() + offset.x())
            # self.origin.setY(self.origin.y() + offset.y())
            for i in self.managedfields:
                i.setX(i.x() + offset.x())
                i.setY(i.y() + offset.y())
            self.rect.setRect(self.managedfields[0].sceneBoundingRect())
        self.mpos = event.pos()
        self.manager.editor.mouse_move_event(event)

    def viewport_to_editor(self, point: QPoint) -> QPoint:
        npoint = point + QPoint(self.horizontalScrollBar().value(), self.verticalScrollBar().value()) - self.managedfields[0].pos().toPoint()
        npoint.setX(npoint.x() / (CELLSIZE * self.zoom))
        npoint.setY(npoint.y() / (CELLSIZE * self.zoom))
        return npoint

    def viewport_to_editor_float(self, point: QPointF) -> QPointF:
        npoint = point + QPointF(self.horizontalScrollBar().value(), self.verticalScrollBar().value()) - self.managedfields[0].pos()
        npoint.setX(npoint.x() / (CELLSIZE * self.zoom))
        npoint.setY(npoint.y() / (CELLSIZE * self.zoom))
        return npoint

    def editor_to_viewport(self, point: QPoint) -> QPoint:
        return (point * CELLSIZE * self.zoom) + self.managedfields[0].pos().toPoint()

    def editor_to_viewport_float(self, point: QPointF) -> QPointF:
        return (point * CELLSIZE * self.zoom) + self.managedfields[0].pos()

