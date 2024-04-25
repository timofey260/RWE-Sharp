import os
import sys

if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
else:
    from pathlib import Path
    application_path = str(Path(__file__).parent.parent.absolute())

VERSION = "0.0.1"
AUTHORS = "timofey26"
NAME = "RWE#"
FULLNAME = "Rain World Editor Sharp"

RP_ID = "1226198202454380677"