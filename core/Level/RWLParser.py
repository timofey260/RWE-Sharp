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
import re
import zipfile
from core.Level.RWELevel import RWELevel
from core.info import PATH_LEVELS
import os


VER = 1
ENCODING = "latin-1"

_stacklist = [1, 2, 11, 3, 4, 5, 6, 7, 9, 10, 12, 13, 19, 21, 20, 18]
_accepted = [0, 1, 6, 9]
_blocks = [0, 1, 2, 3, 4, 5, 6, 9]


class RWLParser:
    @staticmethod
    def parse_rwl(string: str) -> RWELevel:
        mtlevel = RWELevel(None)

        version = 0
        width, height = 10, 10
        light = False
        borders = [0, 0, 0, 0]
        tile_seed = 0
        with zipfile.ZipFile(string) as content:
            with content.open("info") as f:
                lines = [i.decode() for i in f.readlines()]
                version = int(lines[0])
                width, height = [int(i) for i in lines[1].split(";")]
                borders = [int(i) for i in lines[2].split(";")]
                light = lines[3] == "1"
                tile_seed = int(lines[4])
            print(version, width, height, borders, light, tile_seeds)
        return mtlevel


    @staticmethod
    def save_rwl(level: RWELevel) -> bytearray:
        pass

if __name__ == '__main__':
    # benchmark
    # lvl = RWELevel(None, "/levelEditorProjects/SU_A25.wep")
    # encoded = RWLParser.save_rwl(lvl)
    #print(encoded)
    # open("/levelEditorProjects/SU_A25.rwl", "wb").write(encoded)
    # decoded = RWLParser.parse_rwl(encoded)
    level = RWLParser.parse_rwl(os.path.join(PATH_LEVELS, "level.rwl"))
