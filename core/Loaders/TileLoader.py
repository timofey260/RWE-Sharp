import multiprocessing
from core.ItemData import ItemData
from core.lingoIO import tojson, fromarr
from core.info import PATH
from core.Loaders.Tile import Tile, TileCategory, Tiles
from ui.splashuiconnector import SplashDialog
from PySide6.QtGui import QColor, QImage, QPainter, QPixmap, QPen
from PySide6.QtCore import QRect, Qt, QThread, QPoint, QSize, QLine
import json
import os
from core.info import PATH_DRIZZLE, CELLSIZE, SPRITESIZE, CONSTS, PATH_MAT_PREVIEWS, PATH_FILES_CACHE
from core.utils import log, insensitive_path
from core.configTypes.BaseTypes import IntConfigurable

colortable = [[], [], []]
for l in range(3):
    for i in range(90):
        colortable[l].append(QColor(max(0, 90 + i - l * 30), 0, 0, 255).rgba())
            # colortable[l].append(QColor(91 + 30 * i + i2 - 10 * l, 0, 0, 255).rgba())
colortable[0].append(QColor(0, 0, 0, 0).rgba())
colortable[1].append(QColor(0, 0, 0, 0).rgba())
colortable[2].append(QColor(0, 0, 0, 0).rgba())


def return_tile_pixmap(tile: Tile, option: int, layer: int, layercolortable) -> QPixmap:
    if option == 0:
        return tile.image
    elif option == 1:
        return tile.image2
    elif option == 3:
        tile.image3.setColorTable(colortable[layer])
        return QPixmap.fromImage(tile.image3)
    elif option == 2:
        tile.image3.setColorTable(color_colortable(tile.color))
        return QPixmap.fromImage(tile.image3)
    else:
        col = option - 4
        tile.image3.setColorTable(layercolortable[col][layer])
        return QPixmap.fromImage(tile.image3)


