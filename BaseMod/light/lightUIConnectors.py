from RWESharp.Ui import UI, ViewUI
from RWESharp.Configurable import FloatConfigurable, BoolConfigurable, KeyConfigurable
from BaseMod.light.ui.light_ui import Ui_Light
from BaseMod.light.ui.light_vis_ui import Ui_LightView
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QCheckBox
from PySide6.QtGui import QAction


class LightUI(UI):
    def __init__(self, mod):
        from BaseMod.light.lightEditor import LightEditor
        super().__init__(mod)
        self.ui = Ui_Light()
        self.ui.setupUi(self)

        self.editor: LightEditor = mod.lighteditor
        self.editor.lightangle.link_doublespinbox(self.ui.Angle)
        self.editor.lightflatness.link_spinbox(self.ui.Flatness)


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
