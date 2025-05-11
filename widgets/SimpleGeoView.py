from __future__ import annotations
import os
from PySide6.QtWidgets import QGraphicsView, QGraphicsPixmapItem, QGraphicsScene
from PySide6.QtGui import QColor, QPixmap, QBrush, QPainter
from PySide6.QtCore import QRect, QPoint, Qt
from RWESharp.Core import PATH_FILES_IMAGES, CONSTS
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

    def update_pixmaps(self, change=True):
        if os.path.exists(self.settings.imagepath.value):
            self.geo_texture = QPixmap(self.settings.imagepath.value)
        else:
            self.geo_texture = QPixmap(os.path.join(PATH_FILES_IMAGES, "notfound.png"))
        self.l1 = QPixmap(self.geo_texture)
        self.l1_2 = QPixmap(self.geo_texture)
        self.l2 = QPixmap(self.geo_texture)
        self.l2_2 = QPixmap(self.geo_texture)
        self.l3 = QPixmap(self.geo_texture)
        self.l3_2 = QPixmap(self.geo_texture)
        op = 50
        for i in range(2):
            painter = QPainter([self.l2_2, self.l3_2][i])
            painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceAtop)
            painter.fillRect(self.l1.rect(), [QColor(0, 255, 0, op), QColor(255, 0, 0, op)][i])
        if change:
            self.change_shit()

    def add_manager(self, manager, settings: GeoSettings):
        self.manager = manager
        self.settings = settings
        self.workscene = QGraphicsScene(0, 0, 0, 0)
        self._sz = CONSTS.get("geo_image_config", {}).get("itemsize", 100)
        self.update_pixmaps(False)
        self.setScene(self.workscene)

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
        self.setBackgroundBrush(QBrush(self.manager.basemod.gridui.backgroundcolor.value))

        self.settings.ui.Pshow.toggled.connect(self.change_shit)
        self.settings.ui.Sshow.toggled.connect(self.change_shit)
        self.settings.Pop.setting.valueChanged.connect(self.change_shit)
        self.settings.Sop.setting.valueChanged.connect(self.change_shit)
        self.settings.rgbsop.setting.valueChanged.connect(self.change_shit)
        self.settings.rgbpop.setting.valueChanged.connect(self.change_shit)
        self.settings.ui.Leditorpreview.toggled.connect(self.change_shit)
        self.settings.ui.RWEpreview.toggled.connect(self.change_shit)
        self.settings.ui.LayerSlider.valueChanged.connect(self.change_shit)

    @property
    def current_layer(self):
        return self.settings.ui.LayerSlider.value()

    @property
    def popval(self):
        return self.settings.Pop.value if self.settings.ui.Pshow.isChecked() else 0

    @property
    def sopval(self):
        return self.settings.Sop.value if self.settings.ui.Sshow.isChecked() else 0

    @property
    def rgbpopval(self):
        return self.settings.rgbpop.value if self.settings.ui.Pshow.isChecked() else 0

    @property
    def rgbsopval(self):
        return self.settings.rgbsop.value if self.settings.ui.Sshow.isChecked() else 0

    def change_shit(self):
        if self.settings.ui.Leditorpreview.isChecked():
            self.l1g.setPixmap(self.l1_2)
            self.l2g.setPixmap(self.l2_2)
            self.l3g.setPixmap(self.l3_2)
            self.l1g.setOpacity((self.rgbpopval if self.current_layer == 0 else self.rgbsopval) / 255)
            self.l2g.setOpacity((self.rgbpopval if self.current_layer == 1 else self.rgbsopval) / 255)
            self.l3g.setOpacity((self.rgbpopval if self.current_layer == 2 else self.rgbsopval) / 255)
            return
        self.l1g.setPixmap(self.l1)
        self.l2g.setPixmap(self.l2)
        self.l3g.setPixmap(self.l3)
        self.l1g.setOpacity((self.popval if self.current_layer == 0 else self.sopval) / 255)
        if self.current_layer == 1 and not self.settings.renderall.value:
            self.l1g.setOpacity(0)
        self.l2g.setOpacity((self.popval if self.current_layer == 1 else self.sopval) / 255)
        if self.current_layer == 2 and not self.settings.renderall.value:
            self.l1g.setOpacity(0)
            self.l2g.setOpacity(0)
        self.l3g.setOpacity((self.popval if self.current_layer == 2 else self.sopval) / 255)

    def mouseMoveEvent(self, event):
        offset = event.pos() - self.lastpos
        if event.buttons() & self.manager.basemod.bmconfig.movement_button.value:
            self.l1g.setPos(self.l1g.pos() + offset)
            self.l2g.setPos(self.l2g.pos() + offset)
            self.l3g.setPos(self.l3g.pos() + offset)
            self.t1.setPos(self.t1.pos() + offset)
            self.t2.setPos(self.t2.pos() + offset)
            self.t3.setPos(self.t3.pos() + offset)
        self.lastpos = event.pos()
