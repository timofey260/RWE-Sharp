from PySide6.QtCore import Qt, QPoint, QCoreApplication
from PySide6.QtGui import QAction, QColor
from PySide6.QtWidgets import QTreeWidgetItem, QInputDialog, QMenu, QCheckBox

from BaseMod.props.ui.props_ui import Ui_Props
from BaseMod.props.ui.props_vis_ui import Ui_PropsView
from RWESharp2.Configurable import KeyConfigurable, BoolConfigurable, ColorConfigurable
from RWESharp2.Ui import UI, ViewUI


class PropsUI(UI):
    def __init__(self, mod, parent=None):
        super().__init__(mod, parent)
        self.editor = mod.propeditor
        self.editor.propsui = self
        self.ui = Ui_Props()
        self.ui.setupUi(self)
        self.ui.Notes.setText("\n".join(self.editor.prop.notes))

        self.free_transform = KeyConfigurable(mod, "EDIT_props.free_transform", "f", "Free transform")
        self.reset_transform = KeyConfigurable(mod, "EDIT_props.reset_transform", "r", "Reset transform")
        self.explorer_key = KeyConfigurable(mod, "EDIT_props.explorer", "Ctrl+e", "Open Prop Explorer")

        self.prop_prev_key = KeyConfigurable(mod, "EDIT_props.prop_prev", "w", "Previous Prop")
        self.cat_prev_key = KeyConfigurable(mod, "EDIT_props.cat_prev", "a", "Previous Category")
        self.prop_next_key = KeyConfigurable(mod, "EDIT_props.prop_next", "s", "Next Prop")
        self.cat_next_key = KeyConfigurable(mod, "EDIT_props.cat_next", "d", "Next Category")
        self.find_key = KeyConfigurable(mod, "EDIT_props.find_key", "Ctrl+f", "Find Prop")

        self.rotate_cw = KeyConfigurable(mod, "EDIT_props.cw", "Shift+e", "Rotate prop clockwise")
        self.rotate_ccw = KeyConfigurable(mod, "EDIT_props.ccw", "Shift+q", "Rotate prop counter-clockwise")
        self.ui.degreeamount.setValue(90)

        self.explorer_key.link_button(self.ui.Explorer)
        self.prop_next_key.link_button(self.ui.PropNext)
        self.prop_prev_key.link_button(self.ui.PropPrev)
        self.cat_next_key.link_button(self.ui.CatNext)
        self.cat_prev_key.link_button(self.ui.CatPrev)
        self.find_key.link_button(self.ui.FindPE)
        self.rotate_cw.link_button(self.ui.add15)
        self.rotate_ccw.link_button(self.ui.sub15)

        self.ui.PropNext.clicked.connect(self.editor.explorer.item_next)
        self.ui.PropPrev.clicked.connect(self.editor.explorer.item_prev)
        self.ui.CatNext.clicked.connect(self.editor.explorer.cat_next)
        self.ui.CatPrev.clicked.connect(self.editor.explorer.cat_prev)
        self.ui.FindPE.clicked.connect(self.editor.explorer.focussearch)

        self.free_transform.link_button(self.ui.FreeTransform)
        self.ui.FreeTransform.clicked.connect(self.editor.free_transform)
        self.reset_transform.link_button(self.ui.ResetTransform)
        self.ui.ResetTransform.clicked.connect(self.editor.reset_transform)
        self.ui.Explorer.clicked.connect(self.open_explorer)
        self.ui.PropOptions.setColumnCount(2)
        self.ui.PropOptions.itemClicked.connect(self.prop_options_click)
        self.ui.PropOptions.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.PropOptions.customContextMenuRequested.connect(self.settings_context_menu)
        self.ui.add15.clicked.connect(lambda: self.editor.rotate(15))
        self.ui.sub15.clicked.connect(lambda: self.editor.rotate(-15))
        self.ui.Rotateby.clicked.connect(lambda: self.editor.rotate(self.ui.degreeamount.value()))
        self.display_settings()

    def display_settings(self):
        self.ui.PropOptions.clear()
        for k, v in self.editor.prop_settings.items():
            match k:
                case "release":
                    t = ["left", "none", "right"][v - 1]
                case "renderTime":
                    t = ["Pre Effects", "Post Effcts"][v]
                case "variation":
                    t = "random" if v == 0 else str(v)
                case "applyColor":
                    t = ["NO", "YES"][v]
                case "color":
                    t = "NONE" if v == 0 else self.mod.manager.prop_colors[v - 1]
                case _:
                    t = str(v)
            item = QTreeWidgetItem([k, t])
            item.setData(0, Qt.ItemDataRole.UserRole, k)
            self.ui.PropOptions.addTopLevelItem(item)

        self.ui.Notes.setText("\n".join(self.editor.prop.notes))

    def open_explorer(self):
        self.editor.explorer.change_visibility(True)
        self.editor.explorer.focussearch()

    def prop_options_click(self, item: QTreeWidgetItem, column):
        name = item.data(0, Qt.ItemDataRole.UserRole)
        match name:
            case "release":
                val = (self.editor.prop_settings[name] + 2) % 3 - 1
            case "renderTime":
                val = (self.editor.prop_settings[name] + 1) % 2
            case "customDepth":
                val = self.editor.prop_settings[name] % 30 + 1
            case "variation":
                val = (self.editor.prop_settings[name] + 1) % len(self.editor.selectedprop["images"])
                self.editor.variationadd()
            case "thickness":
                val = self.editor.prop_settings[name] % 5 + 1
            case "applyColor":
                val = (self.editor.prop_settings[name] + 1) % 2
            case "color":
                val = (self.editor.prop_settings[name] + 1) % len(self.mod.manager.prop_colors)
            case _:
                nval, ok = QInputDialog.getInt(self, f"Enter {name}", f"{name}:", self.editor.prop_settings[name])
                if not ok:
                    return
                val = nval
        self.editor.prop_settings[name] = val
        self.display_settings()

    def settings_context_menu(self, pos: QPoint):
        if len(self.ui.PropOptions.selectedItems()) == 0:
            return
        item = self.ui.PropOptions.selectedItems()[0]
        key = item.data(0, Qt.ItemDataRole.UserRole)
        menu = QMenu("Options", self.ui.PropOptions)
        vals = []
        match key:
            case "release":
                a = QAction("left", menu)
                b = QAction("none", menu)
                c = QAction("right", menu)
                a.triggered.connect(self.setoption(key, -1))
                b.triggered.connect(self.setoption(key, 0))
                c.triggered.connect(self.setoption(key, 1))
                vals = [a, b, c]
            case "renderTime":
                a = QAction("Pre Effects", menu)
                b = QAction("Post Effcts", menu)
                a.triggered.connect(self.setoption(key, 0))
                b.triggered.connect(self.setoption(key, 1))
                vals = [a, b]
            case "customDepth":
                vals = []
                for i in range(1, 31):
                    a = QAction(str(i), menu)
                    a.triggered.connect(self.setoption(key, i))
                    vals.append(a)
            case "variation":
                vals = []
                for i in range(0, self.editor.prop.vars+1):
                    if i == 0:
                        a = QAction("random", menu)
                        a.triggered.connect(self.setoption(key, 0))
                        vals.append(a)
                        continue
                    a = QAction(str(i), menu)
                    a.triggered.connect(self.setoption(key, i))
                    vals.append(a)
            case "thickness":
                vals = []
                for i in range(1, 6):
                    a = QAction(str(i), menu)
                    a.triggered.connect(self.setoption(key, i))
                    vals.append(a)
            case "applyColor":
                a = QAction("NO", menu)
                b = QAction("YES", menu)
                a.triggered.connect(self.setoption(key, 0))
                b.triggered.connect(self.setoption(key, 1))
                vals = [a, b]
            case "color":
                vals = []
                for i in range(0, len(self.mod.manager.prop_colors)+1):
                    if i == 0:
                        a = QAction("NONE", menu)
                        a.triggered.connect(self.setoption(key, 0))
                        vals.append(a)
                        continue
                    a = QAction(str(self.mod.manager.prop_colors[i - 1]), menu)
                    a.triggered.connect(self.setoption(key, i))
                    vals.append(a)
            case _:
                self.prop_options_click(item, 0)
                return
        if len(vals) == 0:
            return
        # default = None
        menu.addActions(vals)
        menu.popup(self.ui.PropOptions.mapToGlobal(pos))
        menu.show()

    def setoption(self, key, value):
        def callback():
            self.editor.prop_settings[key] = value
            self.display_settings()
        return callback


