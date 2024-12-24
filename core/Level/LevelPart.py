from abc import ABC


class LevelPart(ABC):
    from core.Level.RWELevel import RWELevel

    def __init__(self, level: RWELevel):
        self.level = level
        pass