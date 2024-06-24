from PySide6.QtCore import QPoint
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsPixmapItem


class TilePreview(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.workscene = QGraphicsScene(0, 0, 0, 0)
        self.setScene(self.workscene)
        self.tileimage = self.workscene.addPixmap(QPixmap())
        self.lastpos = QPoint()
        self.manager = None
        self.setMouseTracking(True)

    def add_manager(self, manager):
        self.manager = manager

    def mouseMoveEvent(self, event):
        offset = event.pos() - self.lastpos
        if event.buttons() & self.manager.basemod.bmconfig.movement_button.value:
            self.tileimage.setPos(self.tileimage.pos() + offset)
        self.lastpos = event.pos()
