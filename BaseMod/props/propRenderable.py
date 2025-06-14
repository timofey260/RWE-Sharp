from RWESharp.Renderable import Renderable, RenderPoly, Handle
from RWESharp.Utils import remap
from RWESharp.Loaders import Prop

from PySide6.QtCore import QPoint, QPointF
from PySide6.QtGui import QTransform, QPolygonF, QPixmap, QImage, QPen
from PySide6.QtWidgets import QGraphicsPixmapItem

import random
# todo redo prop editor to optimize it


class PropRenderable(Renderable):
    def __init__(self, module, prop: list | Prop):
        self.hide = False
        self.drawpoly = False
        if not isinstance(prop, Prop):
            self.propdepth = prop[0]
            super().__init__(module, -self.propdepth // 10 * 100 + 100)
            self.poly = RenderPoly(module, self.depth, QPolygonF())
            found = self.manager.props.find_prop(prop[1])
            self.transform: list[QPointF] = prop[3]
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
        self.poly = RenderPoly(module, 100, QPolygonF())
        self.renderedtexture = QGraphicsPixmapItem(QPixmap.fromImage(self.image))
        self.renderedtexture.setZValue(self.depth)
        self.propdepth = 0
        w, h = prop.images[0].width(), prop.images[0].height()
        self.transform: list[QPointF] = [QPointF(0, 0), QPointF(w, 0), QPointF(w, h), QPointF(0, h)]
        self.handlers: list[Handle] = []

    def set_variation(self, variation: int):
        if variation == 0:
            self.image = self.prop.images[random.randint(0, self.prop.vars - 1)]
            self.renderedtexture.setPixmap(QPixmap.fromImage(self.image))
            return
        self.image = self.prop.images[variation - 1]
        self.renderedtexture.setPixmap(QPixmap.fromImage(self.image))

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
        self.retransform()
        #self.free_transform()
        # self.poly.init_graphics(viewport)

    def remove_graphics(self, viewport):
        super().remove_graphics(viewport)
        viewport.workscene.removeItem(self.renderedtexture)
        self.poly.remove_graphics(viewport)

    def remove_myself(self):
        super().remove_myself()
        self.poly.remove_myself()

    def move_event(self):
        super().move_event()
        self.renderedtexture.setPos(self.actual_offset)
        self.retransform()

    def zoom_event(self):
        #self.renderedtexture.setScale(zoom)
        self.retransform()

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
        self.poly.setPoly(QPolygonF(self.transform))
        #transform = transform.scale(self.zoom, self.zoom)

        layer = self.propdepth // 10
        alph = remap(abs(layer - self.propdepth / 10), 3, 0, 40, 190)
        self.renderedtexture.setOpacity(0 if self.hide else (alph / 255))
        self.poly.drawpoly.setOpacity((alph / 255) if self.drawpoly and not self.hide else 0)
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

    def set_visible(self, state):
        self.hide = not state
        self.retransform()

    def set_outline(self, state, outline):
        self.drawpoly = state
        self.poly.drawpoly.setPen(QPen(outline, 4))
        self.retransform()
