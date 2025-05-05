from RWESharp.Configurable import KeyConfigurable


class GeoControls:
    def __init__(self, mod):
        self.wall = KeyConfigurable(mod, "KEYS_geo.wall", "w", "Select tool to place walls at the cursor", "Wall")
        self.air = KeyConfigurable(mod, "KEYS_geo.air", "a", "Select tool to place air at the cursor", "Air")
        self.slope = KeyConfigurable(mod, "KEYS_geo.slope", "s", "Select tool to place slopes at the cursor", "Slope")
        self.floor = KeyConfigurable(mod, "KEYS_geo.floor", "f", "Select tool to place floors at the cursor", "Floor")
        self.glass = KeyConfigurable(mod, "KEYS_geo.glass", "g", "Select tool to place glass at the cursor", "Glass")

        self.rock = KeyConfigurable(mod, "KEYS_geo.rock", "r", "Place a guaranteed rock at the cursor", "Rock")
        self.spear = KeyConfigurable(mod, "KEYS_geo.spear", "q", "Place a guaranteed spear at the cursor", "Spear")
        self.beam = KeyConfigurable(mod, "KEYS_geo.beam", "b",
                                    "Place a climbable beam at the cursor. Use space to rotate", "Beam")
        self.shortcut = KeyConfigurable(mod, "KEYS_geo.shortcut", "z", "Place a pipe entrance at the cursor", "Shortcut Path")
        self.shortcut_entrance = KeyConfigurable(mod, "KEYS_geo.shortcut_entrance", "x",
                                                 "Place a shortcut entrance at the cursor", "Shortcut Entrance")
        self.dragon_den = KeyConfigurable(mod, "KEYS_geo.dragon_den", "t", "Place a creature den at the cursor", "Creature Den")
        self.fly_chains = KeyConfigurable(mod, "KEYS_geo.fly_chains", "y", "Forbid fly chains in the area", "Forbid fly chains")
        self.fly_hive = KeyConfigurable(mod, "KEYS_geo.fly_hive", "h", "Create a fly hive at the cursor", "Fly Hive")
        self.scav_hole = KeyConfigurable(mod, "KEYS_geo.scav_hole", "n", "Create a scavenger den at the cursor", "Scavenger Hole")
        self.garbage_worm_den = KeyConfigurable(mod, "KEYS_geo.garbage_worm_den", "j",
                                                "Create a garbage worm den at the cursor.", "Garbage Worm Den")
        self.whack_a_mole_hole = KeyConfigurable(mod, "KEYS_geo.whack_a_mole_hole", "p",
                                                 "Place a Whack-a-Mole hole at the cursor", "Whack a Mole Hole")
        self.worm_grass = KeyConfigurable(mod, "KEYS_geo.worm_grass", "k", "Place worm grass at the cursor", "Worm Grass")
        self.entrance = KeyConfigurable(mod, "KEYS_geo.entrance", "e", "Place a room entrance at the cursor", "Entrance")
        self.waterfall = KeyConfigurable(mod, "KEYS_geo.waterfall", "u", "Create a waterfall at the cursor", "Waterfall")

        self.clear_all = KeyConfigurable(mod, "KEYS_geo.clear_all", "Ctrl+d", "Clear all blocks on all layers", "Clear all")
        self.clear_upper = KeyConfigurable(mod, "KEYS_geo.clear_upper", "Ctrl+w",
                                           "Clear stable structures such as beams, pipes, etc.", "Clear Stackables")
        self.clear_blocks = KeyConfigurable(mod, "KEYS_geo.clear_blocks", "Ctrl+e",
                                            "Clear solid blocks such as walls, slopes, floors, glass, and entrances", "Clear blocks")
        self.clear_layer = KeyConfigurable(mod, "KEYS_geo.clear_layer", "d", "Clear everything on the selected layer", "Clear layer")
        self.inverse = KeyConfigurable(mod, "KEYS_geo.inverse", "i", "Replace air with solid blocks and invert slopes", "Inverse")
        self.mirror = KeyConfigurable(mod, "KEYS_geo.mirror", "m",
                                      "Create a mirror axis. Everything on one side will be copied to the other", "Mirror")
        self.brushsizeup = KeyConfigurable(mod, "KEYS_geo.brushsizeup", "Ctrl+Shift++", "Increases brush size", "Brush size+")
        self.brushsizedown = KeyConfigurable(mod, "KEYS_geo.brushsizedown", "Ctrl+Shift+-", "Decreases brush size", "Brush size-")

        self.rotate = KeyConfigurable(mod, "KEYS_geo.rotate", "Space", "Rotate beams and slopes")
        self.rotate_back = KeyConfigurable(mod, "KEYS_geo.rotate_back", "Ctrl+Space", "Rotate beams and slopes backwards")
