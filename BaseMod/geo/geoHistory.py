from PySide6.QtCore import QPoint, QRect

from BaseMod.geo.geoUtils import geo_save, geo_undo
from RWESharp.Modify import HistoryElement
from RWESharp.Utils import draw_line, draw_ellipse


nearpoints = [QPoint(-1, 0), QPoint(0, -1), QPoint(1, 0), QPoint(0, 1)]


class GEChange(HistoryElement):
    def __init__(self, history, replace, layers: [bool, bool, bool]):
        super().__init__(history)
        self.history = history
        self.replace = replace
        self.layers = layers
        self.before = []
        self.module = history.level.manager.basemod.geomodule

    def redraw(self):
        for i, l in enumerate(self.layers):
            if not l:
                continue
            self.module.get_layer(i).redraw()


class GERectChange(GEChange):
    def __init__(self, history, rect: QRect, replace, layers: [bool, bool, bool], hollow=False):
        super().__init__(history, replace, layers)
        self.rect = rect
        self.hollow = hollow
        for x in range(self.rect.x(), self.rect.x() + self.rect.width()):
            for y in range(self.rect.y(), self.rect.y() + self.rect.height()):
                for i, l in enumerate(self.layers):
                    if not l or not self.history.level.inside(QPoint(x, y)):
                        continue
                    if self.ishollow(x, y):
                        continue
                    block, save = geo_save(self.replace, self.history.level.geo_data_xy(x, y, i))
                    self.before.append(save)
                    self.history.level.data["GE"][x][y][i] = block
                    t = self.module.get_layer(i)
                    t.draw_geo(x, y, True, self.inborder(x, y))
        self.redraw()

    def inborder(self, x, y):
        return (x == self.rect.x() or y == self.rect.y() or
                x == self.rect.x() + self.rect.width() - 1 or
                y == self.rect.y() + self.rect.height() - 1)

    def ishollow(self, x, y):
        if self.hollow and self.inborder(x, y):
            return False
        return self.hollow

    def undo_changes(self, level):
        c = 0
        for x in range(self.rect.x(), self.rect.x() + self.rect.width()):
            for y in range(self.rect.y(), self.rect.y() + self.rect.height()):
                for i, l in enumerate(self.layers):
                    if not l or not self.history.level.inside(QPoint(x, y)):
                        continue
                    if self.ishollow(x, y):
                        continue
                    block = geo_undo(self.replace, self.history.level.geo_data_xy(x, y, i), self.before[c])
                    self.history.level.data["GE"][x][y][i] = block
                    self.module.get_layer(i).draw_geo(x, y, True, self.inborder(x, y))
                    c += 1  # c++ almost
        self.redraw()

    def redo_changes(self, level):
        for x in range(self.rect.x(), self.rect.x() + self.rect.width()):
            for y in range(self.rect.y(), self.rect.y() + self.rect.height()):
                for i, l in enumerate(self.layers):
                    if not l or not self.history.level.inside(QPoint(x, y)):
                        continue
                    if self.ishollow(x, y):
                        continue
                    block, save = geo_save(self.replace, self.history.level.geo_data_xy(x, y, i))
                    self.history.level.data["GE"][x][y][i] = block
                    t = self.module.get_layer(i)
                    t.draw_geo(x, y, True, self.inborder(x, y))
        self.redraw()


class GEEllipseChange(GEChange):
    def __init__(self, history, rect: QRect, replace, layers: [bool, bool, bool], hollow=False):
        super().__init__(history, replace, layers)
        self.rect = rect
        self.hollow = hollow
        self.area = [[True for _ in range(self.history.level.level_height)] for _ in
                     range(self.history.level.level_width)]
        draw_ellipse(self.rect, self.hollow, self.drawpoint)
        self.redraw()

    def drawpoint(self, pos: QPoint, saveblock=True):
        if not self.area[pos.x()][pos.y()]:
            return
        self.area[pos.x()][pos.y()] = False
        for i, l in enumerate(self.layers):
            if not l:
                continue
            block, save = geo_save(self.replace, self.history.level.geo_data(pos, i))
            if saveblock:
                self.before.append([pos, i, save])
            self.history.level.data["GE"][pos.x()][pos.y()][i] = block
            t = self.module.get_layer(i)
            t.draw_geo(pos.x(), pos.y(), True)

    def drawpointredo(self, pos):
        self.drawpoint(pos, False)

    def undo_changes(self, level):
        for i in self.before:
            point, layer, save = i
            block = geo_undo(self.replace, self.history.level.geo_data(point, layer), save)
            self.history.level.data["GE"][point.x()][point.y()][layer] = block
            self.module.get_layer(layer).draw_geo(point.x(), point.y(), True)
        self.redraw()

    def redo_changes(self, level):
        draw_ellipse(self.rect, self.hollow, self.drawpointredo)
        self.redraw()


