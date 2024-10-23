from RWESharp.Modify import HistoryElement
from RWESharp.Loaders import Effect
from RWESharp.Utils import draw_line
from PySide6.QtCore import QPoint, QLineF, QRect


class EffectBrush(HistoryElement):
    def __init__(self, history, index, start: QPoint, size: int, remove: bool, ultra: bool):
        super().__init__(history)
        self.changes = {}
        self.start = start
        self.size = size
        self.remove = remove
        self.ultra = ultra  # kill
        self.effect = history.level.manager.effects.find_effect(self.history.level.effects[index]["nm"])
        self.index = index
        self.lastpos = start
        self.paintapoint(start)
        self.redraw()

    def redraw(self):
        self.history.level.manager.basemod.effecteditor.layer.redraw()

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
                cellval = self.history.level["FE"]["effects"][self.index]['mtrx'][xp][yp]
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
                    self.history.level["FE"]["effects"][self.index]['mtrx'][xp][yp] = val
                    self.history.level.manager.basemod.effecteditor.layer.draw_pixel(newpoint, True)

    def undo_changes(self):
        for point, v in self.changes.items():
            before, _ = v
            self.history.level["FE"]["effects"][self.index]['mtrx'][point.x()][point.y()] = before
            self.history.level.manager.basemod.effecteditor.layer.draw_pixel(point, True)
        self.redraw()

    def redo_changes(self):
        for point, v in self.changes.items():
            _, after = v
            self.history.level["FE"]["effects"][self.index]['mtrx'][point.x()][point.y()] = after
            self.history.level.manager.basemod.effecteditor.layer.draw_pixel(point, True)
        self.redraw()


class EffectAdd(HistoryElement):
    def __init__(self, history, effect: Effect):
        super().__init__(history)
        self.effect = effect
        self.add_effect()

    def add_effect(self):
        self.history.level["FE"]["effects"].append(self.effect.todict(self.history.level.level_size_qsize))
        self.history.level.manager.basemod.effectui.add_effects()
        self.history.level.manager.basemod.effecteditor.effectindex.update_value(self.history.level.effect_len - 1)

    def undo_changes(self):
        self.history.level["FE"]["effects"].pop()
        self.history.level.manager.basemod.effectui.add_effects()

    def redo_changes(self):
        self.add_effect()


class EffectOptionChange(HistoryElement):
    def __init__(self, history, index, option, value):
        super().__init__(history)
        self.prevvalue = history.level.effects[index]["options"][option][2]
        self.index = index
        self.option = option
        self.value = value
        self.redo_changes()

    def undo_changes(self):
        self.level.effects[self.index]["options"][self.option][2] = self.prevvalue
        self.level.manager.basemod.effectui.effect_settings()

    def redo_changes(self):
        self.level.effects[self.index]["options"][self.option][2] = self.value
        self.level.manager.basemod.effectui.effect_settings()
