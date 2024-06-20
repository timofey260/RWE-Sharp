from PySide6.QtWidgets import QWidget
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from core.Modify.Mod import Mod
    from widgets.SettingsViewer import SettingsViewer


class UI(QWidget):
    def __init__(self, mod: 'Mod', parent=None):
        super().__init__(parent)
        self.mod = mod


class ViewUI(UI):
    def add_myself(self):
        self.mod.add_vis_ui(self)
        return self


class SettingUI(QWidget):
    def __init__(self, mod: 'Mod', reference: str):
        super().__init__()
        self.mod = mod
        self.reference = reference

    def add_myself(self):
        self.mod.add_setting_ui(self)
        return self

    def init_ui(self, viewer: 'SettingsViewer'):
        """
        Called when ui is being initiated
        :param viewer:
        :return:
        """
        pass
