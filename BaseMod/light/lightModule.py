from RWESharp.Modify import Module
from RWESharp.Renderable import RenderImage
from RWESharp.Configurable import FloatConfigurable
from RWESharp.Utils import rotate_point
from RWESharp.Core import CELLSIZE, ofsleft, ofstop
from PySide6.QtCore import QSize, QPointF, QRect
from PySide6.QtGui import QPixmap


class LightModule(Module):
    def __init__(self, mod):
        super().__init__(mod)
        self.lightopacity = FloatConfigurable(mod, "VIEW_light.lightop", .4, "Light image opacity")
        self.lightstaticopacity = FloatConfigurable(mod, "VIEW_light.lightstaticop", .4, "Static Light image opacity")
        self.lightimage = RenderImage(self, 100, QSize(1, 1))
        self.lightimagestatic = RenderImage(self, 100, QSize(1, 1))
        self.lightimage.setOpacity(self.lightopacity.value)
        self.lightimagestatic.setOpacity(self.lightstaticopacity.value)

        self.lightopacity.valueChanged.connect(self.lightimage.setOpacity)
        self.lightstaticopacity.valueChanged.connect(self.lightimagestatic.setOpacity)

    def init_scene_items(self, viewport):
        super().init_scene_items(viewport)
        newimage = QPixmap.fromImage(self.level.l_light.image)
        self.lightimage.setPixmap(newimage)
        self.lightimagestatic.setPixmap(newimage)
        self.update_position()

    def level_resized(self, newrect: QRect):
        super().level_resized(newrect)
        self.update_position()

    def update_position(self):
        newpos = rotate_point(QPointF(0, -CELLSIZE * self.level.l_light.flatness), self.level.l_light.angle)
        self.lightimage.setPos(newpos - QPointF(ofsleft, ofstop) * CELLSIZE)
        self.lightimagestatic.setPos(-QPointF(ofsleft, ofstop) * CELLSIZE)
