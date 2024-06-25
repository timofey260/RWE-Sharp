from PySide6.QtGui import QImage, QColor, QPixmap
from PySide6.QtCore import QPoint, QSize
from dataclasses import dataclass


@dataclass(frozen=True)
class Tile:
    name: str
    type: str
    repeatl: list[int]
    description: str
    bfTiles: int
    image: QPixmap
    image2: QPixmap | None
    image3: QImage | None
    size: QSize
    category: str
    color: QColor
    cols: [list[int], [list[int] | int]]
    cat: QPoint
    tags: list[str]
    printcols: bool
    preview: QImage | None
    err: bool