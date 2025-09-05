from RWESharp.Ui import UI, ViewUI
from BaseMod.light.ui.light_ui import Ui_Light


class LightUI(UI):
    def __init__(self, mod):
        from BaseMod.light.lightEditor import LightEditor
        super().__init__(mod)
        self.ui = Ui_Light()
        self.ui.setupUi(self)

        self.editor: LightEditor = mod.lighteditor
        self.editor.lightangle.link_doublespinbox(self.ui.Angle)
        self.editor.lightflatness.link_spinbox(self.ui.Flatness)
