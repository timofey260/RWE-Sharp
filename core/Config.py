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
        # self.modules: list[ConfigModule] = []
        self.values: dict[str, str] = {}

        # 1st step: apply all configs
        # 2nd step: apply all settings from configs to mods and ui
        # 3rd step: store settings when we save level

    def init_configs(self):
        # get config file
        path = self.ensure_config()
        with open(path) as f:
            for l in f.readlines():
                l = l.strip()
                if len(l) == 0 or l[:1] == "//":
                    continue
                # if l.find("//") != -1:
                #     l = l[:l.find("//")]

                name = l[:l.find("=")]
                value = l[l.find("=") + 1:]
                # print(name, id, value)
                self.values[name] = value

    def save_configs(self):
        path = self.ensure_config()
        with open(path, "w") as f:
            for i in self.manager.mods:
                # f.write(f"// {i.subeditor.title()}\n")
                for v in i.configs:
                    if v.description.strip() != "":
                        f.write(f"// {v.description}\n")
                    f.write(f"{i.author_name}.{v.name}={v.save_str_value()}\n")
                f.write("\n\n")

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
