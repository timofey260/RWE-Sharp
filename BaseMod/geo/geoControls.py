from core.configTypes.QtTypes import KeyConfigurable


class GeoControls:
    def __init__(self, mod):
        self.wall = KeyConfigurable(mod, "KEYS_geo.wall", "w", "Wall key")
        self.air = KeyConfigurable(mod, "KEYS_geo.air", "a", "Air key")
        self.slope = KeyConfigurable(mod, "KEYS_geo.slope", "s", "Slope key")
        self.floor = KeyConfigurable(mod, "KEYS_geo.floor", "f", "Floor key")
        self.glass = KeyConfigurable(mod, "KEYS_geo.glass", "g", "Glass key")

        self.rock = KeyConfigurable(mod, "KEYS_geo.rock", "r", "Rock key")
        self.spear = KeyConfigurable(mod, "KEYS_geo.spear", "q", "Spear key")
        self.beam = KeyConfigurable(mod, "KEYS_geo.beam", "b", "Beam key")
        self.shortcut = KeyConfigurable(mod, "KEYS_geo.shortcut", "z", "Shortcut key")
        self.shortcut_entrance = KeyConfigurable(mod, "KEYS_geo.shortcut_entrance", "x", "Shortcut Entrance key")
        self.dragon_den = KeyConfigurable(mod, "KEYS_geo.dragon_den", "t", "Dragon Den key")
        self.fly_chains = KeyConfigurable(mod, "KEYS_geo.fly_chains", "y", "Forbid Fly Chains key")
        self.fly_hive = KeyConfigurable(mod, "KEYS_geo.fly_hive", "h", "Fly Hive key")
        self.scav_hole = KeyConfigurable(mod, "KEYS_geo.scav_hole", "n", "Scavenger Hole key")
        self.garbage_worm_den = KeyConfigurable(mod, "KEYS_geo.garbage_worm_den", "j", "Garbage Worm Den key")
        self.whack_a_mole_hole = KeyConfigurable(mod, "KEYS_geo.whack_a_mole_hole", "p", "Whack a Mole Hole key")
        self.worm_grass = KeyConfigurable(mod, "KEYS_geo.worm_grass", "k", "Worm Grass key")
        self.entrance = KeyConfigurable(mod, "KEYS_geo.entrance", "e", "Entrance key")
        self.waterfall = KeyConfigurable(mod, "KEYS_geo.waterfall", "u", "Waterfall key")

        self.clear_all = KeyConfigurable(mod, "KEYS_geo.clear_all", "Ctrl+d", "Clear All key\nClears all blocks on all layers")
        self.clear_upper = KeyConfigurable(mod, "KEYS_geo.clear_upper", "Ctrl+w", "Clear Upper key\nClears only stackables, such as beams, pipes etc")
        self.clear_blocks = KeyConfigurable(mod, "KEYS_geo.clear_blocks", "Ctrl+q", "Clear Block key\nClears only blocks, such as walls, slopes, floors, glass and entrances")
        self.clear_layer = KeyConfigurable(mod, "KEYS_geo.clear_layer", "d", "Clear Layer key\nClears all on selected layers")
        self.inverse = KeyConfigurable(mod, "KEYS_geo.inverse", "i", "Inverse key\nInverses wall so air and vice versa\nalso inverses slopes")
        self.mirror = KeyConfigurable(mod, "KEYS_geo.mirror", "m", "Mirror key\n Adds a second cursor")
