from PySide6.QtWidgets import QWidget, QPushButton, QDialogButtonBox
from core.Modify.ui import SettingUI


class SettingsViewer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.settingui: None | SettingUI = None
        self.apply_button: QPushButton | None = None
        self.reset_button: QPushButton | None = None
        self.close_button: QPushButton | None = None
        self.restore_button: QPushButton | None = None

    def load_ui(self, settingui: SettingUI):
        self.clear_settings()
        self.settingui = settingui
        self.settingui.init_ui(self)
        self.settingui.reset_values()

    def got_buttons(self, ui):
        self.ui = ui
        self.close_button = ui.ui.buttonBox.button(QDialogButtonBox.StandardButton.Close)
        self.reset_button = ui.ui.buttonBox.button(QDialogButtonBox.StandardButton.Reset)
        self.apply_button = ui.ui.buttonBox.button(QDialogButtonBox.StandardButton.Apply)
        self.restore_button = ui.ui.buttonBox.button(QDialogButtonBox.StandardButton.RestoreDefaults)
        self.apply_button.clicked.connect(self.apply_settings)
        self.reset_button.clicked.connect(self.reset_settings)
        self.close_button.clicked.connect(self.close_settings)
        self.restore_button.clicked.connect(self.restore_settings)

    def reset_settings(self):
        if self.settingui is None:
            return
        self.settingui.reset_values()

    def close_settings(self):
        self.ui.close()

    def restore_settings(self):
        if self.settingui is None:
            return
        self.settingui.reset_values_default()

    def apply_settings(self):
        if self.settingui is None:
            return
        self.settingui.apply_values()

    def clear_settings(self):
        for i in self.children():
            i.deleteLater()
        self.settingui = None
