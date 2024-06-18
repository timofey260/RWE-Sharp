from core.Renderable.Renderable import Renderable


class Module:
    """
    Module for passive editor and viewport work
    """
    def __init__(self, mod):
        from widgets.Viewport import ViewPort

        self.mod = mod
        self.manager = mod.manager
        self.renderables: list[Renderable] = []
        self.viewport: ViewPort = mod.manager.viewport

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

    def on_resize(self):
        """
        Called once level is resized
        """
        pass

    def append_layer(self, renderable: Renderable):
        self.renderables.append(renderable)

    def add_myself(self):
        self.mod.add_module(self)
        return self

    def zoom_event(self, zoom):
        for i in self.renderables:
            i.zoom_event(zoom)

    def move_event(self, pos):
        for i in self.renderables:
            i.move_event(pos)
