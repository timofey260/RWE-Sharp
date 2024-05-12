from PySide6.QtWidgets import QMainWindow, QFileDialog, QSpacerItem, QSizePolicy
from PySide6.QtCore import Slot
from PySide6.QtGui import QAction
from ui.uiscripts.mainui import Ui_MainWindow
from ui.aboutuiconnector import AboutDialog
from ui.settingsuiconnector import SettingsUI
from core import info
from core.Manager import Manager


class MainWindow(QMainWindow):
    '''
    Main window of RWE#
    '''
    def __init__(self, filename=None):
        """

        :param filename:  file to load by default
        """
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionClose.triggered.connect(self.close)
        self.ui.actionAbout.triggered.connect(self.open_about)
        self.ui.actionPreferences.triggered.connect(self.open_settings)
        self.manager = Manager(self, filename)

        self.ui.viewPort.add_managed_fields(self.manager)

        # self.ui.menuRecent.addAction(QAction("lol", self.ui.menuRecent))
        self.ui.ToolsTabs.currentChanged.connect(self.change_editor)
        self.about = None
        self.settings = None

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.ui.QuickOverlay.addItem(self.verticalSpacer)


    @Slot(int)
    def change_editor(self, val) -> None:
        print("editor changed to " + str(val))
        self.manager.change_editor(val)

    @Slot()
    def open_about(self) -> None:
        self.about = AboutDialog(self)
        self.about.show()

    @Slot()
    def open_settings(self) -> None:
        self.settings = SettingsUI(self)
        self.settings.show()

    @Slot()
    def close(self) -> None:
        print("imagine it closes")

    @Slot()
    def open_file(self) -> None:
        print("open")
        QFileDialog.getOpenFileName(None, "Open Level", info.PATH)


