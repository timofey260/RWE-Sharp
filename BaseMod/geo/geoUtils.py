def geo_save(form: [int, bool], block: [int, list[int]]) -> ([int, list[int]], ...):
    if form[1] and form[0] < 0:
        match form[0]:
            case -2:  # upper
                if 4 in block[1]:
                    return [block[0], [4]], block[1].copy()
                return [block[0], []], block[1].copy()
            case -3:  # block
                return [0, block[1].copy()], block[0]
            case -4:  # all
                return [0, []], [block[0], block[1].copy()]
            case -5:  # layer
                return [0, []], [block[0], block[1].copy()]
            case -6:
                if block[0] in [2, 3, 4, 5]:
                    return [[5, 4, 3, 2][block[0] - 2], block[1]], block[0]
                elif block[0] == 0:
                    return [1, block[1]], block[0]
                return [0, block[1]], block[0]
    elif form[1]:  # stack
        if form[0] == 4:
            return [7, [4, *block[1]]], [block[0], 4 in block[1]]
        bol = form[0] in block[1]
        ar = block[1].copy()
        if not bol:
            ar.append(form[0])
        return [block[0], ar], bol
    return [form[0], block[1].copy()], block[0]


def geo_undo(form: [int, bool], block: [int, list[int]], saved) -> [int, list[int]]:
    if form[1] and form[0] < 0:
        match form[0]:
            case -2:  # upper
                return [block[0], saved.copy()]
            case -3:  # block
                return [saved, block[1].copy()]
            case -4:  # all
                return [saved[0], saved[1].copy()]
            case -5:  # layer
                return [saved[0], saved[1].copy()]
            case -6:
                return [saved, block[1]]
    elif form[1]:  # stack
        if form[0] == 4:
            l = block[1].copy()
            if saved[1]:
                return [saved[0], l.copy()]
            l.remove(4)
            return [saved[0], l.copy()]
        ar = block[1].copy()
        if not saved:
            ar.remove(form[0])
        return [block[0], ar]
    return [saved, block[1].copy()]
