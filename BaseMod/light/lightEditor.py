from RWESharp.Modify import Editor
from RWESharp.Renderable import Handle, RenderEllipse
from RWESharp.Utils import point2polar, polar2point
from RWESharp.Core import CELLSIZE, ofsleft, ofstop
from RWESharp.Configurable import PenConfigurable, FloatConfigurable, IntConfigurable
from BaseMod.light.lightHistory import LightPosChanged
from PySide6.QtCore import QPointF, QRectF, Qt
from PySide6.QtGui import QPainter, QPen


class LightEditor(Editor):
    def __init__(self, mod):
        super().__init__(mod)
        self.radiuspen = PenConfigurable(mod, "EDIT_light.radiuspen", QPen(Qt.GlobalColor.white, 10, s=Qt.PenStyle.DashLine), "Light Radius Pen")
        self.lightangle = FloatConfigurable(None, "", 0, "Light angle")
        self.lightflatness = IntConfigurable(None, "", 0, "Light flatness")
        self.lighthandle = Handle(self)
        self.lightradius = RenderEllipse(self, 150, QRectF(0, 0, 1, 1), self.radiuspen.value)
        self.painter = QPainter()

        self.lighthandle.posChanged.connect(self.pos_changed)
        self.lighthandle.mouseReleased.connect(self.mouse_released)
        self.lightangle.valueChanged.connect(self.update_light_configurables)
        self.lightflatness.valueChanged.connect(self.update_light_configurables)
        self.updatingconfigurables = False

    def update_light_configurables(self):
        if self.updatingconfigurables:
            return
        oldangle, oldflatness = self.level.l_light.angle, self.level.l_light.flatness
        if oldangle == self.lightangle.value and oldflatness == self.lightflatness.value:
            return
        self.level.add_history(LightPosChanged, self.lightangle.value, self.lightflatness.value)

    def init_scene_items(self, viewport):
        super().init_scene_items(viewport)
        self.update_position()
        self.painter.begin(self.level.l_light.image)

    def remove_items_from_scene(self, viewport):
        super().remove_items_from_scene(viewport)
        if self.painter.isActive():
            self.painter.end()

    def update_position(self):
        staticpos = -QPointF(ofsleft, ofstop) * CELLSIZE
        newpos = polar2point(QPointF(self.level.l_light.angle - 90, CELLSIZE * self.level.l_light.flatness))
        self.lighthandle.setPos(newpos + staticpos)
        self.lightradius.setRect(QRectF(staticpos - QPointF(10, 10) * CELLSIZE, staticpos + QPointF(10, 10) * CELLSIZE))
        self.updatingconfigurables = True
        self.lightangle.update_value_default(self.level.l_light.angle % 360)
        self.lightflatness.update_value_default(self.level.l_light.flatness)
        self.updatingconfigurables = False

    def pos_changed(self, newpos):
        self.level.viewport.modulenames["light"].lightimage.setPos(newpos)

    def mouse_released(self, pos):
        newpolar = point2polar(pos + QPointF(ofsleft, ofstop) * CELLSIZE)
        angle = (newpolar.x() + 90) % 360
        flatness = min(10, max(1, newpolar.y() // CELLSIZE))
        self.level.add_history(LightPosChanged, angle, flatness)
