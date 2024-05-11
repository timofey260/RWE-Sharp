class Mod:
    def __init__(self, manager):
        self.manager = manager

    def add_editor(self, editor, ui):
        self.manager.add_editor(editor, ui)

    def add_module(self, module):
        self.manager.add_module(module)

    def add_vis_ui(self, ui):
        self.manager.add_view(ui)

    def add_quickview_option(self, element):
        self.manager.add_quick_option(element)
