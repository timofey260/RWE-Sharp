from RWESharp.Renderable import Renderable
from RWESharp.Core import lingoIO

from PySide6.QtCore import QPoint, QPointF
from PySide6.QtGui import QTransform, QPolygonF, QPainter, QPixmap, QImage
from PySide6.QtWidgets import QGraphicsPixmapItem

from widgets import Viewport


class PropRenderable(Renderable):
    def __init__(self, mod, depth, prop):
        super().__init__(mod, depth)
        found = self.mod.manager.props.find_prop(prop[1])
        self.renderedtexture: QGraphicsPixmapItem | None = None
        self.transform: list[QPointF] = self.quadlist2points(prop[3])
        if found is None:
            self.prop = None
            self.image = QImage(20, 20, QImage.Format.Format_Mono)
            return
        self.prop = found
        variation = prop[4]["settings"].get("variation", 1) - 1
        self.image = found.images[variation]

    def init_graphics(self, viewport: Viewport):
        self.renderedtexture = viewport.workscene.addPixmap(QPixmap.fromImage(self.image))
        self.renderedtexture.setZValue(self.depth)
        print("shit")
        #self.draw_layer()
        #self.retransform()

    def remove_graphics(self):
        self.renderedtexture.removeFromIndex()
        self.renderedtexture = None

    def move_event(self, pos):
        super().move_event(pos)
        self.renderedtexture.setPos(self.actual_offset)
        #self.retransform()

    def zoom_event(self, zoom):
        self.renderedtexture.setScale(zoom)

    def quadlist2points(self, qlist: list[str]):
        return [QPointF(*lingoIO.fromarr(i, "point")) for i in qlist]

    def setPos(self, pos: QPointF):
        super().setPos(pos)
        self.renderedtexture.setPos(self.actual_offset)

    def retransform(self):
        transform = QTransform()
        w, h = self.image.width(), self.image.height()
        transform.quadToQuad(QPolygonF([QPoint(0, 0), QPoint(w, 0), QPoint(w, h), QPoint(0, h)]),
                             QPolygonF(self.transform))
        self.renderedtexture.setTransform(transform)
