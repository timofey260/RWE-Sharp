from PySide6.QtWidgets import QWidget, QPushButton, QDialogButtonBox, QMessageBox
from RWESharp.Modify.Ui import SettingUI


class SettingsViewer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        from RWESharp.ui.settingsuiconnector import SettingsDialogUI
        self.ui: SettingsDialogUI | None = None
        self.settingui: None | SettingUI = None
        self.nextsettingui: None | SettingUI = None
        self.apply_button: QPushButton | None = None
        self.reset_button: QPushButton | None = None
        self.close_button: QPushButton | None = None
        self.restore_button: QPushButton | None = None
        self.message: QMessageBox | None = None

    def load_ui(self, settingui: SettingUI):
        if (self.layout() is not None and self.layout().count() != 0) and self.settingui is not None:
            if self.settingui.is_changed:
                self.message = QMessageBox(QMessageBox.Icon.Question,
                                           "Apply settings?", "Would you like to apply changes?",
                                           QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No |
                                           QMessageBox.StandardButton.Cancel, self.ui)
                self.nextsettingui = settingui
                self.answer_settings(self.message.exec())
                # self.message.buttonClicked.connect(self.answer_settings)
                # self.message.show()
                return
            self.init_ui(settingui)
            return
        self.init_ui(settingui)

    def init_ui(self, settingsui):
        self.clear_settings()
        self.settingui = settingsui
        if len(self.children()) > 0:
            self.children()[-1].destroyed.connect(self.continue_deleting)
            return
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
                self.answer(self.message.exec())
                return
            else:
                self.ui.close()
                return
        self.ui.close()

    def answer(self, button: QDialogButtonBox.StandardButton):
        if button == QMessageBox.StandardButton.Yes:
            self.apply_settings()
            self.ui.close()
        elif button == QMessageBox.StandardButton.No:
            self.settingui.reset_values_default()
            self.ui.close()

    def answer_settings(self, button: QDialogButtonBox.StandardButton):
        if button == QMessageBox.StandardButton.Yes:
            self.apply_settings()
            self.init_ui(self.nextsettingui)
            self.nextsettingui = None
        elif button == QMessageBox.StandardButton.No:
            self.init_ui(self.nextsettingui)
            self.nextsettingui = None

    def restore_settings(self):
        if self.settingui is None:
            return
        self.settingui.reset_values_default()

    def apply_settings(self):
        if self.settingui is None:
            return
        self.settingui.apply_values()
        self.ui.manager.config.save_configs()

    def clear_settings(self):
        for i in self.children():
            i.deleteLater()
        if self.settingui is not None:
            self.settingui.reset_values_default()
        self.settingui = None
