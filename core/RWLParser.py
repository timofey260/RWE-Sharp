"""
Slug parser

parses .rwl files into dict and vise versa

you would need it: https://docs.google.com/document/d/1zcxeQGibkZORstwGQUovhQk71k00B69oYwkqFpGyOqs/edit#heading=h.7xts9mnasx5f

reading of geo, tiles, and anything matrix related goes from left to right, top to bottom

------

Specification:

1. properties:

first line of file is level properties

line with level size, extra tiles, sunlight, tile seed etc.

format: v;w h;el et er eb;l;s
    * v: rwl version(for compatibility)
    * w, h: width and height
    * el, et, er and eb: extra tiles(left, top right and bottom)
    * l: light(either 0 or 1)
    * s: tile seed

2. Geo

geo amount depends on level size we had added earlier

one cell is 1-5 bytes long

first 2 bits is cell "mode" and dictates should it read other bytes or remain on one
    00 - simple     (1 byte)
        in simple mode we just use all remaining 6 bits to get blocks on 3 layers(no stackables at all)
            mm112233
            m - mode
            1, 2, 3 - layers
                00 - air
                01 - wall
                10 - platform
                11 - glass
            this format is completely useless in case of slopes or entrances on any layers but works great when using it normally
    01 - copy       (1 byte)
        in copy mode we just copy last tile we had(copy both block and stackables)
            mmssssss
            m - mode
            s - steps - how much tiles ago was tile we can copy(64 max)
    10 - compressed (3 bytes)
        in compressed mode we only blocks and stackables on all layers are eiter same or just wall
            mmbbbwww ffffffff ffffffff
            m - mode
            b - block to use(see below)
            w - what layers should be affected. if layer is not affected then it's just a wall without stackables
            f - stackable info for all affected layers
    11 - all info   (5 bytes)
        this mode describes all info all layers have without compressing it.
        this should be used when none of the above mods work
                                                 2222222 22233333 33333333 333 - could've been
            mmaaabbb ccc11111 11111111 11122222 2333333_

            m - mode
            a - layer 1 block
            b - layer 2 block
            c - layer 3 block
            1 - layer 1 stackables list
            2 - layer 2 stackables list(without including last 10)
            3 - layer 3 stackables list(without including last 10)
            _ - unused
        this mode all by itself can getsize of geo 4 times smaller than normal txt

----

blocks(3 bits):
    000 - air      [0]
    001 - wall     [1]
    010 - slope NE [2]
    011 - slope NW [3]
    100 - slope ES [4]
    101 - slope SW [5]
    110 - platform [6]
    111 - glass    [9]

List of stackables(2 bytes):
    |01| * horizontal pole                                   [ 1]
    |02| * vertical pole                                     [ 2]
    |03| * cracked terrain                                   [11]
    |04| * bat hive                                          [ 3]
    |05| - shortcut entrance(if used, block is entrance too) [ 4]
    |06| - shortcut path                                     [ 5]
    |07| + room entrance (den)                               [ 6]
    |08| + dragon den                                        [ 7]
    |09| + rock                                              [ 9]
    |10| + spear                                             [10]
    |11| + forbid fly chains                                 [12]
    |12| + garbage mole hole                                 [13]
    |13| + whack a mole hole                                 [19]
    |14| + scav hole                                         [21]
    |15| + worm grass                                        [20]
    |16| + waterfall                                         [18]
    * - only ones affecting render on all layers
    - - might affect render on layers other than 1(not tested but included)
    + - good to be unused on other layers

2. tiles

tiles formatting consists of 3 parts
1st one is initial data(4 bytes)
first byte is size of one tilehead in bytes
    1 for 6 bits per tilehead(63)
    2 for 14 bits per tilehead(16 383)
    3 for 22 bits per tilehead(4 194 303, never meant to be used)
second byte is amount of different materials used in level + the default material(1)
last 2 bytes are amount of different tiles used in level

2nd part is tile and material database
tile database contains all tile names and their poses that we use
each tile/pos pair is seperated by /xff symbol
example: Big metal/xff/x00/x01/xff
         ^name    ^sep^cat^itm^sep
         name - name of tile
         sep - seperator
         cat - tile category
         itm - tile index in that category
BUT
    if tile is chain holder, it would take 4 more bytes after last seperator
    with structure as: Chain holder/xff/x00/x01/xff/x00/x11/x12/x01/xff
                       ^name       ^sep^cat^itm^sep^ox1^ox2^oy1^oy2^sep
                        ox1 and ox2 - chain pos x + 256
                        ox1 and ox2 - chain pos y + 256

after tile database comes material database
material database is string of all materials, separated by /xff
after last material, default material is placed with /xff at the end

3rd part is level tiles and it specifies all tiles on level
each tile layer is split in different sections(width * height tiles for one layer)
one tile can take 1-3 bytes
first 2 bits of each tile is tile mode
    00 - nothing  (1 byte)
        in this mode we specify how much cells can we skip after this one
            mmssssss
            m - mode
            s - tiles to skip
            tiles to skip says how much cells after this one are empty(63 max)
    01 - material (2 bytes)
        in this mode we just specify what material this is and how many materials under it are the same
            mmssssss tttttttt
            m - mode
            s - materials after it
            t - material index(specified in 2nd part)
            s says how much of same materials are after it(63 max)
    10 - tilebody (2 bytes)
        in this mode we record offset of tilebody to tilehead
            mmllxxxx xxyyyyyy
            m - mode
            l - tilehead layer
            x - x offset + 32(63 max)
            y - y offset + 32(63 max)
    11 - tilehead (1-3 bytes)
        size of tilehead depends on 1st byte(see 1st part)
            mmtttttt
            mmtttttt tttttttt
            mmtttttt tttttttt tttttttt
            m - mode
            t - tile index(see 2nd part)
"""
import copy
import json
from core.lingoIO import fromarr, makearr
import re


