from PySide6.QtWidgets import QDockWidget
from PySide6.QtCore import Signal, Slot
from PySide6.QtGui import QAction


class ViewDockWidget(QDockWidget):
    stateChanged = Signal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.state = True

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
        
    def hide(self):
        print(3)
        self.change_visibility(False)
        super().hide()

    def show(self):
        self.change_visibility(True)
        super().show()
