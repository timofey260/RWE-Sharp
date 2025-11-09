from PySide6.QtCore import QPointF


def copyprop(prop):
    return [prop[0], prop[1], prop[2], prop[3].copy(), prop[4].copy()]


def find_mid(prop) -> QPointF:
    """
    middle of prop in editor's coordinates
    :param prop: prop
    :return: pos in editors coordinates
    """
    return sum(prop.quad, QPointF()) / 4