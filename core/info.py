import os
import sys
import jsoncomment

json = jsoncomment.JsonComment()

if getattr(sys, 'frozen', False):
    PATH = os.path.dirname(sys.executable)
    PE = True
else:
    from pathlib import Path
    PATH = str(Path(__file__).parent.parent.absolute())
    PE = False

PATH_FILES = os.path.join(PATH, "files")
PATH_FILES_VIDEOS = os.path.join(PATH_FILES, "videos")
PATH_FILES_CACHE = os.path.join(PATH_FILES, "cache")
PATH_FILES_IMAGES = os.path.join(PATH_FILES, "images")
PATH_FILES_IMAGES_PALETTES = os.path.join(PATH_FILES_IMAGES, "palettes")
PATH_MODS = os.path.join(PATH_FILES, "mods")
PATH_DRIZZLE = os.path.join(PATH, "drizzle")
PATH_LEVELS = os.path.join(PATH, "levelEditorProjects")
PATH_EFFECT_PREVIEWS = os.path.join(PATH_FILES, "effectPreviews")
PATH_MAT_PREVIEWS = os.path.join(PATH_FILES_IMAGES, "material_previews")
PATH_COLLECTIONS_TILES = os.path.join(PATH_FILES, "collections/tiles")
PATH_COLLECTIONS_PROPS = os.path.join(PATH_FILES, "collections/props")
PATH_DRIZZLE_TILES = os.path.join(PATH_DRIZZLE, "Data/Graphics")
PATH_DRIZZLE_PROPS = os.path.join(PATH_DRIZZLE, "Data/Props")
PATH_DRIZZLE_CAST = os.path.join(PATH_DRIZZLE, "Data/Cast")

if not os.path.exists(PATH_DRIZZLE):  # todo finish database
    print("DRIZZLE NOT FOUND")

assert os.path.exists(PATH_DRIZZLE), "drizzle not found"

ISLINUX = sys.platform == "linux" or sys.platform == "linux2"  # tf is linux2
ISMAC = sys.platform == "darwin"
ISWIN = not ISMAC and not ISLINUX


VERSION = "0.0.1"
AUTHOR = "timofey26"
AUTHORS = "timofey26, atom, Lang0s and Xeno"
NAME = "RWE#"
PROGNAME = "RWESharp.exe" if ISWIN else "RWESharp"
FULLNAME = "Rain World Editor Sharp"
REPO = r"https://github.com/timofey260/RWE-Sharp/"
REPO_ISSUES = r"https://github.com/timofey260/RWE-Sharp/issues/"
REPO_DOWNLOAD = r"https://github.com/timofey260/RWE-Sharp/releases/"
REPO_DOWNLOAD_LATEST = r"https://github.com/timofey260/RWE-Sharp/releases/latest/"
REPO_DATABASE = r"https://raw.githubusercontent.com/timofey260/RWE-Sharp-Database/refs/heads/main/baseinfo.json"

CUSTOM_LINKS = {
    "Rain World Wiki": "https://rainworld.miraheze.org/wiki/Rain_World_Wiki",
    "Modding Wiki": "https://rainworldmodding.miraheze.org/wiki/Main_Page",
    "RWMA Discord Server": "https://discord.gg/rainworldmodding",
    "Interactive Map": "https://henpemaz.github.io/Rain-World-Interactive-Map/",
    "RWE# Mod Database": "https://github.com/timofey260/RWE-Sharp-Database"
}

CONSTS: dict = {}
"""
these things should never be changed
"""
with open(os.path.join(PATH_FILES, "Consts.json")) as f:
    CONSTS = json.load(f)  # NOQA
CELLSIZE = CONSTS.get("cellsize", 20)
"""
size of single cell
can be interpreted as viewport quality
"""
SPRITESIZE = CONSTS.get("spritesize", 16)
"""
size of single tile sprite cell
"""

camw = 70
"""
Camera width(in cells)
"""
camh = 40
"""
Camera height(in cells)
"""

ofsleft = 15
"""
Amount in blocks to add to light image to left 
"""
ofstop = 15
"""
Amount in blocks to add to light image to left
"""

wladd = 5.7
"""
Addition to water level in blocks
"""

LOG = open(os.path.join(PATH, "loadLog.txt"), "w")

os.makedirs(PATH_MODS, exist_ok=True)
os.makedirs(PATH_COLLECTIONS_PROPS, exist_ok=True)
os.makedirs(PATH_COLLECTIONS_TILES, exist_ok=True)
os.makedirs(PATH_FILES_CACHE, exist_ok=True)
os.makedirs(PATH_LEVELS, exist_ok=True)
