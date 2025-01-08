class CustomLevelData:
    def __init__(self, level):
        self.level = level

    def save(self, name, value):
        if self.level.data.get("CLD") is None:
            self.level.data["CLD"] = {}
        self.level.data["CLD"][name] = value

    def get(self, name):
        if self.level.data.get("CLD") is None:
            return None
        return self.level.data["CLD"].get(name, None)
