from RWESharp.Modify import HistoryElement
from RWESharp.Loaders import Prop
from RWESharp.Core import RWELevel
from BaseMod.props.propUtils import copyprop


class PropPlace(HistoryElement):
    def __init__(self, history, prop: list):
        super().__init__(history)
        self.prop = copyprop(prop)
        self.module = history.level.viewport.modulenames["props"]
        #self.index = len(history.level.props)
        self.redo_changes()

    def undo_changes(self):
        self.module.pop_prop()
        # self.manager.viewport.workscene.update(0, 0, 10000, 10000)  # good enough

    def redo_changes(self):
        self.module.append_prop(self.prop)


class PropRemove(HistoryElement):
    def __init__(self, history, index):
        super().__init__(history)
        self.prop = copyprop(history.level.l_props[index])
        self.module = history.level.viewport.modulenames["props"]
        self.index = index
        self.redo_changes()

    def redo_changes(self):
        self.module.remove_prop(self.index)

    def undo_changes(self):
        self.module.add_prop(self.index, copyprop(self.prop))
