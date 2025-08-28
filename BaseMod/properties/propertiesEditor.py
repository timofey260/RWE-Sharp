from RWESharp.Modify import Editor
from RWESharp.Renderable import Handle, RenderRect, GridHandleRectangle, HandleRectangle
from RWESharp.Core import CELLSIZE
from PySide6.QtCore import QPoint, QRect, QRectF

class PropertiesEditor(Editor):
    def __init__(self, mod):
        super().__init__(mod)
        self.rect = RenderRect(self, 0, QRect())
        self.borderrect = RenderRect(self, 0, QRect())
        self.handlerect = GridHandleRectangle(self, QRect(0, 0, 5, 5))
        self.handlerect.recth.rectChanged.connect(lambda x: print(x))
        self.borderhandlerect = GridHandleRectangle(self, QRect(0, 0, 40, 40))
        self.borderhandlerect.recth.rectChanged.connect(lambda x: print(x))

    def init_scene_items(self, viewport):
        super().init_scene_items(viewport)
        self.reposition()

    def reposition(self):
        width = self.level.level_width * CELLSIZE
        height = self.level.level_height * CELLSIZE
        self.rect.setRect(QRect(0, 0, width, height))

        et = self.level.extra_tiles
        tilerect = QRect(et[0], et[1], self.level.level_width - et[2] - et[0], self.level.level_height - et[3] - et[1])
        borderrect = QRect(tilerect.x() * CELLSIZE, tilerect.y() * CELLSIZE, tilerect.width() * CELLSIZE, tilerect.height() * CELLSIZE)
        self.borderrect.setRect(borderrect)
        self.handlerect.setRect(tilerect)
        self.borderhandlerect.setRect(QRect(0, 0, self.level.level_width, self.level.level_height))