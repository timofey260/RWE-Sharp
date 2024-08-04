from PySide6.QtWidgets import QWidget, QPushButton, QDialogButtonBox, QDialog, QMessageBox, QAbstractButton
from core.Modify.ui import SettingUI


class SettingsViewer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui: QDialog | None = None
        self.settingui: None | SettingUI = None
        self.nextsettingui: None | SettingUI = None
        self.apply_button: QPushButton | None = None
        self.reset_button: QPushButton | None = None
        self.close_button: QPushButton | None = None
        self.restore_button: QPushButton | None = None
        self.message: QMessageBox | None = None

    def load_ui(self, settingui: SettingUI):
        if len(self.children()) != 0 and self.settingui is not None:
            if self.settingui.is_changed:
                self.message = QMessageBox(QMessageBox.Icon.Question,
                                           "Apply settings?", "Would you like to apply changes?",
                                           QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No |
                                           QMessageBox.StandardButton.Cancel, self.ui)
                self.message.buttonClicked.connect(self.answer_settings)
                self.nextsettingui = settingui
                self.message.show()
            else:
                self.clear_settings()
                self.settingui = settingui
                self.children()[-1].destroyed.connect(self.continue_deleting)  # no idea how this one works but ok
        else:
            self.clear_settings()
            self.settingui = settingui
            self.continue_deleting()

    def continue_deleting(self):
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
        if self.settingui is not None:
            if self.settingui.is_changed:
                self.message = QMessageBox(QMessageBox.Icon.Question,
                                           "Apply settings?", "Would you like to apply changes?",
                                           QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No |
                                           QMessageBox.StandardButton.Cancel, self.ui)
                self.message.buttonClicked.connect(self.answer)
                self.message.show()
                return
            else:
                self.ui.close()
                return
        self.ui.close()

    def answer(self, button: QAbstractButton):
        if button == self.message.button(QMessageBox.StandardButton.Yes):
            self.settingui.apply_values()
            self.ui.close()
        elif button == self.message.button(QMessageBox.StandardButton.No):
            self.ui.close()

    def answer_settings(self, button: QAbstractButton):
        if button == self.message.button(QMessageBox.StandardButton.Yes):
            self.settingui.apply_values()
            self.clear_settings()
            self.settingui = self.nextsettingui
            self.nextsettingui = None
            self.children()[-1].destroyed.connect(self.continue_deleting)
        elif button == self.message.button(QMessageBox.StandardButton.No):
            self.clear_settings()
            self.settingui = self.nextsettingui
            self.nextsettingui = None
            self.children()[-1].destroyed.connect(self.continue_deleting)

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
