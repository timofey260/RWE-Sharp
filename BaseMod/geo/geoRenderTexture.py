import os.path

from PySide6.QtCore import QRect, QPoint
from PySide6.QtGui import QPixmap, QColor, QPainter

from RWESharp.Core import PATH_FILES_IMAGES, CONSTS, CELLSIZE
from RWESharp.Renderable import RenderLevelImage
import numpy as np

checkpoints = [QPoint(-1, -1), QPoint(0, -1), QPoint(1, -1),
               QPoint(-1, 0), QPoint(1, 0),
               QPoint(-1, 1), QPoint(0, 1), QPoint(1, 1)]

checkpoints2 = [QPoint(0, -1),
               QPoint(-1, 0), QPoint(1, 0),
               QPoint(0, 1)]


class GeoRenderLevelImage(RenderLevelImage):
    def __init__(self, module, depth, geolayer):
        super().__init__(module, depth)
        self.module = module
        self.geolayer = geolayer
        # transform = QTransform()
        # transform.rotate(10)
        # transform.shear(1, 0)
        # transform.squareToQuad(QPolygonF([QPoint(0, 0), QPoint(100, 0), QPoint(50, 50), QPoint(0, 75)]))
        # self.painter.setTransform(transform.quadToQuad(QPolygonF([QPointF(0, 0), QPointF(self.image.width(), 0), QPointF(self.image.width(), self.image.height()), QPointF(0, self.image.height())]),
        #                                                QPolygonF([QPointF(20, 20), QPointF(100, 0), QPointF(1000, 1000), QPointF(0, 100)])))

        if os.path.exists(os.path.join(PATH_FILES_IMAGES, CONSTS.get("geo_image_config", {}).get("image"))):
            self.geo_texture = QPixmap(os.path.join(PATH_FILES_IMAGES, CONSTS.get("geo_image_config", {}).get("image")))
        else:
            self.geo_texture = QPixmap(os.path.join(PATH_FILES_IMAGES, "notfound.png"))
        self.geo_texture_colored = self.geo_texture.copy()
        cp = QPainter(self.geo_texture_colored)  # it's color painter i swear
        cp.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceAtop)
        op = 50
        cp.fillRect(self.geo_texture.rect(), [0, QColor(0, 255, 0, op), QColor(255, 0, 0, op)][self.geolayer])
        #self.painter.drawPixmap(QRect(0, 0, 20, 20), self.geo_texture, QRect(100, 100, 100, 100))
        self.binfo: dict = CONSTS.get("geo_image_config", {}).get("blocksinfo", {})
        self.sinfo: dict = CONSTS.get("geo_image_config", {}).get("stackablesinfo", {})
        self._sz = CONSTS.get("geo_image_config", {}).get("itemsize", 100)
        # self.draw_layer()

    def draw_layer(self):
        self.image.fill(QColor(0, 0, 0, 0))
        for xp, x in enumerate(self.viewport.level["GE"]):
            for yp, y in enumerate(x):
                self.draw_geo(xp, yp, updatearound=False)
        self.redraw()

    def level_resized(self):
        super().level_resized()
        self.image.fill(QColor(0, 0, 0, 0))
        self.draw_layer()

    def redraw_beams(self):
        for xp, x in enumerate(self.viewport.level["GE"]):
            for yp, y in enumerate(x):
                if 1 in y[self.geolayer][1] or 2 in y[self.geolayer][1]:
                    self.draw_geo(xp, yp, True, False)
        self.redraw()

    def redraw_misc(self):
        for xp, x in enumerate(self.viewport.level["GE"]):
            for yp, y in enumerate(x):
                self.draw_geo(xp, yp, True, False)
        self.redraw()

    def redraw_pipes(self):
        for xp, x in enumerate(self.viewport.level["GE"]):
            for yp, y in enumerate(x):
                if 5 in y[self.geolayer][1] or 6 in y[self.geolayer][1] or 7 in y[self.geolayer][1] or 19 in \
                        y[self.geolayer][1]:
                    self.draw_geo(xp, yp, True, False)
        self.redraw()

    @property
    def drawmap(self):
        return self.geo_texture if self.module.ui.drawoption.value == 0 else self.geo_texture_colored

    def draw_geo(self, x: int, y: int, clear: bool = False, updatearound=True):
        # cell: int = self.viewport.level["GE"][x][y][self.geolayer][0]
        cell: np.uint8 = self.viewport.level.l_geo.blocks[x, y, self.geolayer]
        # stackables: list[int] = self.viewport.level["GE"][x][y][self.geolayer][1]
        stackables: np.uint16 = self.viewport.level.l_geo.stack[x, y, self.geolayer]
        # hiding stuff we don't need
        if not self.module.ui.drawlbeams.value:
            stackables &= 0b1111111111111100  # removes beams
        if not self.module.ui.drawlpipes.value:
            stackables &= 0b1110111100011111  # removes pipes
        if not self.module.ui.drawlmisc.value:
            stackables &= 0b1110111100011100  # removes misc
        pos = self.binfo.get(str(cell), [0, 0])
        cellpos = QRect(pos[0] * self._sz, pos[1] * self._sz, self._sz, self._sz)
        placepos = QRect(x * CELLSIZE, y * CELLSIZE, 20, 20)
        drawmap2 = self.module.mod.geoeditor.geo_preload
        point = QPoint(x, y)
        if clear:
            self.painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_Clear)
            self.painter.fillRect(placepos, QColor(0, 0, 0, 0))
            self.painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceOver)
        if updatearound:
            for i in checkpoints:
                p = point + i
                if (self.viewport.level.inside(p) and
                        (4 in self.viewport.level.geo_data(p, self.geolayer)[1] or
                         11 in self.viewport.level.geo_data(p, self.geolayer)[1])):
                    self.draw_geo(p.x(), p.y(), True, False)
        if cell != 7:
            self.painter.drawPixmap(placepos, self.drawmap, cellpos)

        if stackables & 0b10000 > 0:
            self.draw_pipe(point)  # yeah this one is a mess
        elif stackables & 0b100 > 0:
            self.draw_crack(point)
        # spos = self.getinfo(s)
        # self.painter.drawPixmap(placepos, self.drawmap, self.stackpos(spos))
        if stackables & 0b11111111 > 0:
            self.painter.drawPixmap(placepos, drawmap2, QRect((stackables & 0b11111111) * self._sz, 0, self._sz, self._sz))
        if (stackables >> 8) & 0b11111111 > 0:
            self.painter.drawPixmap(placepos, drawmap2, QRect(((stackables >> 8) & 0b11111111) * self._sz, self._sz, self._sz, self._sz))

    def draw_pipe(self, point):
        placepos = QRect(point.x() * CELLSIZE, point.y() * CELLSIZE, 20, 20)
        if not self.viewport.level.inside_border(point):
            self.painter.drawPixmap(placepos, self.drawmap, self.stackpos(self.getinfo2(4, 0)))
            return
        counter = 0
        for i in checkpoints:
            if not self.viewport.level.inside(point + i):
                counter += 1
            elif self.viewport.level.geo_data(point + i, self.geolayer)[0] == 1:
                counter += 1
        if counter != 7:
            self.painter.drawPixmap(placepos, self.drawmap, self.stackpos(self.getinfo2(4, 0)))
            return
        spos = self.getinfo2(4, 0)
        if self.insidedouble(point, QPoint(0, 1)):
            if self.checkrot(point, QPoint(0, -1)):
                spos = self.getinfo2(4, 1)
            elif self.checkrot(point, QPoint(0, 1)):
                spos = self.getinfo2(4, 4)
        if self.insidedouble(point, QPoint(1, 0)):
            if self.checkrot(point, QPoint(-1, 0)):
                spos = self.getinfo2(4, 2)
            elif self.checkrot(point, QPoint(1, 0)):
                spos = self.getinfo2(4, 3)
        self.painter.drawPixmap(placepos, self.drawmap, self.stackpos(spos))

    def draw_crack(self, point):
        placepos = QRect(point.x() * CELLSIZE, point.y() * CELLSIZE, 20, 20)
        counter = 0
        for i in checkpoints2:
            if not self.viewport.level.inside(point + i):
                counter += 1
            elif 11 in self.viewport.level.geo_data(point + i, self.geolayer)[1]:
                counter += 1
        if counter >= 3 or counter == 0:
            spos = self.getinfo2(11, 0)
            self.painter.drawPixmap(placepos, self.drawmap, self.stackpos(spos))
            return
        h = False
        v = False
        if self.checkcrack(point, QPoint(-1, 0)) or self.checkcrack(point, QPoint(1, 0)):
            h = True
        if self.checkcrack(point, QPoint(0, -1)) or self.checkcrack(point, QPoint(0, 1)):
            v = True
        spos = self.getinfo2(11, 0)
        if h and not v:
            spos = self.getinfo2(11, 1)
        elif v and not h:
            spos = self.getinfo2(11, 2)
        self.painter.drawPixmap(placepos, self.drawmap, self.stackpos(spos))

    def getinfo(self, s):
        return self.sinfo.get(str(s), [0, 0])

    def getinfo2(self, s, t):
        return self.sinfo.get(str(s), [[0, 0]])[t]

    def stackpos(self, spos):
        return QRect(spos[0] * self._sz, spos[1] * self._sz, self._sz, self._sz)

    def insidedouble(self, point: QPoint, offset: QPoint) -> bool:
        return self.viewport.level.inside(point + offset) and self.viewport.level.inside(point - offset)

    def checkrot(self, point: QPoint, offset: QPoint) -> bool:
        return self.is_path(self.viewport.level.geo_data(point + offset, self.geolayer)[1]) and \
                            self.viewport.level.geo_data(point - offset, self.geolayer)[0] != 1

    def checkcrack(self, point: QPoint, offset: QPoint) -> bool:
        return self.viewport.level.inside(point + offset) and 11 in \
                self.viewport.level.geo_data(point + offset, self.geolayer)[1]

    def is_path(self, array) -> bool:
        for i in [5, 6, 7, 21]:
            if i in array:
                return True
        return False
