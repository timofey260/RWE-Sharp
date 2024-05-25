from PySide6.QtGui import QPixmap, QColor, QPainter
from PySide6.QtWidgets import QGraphicsPixmapItem


class RenderTexture:
    def __init__(self, module):
        self.module = module
        self.manager = module.manager
        self.image = QPixmap(self.manager.level_width * 20, self.manager.level_height * 20)
        self.image.fill(QColor(0, 0, 0, 0))
        self.painter = QPainter(self.image)
        self.renderedtexture: QGraphicsPixmapItem | None = None

    def redraw(self) -> None:
        """
        Redraws pixmap on screen
        :return: None
        """
        if self.renderedtexture is not None:
            self.renderedtexture.setPixmap(self.image)

    def draw_layer(self) -> None:
        """
        called when layer should be drawn on screen
        called on booting of rwe#
        :return: None
        """

    def field_init(self) -> None:
        """
        called when layer has been added on screen
        :return: None
        """
