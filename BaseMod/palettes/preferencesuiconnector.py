from BaseMod.palettes.preferencesui import Ui_Preferences
from RWESharp.Ui import SettingUI
from PySide6.QtCore import Qt
from widgets.SettingsViewer import SettingsViewer


class PreferencesUI(SettingUI):
    def __init__(self, mod):
        super().__init__(mod)

    def reset_values(self):
        pass

    def reset_values_default(self):
        pass

    def apply_values(self):
        pass

    def init_ui(self, viewer: SettingsViewer):
        self.ui = Ui_Preferences()
        self.ui.setupUi(viewer)
        self.ui.Theme.clear()
        for i, v in enumerate(self.mod.manager.themes):
            self.ui.Theme.addItem(v.name)
            self.ui.Theme.setItemData(i, v, Qt.ItemDataRole.UserRole)
        self.setup_ui(self.ui.Theme.itemData(0, Qt.ItemDataRole.UserRole))

    def setup_ui(self, theme):
        if theme.settings is None:
            return
        theme.settings.setup_ui(self.ui.ThemeUI)
