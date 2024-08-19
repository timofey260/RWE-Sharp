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
        self.ui.Theme.addItem("Disabled")
        for i, v in enumerate(self.mod.manager.themes):
            self.ui.Theme.addItem(v.name, v)
            if v == self.mod.manager.current_theme:
                self.ui.Theme.setCurrentIndex(i + 1)
        self.setup_ui(self.ui.Theme.currentData(Qt.ItemDataRole.UserRole))
        self.ui.Theme.currentIndexChanged.connect(self.index_changed)

    def index_changed(self, index):
        if index == 0:
            self.mod.manager.basemod.bmconfig.theme.update_value("")
        else:
            self.mod.manager.basemod.bmconfig.theme.update_value(self.ui.Theme.currentData(Qt.ItemDataRole.UserRole).config_name)
        self.setup_ui(self.ui.Theme.currentData(Qt.ItemDataRole.UserRole))

    def setup_ui(self, theme, skip=False):
        if len(self.ui.ThemeUI.children()) > 0 and not skip:
            self.ui.ThemeUI.children()[0].destroyed.connect(lambda x: self.setup_ui(theme, True))
            for i in self.ui.ThemeUI.children():
                i.deleteLater()
            return

        if theme is None or theme.settings is None:
            return
        theme.settings.setup_ui(self.ui.ThemeUI)
