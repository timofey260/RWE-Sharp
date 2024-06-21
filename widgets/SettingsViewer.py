from PySide6.QtWidgets import QWidget, QPushButton
from core.Modify.ui import SettingUI


class SettingsViewer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.settingui: None | SettingUI = None
        self.apply_button: QPushButton | None = None
        self.ok_button: QPushButton | None = None
        self.cancel_button: QPushButton | None = None

    def load_ui(self, settingui: SettingUI):
        self.clear_settings()
        self.settingui = settingui
        self.settingui.init_ui(self)

    def clear_settings(self):
        for i in self.children():
            i.deleteLater()
