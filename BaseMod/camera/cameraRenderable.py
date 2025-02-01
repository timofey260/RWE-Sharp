from RWESharp.Renderable import RenderList
from RWESharp.Core import CELLSIZE, SPRITESIZE
from PySide6.QtCore import QRectF, QPointF, Qt
from PySide6.QtGui import QPen, QColor
from PySide6.QtWidgets import QGraphicsRectItem, QGraphicsEllipseItem, QGraphicsLineItem

camw = 70
camh = 40


class RenderCamera(RenderList):
    def __init__(self, module, depth, pos: QPointF):
        super().__init__(module, depth)

        self.drawrect = QGraphicsRectItem(QRectF())
        self.drawrect.setPen(QPen(QColor(255, 0, 0), 10, Qt.PenStyle.DashDotLine))
        self.rendered.append(self.drawrect)

        self.drawrect2 = QGraphicsRectItem(QRectF())
        self.rendered.append(self.drawrect2)

        self.drawrect3 = QGraphicsRectItem(QRectF())
        self.drawrect3.setPen(QPen(QColor(255, 255, 0), 5, Qt.PenStyle.DotLine))
        self.rendered.append(self.drawrect3)

        self.campos = pos
        self.assign_depth()
        self.update_camera()

    def update_camera(self):
        rect = QRectF(self.campos.x(), self.campos.y(), camw * CELLSIZE, camh * CELLSIZE)
        rect2 = QRectF(rect.x() + CELLSIZE, rect.y() + CELLSIZE, rect.width() - CELLSIZE * 2,
                       rect.height() - CELLSIZE * 2)
        rect3 = QRectF(rect2.x() + CELLSIZE * 8, rect2.y(), rect2.width() - CELLSIZE * 16, rect2.height())
        self.drawrect.setRect(rect)
        self.drawrect2.setRect(rect2)
        self.drawrect3.setRect(rect3)

    # def actual_offset(self):
    #     return super().actual_offset() -
