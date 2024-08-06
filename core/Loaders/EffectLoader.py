from core.info import PATH_FILES, PATH_EFFECT_PREVIEWS
import ujson
import os
from core.Loaders.Effect import EffectCategory, Effect, MoveDeleteOption, SeedOption, EffectOption, Effects
from PySide6.QtGui import QColor, QPixmap


def load_effects(splash):
    splash.printmessage("Loading Effects")
    effects_file = os.path.join(PATH_FILES, "effects.json")
    effects = ujson.load(open(effects_file))
    loaded_effects = []
    defaultprops = effects["defaultproperties"]
    for category in effects["effects"]:
        currentcat = EffectCategory(category.get("nm", "NoName"), QColor(*category.get("color", [0, 0, 0])), [])
        for i in category["efs"]:
            e = {**defaultprops, **i}
            effect = Effect(e["nm"],
                            e.get("description"),
                            e.get("tp", "nn"),
                            e.get("crossScreen", 0),
                            currentcat.color,
                            [MoveDeleteOption(), SeedOption(), *[EffectOption(p[0], p[1], p[2]) for p in e.get("options", [])]],
                            e.get("repeats", 60),
                            e.get("affectOpenAreas", 0.5),
                            QPixmap(os.path.join(PATH_EFFECT_PREVIEWS, e["preview"] + ".png")),
                            currentcat)
            currentcat.effects.append(effect)
        loaded_effects.append(currentcat)
    return Effects(loaded_effects)
