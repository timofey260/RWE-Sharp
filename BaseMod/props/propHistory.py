from BaseMod.LevelParts import PropLevelPart
from RWS.Modify import HistoryElement
from RWS.Core import CELLSIZE


class PropPlace(HistoryElement):
    def __init__(self, history, prop: PropLevelPart.PlacedProp):
        super().__init__(history)
        self.prop = prop.copy()
        self.module = history.level.viewport.modulenames["props"]
        #self.index = len(history.level.props)
        self.redo_changes()

    def undo_changes(self):
        self.module.pop_prop()
        # self.manager.viewport.workscene.update(0, 0, 10000, 10000)  # good enough

    def redo_changes(self):
        self.module.append_prop(self.prop)


class PropRemove(HistoryElement):
    def __init__(self, history, index: int):
        super().__init__(history)
        self.prop = history.level.l_props[index].copy()
        self.module = history.level.viewport.modulenames["props"]
        self.index = index
        self.redo_changes()

    def redo_changes(self):
        self.module.remove_prop(self.index)

    def undo_changes(self):
        self.module.add_prop(self.index, self.prop.copy())


class PropsMove(HistoryElement):
    def __init__(self, history, indexes: list[int], offset):
        super().__init__(history)
        self.indexes = indexes
        self.offset = offset
        self.module = self.level.viewport.modulenames["props"]
        self.redo_changes()

    def undo_changes(self):
        for i in self.indexes:
            prop = self.level.l_props.props[i]
            self.module.remove_render_prop(i)
            for q in range(4):
                prop.quad[q] -= self.offset
            self.module.render_prop(i)

    def redo_changes(self):
        for i in self.indexes:
            prop = self.level.l_props.props[i]
            self.module.remove_render_prop(i)
            for q in range(4):
                prop.quad[q] += self.offset
            self.module.render_prop(i)


class LevelResizedProps(PropsMove):
    def __init__(self, history, changerect):
        super().__init__(history, [i for i in range(len(history.level.l_props.props))], -changerect.topLeft() * CELLSIZE)


