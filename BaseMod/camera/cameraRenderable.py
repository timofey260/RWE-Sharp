from RWESharp.Renderable import RenderList, Handle
from RWESharp.Core import CELLSIZE, SPRITESIZE, camh, camw
from RWESharp.Utils import circle2rect, rotate_point, point2polar, polar2point
from PySide6.QtCore import QRectF, QPointF, Qt, QLineF
from PySide6.QtGui import QPen, QColor, QFont
from PySide6.QtWidgets import QGraphicsRectItem, QGraphicsEllipseItem, QGraphicsLineItem, QGraphicsTextItem
import math


class RenderCamera(RenderList):
    def __init__(self, module, depth, camera, add_renderable: bool = True):
        super().__init__(module, depth, add_renderable=False)
        self.ui = self.module.basemod.cameraview

        self.drawrect = QGraphicsRectItem(QRectF())
        # self.ui.rectcolor.valueChanged.connect(self.drawrect.setPen)
        self.drawrect.setPen(self.ui.rectcolor.value)
        self.graphicsitems.append(self.drawrect)

        self.drawrect2 = QGraphicsRectItem(QRectF())
        # self.ui.rect2color.valueChanged.connect(self.drawrect2.setPen)
        self.drawrect2.setPen(self.ui.rect2color.value)
        self.graphicsitems.append(self.drawrect2)

        self.drawrect3 = QGraphicsRectItem(QRectF())
        # self.ui.rect3color.valueChanged.connect(self.drawrect3.setPen)
        self.drawrect3.setPen(self.ui.rect3color.value)
        self.graphicsitems.append(self.drawrect3)

        self.line1 = QGraphicsLineItem(QLineF())
        self.line1.setPen(self.ui.rectcentercolor.value)
        self.graphicsitems.append(self.line1)
        self.line2 = QGraphicsLineItem(QLineF())
        self.line2.setPen(self.ui.rectcentercolor.value)
        self.graphicsitems.append(self.line2)
        self.circle1 = QGraphicsEllipseItem(QRectF())
        self.circle1.setPen(self.ui.rectcentercolor.value)
        self.graphicsitems.append(self.circle1)
        # self.ui.rectcentercolor.valueChanged.connect(self.line1.setPen)
        # self.ui.rectcentercolor.valueChanged.connect(self.line2.setPen)
        # self.ui.rectcentercolor.valueChanged.connect(self.circle1.setPen)

        self.textindex = QGraphicsTextItem("0")
        self.textindex.setFont(QFont("Comic Sans", 30))
        self.textindex.setDefaultTextColor(QColor(168, 168, 168, 255))
        # self.ui.indexcolor.valueChanged.connect(self.textindex.setDefaultTextColor)
        self.graphicsitems.append(self.textindex)

        self.poshandle = None
        self.quadhandles = None
        self.newquads = [QPointF(), QPointF(), QPointF(), QPointF()]

        self.circles: list[QGraphicsEllipseItem] = []
        self.camlines: list[QGraphicsLineItem] = []

        for i in range(4):
            circ = QGraphicsEllipseItem()
            # self.ui.circcolor.valueChanged.connect(circ.setPen)
            circ.setPen(self.ui.circcolor.value)
            self.circles.append(circ)
            self.graphicsitems.append(circ)
            line = QGraphicsLineItem()
            # self.ui.polycolor.valueChanged.connect(line.setPen)
            line.setPen(self.ui.polycolor.value)
            self.camlines.append(line)
            self.graphicsitems.append(line)
            self.newquads[i] = camera.quads[i]

        self.show = True
        self.camera = camera
        self.assign_depth()
        self.update_camera(repaint=True)
        self.zoom_event()
        self.move_event()
        if add_renderable:
            self.module.add_renderable(self)

    @property
    def camerarect(self):
        return QRectF(0, 0, camw * CELLSIZE, camh * CELLSIZE)

    def update_camera(self, setpos=True, repaint=False):
        if setpos:
            self.setPos(self.camera.pos)
        rect = self.camerarect
        rect2 = QRectF(CELLSIZE, CELLSIZE, rect.width() - CELLSIZE * 2,
                       rect.height() - CELLSIZE * 2)
        rect3 = QRectF(CELLSIZE * 8, CELLSIZE, rect2.width() - CELLSIZE * 16, rect2.height())
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

        for i, q in enumerate(self.newquads):
            # n = QPointF()
            # nq = math.radians(q.x() % 360)
            # n.setX(math.sin(nq) * q.y() * CELLSIZE * 5)
            # n.setY(-math.cos(nq) * q.y() * CELLSIZE * 5)
            newquads.append((q * CELLSIZE * 5) + [rect.topLeft(), rect.topRight(), rect.bottomRight(), rect.bottomLeft()][i])
            # if self.quadhandles is not None:
            #     self.quadhandles[i].handle_offset = newquads[i]
        self.camlines[0].setLine(QLineF(newquads[1], newquads[0]))
        self.camlines[1].setLine(QLineF(newquads[2], newquads[1]))
        self.camlines[2].setLine(QLineF(newquads[3], newquads[2]))
        self.camlines[3].setLine(QLineF(newquads[0], newquads[3]))
        self.textindex.setPos(rect.center() * self.zoom + self.actual_offset)
        if not repaint:
            return
        self.drawrect.setPen(self.ui.rectcolor.value if self.ui.showrect.value else Qt.PenStyle.NoPen)
        self.drawrect2.setPen(self.ui.rect2color.value if self.ui.showrect2.value else Qt.PenStyle.NoPen)
        self.drawrect3.setPen(self.ui.rect3color.value if self.ui.showrect3.value else Qt.PenStyle.NoPen)
        self.line1.setPen(self.ui.rectcentercolor.value if self.ui.showrectcenter.value else Qt.PenStyle.NoPen)
        self.line2.setPen(self.ui.rectcentercolor.value if self.ui.showrectcenter.value else Qt.PenStyle.NoPen)
        self.circle1.setPen(self.ui.rectcentercolor.value if self.ui.showrectcenter.value else Qt.PenStyle.NoPen)
        for i in self.camlines:
            i.setPen(self.ui.polycolor.value if self.ui.showpoly.value else Qt.PenStyle.NoPen)
        for i in self.circles:
            i.setPen(self.ui.circcolor.value if self.ui.showcirc.value else Qt.PenStyle.NoPen)
        self.textindex.setDefaultTextColor(self.ui.indexcolor.value if self.ui.showindex.value else Qt.GlobalColor.transparent)

    def move_event(self):
        super().move_event()
        rect = self.camerarect
        self.textindex.setPos(rect.center() * self.zoom + self.actual_offset)

    def change_visibility(self, state):
        self.show = state
        self.setOpacity(1 if self.show else 0)
        self.update_camera()

    def edit_camera(self, edit=True):
        if not edit:
            self.poshandle.remove_myself()
            self.renderables.remove(self.poshandle)
            self.poshandle = None
            for i in self.quadhandles:
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
        #self.poshandle.init_graphics(self.viewport)
        self.poshandle.setPos(self.camera.pos)
        self.poshandle.handle_offset = QPointF(camw / 2 * CELLSIZE, camh / 2 * CELLSIZE)
        self.poshandle.posChanged.connect(self.setPos)
        self.poshandle.move_event()
        self.renderables.append(self.poshandle)
        self.quadhandles = []
        for i, v in enumerate(self.rectsides):
            h = Handle(self.module)
            h.handle_offset = v + self.newquads[i] * 5 * CELLSIZE
            # h.setPos(self.camera.pos)
            h.posChanged.connect(self.movequad(i))
            #h.init_graphics(self.viewport)
            h.move_event()
            self.quadhandles.append(h)
            self.renderables.append(h)
        self.update_camera()

    def movequad(self, quad):
        def move(x):
            # print(x, self.newquads[quad])
            self.newquads[quad] = (self.quadhandles[quad].handle_offset - self.rectsides[quad] + x - self.camera.pos) * (1 / (CELLSIZE * 5))
            pol = point2polar(self.newquads[quad])
            if pol.y() > 1:
                self.newquads[quad] = polar2point(QPointF(pol.x(), 1))
            self.update_camera(False)
        return move

    def fix_offset(self, quad):
        self.newquads = self.camera.quads.copy()
        self.quadhandles[quad].handle_offset = self.rectsides[quad] + self.newquads[quad] * 5 * CELLSIZE
        self.update_camera()

    def paintselected(self, selected=True):
        if selected:
            self.line1.setPen(QPen(QColor(255, 0, 0), 4))
            self.line2.setPen(QPen(QColor(255, 0, 0), 4))
            self.circle1.setPen(QPen(QColor(255, 0, 0), 4))
            return
        self.line1.setPen(self.ui.rectcentercolor.value)
        self.line2.setPen(self.ui.rectcentercolor.value)
        self.circle1.setPen(self.ui.rectcentercolor.value)

    @property
    def rectsides(self):
        return [QPointF(0, 0), self.camerarect.topRight(), self.camerarect.bottomRight(), self.camerarect.bottomLeft()]
