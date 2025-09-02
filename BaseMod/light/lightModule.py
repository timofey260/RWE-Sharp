from RWESharp.Modify import Module
from RWESharp.Renderable import RenderImage
from RWESharp.Configurable import FloatConfigurable
from PySide6.QtCore import QSize
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