def collisions_image(tile: Tile, l1color: QColor = QColor(255, 0, 0, 255), l2color: QColor = QColor(0, 0, 255, 255)) -> QPixmap:
    tile_image = QPixmap((tile.size + QSize(tile.bfTiles * 2, tile.bfTiles * 2)) * CELLSIZE)
    tile_image.fill(QColor(0, 0, 0, 0))
    painter = QPainter(tile_image)

    def drawlayer(specs):
        nonlocal painter
        for i, v in enumerate(specs):
            pos = QPoint(i // tile.size.height(), i % tile.size.height()) * CELLSIZE
            endpos = pos + QPoint(CELLSIZE, CELLSIZE)
            match v:
                case 1:
                    painter.drawRect(QRect(pos, QSize(CELLSIZE - 2, CELLSIZE - 2)))
                case 0:
                    c = CELLSIZE / 2
                    painter.drawEllipse(pos + QPoint(c, c), c, c)
                case 2:
                    pos2 = QPoint(pos.x(), endpos.y())
                    painter.drawLines([QLine(pos, pos2), QLine(pos2, endpos), QLine(endpos, pos)])
                case 3:
                    pos2 = QPoint(pos.x(), endpos.y())
                    pos3 = QPoint(endpos.x(), pos.y())
                    painter.drawLines([QLine(pos2, endpos), QLine(endpos, pos3), QLine(pos3, pos2)])
                case 4:
                    pos2 = QPoint(pos.x(), endpos.y())
                    pos3 = QPoint(endpos.x(), pos.y())
                    painter.drawLines([QLine(pos, pos2), QLine(pos2, pos3), QLine(pos3, pos)])
                case 5:
                    pos3 = QPoint(endpos.x(), pos.y())
                    painter.drawLines([QLine(pos, endpos), QLine(endpos, pos3), QLine(pos3, pos)])

    painter.setBrush(QColor(0, 0, 0, 0))
    if isinstance(tile.cols[1], list):
        painter.setPen(QPen(l2color, 2, Qt.PenStyle.DotLine))
        drawlayer(tile.cols[1])
    painter.setPen(QPen(l1color, 1, Qt.PenStyle.DashLine))
    drawlayer(tile.cols[0])
    return tile_image


def tile_offset(tile: Tile) -> QPoint:
    return QPoint(int((tile.size.width() * 0.5) + .5) - 1, int((tile.size.height() * .5) + .5) - 1)


def color_colortable(color: QColor) -> list[int]:
    table = []
    # for i in range(3):
    #     for i2 in range(10):
    #         newcol = QColor.fromHsv(color.hue(), color.saturation(), color.value() - 90 + (30 * i + i2))
    #         table.append(newcol.rgba())
    for l in range(3):
        for i in range(30):
            table.append(QColor.fromHsv(color.hue(), color.saturation(), min(255, (145 + 45 * l) - (29 - i) * 15)).rgba())
    table.append(QColor(0, 0, 0, 0).rgba())
    return table


def init_solve(file: str):
    output = ItemData()
    s = open(file, "r").readlines()
    category_data = {}
    item_counter = 0
    findcategory = True  # if true, all non-category lines will be ignored until a category line is found
    for ln, i in enumerate(s):
        i = i.strip()
        if len(i) > 1:
            if i[0] == "-":
                try:
                    if category_data:
                        output.append(category_data)
                    js = tojson(i[1:])
                    category_data = {"name": js[0], "color": QColor(*fromarr(js[1], "color")), "items": []}
                    item_counter = 0
                    findcategory = False
                except json.JSONDecodeError:
                    log(
                        f"Failed to convert init CATEGORY line \"{i}\" (line number: {ln}) in file \"{os.path.relpath(file, PATH)}\"! Skipping line and all subsequent tiles!",
                        True)
                    findcategory = True
                    continue
            elif not findcategory:
                try:
                    js = tojson(i)
                    item = {}
                    for p, val in js.items():
                        item[p] = val
                    category_data["items"].append(item)
                    item_counter += 1
                except json.JSONDecodeError:
                    log(
                    f"Failed to convert init ITEM line \"{i}\" (line number: {ln}) in file \"{os.path.relpath(file, PATH)}\"! Skipping line!",
                    True)
                    continue
    output.append(category_data)
    # output.remove([])
    return output


def palette_to_colortable(palette: QImage) -> list[list[list[int], list[int], list[int]], list[list[int], list[int], list[int]], list[list[int], list[int], list[int]], QColor, QColor]:
    table = [[[], [], []], [[], [], []], [[], [], []], palette.pixelColor(0, 0), palette.pixelColor(0, 8)] # 3x3x3 array
    # table[0][1] = [QColor(0, 0, 0).rgb()] * 30
    # table[0][2] = [QColor(0, 0, 0).rgb()] * 60
    # table[1][1] = [QColor(0, 0, 0).rgb()] * 30
    # table[1][2] = [QColor(0, 0, 0).rgb()] * 60
    # table[2][1] = [QColor(0, 0, 0).rgb()] * 30
    # table[2][2] = [QColor(0, 0, 0).rgb()] * 60
    for k in range(3):
        for l in range(90):
            x = 29 - l % 30
            y = l // 30
            table[k][0].append(palette.pixelColor(x, [4, 7, 15][k] - y).rgb())
            # y = (y - 1) % 3
            x = (x + 10) % 30
            table[k][1].append(palette.pixelColor(x, [4, 7, 15][k] - y).rgb())
            x = (x + 10) % 30
            table[k][2].append(palette.pixelColor(x, [4, 7, 15][k] - y).rgb())
        # for l in range(3):
        #     for i in range(30):
        #         # pc = palette.pixelColor(i, [2, 5, 13][k] + l)
        #         # table[k][i // 10].append(pc.rgb())
        #         pc1 = palette.pixelColor(29 - i, [2, 5, 13][k] + l)
        #         pc2 = palette.pixelColor(29 - i, [2, 5, 13][k] + l + 1) if l < 1 else QColor(0, 0, 0)
        #         pc3 = palette.pixelColor(29 - i, [2, 5, 13][k] + l + 2) if l < 2 else QColor(0, 0, 0)
        #         table[k][0].append(pc1.rgb())
        #         table[k][1].append(pc2.rgb())
        #         table[k][2].append(pc3.rgb())
        table[k][0].insert(90, QColor(0, 0, 0, 0).rgba())
        table[k][1].insert(90, QColor(0, 0, 0, 0).rgba())
        table[k][2].insert(90, QColor(0, 0, 0, 0).rgba())
    return table


def loadTile(item, colr, category, catnum, indx) -> Tile | None:
    renderstep = 15
    err = False
    try:
        imagepath = insensitive_path(os.path.join(PATH_DRIZZLE, "Data/Graphics", item["nm"] + ".png"))
        if imagepath is None:
            return None
        origimg = QImage(imagepath)
    except FileNotFoundError:
        return None
    if not origimg.colorTable():
        origimg = origimg.convertToFormat(QImage.Format.Format_Indexed8,
                              [4294901760, 4278255360, 4278190335, 4278190080, 4294967295, 0],
                              Qt.ImageConversionFlag.ThresholdDither)
    try:
        white = origimg.colorTable().index(4294967295)
        origimg.setColor(white, 0)
    except ValueError:
        log(f"Error loading {item['nm']}", True)
    sz = QSize(*fromarr(item["sz"], "point"))
    try:
        ln = len(item["repeatL"])
    except KeyError:
        ln = 1
        # sz:point(x,y) + ( #bfTiles * 2 )) * 20
    tp = item.get("tp", "")
    if tp == "box":  # math
        ln = 4
        size = (ln * sz.height() + (item.get("bfTiles", 0) * 2)) * CELLSIZE
        rect = QRect(0, size, sz.width() * SPRITESIZE, sz.height() * SPRITESIZE)
    elif ((ln * sz.height() + (item.get("bfTiles", 0) * 2 * ln)) * CELLSIZE + 1) > origimg.height():
        rect = QRect(0, origimg.height() - sz.height() * SPRITESIZE, sz.width() * SPRITESIZE, sz.height() * SPRITESIZE)
    else:
        size = (sz.height() + (item.get("bfTiles", 0) * 2)) * ln * CELLSIZE
        rect = QRect(0, size + 1, sz.width() * SPRITESIZE, sz.height() * SPRITESIZE)

    if origimg.rect().contains(rect):
        img = origimg.copy(rect)
    else:
        rect = QRect(0, origimg.height() - sz.height() * SPRITESIZE, sz.width() * SPRITESIZE, sz.height() * SPRITESIZE)
        if origimg.rect().contains(rect):
            img = origimg.copy(rect)
        else:
            rect = QRect(0, 0, 1, 1)
            img = origimg.copy(rect)
    # image
    try:
        black = img.colorTable().index(4278190080)
        img.setColor(black, colr.rgba())
    except ValueError:
        try:
            black = len(img.colorTable()) - 2
            img.setColor(black, colr.rgba())
        except ValueError:
            log(f"Error loading {item['nm']}", True)
            err = True

    # making image2
    bftiles = item.get("bfTiles", 0)
    img2 = QPixmap((sz.width() + bftiles * 2) * CELLSIZE, (sz.height() + bftiles * 2) * CELLSIZE)
    img2.fill(QColor(0, 0, 0, 0))
    p = QPainter(img2)
    if tp == "box":
        p.drawImage(0, 0, origimg.copy(0, sz.width() * CELLSIZE * sz.width(), img2.width(), img2.height()))
    else:
        repl = len(item.get("repeatL", [1]))
        for i in range(repl):
            # for _ in range(repeats):
            widthcap = min(img2.width(), origimg.width())
            # p.setOpacity(min(.2, i / repl + .5))
            p.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceAtop)
            p.fillRect(0, 0, img2.width(), img2.height(), QColor(0, 0, 0, renderstep))
            p.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceOver)
            p.drawImage(0, 0, origimg.copy(0, (repl - i - 1) * img2.height(), widthcap, img2.height()))
    # img3 = img2.convertToFormat(QImage.Format.Format_Indexed8)
    # making image 3
    imagepix = img2.toImage()
    itempath = os.path.join(PATH_FILES_CACHE, item["nm"] + ".png")
    # imagepix.save(os.path.join(PATH_FILES_CACHE, item["nm"] + "_true.png"))
    if os.path.exists(itempath):
        img3 = QImage(itempath)
    else:
        # img3 = QImage(img2.width(), img2.height(), QImage.Format.Format_RGBA64)
        img3 = QImage(img2.width(), img2.height(), QImage.Format.Format_Indexed8)
        img3.setColorTable(colortable[0])
        for xp in range(img3.width()):
            for yp in range(img3.height()):
                pc = imagepix.pixelColor(xp, yp)
                if pc.alpha() == 0 or pc.rgb() == QColor(0, 0, 0).rgb():
                    # img3.setPixelColor(xp, yp, QColor(0, 0, 0, 0))
                    img3.setPixel(xp, yp, 90)
                    continue
                npc = 0
                # if pc.red() > pc.green() and pc.red() > pc.blue():
                #     pc = QColor(91 + (255 - pc.red()) // renderstep, 0, 0, 255)
                # elif pc.green() > pc.red() and pc.green() > pc.blue():
                #     pc = QColor(121 + (255 - pc.green()) // renderstep, 0, 0, 255)
                # elif pc.blue() > pc.green() and pc.blue() > pc.red():
                #     pc = QColor(151 + (255 - pc.blue()) // renderstep, 0, 0, 255)
                if pc.red() > pc.green() and pc.red() > pc.blue():
                    npc = 0 + 29 - round((255 - pc.red()) / renderstep)
                elif pc.green() > pc.red() and pc.green() > pc.blue():
                    npc = 30 + 29 - round((255 - pc.green()) / renderstep)
                elif pc.blue() > pc.green() and pc.blue() > pc.red():
                    npc = 60 + 29 - round((255 - pc.blue()) / renderstep)
                img3.setPixel(xp, yp, npc)
                # img3.setPixelColor(xp, yp, pc)
        # img3 = img3.convertToFormat(QImage.Format.Format_Indexed8, colortable[0],
        #                             Qt.ImageConversionFlag.ThresholdDither)
        img3.save(itempath)

    return Tile(item["nm"], tp, item.get("repeatL", [1]), f"Tile", item.get("bfTiles", 0), QPixmap(img), img2, img3,
                sz, colr, (item.get("specs", [1]), item.get("specs2", 0)),
                QPoint(catnum + 1, indx + 1),
                item.get("tags"), True, None, err, category)


