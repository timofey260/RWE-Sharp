from RWESharp.Modify import Editor
from RWESharp.Renderable import Handle, RenderRect, GridHandleRectangle, HandleRectangle
from RWESharp.Core import CELLSIZE
from BaseMod.properties.PropertiesHistory import BorderChange
from PySide6.QtCore import QPoint, QRect, QRectF

class PropertiesEditor(Editor):
    def __init__(self, mod):
        super().__init__(mod)
        self.handlerect = GridHandleRectangle(self, QRect(0, 0, 5, 5))
        self.handlerect.recth.rectChanged.connect(self.extratiles_changed)
        self.borderhandlerect = GridHandleRectangle(self, QRect(0, 0, 40, 40))
        self.borderhandlerect.recth.rectChanged.connect(print)

    def init_scene_items(self, viewport):
        super().init_scene_items(viewport)
        self.reposition()

    def extratiles_changed(self, rect: QRect):
        newtiles = [max(rect.x(), 0), max(rect.y(), 0), max(self.level.level_width - rect.x() - rect.width(), 0), max(self.level.level_height - rect.y() - rect.height(), 0)]
        self.level.add_history(BorderChange, newtiles)

    def reposition(self):
        width = self.level.level_width
        height = self.level.level_height

        et = self.level.extra_tiles
        tilerect = QRect(et[0], et[1], width - et[2] - et[0], height - et[3] - et[1])
        # w = width - rw - x
        # rw = width - x - w
        # borderrect = QRect(tilerect.x() * CELLSIZE, tilerect.y() * CELLSIZE, tilerect.width() * CELLSIZE, tilerect.height() * CELLSIZE)
        self.handlerect.setRect(tilerect)
        self.borderhandlerect.setRect(QRect(0, 0, width, height))