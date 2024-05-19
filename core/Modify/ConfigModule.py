class ConfigModule:
    """
    Base for creating custom mod configs
    all data we store is either level related or editor related
    config module provides easy way to store editor specific data
    """
    def __init__(self, mod):
        self.mod = mod
        self.manager = mod.manager

    def register_value(self, path, value) -> None:
        """
        registers value to be saved
        """
