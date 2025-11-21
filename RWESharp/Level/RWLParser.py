"""
Slug parser

parses .rwl files into dict and vise versa

you would need it: https://docs.google.com/document/d/1zcxeQGibkZORstwGQUovhQk71k00B69oYwkqFpGyOqs/edit#heading=h.7xts9mnasx5f

Todo: write a better docs about this
"""
import json
import zipfile

from RWESharp.Core.lingoIO import frompoint, tojson, makearr
from RWESharp.Level.RWELevel import RWELevel, defaultlevellines, minimallevellines
from RWESharp.info import PATH_LEVELS
from RWESharp.Core.Exceptions import FileStorageError
import numpy as np
import os
from enum import auto, Flag

class StoreRWL(Flag):
    Geometry = auto()
    Tiles = auto()
    Props = auto()
    Cameras = auto()
    Properties = auto()
    Effects = auto()
    Custom = auto()

STORE_EVERYTHING = StoreRWL.Geometry | StoreRWL.Tiles | StoreRWL.Props | StoreRWL.Cameras | StoreRWL.Effects | StoreRWL.Properties | StoreRWL.Custom


VER = 1
# ENCODING = "latin-1"


class RWLParser:
    @staticmethod
    def parse_rwl(string: str, store=STORE_EVERYTHING) -> tuple[dict, bytes | None]:
        proj = {}
        version = VER
        width, height = 72, 43
        borders = [0, 0, 0, 0]
        lightimage = None
        with zipfile.ZipFile(string) as content:
            proj["EX2"] = tojson(defaultlevellines[5])
            proj["EX"] = tojson(defaultlevellines[4])
            proj["LE"] = tojson(defaultlevellines[3])
            proj["TE"] = tojson(minimallevellines[1])
            proj["WL"] = tojson(minimallevellines[7])
            with content.open("info") as f:
                lines = [i.decode() for i in f.readlines()]
                version = int(lines[0])
                width, height = [int(i) for i in lines[1].split(";")]
                proj["EX2"]["size"] = makearr([width, height], "point")
                borders = [int(i) for i in lines[2].split(";")]
                proj["EX2"]["extraTiles"] = borders
                lightprops = lines[3].split(";")
                proj["EX2"]["light"] = lightprops[0] == "1"
                proj["LE"]["lightAngle"] = int(lightprops[1])
                proj["LE"]["flatness"] = int(lightprops[2])
                proj["EX2"]["tileSeed"] = int(lines[4])
                proj["TE"]["defaultMaterial"] = lines[5].replace("\n", "")
                proj["WL"]["waterLevel"] = int(lines[6])
                proj["WL"]["waterInFront"] = int(lines[7])
            proj["GE"] = []
            from BaseMod.LevelParts import GeoLevelPart
            with content.open("geo") as geo:
                for x in range(width):
                    proj["GE"].append([])
                    for y in range(height):
                        proj["GE"][-1].append([])
                        for l in range(3):
                            proj["GE"][-1][-1].append([int.from_bytes(geo.read(1)), GeoLevelPart.byte2stack(np.frombuffer(geo.read(2), dtype=np.uint16))])
            unique_tiles = {}
            with content.open("tilenames") as tilenames:
                for tile in tilenames.read().decode().split("\n"):
                    s = tile.split(";")
                    unique_tiles[s[0]] = [int(s[1]), int(s[2])]
            unique_materials = []
            with content.open("materials") as materials:
                unique_materials = materials.read().decode().split("\n")
            # print(unique_materials, unique_tiles)
            with content.open("tiles") as tiles:
                for x in range(width):
                    proj["TE"]["tlMatrix"].append([])
                    for y in range(height):
                        proj["TE"]["tlMatrix"][-1].append([])
                        for l in range(3):
                            first = int.from_bytes(tiles.read(1))
                            if first == 0:  # default
                                proj["TE"]["tlMatrix"][-1][-1].append({"tp": "default", "data": 0})
                            elif first & 128 == 0:  # material
                                proj["TE"]["tlMatrix"][-1][-1].append({"tp": "material", "data": unique_materials[(first & 127) - 1]})
                            elif first & 128 == 128:  # tile head/tile body
                                second = int.from_bytes(tiles.read(1))
                                ishead = second & 1 == 0
                                if ishead:
                                    tile = first & 127 + ((second & 126) << 7)
                                    tilename = list(unique_tiles.keys())[tile]
                                    proj["TE"]["tlMatrix"][-1][-1].append({"tp": "tileHead", "data": [makearr(unique_tiles[tilename], "point"), tilename]})
                                    continue
                                third = int.from_bytes(tiles.read(1))
                                # print(bin((third << 16) + (second << 8) + first), third, second, first)
                                layer = first & 3  # magic numbers my beloved
                                ypos = ((first & 124) >> 2) + ((second & 62) << 4) - 512
                                xpos = ((second & 192) >> 6) + (third << 2) - 512
                                # print(xpos, ypos, x, y)
                                xpos = x - xpos
                                ypos = y - ypos
                                # print(xpos, ypos, layer)
                                proj["TE"]["tlMatrix"][-1][-1].append({"tp": "tileBody", "data": [makearr([xpos, ypos], "point"), layer]})
                            else:
                                print("the what")
            proj["FE"] = tojson(minimallevellines[2])
            with content.open("effects") as effects:
                amount = int(effects.readline().decode())
                for i in range(amount):
                    effect = {}
                    stats = effects.readline().decode().rstrip("\n").split(";")
                    effect["nm"] = stats[0]
                    effect["tp"] = stats[1]
                    if stats[2] != "":
                        effect["repeats"] = int(stats[2])
                    if stats[3] != "":
                        effect["affectOpenAreas"] = float(stats[3])
                    if stats[4] != "":
                        effect["crossScreen"] = int(stats[4])
                    optionsamount = int(stats[5])
                    effect["options"] = []
                    for i in range(optionsamount):
                        option = effects.readline().decode().rstrip("\n").split(";")
                        name = option[0]
                        value = int(option[-1]) if name == "Seed" else option[-1]
                        effect["options"].append([name, option[1:-1], value])
                    effect["mtrx"] = []
                    for x in range(width):
                        effect["mtrx"].append([])
                        for y in range(height):
                            effect["mtrx"][-1].append(int.from_bytes(effects.read(1)))
                    proj["FE"]["effects"].append(effect)
            proj["PR"] = tojson(minimallevellines[8])
            with content.open("props") as props:
                amount = int(props.readline().decode().rstrip("\n"))
                for p in range(amount):
                    prop = []
                    stats = props.readline().decode().rstrip("\n").split(";")
                    prop.append(int(stats[0]))
                    prop.append(stats[1])
                    prop.append(makearr([stats[2], stats[3]], "point"))
                    xposes = [float(i) for i in props.readline().decode().rstrip("\n").split(";")]
                    yposes = [float(i) for i in props.readline().decode().rstrip("\n").split(";")]
                    prop.append([makearr([x, y], "point") for x, y in zip(xposes, yposes)])
                    settingsamount = int(props.readline().decode().rstrip("\n"))
                    prop.append({"settings": {}})
                    for s in range(settingsamount):
                        setting = props.readline().decode().rstrip("\n").split(";")
                        prop[4]["settings"][setting[0]] = int(setting[1])
                    proj["PR"]["props"].append(prop)
            proj["CM"] = tojson(minimallevellines[6])
            with content.open("cameras") as cameras:
                amount = int(cameras.readline().decode().rstrip("\n"))
                for c in range(amount):
                    proj["CM"]["cameras"].append(makearr(cameras.readline().decode().rstrip("\n").split(";"), "point"))
                    xposes = [float(i) for i in cameras.readline().decode().rstrip("\n").split(";")]
                    yposes = [float(i) for i in cameras.readline().decode().rstrip("\n").split(";")]
                    proj["CM"]["quads"].append([[x, y] for x, y in zip(xposes, yposes)])
            filenames = [i.filename for i in content.filelist]
            if "light.png" in filenames:
                with content.open("light.png") as light:
                    lightimage = light.read()
            if "custom" in filenames:
                with content.open("custom") as custom:
                    proj["CLD"] = json.loads(custom.read().decode())

        return proj, lightimage

    @staticmethod
    def save_rwl(level: dict, path: str, lightdata: bytes=None):
        with zipfile.ZipFile(path, "w") as content:
            size = [1, 1]
            with content.open("info", "w") as info:
                size = [int(i) for i in frompoint(level["EX2"]["size"])]
                info.write("\n".join([
                    "1",
                    f"{size[0]};{size[1]}",
                    ";".join([str(i) for i in level["EX2"]["extraTiles"]]),
                    f'{"1" if level["EX2"]["light"] == 1 else "0"};{level["LE"]["lightAngle"]};{level["LE"]["flatness"]}',
                    str(level["EX2"]["tileSeed"]),
                    level["TE"]["defaultMaterial"],
                    str(level["WL"]["waterLevel"]),
                    str(level["WL"]["waterInFront"])
                ]).encode())
            from BaseMod.LevelParts import GeoLevelPart
            with content.open("geo", "w") as geo:
                for x in level["GE"]:
                    for y in x:
                        for l in y:
                            geo.write(np.uint8(l[0]))
                            geo.write(GeoLevelPart.stack2byte(l[1]))
            with content.open("tiles", "w") as tiles:  # holy whitespace
                uniquematerials: list[str] = []
                uniquetiles: dict[str, [int, int]] = {}
                for ix, x in enumerate(level["TE"]["tlMatrix"]):
                    for iy, y in enumerate(x):
                        for l in y:
                            type = l["tp"].lower()
                            if type == "default":  # 00000000
                                tiles.write((0).to_bytes(1))
                            elif type == "material":  # 0xxxxxxx > 0
                                if l["data"] not in uniquematerials:
                                    uniquematerials.append(l["data"])
                                tiles.write((uniquematerials.index(l["data"]) + 1).to_bytes(1))
                            elif type == "tilehead":  # xxxxxxx0 1xxxxxxx
                                uniquetiles[l["data"][1]] = frompoint(l["data"][0])
                                num = list(uniquetiles.keys()).index(l["data"][1])
                                export = (128 + ((num & (127 << 7)) << 2) + (num & 127))
                                tiles.write((export & 255).to_bytes(1))
                                tiles.write(((export & 65280) >> 8).to_bytes(1))
                                # print(bin(export), (export & 65280) >> 8, export & 255)
                            elif type == "tilebody":  # XXXXXXXX XXYYYYY1 1YYYYYLL
                                layer = l["data"][1]
                                headpos = [int(i) for i in frompoint(l["data"][0])]
                                xpos = ix - headpos[0] + 512
                                ypos = iy - headpos[1] + 512
                                export = (384 + layer + (xpos << 14) + ((ypos & 31) << 2) + ((ypos & (31 << 5)) << 4))
                                tiles.write((export & 255).to_bytes(1))
                                tiles.write(((export & 65280) >> 8).to_bytes(1))
                                tiles.write(((export & 16711680) >> 16).to_bytes(1))
                                # print(xpos, ypos, xpos - 512, ypos - 512, ix, iy)
                                # print(bin(export), (export & 16711680) >> 16, (export & 65280) >> 8, export & 255)

                                # 0b100001000010000110110111 132 33 183
                                # 528 525 16 13   52 211

                                # 0b100001000010000110110111 132 33 183
                                # 16 13           13 156
                                # -3 143 3
                            else:
                                print("explode")
            if len(uniquematerials) > 127 or len(uniquetiles) > 16383:
                raise FileStorageError("File unable to store with rwl file format")
            with content.open("materials", "w") as materials:
                materials.write("\n".join(uniquematerials).encode())
            with content.open("tilenames", "w") as tilenames:
                tilenames.write("\n".join([f"{k};{v[0]};{v[1]}" for k, v in uniquetiles.items()]).encode())
            with content.open("effects", "w") as effects:
                effects.write(str(len(level["FE"]["effects"])).encode())
                effects.write("\n".encode())
                for i in level["FE"]["effects"]:
                    effects.write(";".join([i["nm"], i["tp"], str(i.get("repeats", "")), str(i.get("affectOpenAreas", "")), str(i.get("crossScreen", "")), str(len(i["options"]))]).encode())
                    effects.write("\n".encode())
                    for o in i["options"]:
                        effects.write(";".join([o[0], *o[1], str(o[2])]).encode())
                        effects.write("\n".encode())
                    # uh some small problem is that values might be less accurate because of rounding but tbh do we care about 0.1234 in 0 to 100?
                    for x in i["mtrx"]:
                        for y in x:
                            effects.write(int(y).to_bytes(1))
            with content.open("props", "w") as props:
                props.write(str(len(level["PR"]["props"])).encode())
                props.write("\n".encode())  # not sure if i should just do b"\n" but it isn't a big deal
                for p in level["PR"]["props"]:
                    catpos = frompoint(p[2])
                    props.write(";".join([str(p[0]), p[1], str(catpos[0]), str(catpos[1])]).encode())
                    props.write("\n".encode())
                    points = [frompoint(i) for i in p[3]]
                    props.write(";".join([str(i[0]) for i in points]).encode())
                    props.write("\n".encode())
                    props.write(";".join([str(i[1]) for i in points]).encode())
                    props.write("\n".encode())
                    props.write(str(len(p[4]["settings"])).encode())
                    props.write("\n".encode())
                    for k, v in p[4]["settings"].items():
                        props.write(f"{k};{v}".encode())
                        props.write("\n".encode())
            with content.open("cameras", "w") as cameras:
                cameras.write(str(len(level["CM"]["cameras"])).encode())
                cameras.write("\n".encode())
                for i, c in enumerate(level["CM"]["cameras"]):
                    cameras.write(";".join([str(d) for d in frompoint(c)]).encode())
                    cameras.write("\n".encode())
                    quads = level["CM"]["quads"][i]
                    cameras.write(";".join([str(q[0]) for q in quads]).encode())
                    cameras.write("\n".encode())
                    cameras.write(";".join([str(q[1]) for q in quads]).encode())
                    cameras.write("\n".encode())
            file, _ = os.path.splitext(path)
            if os.path.exists(file + ".png") or lightdata is not None:
                with content.open("light.png", "w") as light:
                    light.write(open(file + ".png", "rb").read() if lightdata is None else lightdata)
            if level.get("CLD") is None:
                return
            with content.open("custom", "w") as custom:
                custom.write(json.dumps(level["CLD"]).encode())


if __name__ == '__main__':
    # benchmark
    # lvl = RWELevel(None, "/levelEditorProjects/SU_A25.wep")
    # encoded = RWLParser.save_rwl(lvl)
    #print(encoded)
    # open("/levelEditorProjects/SU_A25.rwl", "wb").write(encoded)
    # decoded = RWLParser.parse_rwl(encoded)
    lvl = RWELevel.turntoproject(open(os.path.join(PATH_LEVELS, "HE_LEG.txt")).read())
    # level = RWLParser.parse_rwl(os.path.join(PATH_LEVELS, "level.rwl"))
    level_path = os.path.join(PATH_LEVELS, "HE_LEG.rwl")
    RWLParser.save_rwl(lvl.data, level_path)
    decoded, light = RWLParser.parse_rwl(level_path)
    print(light)
    with open(os.path.join(PATH_LEVELS, "decoded.wep"), "w") as f:
        f.write(json.dumps(decoded))
    # print(decoded)
