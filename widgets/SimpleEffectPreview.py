from PySide6.QtCore import QPointF, QPoint
from PySide6.QtGui import QPixmap
from widgets.SimpleViewport import SimpleViewport


class SimpleEffectPreview(SimpleViewport):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.effect = None
        self.image = self.workscene.addPixmap(QPixmap(1, 1))

    def load_effect(self, effect):
        self.effect = effect
        self.redraw()

    def redraw(self):
        self.image.setPixmap(self.effect.preview)

    def set_pos(self, pos: QPointF | QPoint):
        super().set_pos(pos)
        self.image.setPos(self.topleft.pos())

    def wheelEvent(self, event):
        super().wheelEvent(event)
        self.image.setScale(self.zoom)
