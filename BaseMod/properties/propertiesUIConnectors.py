from RWESharp.Ui import UI
from BaseMod.properties.ui.properties_ui import Ui_Properties
from BaseMod.properties.propertiesEditor import PropertiesEditor
import random

class PropertiesUI(UI):
    def __init__(self, mod):
        super().__init__(mod)
        self.ui = Ui_Properties()
        self.ui.setupUi(self)
        self.editor: PropertiesEditor = self.mod.propertieseditor

        self.editor.xofs.link_spinbox(self.ui.XOfs)
        self.editor.yofs.link_spinbox(self.ui.YOfs)
        self.editor.width.link_spinbox(self.ui.WidthCells)
        self.editor.height.link_spinbox(self.ui.HeightCells)

        self.editor.left.link_spinbox(self.ui.BorderLeft)
        self.editor.top.link_spinbox(self.ui.BorderTop)
        self.editor.right.link_spinbox(self.ui.BorderRight)
        self.editor.bottom.link_spinbox(self.ui.BorderBottom)

        self.editor.waterheight.link_spinbox(self.ui.WaterHeight)
        self.editor.watertype.link_combobox(self.ui.WaterState)

        self.editor.seed.link_spinbox(self.ui.TileSeedSpin, True)
        self.ui.TileSeedRandom.clicked.connect(lambda: self.editor.seed.update_value_default(random.randint(0, 999)))
        self.ui.Reset.clicked.connect(self.editor.reposition)

        self.ui.Resize.clicked.connect(self.editor.confirm_resize)
