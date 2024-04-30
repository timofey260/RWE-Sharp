from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtCore import Slot
from PySide6.QtGui import QKeySequence, QShortcut
from ui.uiscripts.mainui import Ui_MainWindow
from ui.aboutuiconnector import AboutDialog
from core import info
from core.Manager import Manager


class MainWindow(QMainWindow):
    def __init__(self, filename=None):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionClose.triggered.connect(self.close)
        self.ui.actionAbout.triggered.connect(self.open_about)
        self.manager = Manager(filename)
        self.ui.viewPort.manager = self.manager
        self.ui.viewPort.add_managed_fields()
        self.about = None
        self.setStatusTip("Layer: 0, Placing: Wall")



    @Slot()
    def open_about(self):
        self.about = AboutDialog(self)
        self.about.show()

    @Slot()
    def close(self):
        print("imagine it closes")

    @Slot()
    def open_file(self):
        print("open")
        QFileDialog.getOpenFileName(None, "Open Level", info.application_path)


