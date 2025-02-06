from RWESharp.Renderable import RenderList
from RWESharp.Core import CELLSIZE, SPRITESIZE, camh, camw
from RWESharp.Utils import circle2rect, rotate_point
from PySide6.QtCore import QRectF, QPointF, Qt, QLineF
from PySide6.QtGui import QPen, QColor
from PySide6.QtWidgets import QGraphicsRectItem, QGraphicsEllipseItem, QGraphicsLineItem
import math


class RenderCamera(RenderList):
    def __init__(self, module, depth, camera):
        super().__init__(module, depth)

        self.drawrect = QGraphicsRectItem(QRectF())
        self.drawrect.setPen(QPen(QColor(0, 255, 0), 4, Qt.PenStyle.DashDotLine))
        self.graphicsitems.append(self.drawrect)

        self.drawrect2 = QGraphicsRectItem(QRectF())
        self.drawrect2.setPen(QPen(QColor(0, 120, 0), 3))
        self.graphicsitems.append(self.drawrect2)

        self.drawrect3 = QGraphicsRectItem(QRectF())
        self.drawrect3.setPen(QPen(QColor(255, 255, 0), 3, Qt.PenStyle.DotLine))
        self.graphicsitems.append(self.drawrect3)

        self.line1 = QGraphicsLineItem(QLineF())
        self.line1.setPen(QPen(QColor(40, 40, 40), 5))
        self.graphicsitems.append(self.line1)
        self.line2 = QGraphicsLineItem(QLineF())
        self.line2.setPen(QPen(QColor(40, 40, 40), 5))
        self.graphicsitems.append(self.line2)
        self.circle1 = QGraphicsEllipseItem(QRectF())
        self.circle1.setPen(QPen(QColor(40, 40, 40), 5))
        self.graphicsitems.append(self.circle1)

        self.circles: list[QGraphicsEllipseItem] = []
        self.camlines: list[QGraphicsLineItem] = []

        for i in range(4):
            circ = QGraphicsEllipseItem()
            circ.setPen(QPen(QColor(0, 255, 0), 5))
            self.circles.append(circ)
            self.graphicsitems.append(circ)
            line = QGraphicsLineItem()
            line.setPen(QPen(QColor(0, 255, 0), 6, Qt.PenStyle.DashLine))
            self.camlines.append(line)
            self.graphicsitems.append(line)

        self.show = True
        self.camera = camera
        self.assign_depth()
        self.update_camera()

    def update_camera(self):
        rect = QRectF(self.camera.pos.x(), self.camera.pos.y(), camw * CELLSIZE, camh * CELLSIZE)
        rect2 = QRectF(rect.x() + CELLSIZE, rect.y() + CELLSIZE, rect.width() - CELLSIZE * 2,
                       rect.height() - CELLSIZE * 2)
        rect3 = QRectF(rect2.x() + CELLSIZE * 8, rect2.y(), rect2.width() - CELLSIZE * 16, rect2.height())
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
        self.camlines[0].setLine(QLineF(newquads[1], newquads[0]))
        self.camlines[1].setLine(QLineF(newquads[2], newquads[1]))
        self.camlines[2].setLine(QLineF(newquads[3], newquads[2]))
        self.camlines[3].setLine(QLineF(newquads[0], newquads[3]))

    def change_visibility(self, state):
        self.show = state
        for i in self.graphicsitems:
            i.setOpacity(1 if self.show else 0)
        self.update_camera()
