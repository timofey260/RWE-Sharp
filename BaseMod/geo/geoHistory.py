from PySide6.QtCore import QPoint, QRect

from BaseMod.geo.geoUtils import geo_save, geo_undo
from RWESharp.Modify import HistoryElement
from RWESharp.Utils import draw_line


class GERectChange(HistoryElement):
    def __init__(self, history, rect: QRect, replace, layers: list[bool, bool, bool]):
        super().__init__(history)
        self.rect = rect
        self.replace = replace
        self.before = []
        self.layers = layers
        self.module = self.history.level.manager.basemod.geomodule
        for x in range(self.rect.x(), self.rect.width()):
            for y in range(self.rect.y(), self.rect.height()):
                for i, l in enumerate(self.layers):
                    if l:
                        block, save = geo_save(self.replace, self.history.level.geo_data(x, y, i))
                        self.before.append(save)
                        self.history.level.data["GE"][x][y][i] = block
                        t = self.module.get_layer(i)
                        t.draw_geo(x, y, True)
        self.redraw()

    def redraw(self):
        for i, l in enumerate(self.layers):
            if l:
                t = self.module.get_layer(i)
                t.redraw()

    def undo_changes(self, level):
        c = 0
        for x in range(self.rect.x(), self.rect.width()):
            for y in range(self.rect.y(), self.rect.height()):
                for i, l in enumerate(self.layers):
                    if l:
                        block = geo_undo(self.replace, self.history.level.geo_data(x, y, i), self.before[c])
                        self.history.level.data["GE"][x][y][i] = block
                        self.module.get_layer(i).draw_geo(x, y, True)
                        c += 1  # c++ almost
        self.redraw()

    def redo_changes(self, level):
        for x in range(self.rect.x(), self.rect.width()):
            for y in range(self.rect.y(), self.rect.height()):
                for i, l in enumerate(self.layers):
                    if l:
                        block, save = geo_save(self.replace, self.history.level.geo_data(x, y, i))
                        self.before.append(save)
                        self.history.level.data["GE"][x][y][i] = block
                        t = self.module.get_layer(i)
                        t.draw_geo(x, y, True)
        self.redraw()


class GEPointChange(HistoryElement):
    def __init__(self, history, start: QPoint, replace: [int, bool], layers: [bool, bool, bool]):
        super().__init__(history)
        self.positions: list[QPoint] = []
        self.before: list[int] = []
        self.replace = replace
        self.start: QPoint = start
        self.layers = layers
        self.module = self.history.level.manager.basemod.geomodule
        for i, l in enumerate(self.layers):
            if l:
                block, save = geo_save(self.replace, self.history.level.geo_data(start, i))
                self.before.append(save)
                self.history.level.data["GE"][start.x()][start.y()][i] = block
                t = self.module.get_layer(i)
                t.draw_geo(start.x(), start.y(), True)
                t.redraw()

    def add_move(self, position):
        start = self.start
        if len(self.positions) > 0:
            start = self.positions[-1]
        self.positions.append(position)

        points = []
        draw_line(start, position, lambda p: points.append(p))
        points.pop(0)
        for point in points:
            for i, l in enumerate(self.layers):
                if l:
                    block, save = geo_save(self.replace, self.history.level.geo_data(point, i))
                    self.before.append(save)
                    self.history.level.data["GE"][point.x()][point.y()][i] = block
                    self.module.get_layer(i).draw_geo(point.x(), point.y(), True)
        for i, l in enumerate(self.layers):
            if l:
                self.module.get_layer(i).redraw()

    def undo_changes(self, level):  # removing placed cells with replaced ones
        allpoints = []
        activelayers = sum(1 if i else 0 for i in self.layers)
        beforeitem = activelayers
        start = self.start

        for i, v in enumerate(self.positions):
            points = []
            draw_line(start, v, lambda p: points.append(p))
            points.pop(0)
            for point in points:
                if point in allpoints:
                    beforeitem += activelayers
                    continue
                allpoints.append(point)
                for i2, l in enumerate(self.layers):
                    if l:
                        block = geo_undo(self.replace, self.history.level.geo_data(point, i2), self.before[beforeitem])
                        self.history.level.data["GE"][point.x()][point.y()][i2] = block
                        self.module.get_layer(i2).draw_geo(point.x(), point.y(), True)
                        beforeitem += 1
            start = v
        layer = 0
        for i, l in enumerate(self.layers):
            if l:
                block = geo_undo(self.replace, self.history.level.geo_data(self.start, i),
                                 self.before[layer])
                self.history.level.data["GE"][self.start.x()][self.start.y()][i] = block
                layer += 1
                self.module.get_layer(i).draw_geo(self.start.x(), self.start.y(), True)
                self.module.get_layer(i).redraw()

    def redo_changes(self, level):  # re-adding replace cell
        start = self.start
        for i, v in enumerate(self.positions):
            points = []
            draw_line(start, v, lambda p: points.append(p))
            for point in points:
                for li, l in enumerate(self.layers):
                    if l:
                        block, save = geo_save(self.replace, self.history.level.geo_data(point, li))
                        self.before.append(save)
                        self.history.level.data["GE"][point.x()][point.y()][li] = block
                        self.module.get_layer(li).draw_geo(point.x(), point.y(), True)
            start = v
        for i, l in enumerate(self.layers):
            if l:
                self.module.get_layer(i).redraw()
