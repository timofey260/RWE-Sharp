from RWESharp.Renderable import RenderList, Handle
from RWESharp.Core import CELLSIZE, SPRITESIZE, camh, camw
from RWESharp.Utils import circle2rect, rotate_point, point2polar
from PySide6.QtCore import QRectF, QPointF, Qt, QLineF
from PySide6.QtGui import QPen, QColor
from PySide6.QtWidgets import QGraphicsRectItem, QGraphicsEllipseItem, QGraphicsLineItem
import math


class RenderCamera(RenderList):
    def __init__(self, module, depth, camera):
        super().__init__(module, depth)

        self.drawrect = QGraphicsRectItem(QRectF())
        module.basemod.cameraview.rectcolor.valueChanged.connect(self.drawrect.setPen)
        self.drawrect.setPen(module.basemod.cameraview.rectcolor.value)
        self.graphicsitems.append(self.drawrect)

        self.drawrect2 = QGraphicsRectItem(QRectF())
        module.basemod.cameraview.rect2color.valueChanged.connect(self.drawrect2.setPen)
        self.drawrect2.setPen(module.basemod.cameraview.rect2color.value)
        self.graphicsitems.append(self.drawrect2)

        self.drawrect3 = QGraphicsRectItem(QRectF())
        module.basemod.cameraview.rect3color.valueChanged.connect(self.drawrect3.setPen)
        self.drawrect3.setPen(module.basemod.cameraview.rect3color.value)
        self.graphicsitems.append(self.drawrect3)

        self.line1 = QGraphicsLineItem(QLineF())
        self.line1.setPen(module.basemod.cameraview.rectcentercolor.value)
        self.graphicsitems.append(self.line1)
        self.line2 = QGraphicsLineItem(QLineF())
        self.line2.setPen(module.basemod.cameraview.rectcentercolor.value)
        self.graphicsitems.append(self.line2)
        self.circle1 = QGraphicsEllipseItem(QRectF())
        self.circle1.setPen(module.basemod.cameraview.rectcentercolor.value)
        self.graphicsitems.append(self.circle1)
        module.basemod.cameraview.rectcentercolor.valueChanged.connect(self.line1.setPen)
        module.basemod.cameraview.rectcentercolor.valueChanged.connect(self.line2.setPen)
        module.basemod.cameraview.rectcentercolor.valueChanged.connect(self.circle1.setPen)

        self.poshandle = None
        self.quadhandles = None

        self.circles: list[QGraphicsEllipseItem] = []
        self.camlines: list[QGraphicsLineItem] = []

        for i in range(4):
            circ = QGraphicsEllipseItem()
            module.basemod.cameraview.circcolor.valueChanged.connect(circ.setPen)
            circ.setPen(module.basemod.cameraview.circcolor.value)
            self.circles.append(circ)
            self.graphicsitems.append(circ)
            line = QGraphicsLineItem()
            module.basemod.cameraview.polycolor.valueChanged.connect(line.setPen)
            line.setPen(module.basemod.cameraview.polycolor.value)
            self.camlines.append(line)
            self.graphicsitems.append(line)

        self.show = True
        self.camera = camera
        self.assign_depth()
        self.update_camera()
        self.zoom_event()
        self.move_event()

    @property
    def camerarect(self):
        return QRectF(0, 0, camw * CELLSIZE, camh * CELLSIZE)

    def update_camera(self):
        self.setPos(self.camera.pos)
        rect = self.camerarect
        rect2 = QRectF(CELLSIZE, CELLSIZE, rect.width() - CELLSIZE * 2,
                       rect.height() - CELLSIZE * 2)
        rect3 = QRectF(CELLSIZE * 8, 0, rect2.width() - CELLSIZE * 16, rect2.height())
        self.drawrect.setRect(rect)
        self.drawrect2.setRect(rect2)
        self.drawrect3.setRect(rect3)

        self.line1.setLine(QLineF(rect.center() - QPointF(CELLSIZE * 5, 0), rect.center() + QPointF(CELLSIZE * 5, 0)))
        self.line2.setLine(QLineF(rect.center() - QPointF(0, CELLSIZE * 5), rect.center() + QPointF(0, CELLSIZE * 5)))
        self.circle1.setRect(circle2rect(rect.center(), CELLSIZE * 3))
        for i, v in enumerate(self.circles):
            p = [rect.topLeft(), rect.topRight(), rect.bottomRight(), rect.bottomLeft()][i]
            v.setRect(circle2rect(p, CELLSIZE * 5))

        newquads = []

        for i, q in enumerate(self.camera.quads):
            n = QPointF()
            nq = math.radians(q.x() % 360)
            n.setX(math.sin(nq) * q.y() * CELLSIZE * 5)
            n.setY(-math.cos(nq) * q.y() * CELLSIZE * 5)
            newquads.append(n + [rect.topLeft(), rect.topRight(), rect.bottomRight(), rect.bottomLeft()][i])
            # if self.quadhandles is not None:
            #     self.quadhandles[i].handle_offset = newquads[i]
        self.camlines[0].setLine(QLineF(newquads[1], newquads[0]))
        self.camlines[1].setLine(QLineF(newquads[2], newquads[1]))
        self.camlines[2].setLine(QLineF(newquads[3], newquads[2]))
        self.camlines[3].setLine(QLineF(newquads[0], newquads[3]))

    def change_visibility(self, state):
        self.show = state
        self.setOpacity(1 if self.show else 0)
        self.update_camera()

    def edit_camera(self, edit=True):
        if not edit:
            self.poshandle.remove_graphics(self.viewport)
            self.poshandle.remove_myself()
            self.renderables.remove(self.poshandle)
            self.poshandle = None
            for i in self.quadhandles:
                i.remove_graphics(self.viewport)
                i.remove_myself()
                self.renderables.remove(i)
            self.quadhandles = None
            return
        if self.poshandle is not None:
            self.poshandle.posChanged.disconnect()
            self.poshandle.posChangedRelative.disconnect()
            self.poshandle.mouseReleased.disconnect()
            # self.poshandle.mousePressed.disconnect()
            self.poshandle.posChanged.connect(self.setPos)
            for i in self.quadhandles:
                i.posChangedRelative.disconnect()
                i.mouseReleased.disconnect()
            return
        self.poshandle = Handle(self.module)
        self.poshandle.init_graphics(self.viewport)
        self.poshandle.setPos(self.camera.pos)
        self.poshandle.handle_offset = QPointF(camw / 2 * CELLSIZE, camh / 2 * CELLSIZE)
        self.poshandle.posChanged.connect(self.setPos)
        self.poshandle.move_event()
        self.renderables.append(self.poshandle)
        self.quadhandles = []
        for i, v in enumerate(self.rectsides):
            h = Handle(self.module)
            h.handle_offset = v
            # h.setPos(self.camera.pos)
            h.posChanged.connect(self.movequad(i))
            h.init_graphics(self.viewport)
            h.move_event()
            self.quadhandles.append(h)
            self.renderables.append(h)
        self.update_camera()

    def movequad(self, quad):
        def move(x):
            self.camera.quads[quad] = point2polar((x - self.rectsides[quad]) * (1 / (CELLSIZE * 5)))
            self.update_camera()
        return move

    def paintselected(self, selected=True):
        if selected:
            self.line1.setPen(QPen(QColor(255, 0, 0), 4))
            self.line2.setPen(QPen(QColor(255, 0, 0), 4))
            self.circle1.setPen(QPen(QColor(255, 0, 0), 4))
            return
        self.line1.setPen(self.module.basemod.cameraview.rectcentercolor.value)
        self.line2.setPen(self.module.basemod.cameraview.rectcentercolor.value)
        self.circle1.setPen(self.module.basemod.cameraview.rectcentercolor.value)

    @property
    def rectsides(self):
        return [QPointF(0, 0), self.camerarect.topRight(), self.camerarect.bottomRight(), self.camerarect.bottomLeft()]
