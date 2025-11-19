import os
import sys
import json

if getattr(sys, 'frozen', False):
    PATH = os.path.dirname(sys.executable)
    """Path to RWE#'s folder"""
    PE = True
else:
    from pathlib import Path
    PATH = str(Path(__file__).parent.parent.absolute())
    """Path to RWE#'s folder"""
    PE = False

PATH_FILES = os.path.join(PATH, "files")
"""Path to ./files"""
PATH_FILES_VIDEOS = os.path.join(PATH_FILES, "videos")
"""Path to ./files/videos"""
PATH_FILES_CACHE = os.path.join(PATH_FILES, "cache")
"""Path to ./files/cache"""
PATH_FILES_IMAGES = os.path.join(PATH_FILES, "images")
"""Path to ./files/images"""
PATH_FILES_IMAGES_PALETTES = os.path.join(PATH_FILES_IMAGES, "palettes")
"""Path to ./files/palettes"""
PATH_MODS = os.path.join(PATH_FILES, "mods")
"""Path to ./files/mods"""
PATH_DRIZZLE = os.path.join(PATH, "drizzle")
"""Path to ./drizzle"""
PATH_LEVELS = os.path.join(PATH, "levelEditorProjects")
"""Path to ./levelEditorProjects"""
PATH_EFFECT_PREVIEWS = os.path.join(PATH_FILES, "effectPreviews")
"""Path to ./files/effectPreviews"""
PATH_MAT_PREVIEWS = os.path.join(PATH_FILES_IMAGES, "material_previews")
"""Path to ./files/images/material_previews"""
PATH_COLLECTIONS_TILES = os.path.join(PATH_FILES, "collections/tiles")
"""Path to ./files/collection/tiles"""
PATH_COLLECTIONS_PROPS = os.path.join(PATH_FILES, "collections/props")
"""Path to ./drizzle"""
PATH_DRIZZLE_TILES = os.path.join(PATH_DRIZZLE, "Data/Graphics")
"""Path to ./drizzle/Data/Graphics"""
PATH_DRIZZLE_PROPS = os.path.join(PATH_DRIZZLE, "Data/Props")
"""Path to ./drizzle/Data/Props"""
PATH_DRIZZLE_CAST = os.path.join(PATH_DRIZZLE, "Data/Cast")
"""Path to ./drizzle/Data/Cast"""

if not os.path.exists(PATH_DRIZZLE):  # todo finish database
    print("DRIZZLE NOT FOUND")

assert os.path.exists(PATH_DRIZZLE), "drizzle not found"

ISLINUX = sys.platform == "linux" or sys.platform == "linux2"  # tf is linux2
"""Checks if user is using windows"""
ISMAC = sys.platform == "darwin"
"""Checks if user is using mac"""
ISWIN = not ISMAC and not ISLINUX
"""Checks if user is using windows"""


VERSION = "0.0.1"
"""RWE#'s version"""
AUTHOR = "timofey26"
"""Literally me"""
AUTHORS = "timofey26, atom, Lang0s and Xeno"
"""RWE#'s authors"""
NAME = "RWE#"
"""Application name"""
PROGNAME = "RWS.exe" if ISWIN else "RWS"
"""Application executable name"""
FULLNAME = "Rain World Editor Sharp"
"""Application full name"""
REPO = r"https://github.com/timofey260/RWE-Sharp/"
"""RWE# repo"""
REPO_ISSUES = r"https://github.com/timofey260/RWE-Sharp/issues/"
"""RWE# issues"""
REPO_DOWNLOAD = r"https://github.com/timofey260/RWE-Sharp/releases/"
"""RWE# releases page"""
REPO_DOWNLOAD_LATEST = r"https://github.com/timofey260/RWE-Sharp/releases/latest/"
"""Latest RWE# release"""
REPO_DATABASE = r"https://raw.githubusercontent.com/timofey260/RWE-Sharp-Database/refs/heads/main/baseinfo.json"
"""Link to RWE#'s database"""

CUSTOM_LINKS = {
    "Rain World Wiki": "https://rainworld.miraheze.org/wiki/Rain_World_Wiki",
    "Modding Wiki": "https://rainworldmodding.miraheze.org/wiki/Main_Page",
    "RWMA Discord Server": "https://discord.gg/rainworldmodding",
    "Interactive Map": "https://henpemaz.github.io/Rain-World-Interactive-Map/",
    "RWE# Mod Database": "https://github.com/timofey260/RWE-Sharp-Database"
}
"""Custom links for other repos"""

if os.path.exists(os.path.join(PATH_FILES, "Consts.json")):
    with open(os.path.join(PATH_FILES, "Consts.json")) as f:
        CONSTS = json.load(f)  # NOQA
        """
        Constants, shouldn't be changed

        Check files/Consts.json
        """
else:
    CONSTS = {}
CELLSIZE = CONSTS.get("cellsize", 20)
"""
Size of single cell

Can be interpreted as viewport quality
"""

SPRITESIZE = CONSTS.get("spritesize", 16)
"""Size of single tile sprite cell"""

camw = 70
"""Camera width(in cells)"""
camh = 40
"""Camera height(in cells)"""

ofsleft = 15
"""Amount in blocks to add to light image to left"""
ofstop = 15
"""Amount in blocks to add to light image to top"""

wladd = 5.7
"""Addition to water level in blocks"""

_LOG = open(os.path.join(PATH, "loadLog.txt"), "w")
"""Log file, check RWESharp.utils.log"""

os.makedirs(PATH_MODS, exist_ok=True)
os.makedirs(PATH_COLLECTIONS_PROPS, exist_ok=True)
os.makedirs(PATH_COLLECTIONS_TILES, exist_ok=True)
os.makedirs(PATH_FILES_CACHE, exist_ok=True)
os.makedirs(PATH_LEVELS, exist_ok=True)
