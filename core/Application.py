from ui.mainuiconnector import MainWindow
from ui.splashuiconnector import SplashDialog
import sys
from PySide6.QtWidgets import QApplication


class Application:
    def __init__(self, args, argv):
        self.app = QApplication(argv)
        self.splash = SplashDialog(self.post_init)
        self.args = args
        self.window = None
        sys.exit(self.app.exec())

    def post_init(self):
        if self.args.filename is not None:
            self.window = MainWindow(self.splash, self.args.filename)
            # manager.new_process(args.filename)

        else:
            self.window = MainWindow(self.splash)
        self.window.show()
        # sys.exit(self.app.exec())
