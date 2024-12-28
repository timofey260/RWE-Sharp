import numpy as np
from BaseMod.LevelParts import GeoLevelPart


def geo_save(form: [int, bool], block: [np.uint8, np.uint16]) -> ([np.uint8, np.uint16], ...):
    if form[1] and form[0] < 0:
        match form[0]:
            case -2:  # upper
                if block[1] & 0b10000 > 0:
                    return [block[0], np.uint16(0b10000)], block[1]
                return [block[0], 0], block[1].copy()
            case -3:  # block
                return [np.uint8(), block[1]], block[0]
            case -4:  # all
                return [np.uint8(), np.uint16()], [block[0], block[1].copy()]
            case -5:  # layer
                return [np.uint8(), np.uint16()], [block[0], block[1].copy()]
            case -6:  # inverse
                if block[0] in [2, 3, 4, 5]:
                    return [np.uint8([5, 4, 3, 2][block[0] - 2]), block[1]], block[0]
                elif block[0] == 0:
                    return [1, block[1]], block[0]
                return [0, block[1]], block[0]
    elif form[1]:  # stack
        if form[0] == 0b10000:
            return [np.uint8(7), block[1] | 0b10000], [block[0], block[1] & 0b10000 > 0]
        bol = form[0] & block[1] > 0
        ar = block[1]
        if not bol:
            ar |= form[0]
        return [block[0], ar], bol
    return [form[0], block[1]], block[0]


def geo_undo(form: [int, bool], block: [np.uint8, np.uint16], saved) -> [np.uint8, np.uint16]:
    if form[1] and form[0] < 0:
        match form[0]:
            case -2:  # upper
                return [block[0], saved]
            case -3:  # block
                return [saved, block[1]]
            case -4:  # all
                return [saved[0], saved[1]]
            case -5:  # layer
                return [saved[0], saved[1]]
            case -6:  # inverse
                return [saved, block[1]]
    elif form[1]:  # stack
        if form[0] == 0b10000:
            l = block[1]
            if saved[1]:
                return [saved[0], l]
            l &= 0b1111111111101111
            return [saved[0], l]
        ar = block[1]
        if not saved:
            ar &= form[0].__invert__()
        return [block[0], ar]
    return [saved, block[1]]
