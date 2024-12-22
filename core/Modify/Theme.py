from core.Application import Application
from core.Modify.ui import ThemeUI


class Theme:
    def __init__(self, name, mod):
        self.name = name
        self.mod = mod
        self.settings: ThemeUI | None = None

    def add_myself(self):
        from BaseMod.baseMod import BaseMod
        if isinstance(self.mod, BaseMod):
            self.mod.preferences.add_theme(self)
            return self
        self.mod.manager.basemod.preferences.add_theme(self)
        return self

    def theme_enable(self):
        pass

    def theme_disable(self):
        pass

    @property
    def app(self) -> Application:
        return self.mod.manager.application

    @property
    def config_name(self):
        return f"{self.mod.author_name}.{self.name}"
