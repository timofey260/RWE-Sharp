from .Modify.ConfigModule import ConfigModule
import appdirs
from core.info import NAME, PROGNAME, AUTHOR
import os


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

    def init_configs(self):
        # get config file
        path = self.ensure_config()
        for i in self.modules:
            i.register_config()
        modnames = [f"{i.mod.modinfo.author}.{i.mod.modinfo.name}" for i in self.modules]
        with open(path) as f:
            for l in f.readlines():
                l = l.strip()
                if len(l) == 0 or l[0] == "#":
                    continue
                if l.find("#") != -1:
                    l = l[:l.find("#")]

                name = l[:l.find(".", l.find(".") + 1)]
                id = l[l.find(".", l.find(".") + 1) + 1:l.find("=")]
                value = l[l.find("=") + 1:]
                print(name, id, value)
                if name in modnames:
                    self.modules[modnames.index(name)].values[id].load_str_value(value)

    def save_configs(self):
        path = self.ensure_config()
        print(self.modules)
        with open(path, "w") as f:
            for i in self.modules:
                for k, v in i.values.items():
                    if v.description.strip() != "":
                        f.write(f"# {v.description}\n")
                    f.write(f"{i.mod.modinfo.author}.{i.mod.modinfo.name}.{k}={v.save_str_value()}")
                f.write("\n")

    def ensure_config(self) -> str:
        """
        ensures that config file exists and returns path to it
        :return: path to config.txt
        """
        path = appdirs.user_config_dir(NAME, AUTHOR)
        if not os.path.exists(path):
            os.makedirs(appdirs.user_config_dir(NAME, AUTHOR), exist_ok=True)
            with open(os.path.join(path, "config.txt"), "w") as f:
                f.write("# rwe# config file\n#use # for comments")
        return os.path.join(path, "config.txt")

    def add_module(self, module: ConfigModule):
        self.modules.append(module)
