from core.info import *
from ui.mainuiconnector import MainWindow
import argparse
from core.Manager import Manager
import sys
from PySide6.QtWidgets import QApplication


if __name__ == "__main__":
    manager = Manager()

    parser = argparse.ArgumentParser(NAME, description="Console version of RWE#\n"
                                                       "Can render levels",

                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-v", "--version", help="show current RWE# version and exit", action="version")
    # parser.add_argument("-a", "--authors", help="shows all rwee developers", action="authors")
    parser.add_argument("filename", type=str, nargs="?", help="Level to load")
    parser.add_argument("-M", "--nomods", help="Use mods or load without them")
    parser.version = VERSION
    parser.authors = AUTHORS

    args = parser.parse_args()

    app = QApplication(sys.argv)
    window = MainWindow()
    if args.filename is not None:
        manager.new_process(args.filename)
    else:
        manager.new_process()
    window.show()
    sys.exit(app.exec())
