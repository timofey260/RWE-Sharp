from PySide6.QtGui import QColor


class ItemDataItem:
    def __init__(self, name):
        self.name = name


class ItemData:
    def __init__(self):
        self.data = []

    def __getitem__(self, item):
        if isinstance(item, str):
            return self.searchitem(item)
        elif isinstance(item, int):
            return self.data[item]
        elif isinstance(item, tuple):
            return self.searchitem(item[1], item[0])
        return None

    def searchitem(self, name: str, category: str = None) -> ItemDataItem | None:
        if category is None:
            for catnum, cat in enumerate(self.data):
                for itemnum, items in enumerate(cat["items"]):
                    if items.name == name:
                        return items
        else:
            for itemnum, items in enumerate(self.data[self.categories.index(category)]["items"]):
                if items.name == name:
                    return items
        return None

    def getnameindex(self, cat: int, name: str) -> int | None:
        for i, v in enumerate(self.get_items(cat)):
            if v.name == name:
                return i
        return None

    def get_items(self, cat: int) -> list[ItemDataItem]:
        return self.data[cat]["items"]

    @property
    def categories(self) -> list[str]:
        return [i["name"] for i in self.data]

    @property
    def colors(self) -> list[QColor]:
        return [i["color"] for i in self.data]

    def append(self, category_data):
        self.data.append(category_data)

    def addcat(self, name, color):
        self.data.append({"name": name, "color": color, "items": []})

    def remove(self, category_data):
        self.data.remove(category_data)

    def insert(self, index, category_data):
        self.data.insert(index, category_data)

    def pop(self, index):
        self.data.pop(index)

    def __str__(self):
        return str(self.data)

    def __len__(self):
        return len(self.data)

    def isempty(self):
        return len(self.data) == 0

    def __add__(self, other):
        raise NotImplementedError("not able to add")