class PropsViewUI(ViewUI):
    def __init__(self, mod, parent=None):
        super().__init__(mod, parent)
        self.ui = Ui_PropsView()
        self.ui.setupUi(self)

        # self.opshift = BoolConfigurable(mod, "VIEW_props.opshift", True, "Opacity shift")
        self.showprops = BoolConfigurable(mod, "VIEW_props.show", True, "Show Props")
        self.showoutline = BoolConfigurable(mod, "VIEW_props.showoutline", False, "Outline Props")
        self.outline_color = ColorConfigurable(mod, "VIEW_props.showoutline", QColor(255, 0, 0), "Outline Color")

        self.menu_showprops = QAction("Props")
        self.mod.manager.view_menu.addAction(self.menu_showprops)
        self.showprops = BoolConfigurable(mod, "VIEW_props.show", True, "Show Props")
        self.showprops_key = KeyConfigurable(mod, "VIEW_props.show_key", "Alt+p", "Show Props Key")

        self.showoutline.link_button(self.ui.Outline)
        self.outline_color.link_color_picker(self.ui.OutlineColor)
        self.showprops.link_button_action(self.ui.ShowProps, self.menu_showprops, self.showprops_key)

        self.VQuickProps = QCheckBox()
        self.VQuickProps.setObjectName(u"VQuickProps")
        self.VQuickProps.setText(QCoreApplication.translate("MainWindow", u"Props", None))
        self.VQuickProps.setChecked(True)
        self.mod.add_quickview_option(self.VQuickProps)

        self.showprops.link_button_action(self.VQuickProps, self.menu_showprops, self.showprops_key)
