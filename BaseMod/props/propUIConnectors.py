from RWESharp.Ui import UI
from RWESharp.Configurable import KeyConfigurable
from BaseMod.props.ui.props_ui import Ui_Props

from PySide6.QtWidgets import QTreeWidgetItem, QInputDialog, QMenu
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt, QPoint


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
        self.find_key = KeyConfigurable(mod, "EDIT_props.find_key", "Ctrl+f", "Find tile")

        self.explorer_key.link_button(self.ui.Explorer)
        self.prop_next_key.link_button(self.ui.PropNext)
        self.prop_prev_key.link_button(self.ui.PropPrev)
        self.cat_next_key.link_button(self.ui.CatNext)
        self.cat_prev_key.link_button(self.ui.CatPrev)
        self.find_key.link_button(self.ui.FindPE)

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
        self.display_settings()

    def display_settings(self):
        self.ui.PropOptions.clear()
        for k, v in self.editor.prop_settings.items():
            item = QTreeWidgetItem([k, str(v)])
            item.setData(0, Qt.ItemDataRole.UserRole, k)
            self.ui.PropOptions.addTopLevelItem(item)

        self.ui.Notes.setText("\n".join(self.editor.prop.notes))

    def open_explorer(self):
        self.editor.explorer.change_visibility(True)

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
                vals = [-1, 0, 1]
            case "renderTime":
                vals = [0, 1]
            case "customDepth":
                vals = list(range(1, 31))
                # val = self.editor.prop_settings[name] % 30 + 1
            case "variation":
                vals = list(range(0, self.editor.prop.vars+1))
            case "thickness":
                vals = [1, 2, 3, 4, 5]
            case "applyColor":
                vals = [0, 1]
            case "color":
                vals = list(range(len(self.mod.manager.prop_colors)))
            case _:
                self.prop_options_click(item, 0)
                return
        if len(vals) == 0:
            return
        default = None
        for i in vals:
            menu.addAction(str(i), self.setoption(key, i))
            if i == self.editor.prop_settings[key]:
                default = menu.actions()[-1]
        menu.popup(self.ui.PropOptions.mapToGlobal(pos), default)

    def setoption(self, key, value):
        def callback():
            self.editor.prop_settings[key] = value
            self.display_settings()
        return callback