from PySide6.QtCore import QSize, QPointF, QRect
from PySide6.QtGui import QPixmap

from RWESharp2.Core import CELLSIZE, ofsleft, ofstop
from RWESharp2.Modify import Module
from RWESharp2.Renderable import RenderImage
from RWESharp2.Utils import polar2point


class LightModule(Module):
    def __init__(self, mod):
        super().__init__(mod)
        self.ui = mod.lightviewui
        self.lightimage = RenderImage(self, 100, QSize(1, 1))
        self.lightimagestatic = RenderImage(self, 110, QSize(1, 1))

        self.lightimage.painter_enabled = False  # important
        self.lightimagestatic.painter_enabled = False
        self.newlightimage = QPixmap(1, 1)

        self.ui.showlight.valueChanged.connect(self.update_opacity)
        self.ui.showlightstatic.valueChanged.connect(self.update_opacity)
        self.ui.showlightmoved.valueChanged.connect(self.update_opacity)
        self.ui.lightopacity.valueChanged.connect(self.update_opacity)
        self.ui.lightstaticopacity.valueChanged.connect(self.update_opacity)

    def init_scene_items(self, viewport):
        super().init_scene_items(viewport)
        self.update_images()

    def update_images(self):
        self.newlightimage = QPixmap.fromImage(self.level.l_light.image)
        self.lightimage.setPixmap(self.newlightimage)
        self.lightimagestatic.setPixmap(self.newlightimage)
        self.update_opacity()
        self.update_position()

    def update_opacity(self):
        self.lightimage.setOpacity(self.ui.lightopacity.value if self.ui.showlight.value and self.ui.showlightmoved.value else 0)
        self.lightimagestatic.setOpacity(self.ui.lightstaticopacity.value if self.ui.showlight.value and self.ui.showlightstatic.value else 0)

    def level_resized(self, newrect: QRect):
        super().level_resized(newrect)
        self.update_position()

    def update_position(self):
        newpos = polar2point(QPointF(self.level.l_light.angle - 90, CELLSIZE * self.level.l_light.flatness))
        #newpos = rotate_point(QPointF(0, -CELLSIZE * self.level.l_light.flatness), self.level.l_light.angle)
        self.lightimage.setPos(newpos - QPointF(ofsleft, ofstop) * CELLSIZE)
        self.lightimagestatic.setPos(-QPointF(ofsleft, ofstop) * CELLSIZE)
