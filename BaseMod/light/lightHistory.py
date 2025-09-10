from RWESharp.Modify import HistoryElement
from PySide6.QtGui import QImage


class LevelResizedLight(HistoryElement):
    def __init__(self, history, newrect):
        super().__init__(history)
        self.newrect = newrect # todo

    def undo_changes(self):
        pass

    def redo_changes(self):
        pass

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
