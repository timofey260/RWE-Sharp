from __future__ import annotations
import os
from PySide6.QtWidgets import QGraphicsView, QGraphicsPixmapItem, QGraphicsScene
from PySide6.QtGui import QColor, QPixmap, QBrush, QPainter
from PySide6.QtCore import QRect, QPoint, Qt
from core.info import PATH_FILES_IMAGES, CONSTS
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from BaseMod.geo.geoUIConnectors import GeoSettings


class SimpleGeoViewport(QGraphicsView):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)
        self.lastpos = QPoint(0, 0)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setCursor(Qt.CursorShape.SizeAllCursor)

    def add_manager(self, manager, settings: GeoSettings):
        print("yep")
        self.manager = manager
        self.settings = settings
        self.workscene = QGraphicsScene(0, 0, 0, 0)
        if os.path.exists(os.path.join(PATH_FILES_IMAGES, CONSTS.get("geo_image_config", {}).get("image"))):
            self.geo_texture = QPixmap(os.path.join(PATH_FILES_IMAGES, CONSTS.get("geo_image_config", {}).get("image")))
        else:
            self.geo_texture = QPixmap(os.path.join(PATH_FILES_IMAGES, "notfound.png"))

        self._sz = CONSTS.get("geo_image_config", {}).get("itemsize", 100)
        self.setScene(self.workscene)
        self.l1 = QPixmap(self.geo_texture)
        self.l1_2 = QPixmap(self.geo_texture)
        self.l2 = QPixmap(self.geo_texture)
        self.l2_2 = QPixmap(self.geo_texture)
        self.l3 = QPixmap(self.geo_texture)
        self.l3_2 = QPixmap(self.geo_texture)
        op = 50
        for i in range(3):
            painter = QPainter([self.l1_2, self.l2_2, self.l3_2][i])
            painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceAtop)
            painter.fillRect(self.l1.rect(), [0, QColor(0, 255, 0, op), QColor(255, 0, 0, op)][i])

        self.l3g = self.workscene.addPixmap(self.l3)
        self.l2g = self.workscene.addPixmap(self.l2)
        self.l1g = self.workscene.addPixmap(self.l1)
        self.t1 = self.workscene.addText("Layer 1")
        self.t2 = self.workscene.addText("Layer 2")
        self.t3 = self.workscene.addText("Layer 3")

        self.t1.setRotation(90)
        self.t1.setPos(QPoint(self._sz // 2, 0))
        self.t2.setRotation(90)
        self.t2.setPos(QPoint(self._sz, 0))
        self.t3.setRotation(90)
        self.t3.setPos(QPoint(self._sz + self._sz // 2, 0))
        self.l1g.setScale(.5)
        self.l2g.setScale(.5)
        self.l3g.setScale(.5)
        self.l2g.setPos(QPoint(self._sz // 2, 0))
        self.l3g.setPos(QPoint(self._sz, 0))
        self.setBackgroundBrush(QBrush(self.manager.basemod.gridmodule.backgroundcolor.value))

        self.settings.ui.L1show.toggled.connect(self.change_shit)
        self.settings.ui.L2show.toggled.connect(self.change_shit)
        self.settings.ui.L3show.toggled.connect(self.change_shit)
        self.settings.l1op.valueChanged.connect(self.change_shit)
        self.settings.l2op.valueChanged.connect(self.change_shit)
        self.settings.l3op.valueChanged.connect(self.change_shit)
        self.settings.rgbop.valueChanged.connect(self.change_shit)
        self.settings.ui.Leditorpreview.toggled.connect(self.change_shit)
        self.settings.ui.RWEpreview.toggled.connect(self.change_shit)

    def change_shit(self):
        if self.settings.ui.Leditorpreview.isChecked():
            self.l1g.setPixmap(self.l1_2)
            self.l2g.setPixmap(self.l2_2)
            self.l3g.setPixmap(self.l3_2)
            self.l1g.setOpacity(self.settings.rgbop.value / 255 if self.settings.ui.L1show.isChecked() else 0)
            self.l2g.setOpacity(self.settings.rgbop.value / 255 if self.settings.ui.L2show.isChecked() else 0)
            self.l3g.setOpacity(self.settings.rgbop.value / 255 if self.settings.ui.L3show.isChecked() else 0)
            return
        self.l1g.setPixmap(self.l1)
        self.l2g.setPixmap(self.l2)
        self.l3g.setPixmap(self.l3)
        self.l1g.setOpacity(self.settings.l1op.value / 255 if self.settings.ui.L1show.isChecked() else 0)
        if self.settings.opshift.value:
            self.l2g.setOpacity(
                (
                    self.settings.l1op.value / 255 if not self.settings.ui.L1show.isChecked() else
                    self.settings.l2op.value / 255) if self.settings.ui.L2show.isChecked() else 0
            )
            self.l3g.setOpacity(
                (
                    self.settings.l1op.value / 255 if not self.settings.ui.L1show.isChecked() and not self.settings.ui.L2show.isChecked() else
                    self.settings.l2op.value / 255 if not self.settings.ui.L1show.isChecked() or not self.settings.ui.L2show.isChecked() else
                    self.settings.l3op.value / 255
                ) if self.settings.ui.L3show.isChecked() else 0
            )
        else:
            self.l2g.setOpacity(self.settings.l2op.value / 255 if self.settings.ui.L2show.isChecked() else 0)
            self.l3g.setOpacity(self.settings.l3op.value / 255 if self.settings.ui.L3show.isChecked() else 0)

    def mouseMoveEvent(self, event):
        offset = event.pos() - self.lastpos
        if event.buttons() & self.manager.basemod.movement_button.value:
            self.l1g.setPos(self.l1g.pos() + offset)
            self.l2g.setPos(self.l2g.pos() + offset)
            self.l3g.setPos(self.l3g.pos() + offset)
            self.t1.setPos(self.t1.pos() + offset)
            self.t2.setPos(self.t2.pos() + offset)
            self.t3.setPos(self.t3.pos() + offset)
        self.lastpos = event.pos()
