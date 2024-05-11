class ModInfo:
    def __init__(self):
        self.title = "NoName"
        self.description = "This mod has no description"
        self.name = "nope"
        self.author = "NoAuthor"
        self.version = "1.0.0"


class Mod:
    def __init__(self, manager, modinfo):
        self.manager = manager
        self.modinfo = modinfo

    def add_editor(self, editor, ui):
        self.manager.add_editor(editor, ui)

    def add_module(self, module):
        self.manager.add_module(module)

    def add_vis_ui(self, ui):
        self.manager.add_view(ui)

    def add_quickview_option(self, element):
        self.manager.add_quick_option(element)

    def add_config_module(self, config_module):
        self.manager.config.add_module(config_module)
