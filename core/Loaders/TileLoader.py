from core.ItemData import ItemData
from core.lingoIO import tojson, toarr
from core.info import PATH
from ui.splashuiconnector import SplashDialog
from PySide6.QtGui import QColor, QPixmap, QImage
from PySide6.QtCore import QRect
import json
import os
from core.info import log_to_load_log, PATH_DRIZZLE, CELLSIZE, SPRITESIZE


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
                    category_data = {"name": js[0], "color": QColor(*toarr(js[1], "color")), "items": []}
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
    for catnum, catitem in enumerate(solved_copy.data):
        cat = catitem["name"]

        items = catitem["items"]
        colr = catitem["color"]
        solved_copy[catnum]["items"] = []
        for indx, item in enumerate(items):
            printmessage(f"Loading tile {item['nm']}...", f"({tilenum}/{length})")
            window.ui.progressBar.setValue(int(tilenum / length * 100))
            try:
                img = QImage(os.path.join(PATH_DRIZZLE, "Data/Graphics", item["nm"] + ".png"))
            except FileNotFoundError:
                continue
            sz = toarr(item["sz"], "point")
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
            elif ((ln * sz[1] + (item.get("bfTiles", 0) * 2 * ln)) * CELLSIZE + 1) > img.height():
                rect = QRect(0, img.height() - sz[1] * SPRITESIZE, sz[0] * SPRITESIZE, sz[1] * SPRITESIZE)
            else:
                size = (sz[1] + (item.get("bfTiles", 0) * 2)) * ln * SPRITESIZE
                rect = QRect(0, size + 1, sz[0] * SPRITESIZE, sz[1] * SPRITESIZE)

            try:
                img = img.copy(rect)
            except ValueError:
                try:
                    rect = QRect(0, img.height() - sz[1] * SPRITESIZE, sz[0] * SPRITESIZE, sz[1] * SPRITESIZE)
                    img = img.copy(rect)
                except ValueError:
                    rect = QRect(0, 0, 1, 1)
                    img = img.copy(rect)
            # srf = img.copy()
            # srf.fill(colr)
            # img.set_colorkey(pg.Color(0, 0, 0))
            # srf.blit(img, [0, 0])
            # img.fill(colr)
            '''
            s = pg.Surface(img.get_size())
            s.blit(img, [0, 0])
            arr = pg.pixelarray.PixelArray(s.copy())
            arr.replace(pg.Color(0, 0, 0), colr)
            img = arr.make_surface()
            img.set_colorkey(pg.Color(255, 255, 255))'''

            newitem = {
                "nm": item["nm"],
                "tp": item.get("tp"),
                "repeatL": item["repeatL"] if item.get("repeatL") is not None else [1],
                "description": "Size" + str(sz),
                "bfTiles": item.get("bfTiles", 0),
                "image": img,
                "size": sz,
                "category": cat,
                "color": colr,
                "cols": [item.get("specs", [1]), item.get("specs2", 0)],
                "cat": [catnum + 1, indx + 1],
                "tags": item["tags"],
                "printcols": True
            }
            tilenum += 1
            solved_copy[catnum]["items"].append(newitem)
    return solved_copy
    matcat = "materials 0"
    matcatcount = 0
    solved_copy.insert(matcatcount, {"name": matcat, "color": pg.Color(0, 0, 0), "items": []})
    for k, v in globalsettings["matposes"].items():
        col = pg.Color(v)
        img = pg.Surface([image1size, image1size], pg.SRCALPHA)
        img.fill(pg.Color(0, 0, 0, 0))
        ms = globalsettings["matsize"]
        pg.draw.rect(img, v, pg.Rect(ms[0], ms[0], ms[1], ms[1]))
        try:
            preview = loadimage(path2materialPreviews + k + ".png")
        except FileNotFoundError:
            preview = pg.Surface([image1size, image1size])
            preview.set_alpha(0)
        preview.set_colorkey(pg.Color(255, 255, 255))
        printmessage(f"Loading material {k}")
        solved_copy[matcatcount]["items"].append(
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
            })
        if len(solved_copy[matcatcount]["items"]) > 30:
            matcatcount += 1
            matcat = f"materials {matcatcount}"
            solved_copy.insert(matcatcount, {"name": matcat, "color": pg.Color(0, 0, 0), "items": []})
    printmessage("All tiles loaded!")
    return solved_copy