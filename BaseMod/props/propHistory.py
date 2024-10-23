from RWESharp.Modify import HistoryElement
from RWESharp.Loaders import Prop
from RWESharp.Core import RWELevel
from BaseMod.props.propRenderable import PropRenderable


class PropPlace(HistoryElement):
    def __init__(self, history, prop: list):
        super().__init__(history)
        self.prop = self.copyprop(prop)
        #self.index = len(history.level.props)
        self.redo_changes()

    def copyprop(self, prop):
        return [prop[0], prop[1], prop[2], prop[3].copy(), prop[4].copy()]

    def undo_changes(self):
        self.level.props.pop()
        r = self.basemod.propmodule.props.pop()
        self.basemod.propmodule.renderables.remove(r)
        r.remove_graphics()
        self.manager.viewport.workscene.update(0, 0, 10000, 10000)  # good enough
        del r
        print("womp womp")

    def redo_changes(self):
        print("added")
        self.level.data["PR"]["props"].append(self.prop)
        r = PropRenderable(self.basemod, self.prop).add_myself(self.basemod.propmodule)
        self.basemod.propmodule.props.append(r)
        r.init_graphics(self.manager.viewport)
