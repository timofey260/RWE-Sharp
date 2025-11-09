from copy import deepcopy

import numpy as np
from PySide6.QtCore import QPoint, QLineF, QRect

from RWESharp.Modify.HistoryElement import HistoryElement
from RWESharp2.Loaders import Effect
from RWESharp2.Utils import draw_line


def copy_effect(effect):
    return deepcopy(effect)  # i should come up with better solution at sometime


class EffectBrush(HistoryElement):
    def __init__(self, history, index, start: QPoint, size: int, remove: bool, ultra: bool):
        super().__init__(history)
        self.changes = {}
        self.start = start
        self.size = size
        self.remove = remove
        self.ultra = ultra  # kill
        self.effect = history.level.manager.effects.find_effect(self.history.level.l_effects[index]["nm"])
        self.index = index
        self.lastpos = start
        self.paintapoint(start)
        self.redraw()

    def redraw(self):
        self.history.level.manager.basemod.effecteditor.elayer.redraw()

    def add_move(self, position):
        points = []
        draw_line(self.lastpos, position, lambda p: points.append(p))
        points.pop(0)
        for point in points:
            self.paintapoint(point)
        self.lastpos = position
        self.redraw()

    def paintapoint(self, point):
        strength = 10 + (90 if self.ultra else 0)
        if self.effect.ultrablack:
            strength = 10000
        rect = QRect(point - QPoint(self.size, self.size), point + QPoint(self.size, self.size))
        for xp in range(rect.x(), rect.topRight().x()):
            for yp in range(rect.y(), rect.bottomLeft().y()):
                newpoint = QPoint(xp, yp)
                if not self.history.level.inside(newpoint):
                    continue
                cellval = int(self.history.level.l_effects[self.index, xp, yp])
                val = cellval
                dist = self.size - QLineF(newpoint, point).length()
                if dist > 0:
                    val = round(min(max(val + strength * dist * (-1 if self.remove else 1), 0), 100), 4)
                    if val == cellval:
                        continue
                    if self.changes.get(newpoint):
                        self.changes[newpoint] = [self.changes[newpoint][0], val]
                    else:
                        self.changes[newpoint] = [cellval, val]
                    self.history.level.l_effects[self.index, xp, yp] = val
                    self.history.level.manager.basemod.effecteditor.elayer.draw_pixel(newpoint, True)

    def undo_changes(self):
        for point, v in self.changes.items():
            before, _ = v
            self.history.level.l_effects[self.index, point.x(), point.y()] = before
            self.history.level.manager.basemod.effecteditor.elayer.draw_pixel(point, True)
        self.redraw()

    def redo_changes(self):
        for point, v in self.changes.items():
            _, after = v
            self.history.level.l_effects[self.index, point.x(), point.y()] = after
            self.history.level.manager.basemod.effecteditor.elayer.draw_pixel(point, True)
        self.redraw()


class EffectAdd(HistoryElement):
    def __init__(self, history, effect: Effect):
        super().__init__(history)
        self.effect = effect
        self.add_effect()

    def add_effect(self):
        self.level.l_effects.append(self.effect.todict(self.level.level_size_qsize))
        self.basemod.effectui.add_effects()
        self.basemod.effecteditor.effectindex.update_value(len(self.level.l_effects) - 1)

    def undo_changes(self):
        self.level.l_effects.pop()
        self.basemod.effectui.add_effects()

    def redo_changes(self):
        self.add_effect()


class EffectRemove(HistoryElement):
    def __init__(self, history, index):
        super().__init__(history)
        self.index = index
        self.savedeffect = self.history.level.l_effects.pop(index)
        self.remove_effect()

    def remove_effect(self):
        self.basemod.effectui.add_effects()
        self.basemod.effecteditor.effectindex.update_value(max(0, self.index - 1))

    def undo_changes(self):
        self.history.level.l_effects.insert(self.index, self.savedeffect)
        self.basemod.effectui.add_effects()
        self.basemod.effecteditor.effectindex.update_value(max(0, self.index))

    def redo_changes(self):
        self.history.level.l_effects.pop(self.index)
        self.remove_effect()


class EffectOptionChange(HistoryElement):
    def __init__(self, history, index, option, value):
        super().__init__(history)
        self.prevvalue = history.level.l_effects[index]["options"][option][2]
        self.index = index
        self.option = option
        self.value = value
        self.redo_changes()

    def undo_changes(self):
        self.level.l_effects[self.index]["options"][self.option][2] = self.prevvalue
        self.basemod.effectui.effect_settings()

    def redo_changes(self):
        self.level.l_effects[self.index]["options"][self.option][2] = self.value
        self.basemod.effectui.effect_settings()


class EffectMove(HistoryElement):
    def __init__(self, history, index, dir):
        super().__init__(history)
        self.index = index
        self.newindex = index + dir
        self.redo_changes()

    def redo_changes(self):
        self.level.l_effects.insert(self.newindex, self.level.l_effects.pop(self.index))
        self.basemod.effectui.add_effects()
        self.basemod.effecteditor.effectindex.update_value(self.newindex)

    def undo_changes(self):
        self.level.l_effects.insert(self.index, self.level.l_effects.pop(self.newindex))
        self.basemod.effectui.add_effects()
        self.basemod.effecteditor.effectindex.update_value(self.index)


class EffectDuplicate(HistoryElement):
    def __init__(self, history, index):
        super().__init__(history)
        self.index = index
        self.duplicate = deepcopy(self.level.l_effects[index])
        self.redo_changes()

    def redo_changes(self):
        self.level.l_effects.insert(self.index+1, self.duplicate)
        self.basemod.effectui.add_effects()
        self.basemod.effecteditor.effectindex.update_value(self.index+1)

    def undo_changes(self):
        self.level.l_effects.pop(self.index+1)
        self.basemod.effectui.add_effects()
        self.basemod.effecteditor.effectindex.update_value(self.index)


class LevelResizedEffects(HistoryElement):
    def __init__(self, history, newrect):
        super().__init__(history)
        self.newrect = newrect
        self.preveffects = []
        self.redo_changes()

    def undo_changes(self):
        for i, v in enumerate(self.level.l_effects.effects):
            v["mtrx"] = np.copy(self.preveffects[i])

    def redo_changes(self):
        for i, v in enumerate(self.level.l_effects.effects):
            newshape = np.zeros((self.newrect.width(), self.newrect.height()), np.float16)
            self.preveffects.append(np.copy(v["mtrx"]))
            with np.nditer(newshape, flags=['multi_index'], op_flags=['writeonly']) as it:
                for x in it:
                    if it.multi_index[0] < -self.newrect.x() or it.multi_index[1] < -self.newrect.y():
                        x[...] = 0
                        continue
                    newpoints = [it.multi_index[0] + self.newrect.x(), it.multi_index[1] + self.newrect.y()]
                    if newpoints[0] >= v["mtrx"].shape[0] or newpoints[1] >= v["mtrx"].shape[1]:
                        x[...] = 0
                        continue
                    x[...] = v["mtrx"][newpoints[0], newpoints[1]]
            v["mtrx"] = newshape
