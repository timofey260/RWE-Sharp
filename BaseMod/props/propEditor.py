from RWESharp.Modify import Editor
from RWESharp.Core import CELLSIZE
from BaseMod.props.propExplorer import PropExplorer
from BaseMod.props.propRenderable import PropRenderable


class PropEditor(Editor):
    def __init__(self, mod):
        super().__init__(mod)
        self.props = self.manager.props
        self.explorer = PropExplorer(self, self.manager.window)
        self.placingprop = PropRenderable(mod, self.props.find_prop("CogA1")).add_myself(self)

    def move_event(self, pos):
        super().move_event(pos)
        self.placingprop.setPos((self.viewport.viewport_to_editor_float(self.mouse_pos.toPointF()) * CELLSIZE))
