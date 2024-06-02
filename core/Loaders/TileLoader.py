from core.ItemData import ItemData
from core.lingoIO import tojson, fromarr
from core.info import PATH
from core.Loaders.Tile import Tile
from ui.splashuiconnector import SplashDialog
from PySide6.QtGui import QColor, QPixmap, QImage, QPainter
from PySide6.QtCore import QRect, Qt
import json
import os
from core.info import PATH_DRIZZLE, CELLSIZE, SPRITESIZE, CONSTS, PATH_MAT_PREVIEWS, PATH_FILES_CACHE
from core.utils import log_to_load_log

colortable = [[], [], []]
for l in range(3):
    for i in range(3):
        for i2 in range(10):
            colortable[l].append(QColor(91 + 30 * i + i2 - 10 * l, 0, 0, 255).rgba())
colortable[0].append(QColor(0, 0, 0, 0).rgba())
colortable[1].append(QColor(0, 0, 0, 0).rgba())
colortable[2].append(QColor(0, 0, 0, 0).rgba())


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
                    log_to_load_log(
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
                    log_to_load_log(
                    f"Failed to convert init ITEM line \"{i}\" (line number: {ln}) in file \"{os.path.relpath(file, PATH)}\"! Skipping line!",
                    True)
                    continue
    output.append(category_data)
    # output.remove([])
    return output


def palette_to_colortable(palette: QImage) -> list[list[list[int], list[int], list[int]], list[list[int], list[int], list[int]], list[list[int], list[int], list[int]], QColor, QColor]:
    table = [[[], [], []], [[], [], []], [[], [], []], palette.pixelColor(0, 0), palette.pixelColor(0, 8)] # 3x3x3 array
    for k in range(3):
        for l in range(3):
            for i in range(30):
                pc = palette.pixelColor(i, [2, 5, 13][k] + l)
                table[k][i // 10].append(pc.rgb())
        table[k][0].append(QColor(0, 0, 0, 0).rgba())
        table[k][1].append(QColor(0, 0, 0, 0).rgba())
        table[k][2].append(QColor(0, 0, 0, 0).rgba())
    return table


def loadTiles(window: SplashDialog) -> ItemData:
    print("Loading Tiles...")

    def printmessage(message, message2=None):
        window.ui.label.setText(message)
        if message2 is not None:
            window.ui.label_2.setText(message2)

    solved_copy = init_solve(os.path.join(PATH_DRIZZLE, "Data/Graphics/Init.txt"))
    length = sum(list(map(lambda x: len(x["items"]), solved_copy.data)))
    print(f"loading {length} tiles")
    tilenum = 1
    renderstep = 15
    for catnum, catitem in enumerate(solved_copy.data):
        cat = catitem["name"]

        items = catitem["items"]
        colr: QColor = catitem["color"]
        solved_copy[catnum]["items"] = []
        for indx, item in enumerate(items):
            printmessage(f"Loading tile {item['nm']}...", f"({tilenum}/{length})")
            window.ui.progressBar.setValue(int(tilenum / length * 100))
            try:
                origimg = QImage(os.path.join(PATH_DRIZZLE, "Data/Graphics", item["nm"] + ".png"))
            except FileNotFoundError:
                continue
            try:
                white = origimg.colorTable().index(4294967295)
                origimg.setColor(white, 0)
            except ValueError:
                log_to_load_log(f"Error loading {item['nm']}", True)
            sz = fromarr(item["sz"], "point")
            try:
                ln = len(item["repeatL"])
            except KeyError:
                ln = 1
                # sz:point(x,y) + ( #bfTiles * 2 )) * 20
            try:
                tp = item["tp"]
            except KeyError:
                tp = ""
            if tp == "box":  # math
                ln = 4
                size = (ln * sz[1] + (item.get("bfTiles", 0) * 2)) * CELLSIZE
                rect = QRect(0, size, sz[0] * SPRITESIZE, sz[1] * SPRITESIZE)
            elif ((ln * sz[1] + (item.get("bfTiles", 0) * 2 * ln)) * CELLSIZE + 1) > origimg.height():
                rect = QRect(0, origimg.height() - sz[1] * SPRITESIZE, sz[0] * SPRITESIZE, sz[1] * SPRITESIZE)
            else:
                size = (sz[1] + (item.get("bfTiles", 0) * 2)) * ln * CELLSIZE
                rect = QRect(0, size + 1, sz[0] * SPRITESIZE, sz[1] * SPRITESIZE)


            if origimg.rect().contains(rect):
                img = origimg.copy(rect)
            else:
                rect = QRect(0, origimg.height() - sz[1] * SPRITESIZE, sz[0] * SPRITESIZE, sz[1] * SPRITESIZE)
                if origimg.rect().contains(rect):
                    img = origimg.copy(rect)
                else:
                    rect = QRect(0, 0, 1, 1)
                    img = origimg.copy(rect)
            # srf = img.copy()
            # srf.fill(colr)
            # img.set_colorkey(pg.Color(0, 0, 0))
            # srf.blit(img, [0, 0])
            # img.fill(colr)
            # todo tile preview
            # image
            try:
                black = img.colorTable().index(4278190080)
                img.setColor(black, colr.rgba())
            except ValueError:
                log_to_load_log(f"Error loading {item['nm']}", True)

            #making image2, 3, and 4
            bftiles = item.get("bfTiles", 0)
            img2 = QImage((sz[0] + bftiles * 2) * CELLSIZE, (sz[1] + bftiles * 2) * CELLSIZE, QImage.Format.Format_RGBA64)
            img2.fill(QColor(0, 0, 0, 0))
            p = QPainter(img2)
            if tp == "box":
                p.drawImage(0, 0, origimg.copy(0, sz[0] * CELLSIZE * sz[0], img2.width(), img2.height()))
            else:
                repl = len(item.get("repeatL", [1]))
                for i in range(repl):
                    # for _ in range(repeats):
                    p.drawImage(0, 0, origimg.copy(0, (repl - i - 1) * img2.height(), img2.width(), img2.height()))
                    # p.setOpacity(min(.2, i / repl + .5))
                    p.setCompositionMode(p.CompositionMode.CompositionMode_SourceAtop)
                    p.fillRect(0, 0, img2.width(), img2.height(), QColor(0, 0, 0, renderstep))
                    p.setCompositionMode(p.CompositionMode.CompositionMode_SourceOver)
            # img3 = img2.convertToFormat(QImage.Format.Format_Indexed8)
            itempath = os.path.join(PATH_FILES_CACHE, item["nm"] + ".png")
            if os.path.exists(itempath):
                img3 = QImage(itempath)
            else:
                img3 = QImage(img2.width(), img2.height(), QImage.Format.Format_RGBA64)
                for xp in range(img3.width()):
                    for yp in range(img3.height()):
                        pc = img2.pixelColor(xp, yp)
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
                img3 = img3.convertToFormat(QImage.Format.Format_Indexed8, colortable[0], Qt.ImageConversionFlag.ThresholdDither)
                img3.save(itempath)

            img4 = img3.copy()

            newitem = {
                "nm": item["nm"],
                "tp": item.get("tp"),
                "repeatL": item.get("repeatL", [1]),
                "description": "Size" + str(sz),
                "bfTiles": item.get("bfTiles", 0),
                "image": img,  # normal rwe# style
                "image2": img2,  # tile image
                "image3": img3,  # henry colored
                "image4": img4,  # rendered tile
                # "image5": img,  # rendered tile with applied palette
                "size": sz,
                "category": cat,
                "color": colr,
                "cols": [item.get("specs", [1]), item.get("specs2", 0)],
                "cat": [catnum + 1, indx + 1],
                "tags": item["tags"],
                "printcols": True
            }
            tilenum += 1
            solved_copy[catnum]["items"].append(Tile(newitem))
    matcat = "materials 0"
    matcatcount = 0
    solved_copy.insert(matcatcount, {"name": matcat, "color": QColor(0, 0, 0), "items": []})
    for k, v in CONSTS.get("materials", {}).items():
        col = QColor(*v)
        img = QImage(20, 20, QImage.Format.Format_RGBA64)
        img.fill(QColor(0, 0, 0, 0))
        ms = CELLSIZE
        # pg.draw.rect(img, v, pg.Rect(ms[0], ms[0], ms[1], ms[1]))
        try:
            preview = QImage(os.path.join(PATH_MAT_PREVIEWS, CONSTS.get("materialpreviews", {}).get(k, "") + ".png"))
        except FileNotFoundError or TypeError:
            preview = QImage(1, 1, QImage.Format.Format_RGBA64)
        # preview.set_colorkey(pg.Color(255, 255, 255))
        printmessage(f"Loading material {k}")
        solved_copy[matcatcount]["items"].append(Tile(
            {
                "nm": k,
                "tp": None,
                "repeatL": [1],
                "description": "Material",
                "bfTiles": 0,
                "image": img,
                "size": [1, 1],
                "category": matcat,
                "color": col,
                "cols": [[-1], 0],
                "cat": [matcatcount + 1, len(solved_copy[matcatcount]["items"]) + 1],
                "tags": ["material"],
                "preview": preview
            }))
        if len(solved_copy[matcatcount]["items"]) > 30:
            matcatcount += 1
            matcat = f"materials {matcatcount}"
            solved_copy.insert(matcatcount, {"name": matcat, "color": QColor(0, 0, 0), "items": []})
    printmessage("All tiles loaded!")
    return solved_copy