class GEPointChange(GEChange):
    def __init__(self, history, start: QPoint, replace: [int, bool], layers: [bool, bool, bool]):
        super().__init__(history, replace, layers)
        self.positions: list[QPoint] = []
        self.start: QPoint = start
        self.before = {}
        self.paintpoint(start)
        self.redraw()

    def paintpoint(self, pos):
        for i, l in enumerate(self.layers):
            if not l:
                continue
            if not self.history.level.inside(pos):
                continue
            if self.before.get(pos, None) is not None:
                continue
            block, save = geo_save(self.replace, self.history.level.geo_data(pos, i))
            self.before[pos] = [i, save]
            self.history.level.data["GE"][pos.x()][pos.y()][i] = block
            t = self.module.get_layer(i)
            t.draw_geo(pos.x(), pos.y(), True)

    def add_move(self, position):
        start = self.start
        if len(self.positions) > 0:
            start = self.positions[-1]
        self.positions.append(position)

        points = []
        draw_line(start, position, lambda p: points.append(p))
        points.pop(0)
        for point in points:
            self.paintpoint(point)
        self.redraw()

    def undo_changes(self, level):  # removing placed cells with replaced ones
        for k, v in self.before.items():
            block = geo_undo(self.replace, self.history.level.geo_data(k, v[0]), v[1])
            self.history.level.data["GE"][k.x()][k.y()][v[0]] = block
            t = self.module.get_layer(v[0])
            t.draw_geo(k.x(), k.y(), True)
        self.redraw()

    def redo_changes(self, level):  # re-adding replace cell
        for k, v in self.before.items():
            block, save = geo_save(self.replace, self.history.level.geo_data(k, v[0]))
            self.history.level.data["GE"][k.x()][k.y()][v[0]] = block
            t = self.module.get_layer(v[0])
            t.draw_geo(k.x(), k.y(), True)
        self.redraw()


class GEBrushChange(GEChange):
    def __init__(self, history, start: QPoint, replace: [int, bool], layers: [bool, bool, bool], brushsize: int):
        super().__init__(history, replace, layers)
        self.start = start
        self.brushsize = brushsize
        self.area = [[True for _ in range(self.history.level.level_height)] for _ in
                     range(self.history.level.level_width)]
        self.lastpos = start
        self.paint_sphere(start, self.paintpoint)
        self.redraw()

    def paintpoint(self, pos: QPoint):
        if not self.module.manager.level.inside(pos) or not self.area[pos.x()][pos.y()]:
            return
        for i, l in enumerate(self.layers):
            if not l:
                continue
            self.area[pos.x()][pos.y()] = False
            block, save = geo_save(self.replace, self.history.level.geo_data(pos, i))
            self.before.append([pos, i, save])
            self.history.level.data["GE"][pos.x()][pos.y()][i] = block
            t = self.module.get_layer(i)
            t.draw_geo(pos.x(), pos.y(), True)

    def paint_sphere(self, pos, callback):
        point = QPoint(self.brushsize // 2, self.brushsize // 2)
        rect = QRect(pos - point, pos + point)
        draw_ellipse(rect, False, callback)

    def add_move(self, position):
        points = []
        draw_line(self.lastpos, position, lambda p: points.append(p))
        points.pop(0)
        for point in points:
            self.paint_sphere(point, self.paintpoint)
        self.lastpos = position
        self.redraw()

    def undo_changes(self, level):
        for i in self.before:
            point, layer, save = i
            block = geo_undo(self.replace, self.history.level.geo_data(point, layer), save)
            self.history.level.data["GE"][point.x()][point.y()][layer] = block
            self.module.get_layer(layer).draw_geo(point.x(), point.y(), True)
        self.redraw()

    def redo_changes(self, level):
        for i in self.before:
            pos, layer, _ = i
            block, save = geo_save(self.replace, self.history.level.geo_data(pos, layer))
            self.history.level.data["GE"][pos.x()][pos.y()][layer] = block
            t = self.module.get_layer(layer)
            t.draw_geo(pos.x(), pos.y(), True)
        self.redraw()


class GEFillChange(GEChange):
    def __init__(self, history, start: QPoint, replace: [int, bool], layers: [bool, bool, bool]):
        super().__init__(history, replace, layers)
        self.area = [[[True for _ in range(self.history.level.level_height)] for _ in
                     range(self.history.level.level_width)] for _ in range(3)]  # im insaneemowfdwa
        self.start: QPoint = start
        self.before = [[], [], []]
        self.replacefrom = [self.history.level.geo_data(start, 0)[0],
                            self.history.level.geo_data(start, 1)[0],
                            self.history.level.geo_data(start, 2)[0]]
        for i, l in enumerate(self.layers):
            if not l:
                continue
            self.drawpoint(start, i)
        self.dobrush()
        self.redraw()

    def dobrush(self, save=True):
        lastlen = 9999
        while True:
            for i, l in enumerate(self.layers):
                if not l:
                    continue
                for item in range(len(self.before[i])):
                    pos, _, val = self.before[i][item]
                    if not val:
                        continue
                    for p in nearpoints:
                        newpos = pos + p
                        if not self.history.level.inside(newpos) or not self.area[i][newpos.x()][newpos.y()]:
                            continue
                        self.area[i][newpos.x()][newpos.y()] = False
                        if self.history.level.geo_data(newpos, i)[0] != self.replacefrom[i]:
                            continue
                        self.drawpoint(newpos, i, save)
                    self.before[i][item][2] = False
            newlen = sum([len(i) for i in self.before])
            if newlen == lastlen:
                break
            lastlen = newlen
        self.redraw()

    def drawpoint(self, pos: QPoint, layer: int, saveblock=True):
        block, save = geo_save(self.replace, self.history.level.geo_data(pos, layer))
        if saveblock:
            self.before[layer].append([pos, save, True])
        self.history.level.data["GE"][pos.x()][pos.y()][layer] = block
        self.module.get_layer(layer).draw_geo(pos.x(), pos.y(), True)

    def undo_changes(self, level):
        for i, l in enumerate(self.before):
            for item in l:
                point, save, _ = item
                block = geo_undo(self.replace, self.history.level.geo_data(point, i), save)
                self.history.level.data["GE"][point.x()][point.y()][i] = block
                self.module.get_layer(i).draw_geo(point.x(), point.y(), True)
        self.redraw()

    def redo_changes(self, level):
        for i, l in enumerate(self.before):
            for item in l:
                point, save, _ = item
                self.drawpoint(point, i, False)
        self.redraw()
