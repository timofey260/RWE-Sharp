from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtCore import Slot
from PySide6.QtGui import QAction
from ui.uiscripts.mainui import Ui_MainWindow
from ui.aboutuiconnector import AboutDialog
from core.EditorModes.EditorMode import EditorMode
from core.EditorModes.GeometryEditor import GeometryEditor
from core import info
from core.Manager import Manager


class MainWindow(QMainWindow):
    '''
    Main window of RWE#

    :param filename: file to load by default
    '''
    def __init__(self, filename=None):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionClose.triggered.connect(self.close)
        self.ui.actionAbout.triggered.connect(self.open_about)
        self.manager = Manager(self, filename)
        self.ui.viewPort.add_managed_fields(self.manager)
        self.ui.menuRecent.addAction(QAction("lol", self.ui.menuRecent))
        self.ui.ToolsTabs.currentChanged.connect(self.change_editor)
        self.about = None
        self.setStatusTip("Layer: 0, Placing: Wall")

        self.editors: list[EditorMode] = []
        self.current_editor = 0
        # Connecting geo stuff
        geoeditor = GeometryEditor(self.ui.viewPort)
        self.editors.append(geoeditor)
        self.ui.ToolGeoApplyToL1.checkStateChanged.connect(geoeditor.check_l1_change)
        self.ui.ToolGeoApplyToL2.checkStateChanged.connect(geoeditor.check_l2_change)
        self.ui.ToolGeoApplyToL3.checkStateChanged.connect(geoeditor.check_l3_change)

        geoeditor.init_scene_items()


    @Slot(int)
    def change_editor(self, val) -> None:
        print("editor changed to " + str(val))
        self.current_editor = 0

    @property
    def editor(self) -> EditorMode:
        return self.editors[self.current_editor]

    @Slot()
    def open_about(self) -> None:
        self.about = AboutDialog(self)
        self.about.show()

    @Slot()
    def close(self) -> None:
        print("imagine it closes")

    @Slot()
    def open_file(self) -> None:
        print("open")
        QFileDialog.getOpenFileName(None, "Open Level", info.application_path)


