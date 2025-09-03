from RWESharp.Modify import Editor
from RWESharp.Renderable import Handle
from RWESharp.Utils import rotate_point
from RWESharp.Core import CELLSIZE, ofsleft, ofstop
from PySide6.QtCore import QPointF


class LightEditor(Editor):
    def __init__(self, mod):
        super().__init__(mod)
        self.lighthandle = Handle(self)

    def init_scene_items(self, viewport):
        super().init_scene_items(viewport)
        newpos = rotate_point(QPointF(0, -CELLSIZE * self.level.l_light.flatness), self.level.l_light.angle)
        self.lighthandle.setPos(newpos - QPointF(ofsleft, ofstop) * CELLSIZE)
