from RWESharp.Renderable import Renderable
from RWESharp.Core import lingoIO, CELLSIZE, SPRITESIZE
from RWESharp.Utils import remap
from RWESharp.Loaders import Prop

from PySide6.QtCore import QPoint, QPointF
from PySide6.QtGui import QTransform, QPolygonF, QPainter, QPixmap, QImage
from PySide6.QtWidgets import QGraphicsPixmapItem

from widgets import Viewport
import os


class PropRenderable(Renderable):
    def __init__(self, mod, prop: list | Prop):
        self.renderedtexture: QGraphicsPixmapItem | None = None
        if not isinstance(prop, Prop):
            self.propdepth = prop[0]
            super().__init__(mod, -self.propdepth // 10 * 100 + 100)
            found = self.mod.manager.props.find_prop(prop[1])
            self.transform: list[QPointF] = self.quadlist2points(prop[3])
            if found is None:
                self.prop = None
                self.image = QImage(20, 20, QImage.Format.Format_Mono)
                return
            self.prop = found
            variation = prop[4]["settings"].get("variation", 1) - 1
            self.image = found.images[variation]
            return
        super().__init__(mod, 100)
        self.prop = prop
        self.image = prop.images[0]
        self.propdepth = 0
        w, h = prop.images[0].width(), prop.images[0].height()
        self.transform: list[QPointF] = [QPointF(0, 0), QPointF(w, 0), QPointF(w, h), QPointF(0, h)]

    def init_graphics(self, viewport: Viewport):
        self.renderedtexture = viewport.workscene.addPixmap(QPixmap.fromImage(self.image))
        self.renderedtexture.setZValue(self.depth)
        self.setPos(QPointF(0, 0))
        #self.draw_layer()
        #self.retransform()

    def remove_graphics(self):
        self.renderedtexture.removeFromIndex()
        self.renderedtexture = None

    def move_event(self, pos):
        super().move_event(pos)
        self.renderedtexture.setPos(self.actual_offset)
        self.retransform()

    def zoom_event(self, zoom):
        #self.renderedtexture.setScale(zoom)
        self.retransform()

    def quadlist2points(self, qlist: list[str]):
        return [QPointF(*lingoIO.fromarr(i, "point")) * (CELLSIZE / SPRITESIZE) for i in qlist]

    def setPos(self, pos: QPointF):
        super().setPos(pos)
        self.renderedtexture.setPos(self.actual_offset)
        self.retransform()

    def retransform(self):
        transform = QTransform()
        w, h = self.image.width(), self.image.height()
        #transform.translate(self.actual_offset.x(), self.actual_offset.y())
        transform = transform.quadToQuad(QPolygonF([QPoint(0, 0), QPoint(w, 0), QPoint(w, h), QPoint(0, h)]),
                                         QPolygonF([i * self.zoom for i in self.transform]))
        #transform = transform.scale(self.zoom, self.zoom)

        layer = self.propdepth // 10
        alph = remap(abs(layer - self.propdepth / 10), 3, 0, 40, 190)
        self.renderedtexture.setOpacity(alph / 255)
        self.renderedtexture.setTransformOriginPoint(self.actual_offset)
        self.renderedtexture.setTransform(transform)
        #self.renderedtexture.setScale(self.zoom)
