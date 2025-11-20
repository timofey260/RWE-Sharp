from RWESharp.Loaders.Prop import Props, PropCategory, Prop
from RWESharp.Loaders.Tile import Tile, TileCategory, Tiles
from RWESharp.Loaders.TileLoader import init_solve, colortable
from RWESharp.Configurable.PythonTypes import IntConfigurable
from RWESharp.utils import log, color_lerp
from RWESharp.info import PATH_FILES, PATH_DRIZZLE_PROPS, PATH_FILES_CACHE, CELLSIZE, PATH_DRIZZLE_CAST
from RWESharp.Core.lingoIO import fromarr, tojson
from RWESharp.ui.splashuiconnector import SplashDialog
from PySide6.QtCore import QThread, Qt, QSize, QPoint
from PySide6.QtGui import QImage, QColor, QPainter, QPixmap
import os
import multiprocessing


def load_prop(item: dict, colr, category, catnum, indx):
    # img.set_colorkey(pg.color.Color(255, 255, 255))

    vars = max(item.get("vars", 1), 1)
    repeatl = item.get("repeatL", [1])
    path = item["nm"]
    renderstep = 15
    err = False
    if all(os.path.exists(os.path.join(PATH_FILES_CACHE, f"{path}_{i}.png")) for i in range(vars)):
        images = []
        for i in range(vars):
            images.append(QImage(os.path.join(PATH_FILES_CACHE, f"{path}_{i}.png")))
        return Prop(item, item.get("nm", "NoName"), item.get("tp"), repeatl, "None",
                    images, item.get("colorTreatment", "standard"), vars,
                    colr, QPoint(catnum, indx), item.get("tags", []), err,
                    category, item.get("notes", []), images[0].size(), item.get("layerExceptions", []),
                    rope=item.get("tp") == "rope", long=item.get("tp") == "long")
    standard = item.get("tp", "standard") in ["standard", "variedStandard"]
    soft = item.get("tp", "soft") in ["soft", "variedSoft"]
    rope_long = item.get("tp", "standard") in ["rope", "long"]

    imagepath = os.path.join(PATH_DRIZZLE_PROPS, f"{path}.png")
    if not os.path.exists(imagepath) and rope_long:
        for i in os.listdir(PATH_DRIZZLE_PROPS):
            if i.lower() == f"{path}.png".lower():
                imagepath = os.path.join(PATH_DRIZZLE_PROPS, i)
                break
    if not os.path.exists(imagepath) and rope_long:
        for i in os.listdir(PATH_DRIZZLE_CAST):
            if i.endswith(f"{path}.png"):
                imagepath = os.path.join(PATH_DRIZZLE_CAST, i)
                break
    if not os.path.exists(imagepath):
        imagepath = os.path.join(PATH_FILES, "images", "notfound.png")
    img = QImage(imagepath)

    ws, hs = img.width(), img.height()
    w, h = ws, hs
    if item.get("pxlSize") is not None:
        w, h = fromarr(item["pxlSize"], "point")
    elif item.get("sz") is not None:
        w, h = fromarr(item["sz"], "point")
        w *= CELLSIZE
        h *= CELLSIZE

    images = []

    if img is None:
        img = QImage(1, 1, QImage.Format.Format_Indexed8)
    if standard:
        try:
            if not img.colorTable():
                img = img.convertToFormat(QImage.Format.Format_Indexed8,
                                          [4294901760, 4278255360, 4278190335, 4278190080, 4294967295, 0], Qt.ImageConversionFlag.ThresholdDither)
            img.setColor(img.colorTable().index(4294967295), 0)
            # img.setColor(img.colorTable().index(4278190080), 0)
        except ValueError:
            log(f"Error loading {item['nm']}", True)
            err = True

    if rope_long:
        mask = img.createMaskFromColor(QColor(255, 255, 255, 255).rgba(), Qt.MaskMode.MaskOutColor)
        mask.setColorTable([4294967295, 0])
        newimg = QPixmap(img.size())
        newimg.fill(QColor(0, 0, 0, 0))
        painter = QPainter(newimg)
        painter.drawImage(0, 0, img)
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_DestinationOut)
        painter.drawImage(0, 0, mask)
        painter.end()
    elif not standard or soft:
        mask = img.createMaskFromColor(QColor(255, 255, 255, 255).rgba(), Qt.MaskMode.MaskOutColor)
        mask.setColorTable([4294967295, 0])
        mask2 = img.createMaskFromColor(QColor(0, 0, 0, 0).rgba(), Qt.MaskMode.MaskOutColor)
        mask2.setColorTable([4294967295, 0])
        mask3 = img.createMaskFromColor(QColor(0, 0, 0, 255).rgba(), Qt.MaskMode.MaskOutColor)
        mask3.setColorTable([4294967295, 0])
        # mask.save(os.path.join(PATH_FILES_CACHE, f"{path}_test_0.png"))
        # img.save(os.path.join(PATH_FILES_CACHE, f"{path}_test_1.png"))
        newimg = QPixmap(img.size())
        newimg.fill(QColor(0, 0, 0, 0))
        painter = QPainter(newimg)
        painter.drawImage(0, 0, img)
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_DestinationOut)
        painter.drawImage(0, 0, mask)
        painter.drawImage(0, 0, mask2)
        painter.drawImage(0, 0, mask3)
        painter.end()
        # if soft:
        #     newimg = newimg.copy(0, 0, ws, h)
        #newimg.save(os.path.join(PATH_FILES_CACHE, f"{path}_0.png"))
    else:
        newimg = QPixmap(ws, h)
        newimg.fill(QColor(0, 0, 0, 0))
        painter = QPainter(newimg)

        wh = QColor("#ffffff")
        gr = QColor("#dddddd")
        bl = QColor("#000000")
        cons = 0.4
        curcol = gr

        for i, v in zip(range(len(repeatl) - 1, -1, -1), reversed(repeatl)):
            if item.get("colorTreatment", "normal") == "bevel":
                curcol = color_lerp(curcol, bl, cons)  # todo
                newi = img.copy(0, h * i, ws, h).createMaskFromColor(QColor(0, 0, 0).rgba(), Qt.MaskMode.MaskInColor)
                newi.setColorTable([0, QColor(0, 255, 0).rgba()])
                painter.drawImage(0, 0, newi)
            else:
                painter.drawImage(0, 0, img.copy(0, h * i, ws, h))
            painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceAtop)
            painter.fillRect(0, 0, ws, h, QColor(0, 0, 0, renderstep))
            painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceOver)
        painter.end()
        img3 = QImage(newimg.width(), newimg.height(), QImage.Format.Format_RGBA64)
        imagepix = newimg.toImage()
        # newimg.save(os.path.join(PATH_FILES_CACHE, f"test.png"))
        # print(ws, hs, w, h)

        for xp in range(img3.width()):
            for yp in range(img3.height()):
                pc = imagepix.pixelColor(xp, yp)
                if pc.alpha() == 0 or pc.rgb() == QColor(0, 0, 0).rgb():
                    img3.setPixelColor(xp, yp, QColor(0, 0, 0, 0))
                    continue
                if pc.red() > pc.green() == pc.blue():
                    pc = QColor(91 + (255 - pc.red()) // renderstep, 0, 0, 255)
                elif pc.green() > pc.red() == pc.blue():
                    pc = QColor(121 + (255 - pc.green()) // renderstep, 0, 0, 255)
                elif pc.blue() > pc.green() == pc.red():
                    pc = QColor(151 + (255 - pc.blue()) // renderstep, 0, 0, 255)
                img3.setPixelColor(xp, yp, pc)
        #img3.save(os.path.join(PATH_FILES_CACHE, f"test2.png"))
        newimg = img3.convertToFormat(QImage.Format.Format_Indexed8, colortable[0],
                                    Qt.ImageConversionFlag.ThresholdDither)
        newimg = QPixmap.fromImage(newimg)

    for i in range(vars):
        images.append(newimg.toImage().copy(w * i, 0, w, h))
        images[-1].save(os.path.join(PATH_FILES_CACHE, f"{path}_{i}.png"))

    return Prop(item, item.get("nm", "NoName"), item.get("tp"), repeatl, "None",
                images, item.get("colorTreatment", "standard"), vars,
                colr, QPoint(catnum, indx), item.get("tags", []), err,
                category, item.get("notes", []), QSize(w, h), item.get("layerExceptions", []),
                rope=item.get("tp") == "rope", long = item.get("tp") == "long")


def tile2prop(tile: Tile, cat, category):
    err = tile.err
    if tile.type != "VoxelStruct" or "notProp" in tile.tags:
        err = True
    return Prop({"depth": 10 * (int(tile.cols1 != []) + 1)}, tile.name, "standard", tile.repeatl, tile.description,
                [tile.image3], "standard", 1,
                tile.color, cat, [*tile.tags, "tile"], err, category, ["Tile as Prop"],
                (tile.size + QSize(tile.bfTiles, tile.bfTiles) * 2) * CELLSIZE)


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
                tile = load_prop(item, colr, propcat, catnum, indx)
                self.progress += 1
                if tile is None:
                    self.errors += 1
                    continue
                proplist.append(tile)
                if tile.err:
                    self.errors += 1
            self.cats.append(propcat)
        # self.finished.emit()


class Tile2PropLoader(QThread):
    def __init__(self, categories: list[TileCategory], parent=None):
        super().__init__(parent)
        self.categories = categories
        self.cats = []
        self.progress = 0
        self.errors = 0
        self.amount = sum(list(map(lambda x: len(x.tiles), self.categories)))
        self.finished.connect(self.deleteLater)

    def run(self):
        for catnum, catitem in enumerate(self.categories):
            proplist = []
            propcat = PropCategory(catitem.name, catitem.color, proplist)

            items = catitem.tiles
            colr: QColor = catitem.color
            # self.data[catnum]["items"] = []
            if catitem.name == "materials":
                self.progress += len(items)
                continue
            for indx, item in enumerate(items):
                prop = tile2prop(item, QPoint(catnum, indx), propcat)
                self.progress += 1
                if prop is None:
                    self.errors += 1
                    continue
                proplist.append(prop)
                if prop.err:
                    self.errors += 1
            self.cats.append(propcat)
        # self.finished.emit()


class PropProgress(QThread):
    def __init__(self, window, workers):
        super().__init__()
        window.printmessage("Loading Props...")
        self.workers = workers
        self.window = window
        self.overall = sum(list(map(lambda x: x.amount, self.workers)))
        self.loaded = IntConfigurable(None, "da", 0)
        self.loaded.valueChanged.connect(self.window.ui.progressBar.setValue)
        self.finished.connect(self.deleteLater)

    def run(self):
        loaded = sum(list(map(lambda x: x.progress, self.workers)))
        while loaded != self.overall:
            self.msleep(100)
            loaded = sum(list(map(lambda x: x.progress, self.workers)))
            self.window.ui.label_2.setText(f"({loaded}/{self.overall})")
            self.loaded.update_value(loaded / self.overall * 100)


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
    progress = PropProgress(window, workers)
    for i in workers:
        i.start()
    progress.start()
    for i in workers:
        i.wait()
    progress.wait()
    categories = []
    for i in workers:
        categories = [*categories, *i.cats]

    log(f"Loading Tiles as props")
    # yeah me lazy go brrrr
    catsnum = len(tiles.categories_nocustom)
    data_per_thread = catsnum // threadsnum
    unused = catsnum - data_per_thread * threadsnum

    workers: list[Tile2PropLoader] = []
    for i in range(threadsnum):
        workers.append(Tile2PropLoader(tiles.categories_nocustom[i * data_per_thread:i * data_per_thread + data_per_thread]))
    if unused > 0:
        workers.append(Tile2PropLoader(tiles.categories_nocustom[-unused:]))
    progress = PropProgress(window, workers)
    for i in workers:
        i.start()
    progress.start()
    for i in workers:
        i.wait()
    progress.wait()
    for i in workers:
        categories = [*categories, *i.cats]
    window.printmessage("All Props loaded!")
    log("Finished Loading")
    return Props(categories)


def getcolors():
    solved = open(os.path.join(PATH_DRIZZLE_PROPS, "propColors.txt")).readlines()
    cols = []
    for line in solved:
        if line[0] != '[':
            continue
        l = tojson(line)
        l[1] = fromarr(l[1], "color")
        cols.append(l)
    return cols
