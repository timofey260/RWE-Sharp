from RWESharp.Renderable import Renderable
from RWESharp.Core import lingoIO, CELLSIZE, SPRITESIZE
from RWESharp.Utils import remap
from RWESharp.Loaders import Prop

from PySide6.QtCore import QPoint, QPointF
from PySide6.QtGui import QTransform, QPolygonF, QPainter, QPixmap, QImage
from PySide6.QtWidgets import QGraphicsPixmapItem

from BaseMod.props.Handle import Handle


class PropRenderable(Renderable):
    def __init__(self, module, prop: list | Prop):
        if not isinstance(prop, Prop):
            self.propdepth = prop[0]
            super().__init__(module, -self.propdepth // 10 * 100 + 100)
            found = self.manager.props.find_prop(prop[1])
            self.transform: list[QPointF] = self.quadlist2points(prop[3])
            if found is None:
                self.prop = None
                self.image = QImage(20, 20, QImage.Format.Format_Mono)
                self.renderedtexture = QGraphicsPixmapItem(QPixmap.fromImage(self.image))
                self.renderedtexture.setZValue(self.depth)
                return
            self.prop = found
            variation = prop[4]["settings"].get("variation", 1) - 1
            self.image = found.images[variation]
            self.renderedtexture = QGraphicsPixmapItem(QPixmap.fromImage(self.image))
            self.renderedtexture.setZValue(self.depth)
            return
        self.prop = prop
        self.image = prop.images[0]
        super().__init__(module, 100)
        self.renderedtexture = QGraphicsPixmapItem(QPixmap.fromImage(self.image))
        self.renderedtexture.setZValue(self.depth)
        self.propdepth = 0
        w, h = prop.images[0].width(), prop.images[0].height()
        self.transform: list[QPointF] = [QPointF(0, 0), QPointF(w, 0), QPointF(w, h), QPointF(0, h)]
        self.handlers: list[Handle] = []

    def setprop(self, prop: Prop):
        self.prop = prop
        self.image = prop.images[0]
        w, h = prop.images[0].width(), prop.images[0].height()
        self.transform: list[QPointF] = [QPointF(0, 0), QPointF(w, 0), QPointF(w, h), QPointF(0, h)]
        if self.renderedtexture is not None:
            self.renderedtexture.setPixmap(QPixmap.fromImage(self.image))
        if len(self.handlers) > 0:
            self.delete_handlers()
            self.free_transform()
            self.retransform()
            self.viewport.clean()

    def init_graphics(self, viewport):
        super().init_graphics(viewport)
        viewport.workscene.addItem(self.renderedtexture)
        #self.draw_layer()
        self.move_event(self.viewport.topleft.pos())
        self.retransform()
        #self.free_transform()

    def remove_graphics(self, viewport):
        super().remove_graphics(viewport)
        viewport.workscene.removeItem(self.renderedtexture)

    def move_event(self, pos):
        super().move_event(pos)
        self.renderedtexture.setPos(self.actual_offset)
        self.retransform()

    def zoom_event(self, zoom):
        #self.renderedtexture.setScale(zoom)
        self.retransform()

    def quadlist2points(self, qlist: list[str]):
        return [i * (CELLSIZE / SPRITESIZE) for i in qlist]

    def setPos(self, pos: QPointF):
        super().setPos(pos)
        self.renderedtexture.setPos(self.actual_offset)
        self.retransform()

    def retransform(self):
        transform = QTransform()
        w, h = self.image.width(), self.image.height()
        #transform.translate(self.actual_offset.x(), self.actual_offset.y())
        transform = transform.quadToQuad(QPolygonF([QPoint(0, 0), QPoint(w, 0), QPoint(w, h), QPoint(0, h)]),
                                         QPolygonF([i * self.zoom * self.scale for i in self.transform]))
        #transform = transform.scale(self.zoom, self.zoom)

        layer = self.propdepth // 10
        alph = remap(abs(layer - self.propdepth / 10), 3, 0, 40, 190)
        self.renderedtexture.setOpacity(alph / 255)
        #self.renderedtexture.setTransformOriginPoint(self.actual_offset)
        self.renderedtexture.setTransform(transform)
        #self.renderedtexture.setScale(self.zoom)

    def delete_handlers(self):
        for i in self.handlers:
            i.remove_graphics(self.viewport)
            i.remove_myself()
        self.handlers.clear()

    def free_transform(self):
        self.handlers = []
        for i in range(4):
            self.handlers.append(Handle(self.module))
            self.handlers[i].init_graphics(self.viewport)
            self.handlers[i].setPos(self.transform[i] + self.offset)
            self.handlers[i].posChanged.connect(self.pointchange(i))

    def pointchange(self, i):
        def p(v):
            self.transform[i] = v - self.offset
            self.retransform()
        return p
