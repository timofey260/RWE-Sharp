from RWESharp.Configurable import KeyConfigurable


class GeoControls:
    def __init__(self, mod):
        self.wall = KeyConfigurable(mod, "KEYS_geo.wall", "w", "Select tool to place walls at the cursor")
        self.air = KeyConfigurable(mod, "KEYS_geo.air", "a", "Select tool to place air at the cursor")
        self.slope = KeyConfigurable(mod, "KEYS_geo.slope", "s", "Select tool to place slopes at the cursor")
        self.floor = KeyConfigurable(mod, "KEYS_geo.floor", "f", "Select tool to place floors at the cursor")
        self.glass = KeyConfigurable(mod, "KEYS_geo.glass", "g", "Select tool to place glass at the cursor")

        self.rock = KeyConfigurable(mod, "KEYS_geo.rock", "r", "Place a guaranteed rock at the cursor")
        self.spear = KeyConfigurable(mod, "KEYS_geo.spear", "q", "Place a guaranteed spear at the cursor")
        self.beam = KeyConfigurable(mod, "KEYS_geo.beam", "b",
                                    "Place a climbable beam at the cursor. Use space to rotate")
        self.shortcut = KeyConfigurable(mod, "KEYS_geo.shortcut", "z", "Place a pipe entrance at the cursor")
        self.shortcut_entrance = KeyConfigurable(mod, "KEYS_geo.shortcut_entrance", "x",
                                                 "Place a shortcut entrance at the cursor")
        self.dragon_den = KeyConfigurable(mod, "KEYS_geo.dragon_den", "t", "Place a creature den at the cursor")
        self.fly_chains = KeyConfigurable(mod, "KEYS_geo.fly_chains", "y", "Forbid fly chains in the area")
        self.fly_hive = KeyConfigurable(mod, "KEYS_geo.fly_hive", "h", "Create a fly hive at the cursor")
        self.scav_hole = KeyConfigurable(mod, "KEYS_geo.scav_hole", "n", "Create a scavenger den at the cursor")
        self.garbage_worm_den = KeyConfigurable(mod, "KEYS_geo.garbage_worm_den", "j",
                                                "Create a garbage worm den at the cursor.")
        self.whack_a_mole_hole = KeyConfigurable(mod, "KEYS_geo.whack_a_mole_hole", "p",
                                                 "Place a Whack-a-Mole hole at the cursor")
        self.worm_grass = KeyConfigurable(mod, "KEYS_geo.worm_grass", "k", "Place worm grass at the cursor")
        self.entrance = KeyConfigurable(mod, "KEYS_geo.entrance", "e", "Place a room entrance at the cursor")
        self.waterfall = KeyConfigurable(mod, "KEYS_geo.waterfall", "u", "Create a waterfall at the cursor")

        self.clear_all = KeyConfigurable(mod, "KEYS_geo.clear_all", "Ctrl+d", "Clear all blocks on all layers")
        self.clear_upper = KeyConfigurable(mod, "KEYS_geo.clear_upper", "Ctrl+w",
                                           "Clear stable structures such as beams, pipes, etc.")
        self.clear_blocks = KeyConfigurable(mod, "KEYS_geo.clear_blocks", "Ctrl+e",
                                            "Clear solid blocks such as walls, slopes, floors, glass, and entrances")
        self.clear_layer = KeyConfigurable(mod, "KEYS_geo.clear_layer", "d", "Clear everything on the selected layer")
        self.inverse = KeyConfigurable(mod, "KEYS_geo.inverse", "i", "Replace air with solid blocks and invert slopes")
        self.mirror = KeyConfigurable(mod, "KEYS_geo.mirror", "m",
                                      "Create a mirror axis. Everything on one side will be copied to the other")