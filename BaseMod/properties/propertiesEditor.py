from RWESharp.Modify import Editor
from RWESharp.Renderable import Handle, RenderRect, HandleRectangle
from RWESharp.Core import CELLSIZE
from PySide6.QtCore import QPoint, QRect

class PropertiesEditor(Editor):
    def __init__(self, mod):
        super().__init__(mod)
        self.sidehandles = [Handle(self), Handle(self), Handle(self), Handle(self)]
        self.sideborderhandles = [Handle(self), Handle(self), Handle(self), Handle(self)]
        self.cornerhandles = [Handle(self), Handle(self), Handle(self), Handle(self)]
        self.cornerborderhandles = [Handle(self), Handle(self), Handle(self), Handle(self)]
        self.rect = RenderRect(self, 0, QRect())
        self.borderrect = RenderRect(self, 0, QRect())
        self.handlerect = HandleRectangle(self)

    def init_scene_items(self, viewport):
        super().init_scene_items(viewport)
        self.reposition()

    def reposition(self):
        width = self.level.level_width * CELLSIZE
        w2 = width / 2
        height = self.level.level_height * CELLSIZE
        h2 = height / 2
        rect = QRect(0, 0, width, height)
        for i, i2 in zip([QPoint(0, h2), QPoint(w2, 0), QPoint(width, h2), QPoint(w2, height)], self.sidehandles):
            i2.setPos(i)
        for i, i2 in zip([rect.topLeft(), rect.topRight(), rect.bottomRight(), rect.bottomLeft()], self.cornerhandles):
            i2.setPos(i)
        self.rect.setRect(QRect(0, 0, width, height))

        et = self.level.extra_tiles
        borderrect = QRect(et[0] * CELLSIZE, et[1] * CELLSIZE, rect.width() - (et[2] + et[0]) * CELLSIZE, rect.height() - (et[3] + et[1]) * CELLSIZE)
        self.borderrect.setRect(borderrect)
        for i, i2 in zip([QPoint(borderrect.left(), borderrect.center().y()), QPoint(borderrect.center().x(), borderrect.top()), QPoint(borderrect.right(), borderrect.center().y()), QPoint(borderrect.center().x(), borderrect.bottom())], self.sideborderhandles):
            i2.setPos(i)
        for i, i2 in zip([borderrect.topLeft(), borderrect.topRight(), borderrect.bottomRight(), borderrect.bottomLeft()], self.cornerborderhandles):
            i2.setPos(i)