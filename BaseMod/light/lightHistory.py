from PySide6.QtCore import QSize, QRect, QPoint
from PySide6.QtGui import QImage, QColor, QPainter

from RWS.Modify import HistoryElement
from RWS.Core import ofstop, ofsleft, CELLSIZE


class LevelResizedLight(HistoryElement):
    def __init__(self, history, newrect: QRect):
        super().__init__(history)
        self.newrect = newrect
        self.oldimage = self.level.l_light.image.copy()
        self.newsize = QSize((self.newrect.width() + ofsleft) * CELLSIZE, (self.newrect.height() + ofstop) * CELLSIZE)
        newimage = QImage(self.newsize, QImage.Format.Format_Mono)
        newimage.setColorTable([QColor(0, 0, 0, 0).rgba(), QColor(0, 0, 0, 255).rgba()])
        newimage.fill(0)
        painter = QPainter(newimage)
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_Source)
        painter.drawImage(QPoint(-self.newrect.x() * CELLSIZE, -self.newrect.y() * CELLSIZE), self.level.l_light.image)
        painter.end()
        self.newimage = newimage
        self.redo_changes()

    def undo_changes(self):
        self.basemod.lighteditor.end_painter()
        self.level.l_light.image = self.oldimage.copy()
        self.basemod.lighteditor.update_painter()
        self.level.viewport.modulenames["light"].update_images()

    def redo_changes(self):
        self.basemod.lighteditor.end_painter()
        self.level.l_light.image = self.newimage.copy()
        self.basemod.lighteditor.update_painter()
        self.level.viewport.modulenames["light"].update_images()

class LightPosChanged(HistoryElement):
    def __init__(self, history, angle: float, flatness):
        super().__init__(history)
        self.angle = angle % 360
        self.flatness = int(flatness)
        self.oldangle = self.level.l_light.angle
        self.oldflatness = self.level.l_light.flatness
        self.redo_changes()

    def undo_changes(self):
        self.level.l_light.angle = self.oldangle
        self.level.l_light.flatness = self.oldflatness
        self.level.viewport.modulenames["light"].update_position()
        self.basemod.lighteditor.update_position()

    def redo_changes(self):
        self.level.l_light.angle = self.angle
        self.level.l_light.flatness = self.flatness
        self.level.viewport.modulenames["light"].update_position()
        self.basemod.lighteditor.update_position()


class LightImageChanged(HistoryElement):
    def __init__(self, history, oldimage: QImage):
        super().__init__(history)
        self.newimage = self.level.l_light.image.copy()
        self.oldimage = oldimage.copy()
        self.redo_changes()

    def undo_changes(self):
        self.basemod.lighteditor.end_painter()
        self.level.l_light.image = self.oldimage.copy()
        self.basemod.lighteditor.update_painter()
        self.level.viewport.modulenames["light"].update_images()

    def redo_changes(self):
        self.basemod.lighteditor.end_painter()
        self.level.l_light.image = self.newimage.copy()
        self.basemod.lighteditor.update_painter()
        self.level.viewport.modulenames["light"].update_images()
