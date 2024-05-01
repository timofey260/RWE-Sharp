from PySide6.QtGui import QColor, QBrush
from PySide6.QtCore import Qt, QPoint, QRect
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QApplication, QGraphicsRectItem


class ViewPort(QGraphicsView):
    '''
    Viewport for visualizing level and editors

    :param parent: widget parent
    '''
    def __init__(self, parent):
        super().__init__(parent)
        self.manager = None
        self.workscene = QGraphicsScene(self)
        self.setScene(self.workscene)
        self.zoom = 1
        self.rect: QGraphicsRectItem = self.workscene.addRect(QRect(0, 0, 1, 1), brush=QBrush(QColor(150, 150, 150), Qt.BrushStyle.SolidPattern))
        self.managedfields: list[QGraphicsPixmapItem] = []

    def add_managed_fields(self, manager):
        self.manager = manager
        for i, v in enumerate(self.manager.rendertextures):
            self.managedfields.append(self.workscene.addPixmap(v.image))
            #self.managedfields[i].setPos(QPoint(200, 200))
        self.rect.setRect(self.managedfields[0].sceneBoundingRect())
        self.managedfields[0].setOpacity(.3)
        self.managedfields[1].setOpacity(.5)
        self.managedfields[2].setOpacity(1)
        # self.setBackgroundBrush(QBrush(QColor(30, 30, 30), Qt.BrushStyle.SolidPattern))

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.manager.window.editor.mouse_click_event(event)

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
        # self.horizontalScrollBar().
        # self.scroll(-20, 20)
        self.zoom = max(0.1, self.zoom + (event.angleDelta().y() / 800))
        for i in self.managedfields:
            i.setScale(self.zoom)
        self.rect.setRect(self.managedfields[0].sceneBoundingRect())
        #self.verticalScrollBar().size
        #self.horizontalScrollBar().adjustSize()

    def mouseMoveEvent(self, event):
        self.manager.window.editor.mouse_move_event(event)

    def fullrender(self):
        pass
