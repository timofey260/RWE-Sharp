from core.info import *
from ui.mainuiconnector import MainWindow
import argparse
import sys
from PySide6.QtWidgets import QApplication


if __name__ == "__main__":

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

    if args.filename is not None:
        app = QApplication(sys.argv)
        window = MainWindow(args.filename)
        #manager.new_process(args.filename)
        window.show()
        sys.exit(app.exec())
    else:
        pass
        #manager.new_process()
