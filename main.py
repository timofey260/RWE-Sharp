from core.stuff import *
from ui.mainuiconnector import MainWindow
import argparse

import sys
from PySide6.QtWidgets import QApplication


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":

    parser = argparse.ArgumentParser(NAME, description="Console version of RWE#\n"
                                                       "Can render levels",

                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-v", "--version", help="show current RWE# version and exit", action="version")
    # parser.add_argument("-a", "--authors", help="shows all rwee developers", action="authors")
    parser.add_argument("filename", type=str, nargs="?", help="Level to load")
    parser.version = VERSION
    parser.authors = AUTHORS

    args = parser.parse_args()

