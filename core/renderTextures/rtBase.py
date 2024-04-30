from PySide6.QtGui import QPixmap, QColor, QPainter
from PySide6.QtCore import QSize


class RenderTexture:
    def __init__(self, manager):
        self.manager = manager
        self.image = QPixmap(manager.level_width * 20, manager.level_height * 20)
        self.image.fill(QColor(0, 0, 0, 0))
        self.painter = QPainter(self.image)