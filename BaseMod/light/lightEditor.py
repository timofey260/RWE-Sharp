import os

from PySide6.QtCore import QPointF, QRectF, Qt, QSize, QPoint
from PySide6.QtGui import QPainter, QPen, QPixmap, QMoveEvent, QImage, QTransform, QColor
from PySide6.QtWidgets import QGraphicsPixmapItem, QGraphicsScene

from BaseMod.light.lightHistory import LightPosChanged, LightImageChanged
from RWS.Configurable import PenConfigurable, FloatConfigurable, IntConfigurable, BoolConfigurable
from RWS.Core import CELLSIZE, ofsleft, ofstop, PATH_DRIZZLE_CAST, CONSTS
from RWS.Modify import Editor
from RWS.Renderable import Handle, RenderEllipse, RenderImage
from RWS.Utils import point2polar, polar2point


class LightEditor(Editor):
    def __init__(self, mod):
        super().__init__(mod)
        self.radiuspen = PenConfigurable(mod, "EDIT_light.radiuspen", QPen(Qt.GlobalColor.white, 10, s=Qt.PenStyle.DashLine), "Light Radius Pen")
        self.lightangle = FloatConfigurable(None, "", 0, "Light angle")
        self.lightflatness = IntConfigurable(None, "", 0, "Light flatness")
        self.lighthandle = Handle(self)
        self.lightradius = RenderEllipse(self, 150, QRectF(0, 0, 1, 1), self.radiuspen.value)

        self.brushwidth = FloatConfigurable(None, "", 1, "Brush Width Scale")
        self.brushheight = FloatConfigurable(None, "", 1, "Brush Height Scale")
        self.brushrotation = FloatConfigurable(None, "", 0, "Brush Rotation")
        self.drawonmoved = BoolConfigurable(None, "", False, "Draw on Moved Light")
        self.brush = RenderImage(self, 0, QSize(1, 1))
        self.painter = QPainter()

        self.lighthandle.posChanged.connect(self.pos_changed)
        self.lighthandle.mouseReleased.connect(self.mouse_released)
        self.lightangle.valueChanged.connect(self.update_light_configurables)
        self.lightflatness.valueChanged.connect(self.update_light_configurables)
        self.brushrotation.valueChanged.connect(self.update_brush_transform)
        self.brushwidth.valueChanged.connect(self.update_brush_transform)
        self.brushheight.valueChanged.connect(self.update_brush_transform)
        self.updatingconfigurables = False
        self.brushimages = {}
        for k, v in CONSTS.get("shadowimages", {}).items():
            path = os.path.join(PATH_DRIZZLE_CAST, v)
            if not os.path.exists(path):
                continue
            newimage = QImage(path)
            newimage.convertTo(QImage.Format.Format_Mono)
            newimage.setColorTable([QColor(0, 0, 0, 0).rgba(), QColor(120, 120, 120, 255).rgba()])
            self.brushimages[k] = QPixmap.fromImage(newimage)
        self.brush.setPixmap(list(self.brushimages.values())[0])
        self.oldimage = QImage(1, 1, QImage.Format.Format_Mono)

        t = QTransform()
        self.transform = t.rotate(45)
        # self.brush.renderedtexture.setTransform(self.transform)

        self.drawimage = list(self.brushimages.values())[0]
        self.drawscene = QGraphicsScene(self.drawimage.rect())
        self.virtgraphicspixmap = self.drawscene.addPixmap(list(self.brushimages.values())[0])
        self.virtpainter = QPainter()
        self.virtgraphicspixmap.setShapeMode(QGraphicsPixmapItem.ShapeMode.BoundingRectShape)
        self.update_brush_transform()

    def update_light_configurables(self):
        if self.updatingconfigurables:
            return
        oldangle, oldflatness = self.level.l_light.angle, self.level.l_light.flatness
        if oldangle == self.lightangle.value and oldflatness == self.lightflatness.value:
            return
        self.level.add_history(LightPosChanged, self.lightangle.value, self.lightflatness.value)

    def init_scene_items(self, viewport):
        super().init_scene_items(viewport)
        self.end_painter()
        self.update_position()
        self.painter.begin(self.level.l_light.image)

    def remove_items_from_scene(self, viewport):
        super().remove_items_from_scene(viewport)
        self.end_painter()

    def mouse_left_press(self):
        self.tool_specific_press()

    def mouse_right_press(self):
        if self.mouse_left:
            return
        self.tool_specific_press(False)

    def mouse_left_release(self):
        self.tool_specific_release()

    def mouse_right_release(self):
        if self.mouse_left:
            return
        self.tool_specific_release(True)

    def mouse_move_event(self, event: QMoveEvent):
        super().mouse_move_event(event)
        self.tool_specific_update()

    def tool_specific_update(self):
        imageoffset = QPoint(self.drawimage.width() // 2, self.drawimage.height() // 2)
        self.brush.setPos(self.editor_pos - imageoffset)
        if self.mouse_right or self.mouse_left:
            newpos = self.editor_pos + QPoint(ofsleft, ofstop) * CELLSIZE - imageoffset
            if self.drawonmoved.value:
                newpos -= polar2point(QPointF(self.level.l_light.angle - 90, CELLSIZE * self.level.l_light.flatness)).toPoint()
            self.painter.drawPixmap(newpos, self.drawimage)
            self.viewport.modulenames["light"].update_images()
            # self.viewport.modulenames["light"].lightimage.redraw()
            # self.viewport.modulenames["light"].lightimagestatic.redraw()

    def tool_specific_release(self, shadow=True):
        self.level.add_history(LightImageChanged, self.oldimage)

    def update_position(self):
        staticpos = -QPointF(ofsleft, ofstop) * CELLSIZE
        newpos = polar2point(QPointF(self.level.l_light.angle - 90, CELLSIZE * self.level.l_light.flatness))
        self.lighthandle.setPos(newpos + staticpos)
        self.lightradius.setRect(QRectF(staticpos - QPointF(10, 10) * CELLSIZE, staticpos + QPointF(10, 10) * CELLSIZE))
        self.updatingconfigurables = True
        self.lightangle.update_value_default(self.level.l_light.angle % 360)
        self.lightflatness.update_value_default(self.level.l_light.flatness)
        self.updatingconfigurables = False

    def end_painter(self):
        if self.painter.isActive():
            self.painter.end()

    def update_painter(self):
        if self.manager.editor != self:
            return
        self.painter.begin(self.level.l_light.image)

    def pos_changed(self, newpos):
        self.level.viewport.modulenames["light"].lightimage.setPos(newpos)

    def mouse_released(self, pos):
        newpolar = point2polar(pos + QPointF(ofsleft, ofstop) * CELLSIZE)
        angle = (newpolar.x() + 90) % 360
        flatness = min(10, max(1, newpolar.y() // CELLSIZE))
        self.level.add_history(LightPosChanged, angle, flatness)

    def tool_specific_press(self, shadow=True):
        self.oldimage = self.level.l_light.image.copy()
        if shadow:
            self.painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceOver)
            self.tool_specific_update()
            return
        self.painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_DestinationOut)
        self.tool_specific_update()

    def update_brush_transform(self):
        if self.virtpainter.isActive():
            self.virtpainter.end()
        t = QTransform()
        t = t.rotate(self.brushrotation.value)
        t = t.scale(self.brushwidth.value, self.brushheight.value)
        self.transform = t
        self.virtgraphicspixmap.setTransform(self.transform)
        self.drawimage = QPixmap(self.virtgraphicspixmap.sceneBoundingRect().size().toSize())
        self.drawimage.fill(Qt.GlobalColor.transparent)
        self.virtpainter.begin(self.drawimage)
        self.drawscene.setSceneRect(self.virtgraphicspixmap.sceneBoundingRect())
        self.drawscene.render(self.virtpainter, self.drawimage.rect(), self.virtgraphicspixmap.sceneBoundingRect())
        self.brush.setPixmap(self.drawimage)

