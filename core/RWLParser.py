"""
Slug parser

parses .rwl files into dict and vise versa

you would need it: https://docs.google.com/document/d/1zcxeQGibkZORstwGQUovhQk71k00B69oYwkqFpGyOqs/edit#heading=h.7xts9mnasx5f

------

Specification:

1. properties:

first line of file is level properties

line with level size, extra tiles, sunlight, tile seed etc.

format: v;w h;el et er eb;l;s
    * v: slug version
    * w, h: width and height
    * el, et, er and eb: extra tiles(left, top right and bottom)
    * l: light(either 0 or 1)
    * s: tile seed

2. Geo

geo amount depends on level size we had added earlier

the reader checks exactly 7*width*height bytes in front of it

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
    |07| + room entrance                                     [ 6]
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
    - - might affect render on layers other than 1(not tested)
    + - good to be unused on other layers

2. tiles
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
        c1 = 0
        c2 = 0
        c3 = 0
        c4 = 0
        for i in range(0, size[0] * size[1]):
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
                    c1 += 1
                case "01":
                    cblock = copy.deepcopy(history[int(curbin[2:8], 2)])
                    c2 += 1
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
                    c3 += 1
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
                    c4 += 1
            # decodecodes.append(curbin)
            level["GE"][poscursor[0]][poscursor[1]] = cblock
            history.insert(0, cblock)
            history = history[:64]
        print(c1, c2, c3, c4)


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
        levelstring = bytearray("", ENCODING)
        # level properties
        size = fromarr(level["EX2"].get("size"), "point")
        extra = level["EX2"].get("extraTiles")
        light = level["EX2"].get("light")
        seed = level["EX2"].get("tileSeed")
        levelstring += f"{VER};{size[0]} {size[1]};{extra[0]} {extra[1]} {extra[2]} {extra[3]};{light};{seed}\n".encode(ENCODING)
        # geo
        lastgeo = []
        say = True

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
                    if say:
                        print(indx, y, lastgeo)
                        say = False
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
                print(y, newstr)
                for i in RWLParser.splitval(newstr):
                    levelstring.append(int(i, 2))
                # encodecodes.append([newstr, y])
                lastgeo.insert(0, y)
                lastgeo = lastgeo[:64]
        #level["GE"]
        return levelstring

if __name__ == '__main__':
    # benchmark
    lvl = json.load(open("F:\Desktop\RWE#\levelEditorProjects\SU_A25.wep"))
    encoded = RWLParser.save_rwl(lvl)
    #print(encoded)
    decoded = RWLParser.parse_rwl(encoded)
    open("F:\Desktop\RWE#\levelEditorProjects\SU_A25.rwl", "wb").write(encoded)
    f = 0
    for xp, x in enumerate(decoded["GE"]):
        for yp, y in enumerate(x):
            pos = xp * len(decoded["GE"][0]) + yp
            c = lvl["GE"][xp][yp] == y
            if not c:
                f += 1
            print("%4d: %40s | %40s [%2s] %40s | %40s" % (pos, lvl["GE"][xp][yp], encodecodes[pos][0], "==" if c else "!=", decodecodes[pos], y))
            # 1101100100100000000000000000000000000000
            # 1101100100100000001101100100011011001000011011001
            # [[7, [4, 7, 9, 20]], [1, [11, 3]], [1, [3]]]
    print(f"failure: {f}")
    print(f"rwl: {len(encoded)}")
    print(f"txt: {len(str(lvl['GE']))}")