VER = 1
ENCODING = "latin-1"

_stacklist = [1, 2, 11, 3, 4, 5, 6, 7, 9, 10, 12, 13, 19, 21, 20, 18]
_accepted = [0, 1, 6, 9]
_blocks = [0, 1, 2, 3, 4, 5, 6, 9]

# encodecodes = []
# decodecodes = []


class RWLParser:
    def __init__(self):
        pass
    @staticmethod
    def parse_rwl(string: bytearray) -> dict:
        # global decodecodes
        level = {}
        # level properties
        regmatch = re.match("^(\d+);(\d+ \d+);(\d+ \d+ \d+ \d+);(\d+);(\d+)", string.decode(ENCODING))
        level["EX2"] = {}
        version = int(regmatch.group(1))
        size = list(map(lambda x: int(x), regmatch.group(2).split()))
        border = list(map(lambda x: int(x), regmatch.group(3).split()))
        light = int(regmatch.group(4))
        seed = int(regmatch.group(5))
        level["EX2"]["size"] = makearr(size, "point")
        level["EX2"]["extraTiles"] = border
        level["EX2"]["light"] = light
        level["EX2"]["tileSeed"] = seed

        # geo
        level["GE"] = [[[] for _ in range(size[1])] for _ in range(size[0])]
        geopart = string.find(b"\n") + 1
        history = []

        cursor = 0
        #c1 = 0
        #c2 = 0
        #c3 = 0
        #c4 = 0
        for i in range(size[0] * size[1]):
            curpos = string[geopart + i + cursor]
            poscursor = [i // size[1], i % size[1]]
            curbin = RWLParser.goodbin(curpos, 8)
            cblock = [[0, []], [0, []], [0, []]]
            match curbin[:2]:
                case "00":
                    curblock1 = _accepted[int(curbin[2:4], 2)]
                    curblock2 = _accepted[int(curbin[4:6], 2)]
                    curblock3 = _accepted[int(curbin[6:8], 2)]
                    cblock = [[curblock1, []], [curblock2, []], [curblock3, []]]
                    #c1 += 1
                case "01":
                    cblock = copy.deepcopy(history[int(curbin[2:8], 2)])
                    #c2 += 1
                case "10":
                    curbin = curbin + RWLParser.goodbin(string[geopart + i + cursor + 1], 8) + \
                             RWLParser.goodbin(string[geopart + i + cursor + 2], 8)
                    block = RWLParser.cut(curbin, 2, 5)
                    affected = curbin[5:8]
                    stackables = RWLParser.destack(curbin[8:])
                    if 4 in stackables: block = 7
                    cblock = [
                        [1, []] if affected[0] == "0" else [block, stackables],
                        [1, []] if affected[1] == "0" else [block, stackables],
                        [1, []] if affected[2] == "0" else [block, stackables]
                    ]
                    cursor += 2
                    #c3 += 1
                case "11":
                    curbin = curbin + RWLParser.goodbin(string[geopart + i + cursor + 1], 8) + \
                             RWLParser.goodbin(string[geopart + i + cursor + 2], 8) + \
                             RWLParser.goodbin(string[geopart + i + cursor + 3], 8) + \
                             RWLParser.goodbin(string[geopart + i + cursor + 4], 8)
                    block1 = RWLParser.cut(curbin, 2, 5)
                    block2 = RWLParser.cut(curbin, 5, 8)
                    block3 = RWLParser.cut(curbin, 8, 11)
                    stackables1 = RWLParser.destack(curbin[11:27])
                    stackables2 = RWLParser.destack(curbin[27:33])
                    stackables3 = RWLParser.destack(curbin[33:39])
                    if 4 in stackables1: block1 = 7
                    if 4 in stackables2: block2 = 7
                    if 4 in stackables3: block3 = 7
                    cblock = [
                        [block1, stackables1],
                        [block2, stackables2],
                        [block3, stackables3]
                    ]
                    cursor += 4
                    #c4 += 1
            # decodecodes.append(curbin)
            level["GE"][poscursor[0]][poscursor[1]] = cblock
            history.insert(0, cblock)
            history = history[:64]
        # print(c1, c2, c3, c4)
        del history

        # tiles
        tiles = []
        mats = []

        # reading params
        tilepart = size[0] * size[1] + geopart + cursor
        bytemode = string[tilepart]
        matamount = string[tilepart + 1]
        tileamount = string[tilepart + 2] + (string[tilepart + 3] << 8)
        tilepart += 4

        i = 0
        cursor = 0
        tile = ""
        while i < tileamount:
            letter = string[tilepart + i + cursor]
            if letter != 255:
                tile += chr(letter)
                cursor += 1
                continue
            cursor += 1
            pos1 = string[tilepart + i + cursor]
            pos2 = string[tilepart + i + cursor + 1]
            cursor += 2
            if tile.lower() == "chain holder":
                ch1 = string[tilepart + i + cursor] + (string[tilepart + i + cursor + 1] << 8) - 256
                ch2 = string[tilepart + i + cursor + 2] + (string[tilepart + i + cursor + 3] << 8) - 256
                cursor += 4
                tiles.append([makearr([pos1, pos2], "point"), tile, makearr([ch1, ch2], "point")])
            else:
                tiles.append([makearr([pos1, pos2], "point"), tile])
            tile = ""
            i += 1
        del tile
        tilepart += cursor + tileamount
        cursor = 0
        mat = ""
        i = 0
        while i < matamount:
            letter = string[tilepart + i + cursor]
            if letter != 255:
                mat += chr(letter)
                cursor += 1
                continue
            mats.append(mat)
            mat = ""
            i += 1
        tilepart += matamount + cursor
        del matamount, tileamount

        level["TE"] = {"tlMatrix": [[[{"tp": "default", "data": 0} for _ in range(3)] for _ in range(size[1])] for _ in range(size[0])], "defaultMaterial": mats[-1]}
        # decodecodes = [[] for _ in range(size[0] * size[1])]
        for l in range(3):
            i = 0
            cursor = 0
            while i < size[0] * size[1]:
                poscursor = [i // size[1], i % size[1]]
                curpos = string[tilepart + cursor]
                curbin = RWLParser.goodbin(curpos, 8)
                match curbin[:2]:
                    case "00": # nothing
                        # decodecodes[i].append(curbin)
                        skip = int(curbin[2:], 2)
                        level["TE"]["tlMatrix"][poscursor[0]][poscursor[1]][l] = {"tp": "default", "data": 0}
                        for b in range(skip):
                            poscursor = [(i + b + 1) // size[1], (i + b + 1) % size[1]]
                            level["TE"]["tlMatrix"][poscursor[0]][poscursor[1]][l] = {"tp": "default", "data": 0}
                            # decodecodes[i + b + 1].append("")
                        i += skip
                    case "01": # material
                        skip = int(curbin[2:], 2)
                        data = string[tilepart + cursor + 1]

                        curbin += RWLParser.goodbin(string[tilepart + cursor + 1], 8)
                        # decodecodes[i].append(curbin)

                        level["TE"]["tlMatrix"][poscursor[0]][poscursor[1]][l] = {"tp": "material", "data": mats[data]}
                        for b in range(skip):
                            poscursor = [(i + b + 1) // size[1], (i + b + 1) % size[1]]
                            level["TE"]["tlMatrix"][poscursor[0]][poscursor[1]][l] = {"tp": "material", "data": mats[data]}
                            # decodecodes[i + b + 1].append("")
                        i += skip
                        cursor += 1
                    case "10": # tilebody
                        curbin += RWLParser.goodbin(string[tilepart + cursor + 1], 8)
                        data = [makearr([poscursor[0] + 1 + int(curbin[4:10], 2) - 32, poscursor[1] + 1 + int(curbin[10:], 2) - 32], "point"), int(curbin[2:4], 2)]
                        level["TE"]["tlMatrix"][poscursor[0]][poscursor[1]][l] = {"tp": "tileBody", "data": data}
                        cursor += 1
                        # decodecodes[i].append(curbin)
                    case "11":
                        match bytemode:
                            case 2:
                                curbin += RWLParser.goodbin(string[tilepart + cursor + 1], 8)
                                cursor += 1
                            case 3:
                                curbin += RWLParser.goodbin(string[tilepart + cursor + 1], 8) + \
                                          RWLParser.goodbin(string[tilepart + cursor + 2], 8)
                                cursor += 2
                        indx = int(curbin[2:], 2)
                        level["TE"]["tlMatrix"][poscursor[0]][poscursor[1]][l] = {"tp": "tileHead", "data": tiles[indx]}
                        # decodecodes[i].append(curbin)
                # print(curbin)
                i += 1
                cursor += 1
            tilepart += cursor
        return level

    @staticmethod
    def destack(stack: str) -> list[int]:
        l = []
        for i, v in enumerate(stack):
            if v == "1":
                l.append(_stacklist[i])
        return l

    @staticmethod
    def cut(b, s, e):
        return _blocks[int(b[s:e], 2)]

    @staticmethod
    def goodbin(i: int, n: int) -> str:
        bl = bin(i)[2:]
        return "0" * (n - len(bl)) + bl

    @staticmethod
    def checkgeo(cell) -> tuple[str, str]:
        stackables = cell[1]
        stackcode = "".join(map(lambda x: "1" if x in stackables else "0", _stacklist))
        if cell[0] in _blocks:
            return RWLParser.goodbin(_blocks.index(cell[0]), 3), stackcode
        return "000", stackcode

    @staticmethod
    def splitval(val: str) -> list[str]:
        return [val[i:i+8] for i in range(0, len(val), 8)]

    @staticmethod
    def save_rwl(level: dict) -> bytearray:
        # global encodecodes
        levelstring = bytearray("", ENCODING)
        # level properties
        size = fromarr(level["EX2"].get("size"), "point")
        extra = level["EX2"].get("extraTiles")
        light = level["EX2"].get("light")
        seed = level["EX2"].get("tileSeed")
        levelstring += f"{VER};{size[0]} {size[1]};{extra[0]} {extra[1]} {extra[2]} {extra[3]};{light};{seed}\n".encode(ENCODING)
        # geo
        lastgeo = []

        for xp, x in enumerate(level["GE"]):
            for yp, y in enumerate(x):
                if y[0][0] in _accepted and y[1][0] in _accepted and y[2][0] in _accepted \
                        and len(y[0][1]) == 0 and len(y[1][1]) == 0 and len(y[2][1]) == 0: # mode 00
                    newstr = "00" + RWLParser.goodbin(_accepted.index(y[0][0]), 2) + \
                             RWLParser.goodbin(_accepted.index(y[1][0]), 2) + \
                             RWLParser.goodbin(_accepted.index(y[2][0]), 2)
                elif y in lastgeo: # mode 01
                    indx = lastgeo.index(y)
                    newstr = "01" + RWLParser.goodbin(indx, 6)
                elif y[0] == y[1] and y[2][0] in _accepted and len(y[2][1]) == 0: # mode 10
                    newblock, newstack = RWLParser.checkgeo(y[0])
                    newstr = "10" + newblock + "110" + newstack
                elif y[1] == y[2] and y[0][0] in _accepted and len(y[0][1]) == 0:
                    newblock, newstack = RWLParser.checkgeo(y[1])
                    newstr = "10" + newblock + "011" + newstack
                elif y[2] == y[0] and y[1][0] in _accepted and len(y[1][1]) == 0:
                    newblock, newstack = RWLParser.checkgeo(y[2])
                    newstr = "10" + newblock + "101" + newstack
                elif y[0] == y[1] == y[2]:
                    newblock, newstack = RWLParser.checkgeo(y[0])
                    newstr = "10" + newblock + "111" + newstack

                elif y[0] == y[1] == [1, []]:
                    newblock, newstack = RWLParser.checkgeo(y[2])
                    newstr = "10" + newblock + "001" + newstack
                elif y[1] == y[2] == [1, []]:
                    newblock, newstack = RWLParser.checkgeo(y[0])
                    newstr = "10" + newblock + "100" + newstack
                elif y[2] == y[0] == [1, []]:
                    newblock, newstack = RWLParser.checkgeo(y[1])
                    newstr = "10" + newblock + "010" + newstack
                else: # mode 11
                    newblock1, newstack1 = RWLParser.checkgeo(y[0])
                    newblock2, newstack2 = RWLParser.checkgeo(y[1])
                    newblock3, newstack3 = RWLParser.checkgeo(y[2])
                    newstr = "11" + newblock1 + newblock2 + newblock3 + newstack1 + newstack2[:6] + newstack3[:6] + "0"
                # print(newstr, RWLParser.splitval(newstr))
                # print(y, newstr)
                for i in RWLParser.splitval(newstr):
                    levelstring.append(int(i, 2))
                # encodecodes.append([newstr, y])
                lastgeo.insert(0, y)
                lastgeo = lastgeo[:64]
        del lastgeo
        # tiles
        skiptiles = 0
        tilelist = []
        matlist = []
        for xp, x in enumerate(level["TE"]["tlMatrix"]):
            for yp, y in enumerate(x):
                for lp, l in enumerate(y):
                    if l["tp"] == "material" and l["data"] not in matlist:
                        matlist.append(l["data"])
                    elif l["tp"] == "tileHead":
                        tile = [fromarr(l["data"][0], "point"), l["data"][1]]
                        if tile not in tilelist:
                            if tile[1].lower() == "chain holder":
                                tile.append(fromarr(l["data"][2], "point"))
                            tilelist.append(tile)

        if len(tilelist) <= 64:
            bpt = 1
        elif len(tilelist) <= 16384:
            bpt = 2
        else:
            bpt = 3
        levelstring.append(bpt)
        levelstring.append(len(matlist) + 1)
        if bpt == 1:
            levelstring.append(len(tilelist))
            levelstring.append(0)
        else:
            for i in RWLParser.splitval(RWLParser.goodbin(len(tilelist), 16)):
                levelstring.append(int(i, 2))
        matlist.append(level["TE"]["defaultMaterial"])

        for i in tilelist:
            for l in i[1]:
                levelstring.append(ord(l))
            levelstring.append(255)
            levelstring.append(i[0][0])
            levelstring.append(i[0][1])
            levelstring.append(255)
            if len(i) == 3:
                c = RWLParser.splitval(RWLParser.goodbin(i[2][0] + 256, 16))
                levelstring.append(c[0])
                levelstring.append(c[1])
                c = RWLParser.goodbin(i[2][1] + 256, 16)
                levelstring.append(c[0])
                levelstring.append(c[1])
                levelstring.append(255)
        for i in matlist:
            for l in i:
                levelstring.append(ord(l))
            levelstring.append(255)

        # encodecodes = [[] for _ in range(size[0] * size[1])]

        for lp in range(3):
            for xp, x in enumerate(level["TE"]["tlMatrix"]):
                for yp, y in enumerate(x):
                    curpoint = xp * size[1] + yp
                    if skiptiles > 0:
                        skiptiles -= 1
                        # encodecodes[curpoint].append("")
                        continue
                    type = y[lp]["tp"]
                    data = y[lp]["data"]
                    tile = "0"
                    match type:
                        case "default":
                            curpoint = xp * size[1] + yp
                            charge = 0
                            while charge < 63:
                                nextpoint = curpoint + charge + 1
                                nextpos = [nextpoint // size[1], nextpoint % size[1]]
                                if nextpoint + 1 >= size[0] * size[1]:
                                    break
                                if level["TE"]["tlMatrix"][nextpos[0]][nextpos[1]][lp]["tp"] != "default":
                                    break
                                charge += 1
                            tile = "00" + RWLParser.goodbin(charge, 6)
                            skiptiles = charge

                        case "material":
                            index = matlist.index(data)
                            curpoint = xp * size[1] + yp
                            charge = 0
                            while charge < 63:
                                nextpoint = curpoint + charge + 1
                                nextpos = [nextpoint // size[1], nextpoint % size[1]]
                                if nextpoint + 1 >= size[0] * size[1]:
                                    break
                                if level["TE"]["tlMatrix"][nextpos[0]][nextpos[1]][lp]["tp"] != "material" or \
                                        level["TE"]["tlMatrix"][nextpos[0]][nextpos[1]][lp]["data"] != data:
                                    break
                                charge += 1
                            tile = "01" + RWLParser.goodbin(charge, 6) + RWLParser.goodbin(index, 8)
                            skiptiles = charge
                        case "tileBody":
                            pos = fromarr(data[0], "point")
                            # print(pos[0] - 1, pos[1] - 1, "|", xp, yp)
                            offset = [pos[0] - 1 - xp + 32, pos[1] - 1 - yp + 32]
                            #print(offset)
                            tile = "10" + RWLParser.goodbin(data[1], 2) + RWLParser.goodbin(offset[0], 6) + \
                                   RWLParser.goodbin(offset[1], 6)
                        case "tileHead":
                            t = [fromarr(data[0], "point"), data[1]]
                            tile = "11" + RWLParser.goodbin(tilelist.index(t), [6, 14, 22][bpt - 1])
                    # print(tile, y[lp])
                    for i in RWLParser.splitval(tile):
                        levelstring.append(int(i, 2))
                    # encodecodes[curpoint].append(tile)

        return levelstring


if __name__ == '__main__':
    # benchmark
    lvl = json.load(open("F:\Desktop\RWE#\levelEditorProjects\SU_A25.wep"))
    encoded = RWLParser.save_rwl(lvl)
    #print(encoded)
    open("F:\Desktop\RWE#\levelEditorProjects\SU_A25.rwl", "wb").write(encoded)
    decoded = RWLParser.parse_rwl(encoded)
    f = 0
    for xp, x in enumerate(decoded["TE"]["tlMatrix"]):
        for yp, y in enumerate(x):
            pos = xp * len(decoded["GE"][0]) + yp
            c = lvl["TE"]["tlMatrix"][xp][yp] == y
            if not c:
                f += 1
            # print("%4d: %30s | %16s,%16s,%16s %2s %16s,%16s,%16s | %30s" % (pos, " ".join([i["tp"] for i in lvl["TE"]["tlMatrix"][xp][yp]]), encodecodes[pos][0], encodecodes[pos][1], encodecodes[pos][2], "==" if c else "!=", decodecodes[pos][0], decodecodes[pos][1], decodecodes[pos][2], " ".join([i["tp"] for i in y]))) # encodecodes[pos], decodecodes[pos], y))
    print(f"failure: {f}")
    print(f"rwl: {len(encoded)}")
    print(f"txt: {len(str(lvl['TE']))}")
