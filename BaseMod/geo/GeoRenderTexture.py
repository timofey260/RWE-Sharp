import os.path
from core.Modify.RenderTexture import RenderTexture
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtCore import QRect
from core.info import PATH_FILES_IMAGES, CONSTS, CELLSIZE

class GeoRenderTexture(RenderTexture):
    def __init__(self, manager, layer):
        super().__init__(manager)
        self.layer = layer

        if os.path.exists(os.path.join(PATH_FILES_IMAGES, CONSTS.get("geo_image_config", {}).get("image"))):
            self.geo_texture = QPixmap(os.path.join(PATH_FILES_IMAGES, CONSTS.get("geo_image_config", {}).get("image")))
        else:
            self.geo_texture = QPixmap(os.path.join(PATH_FILES_IMAGES, "notfound.png"))
        #self.painter.drawPixmap(QRect(0, 0, 20, 20), self.geo_texture, QRect(100, 100, 100, 100))
        self.binfo: dict = CONSTS.get("geo_image_config", {}).get("blocksinfo", {})
        self.sinfo: dict = CONSTS.get("geo_image_config", {}).get("stackablesinfo", {})
        self.draw_layer()


    def draw_layer(self):
        self.image.fill(QColor(0, 0, 0, 0))
        sz = CONSTS.get("geo_image_config", {}).get("itemsize", 100)
        for xp, x in enumerate(self.manager.level["GE"]):
            for yp, y in enumerate(self.manager.level["GE"][xp]):
                cell = y[self.layer][0]
                stackables = y[self.layer][1]
                pos = self.binfo.get(str(cell), [0, 0])
                cellpos = QRect(pos[0] * sz, pos[1] * sz, sz, sz)
                placepos = QRect(xp * CELLSIZE, yp * CELLSIZE, 20, 20)
                self.painter.drawPixmap(placepos, self.geo_texture, cellpos)

                for s in stackables:
                    spos = self.sinfo.get(str(s), [0, 0])
                    stackpos = QRect(spos[0] * sz, spos[1] * sz, sz, sz)
                    self.painter.drawPixmap(placepos, self.geo_texture, stackpos)

