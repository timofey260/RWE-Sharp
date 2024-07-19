from ui.mainuiconnector import MainWindow
from ui.splashuiconnector import SplashDialog
import sys
from PySide6.QtWidgets import QApplication


class Application:
    """
    Holds loading and main menu window together
    """
    def __init__(self, args, argv):
        self.app = QApplication(argv)
        self.splash = SplashDialog(self.post_init)
        self.args = args
        self.window: MainWindow | None = None
        sys.exit(self.app.exec())

    def post_init(self):
        if self.args.filename is not None:
            self.window = MainWindow(self, self.args.filename)
            # manager.new_process(args.filename)

        else:
            self.window = MainWindow(self)
        self.window.show()
        # sys.exit(self.app.exec())

    def restart(self):
        self.window.deleteLater()
        self.window.manager = None
        self.post_init()