class TilePackLoader(QThread):
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
            tileslist = []
            tilecat = TileCategory(catitem["name"], catitem["color"], tileslist)

            items = catitem["items"]
            colr: QColor = catitem["color"]
            # self.data[catnum]["items"] = []
            for indx, item in enumerate(items):
                # printmessage(f"Loading tile {item['nm']}...", f"({tilenum}/{length})")
                # window.ui.progressBar.setValue(int(tilenum / length * 100))

                tile = loadTile(item, colr, tilecat, catnum, indx)
                self.progress += 1
                if tile is None:
                    self.errors += 1
                    continue
                # tilenum += 1
                # self.data[catnum]["items"].append(tile)
                tileslist.append(tile)
                if tile.err:
                    self.errors += 1
            self.cats.append(tilecat)
        # self.finished.emit()


class TileProgress(QThread):
    def __init__(self, window, workers):
        window.printmessage("Loading Tiles...")
        super().__init__()
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


def load_tiles(window: SplashDialog) -> Tiles:
    solved_copy = init_solve(os.path.join(PATH_DRIZZLE, "Data/Graphics/Init.txt"))
    length = sum(list(map(lambda x: len(x["items"]), solved_copy.data)))
    log(f"Loading {length} tiles")

    threadsnum = min(1, multiprocessing.cpu_count() - 1)
    catsnum = len(solved_copy.data)
    data_per_thread = catsnum // threadsnum
    unused = catsnum - data_per_thread * threadsnum
    # 1. split data to threads
    # 2. make threads and adress them the data
    # 3. activate all threads and wait for the result
    # 4. combine results of all the threads into a specified class
    workers: list[TilePackLoader] = []
    for i in range(threadsnum):
        workers.append(TilePackLoader(solved_copy.data[i * data_per_thread:i * data_per_thread + data_per_thread]))
    if unused > 0:
        workers.append(TilePackLoader(solved_copy.data[-unused:]))
    progress = TileProgress(window, workers)
    for i in workers:
        i.start()
    progress.start()
    for i in workers:
        i.wait()
    progress.wait()
    log(f"Errors: {sum(list(map(lambda x: x.errors, workers)))}")
    # solved_copy = ItemData()
    categories_list = []
    for i in workers:
        for d in i.cats:
            categories_list.append(d)
    del workers, progress
    # aint no way i'm doing multi threading material loading
    # matcat = "materials 0"
    matcatcount = 0
    materialtiles = []
    material_category = TileCategory("materials", QColor(0, 0, 0), materialtiles)
    # solved_copy.insert(matcatcount, {"name": matcat, "color": QColor(0, 0, 0), "items": []})
    for k, v in CONSTS.get("materials", {}).items():
        col = QColor(*v)
        img = QPixmap(20, 20)
        img.fill(col)
        ms = CELLSIZE
        # pg.draw.rect(img, v, pg.Rect(ms[0], ms[0], ms[1], ms[1]))
        try:
            preview = QImage(os.path.join(PATH_MAT_PREVIEWS, CONSTS.get("materialpreviews", {}).get(k, "") + ".png"))
        except FileNotFoundError or TypeError:
            preview = QImage(1, 1, QImage.Format.Format_RGBA64)
        # preview.set_colorkey(pg.Color(255, 255, 255))
        # window.printmessage(f"Loading material {k}")
        materialtiles.append(Tile(k, "material", [1], "Material", 0, img, img, img.toImage(), QSize(1, 1), col, [[-1], 0],
                                                      QPoint(matcatcount + 1, len(solved_copy[matcatcount]["items"]) + 1),
                                                      ["material"], False, preview, False, material_category))
        # solved_copy[matcatcount]["items"].append(Tile(k, None, [1], "Material", 0, img, img, img.toImage(), QSize(1, 1),
        #                                               matcat, col, [[-1], 0],
        #                                               QPoint(matcatcount + 1, len(solved_copy[matcatcount]["items"]) + 1),
        #                                               ["material"], False, preview, False))

        # if len(solved_copy[matcatcount]["items"]) > 30:
        #     matcatcount += 1
        #     matcat = f"materials {matcatcount}"
        #     solved_copy.insert(matcatcount, {"name": matcat, "color": QColor(0, 0, 0), "items": []})
    # window.printmessage("All tiles loaded!")
    categories_list.insert(0, material_category)
    return Tiles(categories_list)
