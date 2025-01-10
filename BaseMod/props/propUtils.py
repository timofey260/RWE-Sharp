from PySide6.QtCore import QPointF
from RWESharp.Core import SPRITESIZE, CELLSIZE


def copyprop(prop):
    return [prop[0], prop[1], prop[2], prop[3].copy(), prop[4].copy()]


def find_mid(prop):
    """
    middle of prop in editor's coordinates
    :param prop: prop
    :return: pos in editors coordinates
    """
    return sum(prop[3], QPointF()) / 4