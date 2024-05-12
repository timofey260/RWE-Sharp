class ModInfo:
    def __init__(self, title: str, description: str, name: str, author: str, version="1.0.0", tags=None):
        """
        Info of mod
        :param title: Title of mod to show
        :param description: Mod description
        :param name: id of mod for config management, should not include spaces
        :param author: Mod author
        :param version: Mod version, 1.0.0 by default
        """
        if tags is None:
            tags = []
        self.title = title
        self.description = description
        self.name = name
        self.author = author
        self.version = version
        self.tags = tags


class Mod:
    def __init__(self, manager, modinfo: ModInfo):
        """
        Base Mod class to load
        :param manager: manager to use
        :param modinfo: mod info, should be filled with class
        """
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
