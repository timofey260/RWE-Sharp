from core.info import *
from ui.mainuiconnector import MainWindow
from ui.splashuiconnector import SplashDialog
import argparse
import sys
from PySide6.QtWidgets import QApplication

args = None
app = None
splash = None


def main(argv):
    global args, app, splash
    print("""
       ___ _      ______  ____ 
      / _ \ | /| / / __/_/ / /_
     / , _/ |/ |/ / _//_  . __/
    /_/|_||__/|__/___/_    __/ 
                      /_/_/    

    RWE# - timofey26 and atom
    """)
    parser = argparse.ArgumentParser(PROGNAME, description="Console version of RWE#\n"
                                                           "Can render levels",

                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-v", "--version", help="show current RWE# version and exit", action="version")
    # parser.add_argument("-a", "--authors", help="shows all rwee developers", action="authors")
    parser.add_argument("filename", type=str, nargs="?", help="Level to load")
    parser.add_argument("-M", "--nomods", dest="nomods", help="Use mods or load without them", action="store_true")
    parser.version = VERSION
    parser.authors = AUTHORS

    args = parser.parse_args()

    app = QApplication(argv)
    # loading of tiles etc
    splash = SplashDialog(post_init)

# problem: splash screen and thread gets garbage collected
def post_init():
    print("post")
    if args.filename is not None:
        window = MainWindow(splash, args.filename)
        # manager.new_process(args.filename)

    else:
        window = MainWindow(splash)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main(sys.argv)
