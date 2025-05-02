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
PATH_BASEMOD = os.path.join(PATH, "BaseMod")
PATH_DRIZZLE_TILES = os.path.join(PATH_DRIZZLE, "Data/Graphics")
PATH_DRIZZLE_PROPS = os.path.join(PATH_DRIZZLE, "Data/Props")

assert os.path.exists(PATH_DRIZZLE), "No drizzle found"

ISLINUX = sys.platform == "linux" or sys.platform == "linux2"
ISMAC = sys.platform == "darwin"
ISWIN = not ISMAC and not ISLINUX


VERSION = "0.0.1"
AUTHOR = "timofey26"
AUTHORS = "timofey26, atom, Lang0s"
NAME = "RWE#"
PROGNAME = "RWESharp.exe" if ISWIN else "RWESharp"
FULLNAME = "Rain World Editor Sharp"
REPO = "https://github.com/timofey260/RWE-Sharp"
REPO_ISSUES = "https://github.com/timofey260/RWE-Sharp/issues"
REPO_DOWNLOAD = "https://github.com/timofey260/RWE-Sharp/releases"
REPO_DOWNLOAD_LATEST = "https://github.com/timofey260/RWE-Sharp/releases/latest"

RP_ID = "1226198202454380677"

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
size of tile sprite
"""

camw = 70
"""
Camera width(in cells)
"""
camh = 40
"""
Camera height(in cells)
"""

LOG = open(os.path.join(PATH, "loadLog.txt"), "w")

os.makedirs(PATH_MODS, exist_ok=True)
os.makedirs(PATH_COLLECTIONS_PROPS, exist_ok=True)
os.makedirs(PATH_COLLECTIONS_TILES, exist_ok=True)
os.makedirs(PATH_FILES_CACHE, exist_ok=True)
os.makedirs(PATH_LEVELS, exist_ok=True)
