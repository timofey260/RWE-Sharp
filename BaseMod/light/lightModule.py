from RWESharp.Modify import Module
from RWESharp.Renderable import RenderImage
from RWESharp.Configurable import FloatConfigurable
from RWESharp.Utils import rotate_point
from RWESharp.Core import CELLSIZE, ofsleft, ofstop
from PySide6.QtCore import QSize, QPointF
from PySide6.QtGui import QPixmap


class LightModule(Module):
    def __init__(self, mod):
        super().__init__(mod)
        self.lightopacity = FloatConfigurable(mod, "VIEW_light.lightop", .6, "Light image opacity")
        self.lightimage = RenderImage(self, 100, QSize(1, 1))
        self.lightimage.setOpacity(self.lightopacity.value)

        self.lightopacity.valueChanged.connect(self.lightimage.setOpacity)

    def init_scene_items(self, viewport):
        super().init_scene_items(viewport)
        self.lightimage.setPixmap(QPixmap.fromImage(self.level.l_light.image))
        self.update_position()

    def update_position(self):
        newpos = rotate_point(QPointF(0, -CELLSIZE * self.level.l_light.flatness), self.level.l_light.angle)
        self.lightimage.setPos(newpos - QPointF(ofsleft, ofstop) * CELLSIZE)
