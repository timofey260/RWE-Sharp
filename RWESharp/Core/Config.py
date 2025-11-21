from RWESharp.info import NAME, AUTHOR
import json
from PySide6.QtCore import QSettings


class Config:
    """
    Config class is made to manage stuff that we change inside editor with the ui. This includes:
     * checkbox presses
     * editor specific stuff

    config stores mod settings by using config modules
    """
    def __init__(self, manager):
        self.settings = QSettings(AUTHOR, NAME, manager.application)
        self.manager = manager
        # self.modules: list[ConfigModule] = []

        # 1st step: apply all configs
        # 2nd step: apply all settings from configs to mods and ui
        # 3rd step: store settings when we save level

    def init_configs(self, clear):
        if clear:
            self.settings.clear()
        # uuh done i think???
        # get config file
        # path = self.ensure_config()
        # with open(path) as f:
        #     js = json.load(f)
        #     self.values = {k: v for k, v in js.items()}
        # old method
        # path = self.ensure_config()
        # with open(path) as f:
        #     for l in f.readlines():
        #         l = l.strip()
        #         if len(l) == 0 or l[:1] == "//":
        #             continue
        #         name = l[:l.find("=")]
        #         value = l[l.find("=") + 1:]
        #         self.values[name] = value

    def save_configs(self):
        # uuh that it i think
        if self.manager.application.parser.isSet(self.manager.application.args.blocksave):
            return
        for i in self.manager.mods:
            for v in i.configs:
                self.settings.setValue(f"{i.author_id}.{v.name}", v.save_str_value())
        return
        # js = {}
        # for i in self.manager.mods:
        #     for v in i.configs:
        #         js[f"{i.author_id}.{v.name}"] = v.save_str_value()
        # path = self.ensure_config()
        # with open(path, "w") as f:
        #     f.write(json.dumps(js))

        # old method
        # path = self.ensure_config()
        # with open(path, "w") as f:
        #     for i in self.manager.mods:
        #         for v in i.configs:
        #             if v.description.strip() != "":
        #                 f.write(f"// {v.description}\n")
        #             f.write(f"{i.author_name}.{v.name}={v.save_str_value()}\n")
        #         f.write("\n\n")

    # def ensure_config(self) -> str:
    #     """
    #     !!!OBSOLETE!!!
    #
    #     ensures that config file exists and returns path to it
    #     :return: path to config.txt
    #     """
    #     path = appdirs.user_config_dir(NAME, AUTHOR)
    #     if not os.path.exists(path):
    #         os.makedirs(path, exist_ok=True)
    #     if not os.path.exists(os.path.join(path, "config.json")):
    #         print(f'Trying to create {os.path.join(path, "config.json")}')
    #         with open(os.path.join(path, "config.json"), "w") as f:
    #             f.write("{}")
    #     if not os.path.exists(os.path.join(path, "config.json")):
    #         path = PATH_FILES
    #         print(f'Trying to create {os.path.join(path, "config.json")}')
    #         with open(os.path.join(path, "config.json"), "w") as f:
    #             f.write("{}")
    #     if not os.path.exists(os.path.join(path, "config.json")):
    #         print("well shit")
    #
    #     return os.path.join(path, "config.json")
