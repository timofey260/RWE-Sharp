from .Modify.ConfigModule import ConfigModule

class Config:
    """
    Config class is made to manage stuff that we change inside editor with the ui. This includes:
     * checkbox presses
     * editor specific stuff

    config stores mod settings by using config modules
    """
    def __init__(self, manager):
        self.manager = manager
        self.modules: list[ConfigModule] = []

        # 1st step: apply all configs
        # 2nd step: apply all settings from configs to mods and ui
        # 3rd step: store settings when we save level

    def add_module(self, module: ConfigModule):
        self.modules.append(module)
