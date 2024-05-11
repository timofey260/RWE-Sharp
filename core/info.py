import os
import sys
import jsoncomment

json = jsoncomment.JsonComment()

if getattr(sys, 'frozen', False):
    PATH = os.path.dirname(sys.executable) + "\\"
else:
    from pathlib import Path
    PATH = str(Path(__file__).parent.parent.absolute()) + "\\"

PATH_FILES = PATH + "files\\"
PATH_FILES_IMAGES = PATH_FILES + "images\\"
PATH_MODS = PATH_FILES + "mods\\"
PATH_DRIZZLE = PATH + "drizzle\\"

ISLINUX = sys.platform == "linux" or sys.platform == "linux2"
ISMAC = sys.platform == "darwin"
ISWIN = not ISMAC and not ISLINUX


VERSION = "0.0.1"
AUTHORS = "timofey26"
NAME = "RWE#"
FULLNAME = "Rain World Editor Sharp"

RP_ID = "1226198202454380677"

CONSTS: dict = json.load(open(PATH_FILES + "Consts.json"))
CELLSIZE = CONSTS.get("cellsize", 20)