from PySide6.QtGui import QColor, QBrush
from PySide6.QtCore import Qt, QPoint, QRect, Slot
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QApplication, QGraphicsRectItem


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
        self.rect: QGraphicsRectItem = self.workscene.addRect(QRect(0, 0, 1, 1), brush=QBrush(QColor(150, 150, 150), Qt.BrushStyle.SolidPattern))
        self.managedfields: list[QGraphicsPixmapItem] = []
        self.verticalScrollBar().sliderReleased.connect(self.redraw)
        self.horizontalScrollBar().sliderReleased.connect(self.redraw)
        self._lmb = False
        self._rmb = False

    @Slot()
    def redraw(self):
        self.repaint()

    def add_texture(self, pixmap) -> QGraphicsPixmapItem:
        newpixmap = self.workscene.addPixmap(pixmap)
        self.managedfields.append(newpixmap)
        return newpixmap

    def add_managed_fields(self, manager):
        self.manager = manager
        if len(self.managedfields) > 0:
            self.rect.setRect(self.managedfields[0].sceneBoundingRect())
        # self.setBackgroundBrush(QBrush(QColor(30, 30, 30), Qt.BrushStyle.SolidPattern))

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        if event.buttons() & Qt.MouseButton.LeftButton:
            self._lmb = True
        if event.buttons() & Qt.MouseButton.RightButton:
            self._rmb = True
        self.manager.editor.mouse_press_event(event)

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        if event.button() & Qt.MouseButton.LeftButton:
            self._lmb = False
        if event.button() & Qt.MouseButton.RightButton:
            self._rmb = False
        self.manager.editor.mouse_release_event(event)

    @property
    def mouse_left(self) -> bool:
        return self._lmb

    @property
    def mouse_right(self) -> bool:
        return self._rmb

    def wheelEvent(self, event):
        mods = QApplication.keyboardModifiers()
        #print(self.map.scale() + (event.angleDelta().y() / 80))
        self.manager.editor.mouse_wheel_event(event)
        if mods == mods.ShiftModifier:
            event.setModifiers(Qt.KeyboardModifier.NoModifier)
            self.verticalScrollBar().wheelEvent(event)
            return
        elif mods == mods.ControlModifier:
            event.setModifiers(Qt.KeyboardModifier.NoModifier)
            self.horizontalScrollBar().wheelEvent(event)
            return
        # self.horizontalScrollBar().
        # self.scroll(-20, 20)
        self.zoom = max(0.1, self.zoom + (event.angleDelta().y() / 800))
        for i in self.managedfields:
            i.setScale(self.zoom)
        self.rect.setRect(self.managedfields[0].sceneBoundingRect())
        #self.verticalScrollBar().size
        #self.horizontalScrollBar().adjustSize()

    def mouseMoveEvent(self, event):
        self.manager.editor.mouse_move_event(event)

    def fullrender(self):
        pass
