from PySide6.QtGui import QColor, QBrush
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QApplication

class ViewPort(QGraphicsView):
    def __init__(self, parent):
        super().__init__(parent)
        self.manager = None
        self.workscene = QGraphicsScene(self)
        self.setScene(self.workscene)
        self.zoom = 1
        self.managedfields: list[QGraphicsPixmapItem] = []

    def add_managed_fields(self):
        for i in self.manager.rendertextures:
            self.managedfields.append(self.workscene.addPixmap(i.image))
        self.managedfields[0].setOpacity(.1)
        self.managedfields[1].setOpacity(.3)
        self.managedfields[2].setOpacity(1)
        self.setBackgroundBrush(QBrush(QColor(150, 150, 150, 255), Qt.BrushStyle.SolidPattern))

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        print("thing")

    def dragMoveEvent(self, event):
        print("event")

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
        self.zoom = max(0.1, self.zoom + (event.angleDelta().y() / 800))
        for i in self.managedfields:
            i.setScale(self.zoom)
        #self.verticalScrollBar().size
        #self.horizontalScrollBar().adjustSize()

    def fullrender(self):
        pass
