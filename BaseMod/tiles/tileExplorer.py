from BaseMod.tiles.ui.tileexplorer import Ui_TileExplorer
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QAction
from PySide6.QtCore import Slot, Signal


class TileExplorer(QMainWindow):
    stateChanged = Signal(bool)

    def __init__(self, manager, parent=None):
        super().__init__(parent)
        self.ui = Ui_TileExplorer()
        self.ui.setupUi(self)
        self.state = False

    def link_action(self, action: QAction):
        action.setCheckable(True)
        action.setChecked(self.state)
        action.toggled.connect(self.change_visibility)
        self.stateChanged.connect(action.setChecked)

    @Slot(bool)
    def change_visibility(self, value: bool):
        if self.state == value:
            return
        self.state = value
        if value:
            self.stateChanged.emit(value)
            self.show()
            return
        self.stateChanged.emit(value)
        self.hide()

    def hideEvent(self, event):
        self.change_visibility(False)
        super().hideEvent(event)

    def showEvent(self, event):
        self.change_visibility(True)
        super().showEvent(event)
