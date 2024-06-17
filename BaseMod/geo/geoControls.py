from core.configTypes.QtTypes import KeyConfigurable


class GeoControls:
    def __init__(self, mod):
        self.wall = KeyConfigurable(mod, "KEYS_geo.wall", "w", "wall key")
        self.air = KeyConfigurable(mod, "KEYS_geo.air", "a", "air key")
        self.slope = KeyConfigurable(mod, "KEYS_geo.slope", "s", "slope key")
        self.floor = KeyConfigurable(mod, "KEYS_geo.floor", "f", "floor key")
        self.glass = KeyConfigurable(mod, "KEYS_geo.glass", "g", "glass key")

        self.rock = KeyConfigurable(mod, "KEYS_geo.rock", "r", "rock key")
        self.spear = KeyConfigurable(mod, "KEYS_geo.spear", "q", "spear key")
        self.crack = KeyConfigurable(mod, "KEYS_geo.crack", "c", "crack key")
