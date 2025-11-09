from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QCheckBox

from BaseMod.light.ui.light_ui import Ui_Light
from BaseMod.light.ui.light_vis_ui import Ui_LightView
from RWESharp2.Configurable import FloatConfigurable, BoolConfigurable, KeyConfigurable, StringConfigurable
from RWESharp2.Ui import UI, ViewUI


class LightUI(UI):
    def __init__(self, mod):
        from BaseMod.light.lightEditor import LightEditor
        super().__init__(mod)
        self.ui = Ui_Light()
        self.ui.setupUi(self)

        self.editor: LightEditor = mod.lighteditor
        self.editor.lightangle.link_doublespinbox(self.ui.Angle)
        self.editor.lightflatness.link_spinbox(self.ui.Flatness)
        self.editor.brushrotation.link_doublespinbox(self.ui.Rotation)
        self.editor.brushwidth.link_doublespinbox(self.ui.Width)
        self.editor.brushheight.link_doublespinbox(self.ui.Height)
        self.editor.drawonmoved.link_button(self.ui.DrawOnMoved)
        for k, v in self.editor.brushimages.items():
            self.ui.Shape.addItem(v, k, userData=v)

        self.brushimage = StringConfigurable(None, "", list(self.editor.brushimages.keys())[0], "Brush Image")
        self.brushimage.link_combobox(self.ui.Shape)
        self.brushimage.valueChanged.connect(self.update_brush)

    def update_brush(self, newimage):
        self.editor.virtgraphicspixmap.setPixmap(self.editor.brushimages[newimage])
        self.editor.update_brush_transform()


class LightViewUI(ViewUI):
    def __init__(self, mod):
        super().__init__(mod)
        self.ui = Ui_LightView()
        self.ui.setupUi(self)
        self.showlightaction = QAction("Light")

        self.showlight_key = KeyConfigurable(mod, "VIEW_light.showlight_key", "Alt+l", "Show Lights")

        self.lightopacity = FloatConfigurable(mod, "VIEW_light.lightop", .4, "Light image opacity")
        self.lightstaticopacity = FloatConfigurable(mod, "VIEW_light.lightstaticop", .3, "Static Light image opacity")
        self.showlight = BoolConfigurable(mod, "VIEW_light.showlight", False)
        self.showlightstatic = BoolConfigurable(mod, "VIEW_light.showlightstatic", True)
        self.showlightmoved = BoolConfigurable(mod, "VIEW_light.showlightmoved", True)

        self.showlight.link_button(self.ui.ShowLight)
        self.showlightstatic.link_button(self.ui.ShowStatic)
        self.showlightmoved.link_button(self.ui.ShowMoved)
        self.lightopacity.link_slider(self.ui.MovedSlider, division=100)
        self.lightstaticopacity.link_slider(self.ui.StaticSlider, division=100)

        self.VQuickLight = QCheckBox()
        self.VQuickLight.setObjectName(u"VQuickLight")
        self.VQuickLight.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self.VQuickLight.setChecked(True)
        self.mod.add_quickview_option(self.VQuickLight)
        self.showlight.link_button_action(self.VQuickLight, self.showlightaction, self.showlight_key)
        self.mod.manager.view_menu.addAction(self.showlightaction)
