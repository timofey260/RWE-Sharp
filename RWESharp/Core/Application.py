from RWESharp.ui.mainuiconnector import MainWindow
from RWESharp.ui.splashuiconnector import SplashDialog
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QCommandLineParser, QCommandLineOption
from RWESharp.info import FULLNAME, AUTHORS, VERSION, NAME

class CommandLineOptions:
    """
    List of command line options for application
    """
    def __init__(self, parser: QCommandLineParser):
        self.reset = QCommandLineOption(("r", "reset"), f"Reset {NAME}")
        self.nomods = QCommandLineOption(("M", "no-mods"), f"Load {NAME} without mods")
        self.debug = QCommandLineOption(("d", "debug"), f"Debug Mode")

        self.parser = parser
        self.parser.addOption(self.reset)
        self.parser.addOption(self.nomods)
        self.parser.addOption(self.debug)

        self.parser.addVersionOption()
        self.parser.addHelpOption()

        self.parser.addPositionalArgument("filename", "Level to load")

class Application(QApplication):
    """
    Holds loading and main menu window together
    """
    def __init__(self):
        from RWESharp.Core.Manager import Manager
        super().__init__(sys.argv)
        self.setApplicationName(NAME)
        self.setApplicationDisplayName(FULLNAME)
        self.setOrganizationName(AUTHORS)
        self.setApplicationVersion(VERSION)

        self.parser = QCommandLineParser()
        self.args = CommandLineOptions(self.parser)
        self.parser.setApplicationDescription(f"Console version of {NAME}\nCan render levels")

        self.parser.process(self)
        self.args2 = self.parser.positionalArguments()

        self.splash = SplashDialog(self.post_init)
        self.window: MainWindow | None = None
        self.manager: Manager | None = None
        sys.exit(self.exec())

    def post_init(self) -> None:
        print(self.args2)
        if len(self.args2) == 1:
            self.window = MainWindow(self, self.args2[0])
            # manager.new_process(args.filename)
        else:
            self.window = MainWindow(self)
        self.manager = self.window.manager
        self.window.show()
        # sys.exit(self.app.exec())

    @property
    def debug(self) -> bool:
        return self.parser.isSet(self.args.debug)

    def restart(self) -> None:
        self.window.deleteLater()
        self.window.manager = None
        self.post_init()
