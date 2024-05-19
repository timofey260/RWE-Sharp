from core.Modify.RenderTexture import RenderTexture

class TileRenderTexture(RenderTexture):
    def __init__(self, module, layer):
        super().__init__(module)
        self.layer = layer
        self.draw()

    def draw(self):
        self.painter.drawImage(0, 0, self.manager.tiles["Four Holes"]["image"])