from RWESharp.Modify import Editor
from RWESharp.Core import CELLSIZE
from BaseMod.props.propExplorer import PropExplorer
from BaseMod.props.propRenderable import PropRenderable

from PySide6.QtCore import QPointF


class PropEditor(Editor):
    def __init__(self, mod):
        super().__init__(mod)
        self.props = self.manager.props
        self.explorer = PropExplorer(self, self.manager.window)
        self.prop = self.props.find_prop("CogA1")
        self.placingprop = PropRenderable(mod, self.prop).add_myself(self)

    def move_event(self, pos):
        super().move_event(pos)
        w, h, = self.prop.size.width() / 2, self.prop.size.height() / 2
        self.placingprop.transform = [QPointF(-w, -h), QPointF(w, -h), QPointF(w, h), QPointF(-w, h)]
        self.placingprop.setPos((self.viewport.viewport_to_editor_float(self.mouse_pos.toPointF()) * CELLSIZE))

    @property
    def transform(self):
        return self.placingprop.transform

    @transform.setter
    def transform(self, value):
        self.placingprop.transform = value
