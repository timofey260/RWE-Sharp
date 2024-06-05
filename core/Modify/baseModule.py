from .RenderTexture import RenderTexture

class Module:
    """
    Module for passive editor and viewport work
    """
    def __init__(self, mod):
        self.mod = mod
        self.manager = mod.manager
        self.editorlayers: list[tuple[int, RenderTexture]] = []

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

    def append_layer(self, depth: int, texture: RenderTexture):
        self.editorlayers.append((depth, texture))

    def add_myself(self):
        self.mod.add_module(self)
        return self
