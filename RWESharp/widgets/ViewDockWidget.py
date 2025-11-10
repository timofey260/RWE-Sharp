from PySide6.QtWidgets import QDockWidget
from PySide6.QtCore import Signal, Slot, QEvent, Qt
from PySide6.QtGui import QAction


class ViewDockWidget(QDockWidget):
    stateChanged = Signal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowModality(Qt.WindowModality.NonModal)
        self.state = True

    def link_action(self, action: QAction):
        action.setCheckable(True)
        action.setChecked(self.state)
        action.toggled.connect(self.change_visibility)
        self.stateChanged.connect(action.setChecked)


    @Slot(bool)
    def change_visibility(self, value: bool, hide=True):
        if self.state == value:
            return
        self.state = value
        if value:
            self.stateChanged.emit(value)
            if hide:
                self.show()
            return
        self.stateChanged.emit(value)
        if hide:
            self.hide()

    def showEvent(self, event):
        self.change_visibility(True)
        super().showEvent(event)

    def closeEvent(self, event):
        self.change_visibility(False)
        super().closeEvent(event)

    def hide(self):
        self.change_visibility(False, False)
        super().hide()

    def show(self):
        self.change_visibility(True, False)
        super().show()
