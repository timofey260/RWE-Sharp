from RWESharp.ui.mainuiconnector import MainWindow
from RWESharp.ui.splashuiconnector import SplashDialog
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QCommandLineParser, QCommandLineOption
from RWESharp.info import FULLNAME, AUTHOR, VERSION, NAME

class CommandLineOptions:
    """
    List of command line options for application
    """
    def __init__(self, parser: QCommandLineParser):
        self.reset = QCommandLineOption(("r", "reset"), f"Reset {NAME}")
        self.nomods = QCommandLineOption(("M", "no-mods"), f"Load {NAME} without mods")
        self.debug = QCommandLineOption(("d", "debug"), f"Debug Mode")
        self.mainw = QCommandLineOption(("m", "no-main-window"), "Don't load Main Window(Only resource caching)")
        self.blocksave = QCommandLineOption(("s", "no-save"), "Don't save configurables")

        self.parser = parser
        self.parser.addOption(self.reset)
        self.parser.addOption(self.nomods)
        self.parser.addOption(self.debug)
        self.parser.addOption(self.mainw)
        self.parser.addOption(self.blocksave)

        self.parser.addVersionOption()
        self.parser.addHelpOption()

        self.parser.addPositionalArgument("filename", "Level to load")

class Application(QApplication):
    """
    Handles Splash, main menu loading and command line arguments
    """
    def __init__(self):
        from RWESharp.Core.Manager import Manager
        super().__init__(sys.argv)
        self.setApplicationName(NAME)
        self.setApplicationDisplayName(FULLNAME)
        self.setOrganizationName(AUTHOR)
        self.setApplicationVersion(VERSION)

        self.parser: QCommandLineParser = QCommandLineParser()
        self.args: CommandLineOptions = CommandLineOptions(self.parser)
        self.parser.setApplicationDescription(f"Console version of {NAME}\nCan render levels")

        self.parser.process(self)
        self.args2: list[str] = self.parser.positionalArguments()

        self.splash: SplashDialog = SplashDialog(self.post_init)
        self.window: MainWindow | None = None
        self.manager: Manager | None = None
        sys.exit(self.exec())

    def post_init(self) -> None:
        if self.parser.isSet(self.args.mainw):
            return
        if not self.splash.loader.load_success:
            print("LOAD FAILURE")
            self.exit(1)
            return
        if len(self.args2) == 1:
            self.window = MainWindow(self, self.args2[0])
            # manager.new_process(args.filename)
        else:
            self.window = MainWindow(self)
        self.manager = self.window.manager
        self.window.show()
        # sys.exit(self.exec())

    @property
    def debug(self) -> bool:
        return self.parser.isSet(self.args.debug)

    def close(self):
        print("Closing...")
        self.manager.close()
        self.exit(0)

    def restart(self) -> None:
        self.window.deleteLater()
        self.window.manager = None
        self.post_init()
