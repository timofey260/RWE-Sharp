from BaseMod.themes.preferencesui import Ui_Preferences
from RWESharp.Ui import SettingUI
from RWESharp.Configurable import StringConfigurable
from RWESharp.Utils import log
from PySide6.QtCore import Qt
from widgets.SettingsViewer import SettingsViewer


class PreferencesUI(SettingUI):
    def __init__(self, mod):
        super().__init__(mod)
        self.theme = StringConfigurable(mod, "basemod.theme", "",
                                        "palette colors")  # "timofey26.basemod.Raspberry Dark"
        self.lasttheme = StringConfigurable(None, "lasttheme", "",
                                        "palette colors")  # "timofey26.basemod.Raspberry Dark"
        self.current_theme = None
        self.themes = []

    def change_theme(self):
        if self.theme.value == "":
            if self.current_theme is not None:
                self.current_theme.theme_disable()
                log("Theme is Disabled")
                self.current_theme = None
            return
        for i in self.themes:
            if self.theme.value == i.config_name:
                if self.current_theme is not None:
                    self.current_theme.theme_disable()
                i.theme_enable()
                self.current_theme = i
                log(f"Using Theme {i.id}")
                return

    def add_theme(self, theme):
        self.themes.append(theme)
        self.change_theme()

    def apply_values(self):
        self.theme.update_value(self.lasttheme.value)
        self.change_theme()
        super().apply_values()

    def reset_values(self):
        super().reset_values()
        self.pick_active()

    def reset_values_default(self):
        super().reset_values_default()
        self.pick_active()

    def init_ui(self, viewer: SettingsViewer):
        self.ui = Ui_Preferences()
        self.ui.setupUi(viewer)
        self.ui.Theme.clear()
        self.ui.Theme.addItem("Disabled")
        for i, v in enumerate(self.themes):
            self.ui.Theme.addItem(v.id, v)
        self.pick_active()
        self.setup_ui(self.ui.Theme.currentData(Qt.ItemDataRole.UserRole))
        self.ui.Theme.currentIndexChanged.connect(self.index_changed)

    def pick_active(self):
        for i, v in enumerate(self.themes):
            # print(v, self.current_theme)
            if v == self.current_theme:
                self.ui.Theme.setCurrentIndex(i + 1)
                break
        else:
            self.ui.Theme.setCurrentIndex(0)
        # self.setup_ui(self.ui.Theme.currentData(Qt.ItemDataRole.UserRole))

    def index_changed(self, index):
        if index == 0:
            self.lasttheme.update_value("")
        else:
            self.lasttheme.update_value(self.ui.Theme.currentData(Qt.ItemDataRole.UserRole).config_name)
        self.setup_ui(self.ui.Theme.currentData(Qt.ItemDataRole.UserRole))

    def setup_ui(self, theme, skip=False):

        if not skip and len(self.ui.ThemeUI.children()) > 0:
            self.ui.ThemeUI.children()[0].destroyed.connect(lambda x: self.setup_ui(theme, True))
            for i in self.ui.ThemeUI.children():
                i.deleteLater()
            return

        if theme is None or theme.settings is None:
            return
        theme.settings.setup_ui(self.ui.ThemeUI)
