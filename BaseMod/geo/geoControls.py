from RWS.Configurable import KeyConfigurable


class GeoControls:
    def __init__(self, mod):
        self.wall = KeyConfigurable(mod, "KEYS_geo.wall", "w", "Place Wall", "Wall")
        self.air = KeyConfigurable(mod, "KEYS_geo.air", "a", "Place Air", "Air")
        self.slope = KeyConfigurable(mod, "KEYS_geo.slope", "s", "Place Slopes", "Slope")
        self.floor = KeyConfigurable(mod, "KEYS_geo.floor", "f", "Place Floors", "Floor")
        self.glass = KeyConfigurable(mod, "KEYS_geo.glass", "g", "Place Glass", "Glass")

        self.rock = KeyConfigurable(mod, "KEYS_geo.rock", "r", "Place guaranteed Rock", "Rock")
        self.spear = KeyConfigurable(mod, "KEYS_geo.spear", "q", "Place guaranteed Spear", "Spear")
        self.beam = KeyConfigurable(mod, "KEYS_geo.beam", "b",
                                    "Place climbable beams", "Beam")
        self.shortcut = KeyConfigurable(mod, "KEYS_geo.shortcut", "z", "Place Shortcuts", "Shortcut Path")
        self.shortcut_entrance = KeyConfigurable(mod, "KEYS_geo.shortcut_entrance", "x",
                                                 "Place Shortcut Entrances", "Shortcut Entrance")
        self.dragon_den = KeyConfigurable(mod, "KEYS_geo.dragon_den", "t", "Place Creature Den", "Creature Den")
        self.fly_chains = KeyConfigurable(mod, "KEYS_geo.fly_chains", "y", "Place Forbid Fly Chains", "Forbid fly chains")
        self.fly_hive = KeyConfigurable(mod, "KEYS_geo.fly_hive", "h", "Place Fly Hives", "Fly Hive")
        self.scav_hole = KeyConfigurable(mod, "KEYS_geo.scav_hole", "n", "Place Scavenger Hole", "Scavenger Hole")
        self.garbage_worm_den = KeyConfigurable(mod, "KEYS_geo.garbage_worm_den", "j",
                                                "Place Garbage worm den", "Garbage Worm Den")
        self.whack_a_mole_hole = KeyConfigurable(mod, "KEYS_geo.whack_a_mole_hole", "p",
                                                 "Place Whack-a-Mole hole", "Whack a Mole Hole")
        self.worm_grass = KeyConfigurable(mod, "KEYS_geo.worm_grass", "k", "Place Worm Grass", "Worm Grass")
        self.entrance = KeyConfigurable(mod, "KEYS_geo.entrance", "e", "Place Entrance", "Entrance")
        self.waterfall = KeyConfigurable(mod, "KEYS_geo.waterfall", "u", "Place Waterfall", "Waterfall")

        self.clear_all = KeyConfigurable(mod, "KEYS_geo.clear_all", "Ctrl+d", "Clear all blocks on all layers", "Clear all")
        self.clear_upper = KeyConfigurable(mod, "KEYS_geo.clear_upper", "Ctrl+w",
                                           "Clear stable structures such as beams, pipes, etc.", "Clear Stackables")
        self.clear_blocks = KeyConfigurable(mod, "KEYS_geo.clear_blocks", "Ctrl+e",
                                            "Clear solid blocks such as walls, slopes, floors, glass, and entrances", "Clear blocks")
        self.clear_layer = KeyConfigurable(mod, "KEYS_geo.clear_layer", "d", "Clear everything on the selected layer", "Clear layer")
        self.inverse = KeyConfigurable(mod, "KEYS_geo.inverse", "i", "Replace air with solid blocks and invert slopes", "Inverse")
        self.mirror = KeyConfigurable(mod, "KEYS_geo.mirror", "m",
                                      "Create a mirror axis. Everything on one side will be copied to the other", "Mirror")
        self.copy = KeyConfigurable(mod, "KEYS_geo.copy", "Ctrl+c",
                                      "Select Tiles to copy", "Copy")
        self.paste = KeyConfigurable(mod, "KEYS_geo.paste", "Ctrl+v",
                                      "Paste blocks on specific point", "Paste")
        self.move = KeyConfigurable(mod, "KEYS_geo.move", "Ctrl+m",
                                     "Move blocks",
                                     "Move")

        self.brushsizeup = KeyConfigurable(mod, "KEYS_geo.brushsizeup", "Ctrl+Shift++", "Increases brush size", "Brush size+")
        self.brushsizedown = KeyConfigurable(mod, "KEYS_geo.brushsizedown", "Ctrl+Shift+-", "Decreases brush size", "Brush size-")

        self.rotate = KeyConfigurable(mod, "KEYS_geo.rotate", "Space", "Rotate beams and slopes")
        self.rotate_back = KeyConfigurable(mod, "KEYS_geo.rotate_back", "Ctrl+Space", "Rotate beams and slopes backwards")
