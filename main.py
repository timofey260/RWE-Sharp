from core.info import *
import argparse
import sys
from core.Application import Application


def main(argv):
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

    app = Application(args, argv)


if __name__ == "__main__":
    main(sys.argv)
