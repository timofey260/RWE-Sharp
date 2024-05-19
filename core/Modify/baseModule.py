class Module:
    """
    Module for passive editor and viewport work
    """
    def __init__(self, mod):
        self.mod = mod
        self.manager = mod.manager
        self.editorlayers = []

    def init_module_textures(self):
        """
        Called after all texture modules were initialized
        :return: None
        """
        pass

    def render_module(self):
        """
        Called when user asks for viewport cleanup
        Also called when booting up rwe#
        :return: None
        """
        pass
