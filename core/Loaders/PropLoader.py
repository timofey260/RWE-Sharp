from core.Loaders.Prop import Props, PropCategory, Prop
from core.Loaders.Tile import Tile, TileCategory, Tiles
from core.Loaders.TileLoader import init_solve
from core.utils import log, color_lerp
from core.info import PATH_DRIZZLE, PATH_FILES, SPRITESIZE, PATH_DRIZZLE_PROPS
from core.lingoIO import fromarr
from ui.splashuiconnector import SplashDialog
from PySide6.QtCore import QThread, Qt, QRect, QSize, QPoint
from PySide6.QtGui import QImage, QColor, QPainter, QPixmap
import math
import os
import multiprocessing


def load_prop(item: dict, colr, category, catnum, indx, img: QImage):
    # img.set_colorkey(pg.color.Color(255, 255, 255))
    err = False
    if img is None:
        img = QImage(1, 1, QImage.Format.Format_Indexed8)
    try:
        if not img.colorTable():
            img = img.convertToFormat(QImage.Format.Format_Indexed8, Qt.ImageConversionFlag.ThresholdDither)
        white = img.colorTable().index(4294967295)
        img.setColor(white, 0)
    except ValueError:
        log(f"Error loading {item['nm']}", True)
        err = True
    painter = QPainter()
    images = []
    if item.get("vars") is not None:
        item["vars"] = max(item["vars"], 1)

    ws, hs = img.width(), img.height()
    sz = [ws, hs]
    if item.get("pxlSize") is not None:
        w, h = fromarr(item["pxlSize"], "point")
    else:
        w, h = ws, hs
        if item.get("vars") is not None:
            w = round(ws / item["vars"])
        if item.get("repeatL") is not None:
            repeatl = item.get("repeatL")
            h = math.floor((hs / len(repeatl)))
            if item.get("sz") is not None:
                sz = fromarr(item["sz"], "point")
                w = min(sz[0] * SPRITESIZE, ws)
                h = sz[1] * SPRITESIZE

            cons = 0.4
            wh = QColor("#ffffff")
            gr = QColor("#dddddd")
            bl = QColor("#000000")

            vars = item.get("vars", 1)

            for varindx in range(vars):
                curcol = gr

                for iindex, _ in enumerate(repeatl):
                    # print(img, item["nm"], varindx * w, h * (len(repeatl) - 1), w, h)
                    curcol = color_lerp(curcol, bl, cons)
                    rect = QRect(varindx * w, (len(repeatl) - 1 - iindex) * h, w, h + 1)
                    # rect = rect.clip(QRect(0, 0, ws, hs))
                    try:
                        ss = img.copy(rect)
                    except ValueError:
                        continue
                    painter.begin(img)

                    if item["colorTreatment"] == "bevel":
                        pass
                        # pxl = pg.PixelArray(ss)
                        # pxl.replace(bl, curcol)
                        # ss = pxl.make_surface()
                    #ss.set_colorkey(wh)
                    painter.drawImage(0, h * (len(repeatl) - 1), ss)
                    # img.blit(ss, [0, h * (len(repeatl) - 1)])
                    painter.end()

    if item.get("vars") is not None:
        for iindex in range(item["vars"]):
            images.append(img.copy(iindex * w, 0, w, h))
    else:
        images.append(img.copy(0, hs - h if item.get("colorTreatment", "") == "bevel" else 0, w, h))
    prop = Prop(item.get("nm", "NoName"), item.get("tp"), item.get("repeatL"), "todo",
                [QPixmap.fromImage(i) for i in images], item.get("colorTreatment", "standard"),
                colr, QSize(*sz), QPoint(catnum, indx), item.get("tags", []), QPixmap.fromImage(images[0]), err,
                category, item.get("notes", []), item.get("layerExceptions", []))
    return prop


class PropPackLoader(QThread):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.data = data
        self.cats = []
        self.progress = 0
        self.errors = 0
        self.amount = sum(list(map(lambda x: len(x["items"]), self.data)))
        self.finished.connect(self.deleteLater)

    def run(self):
        for catnum, catitem in enumerate(self.data):
            proplist = []
            propcat = PropCategory(catitem["name"], catitem["color"], proplist)

            items = catitem["items"]
            colr: QColor = catitem["color"]
            # self.data[catnum]["items"] = []
            for indx, item in enumerate(items):
                # printmessage(f"Loading tile {item['nm']}...", f"({tilenum}/{length})")
                # window.ui.progressBar.setValue(int(tilenum / length * 100))
                image = QImage(os.path.join(PATH_DRIZZLE_PROPS, f"{item['nm']}.png"))
                tile = load_prop(item, colr, propcat, catnum, indx, image)
                self.progress += 1
                if tile is None:
                    self.errors += 1
                    continue
                # tilenum += 1
                # self.data[catnum]["items"].append(tile)
                proplist.append(tile)
                if tile.err:
                    self.errors += 1
            self.cats.append(propcat)
        # self.finished.emit()


def load_props(tiles: Tiles, window: SplashDialog):
    log("Loading Props")
    solved_copy = init_solve(os.path.join(PATH_DRIZZLE_PROPS, "Init.txt"))
    length = sum(list(map(lambda x: len(x["items"]), solved_copy.data)))
    additional = init_solve(os.path.join(PATH_FILES, "additionprops.txt"))

    for i in additional.data:
        solved_copy.append(i)

    log(f"Loading {length} Props")

    threadsnum = min(1, multiprocessing.cpu_count() - 1)
    catsnum = len(solved_copy.data)
    data_per_thread = catsnum // threadsnum
    unused = catsnum - data_per_thread * threadsnum

    workers: list[PropPackLoader] = []
    for i in range(threadsnum):
        workers.append(PropPackLoader(solved_copy.data[i * data_per_thread:i * data_per_thread + data_per_thread]))
    if unused > 0:
        workers.append(PropPackLoader(solved_copy.data[-unused:]))
    # progress = Tileprogress(window, workers)
    for i in workers:
        i.start()
    # progress.start()
    for i in workers:
        i.wait()
    log("finished")

