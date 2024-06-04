from PySide6.QtGui import QImage, QColor
from core.ItemData import ItemDataItem

class Tile(ItemDataItem):
    def __init__(self, data: dict):
        super().__init__(data["nm"])
        self.type: str = data.get("tp", "")
        self.repeatl: list[int] = data.get("repeatL", [1])
        self.description: str = data["description"]
        self.bfTiles: list[int, int] = data["bfTiles"]
        self.image: QImage = data["image"]
        self.image2: QImage = data.get("image2", QImage(1, 1, QImage.Format.Format_RGBA64))
        self.image3: QImage = data.get("image3", QImage(1, 1, QImage.Format.Format_RGBA64))
        self.image4: QImage = data.get("image4", QImage(1, 1, QImage.Format.Format_RGBA64))
        self.size: list[int, int] = data["size"]
        self.category: str = data["category"]
        self.color: QColor = data["color"]
        self.cols: list[list[int], [list[int] | -1]] = data["cols"]
        self.cat: list[int, int] = data["cat"]
        self.tags: list[str] = data["tags"]
        self.printcols: bool = data.get("printcols", False)
        self.preview: QImage = data.get("preview")
        self.err = data.get("err")