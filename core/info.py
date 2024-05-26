import os
import sys
import jsoncomment
import datetime

json = jsoncomment.JsonComment()

if getattr(sys, 'frozen', False):
    PATH = os.path.dirname(sys.executable)
else:
    from pathlib import Path
    PATH = str(Path(__file__).parent.parent.absolute())

PATH_FILES = os.path.join(PATH, "files")
PATH_FILES_CACHE = os.path.join(PATH_FILES, "cache")
PATH_FILES_IMAGES = os.path.join(PATH_FILES, "images")
PATH_FILES_IMAGES_PALETTES = os.path.join(PATH_FILES_IMAGES, "palettes")
PATH_MODS = os.path.join(PATH_FILES, "mods")
PATH_DRIZZLE = os.path.join(PATH, "drizzle")
PATH_MAT_PREVIEWS = os.path.join(PATH_FILES_IMAGES, "material_previews")


ISLINUX = sys.platform == "linux" or sys.platform == "linux2"
ISMAC = sys.platform == "darwin"
ISWIN = not ISMAC and not ISLINUX


VERSION = "0.0.1"
AUTHOR = "timofey26"
AUTHORS = "timofey26, atom"
NAME = "RWE#"
PROGNAME = "RWESharp.exe" if ISWIN else "RWESharp"
FULLNAME = "Rain World Editor Sharp"

RP_ID = "1226198202454380677"

CONSTS: dict = json.load(open(os.path.join(PATH_FILES, "Consts.json")))
"""
these things should never be changed
"""
CELLSIZE = CONSTS.get("cellsize", 20)
"""
size of single cell
can be interpreted as viewport quality
"""
SPRITESIZE = CONSTS.get("spritesize", 16)
"""
size of tile sprite
"""

print("clearing load log")
if os.path.exists(os.path.join(PATH, "loadLog.txt")):
    with open(os.path.join(PATH, "loadLog.txt"), "w") as file:
        file.write("log started!\n")


def log_to_load_log(message, error=False):
    with open(os.path.join(PATH, "loadLog.txt"), "a") as file:
        msg = f"[{datetime.datetime.now().strftime('%H:%M')}; {'ERROR' if error else ' INFO'}]: {message}\n"
        file.write(msg)
        print(msg, end="")