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
        self.basemod.propmodule.pop_prop()
        # self.manager.viewport.workscene.update(0, 0, 10000, 10000)  # good enough

    def redo_changes(self):
        self.basemod.propmodule.append_prop(self.prop)
