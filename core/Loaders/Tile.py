from PySide6.QtGui import QImage, QColor
from PySide6.QtCore import QPoint
from dataclasses import dataclass


@dataclass(frozen=True)
class Tile:
    name: str
    type: str
    repeatl: list[int]
    description: str
    bfTiles: int
    image: QImage
    image2: QImage | None
    image3: QImage | None
    image4: QImage | None
    size: QPoint
    category: str
    color: QColor
    cols: tuple[list[int], [list[int] | int]]
    cat: QPoint
    tags: list[str]
    printcols: bool
    preview: QImage | None
    err: bool