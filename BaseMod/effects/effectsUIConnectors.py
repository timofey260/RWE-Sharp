from random import randint

from PySide6.QtCore import Qt, QPoint, QItemSelectionModel
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QTreeWidgetItem, QDialog, QInputDialog, QMenu

from BaseMod.effects.effectHistory import EffectOptionChange, EffectRemove, EffectMove, EffectDuplicate
from BaseMod.effects.ui.effects_ui import Ui_Effects
from BaseMod.effects.ui.effectsdialog import Ui_EffectDialog
from RWS.Configurable import KeyConfigurable
from RWS.Ui import UI


class EffectDialog(QDialog):
    def __init__(self, options: list[str], name, parent=None):
        super().__init__(parent)
        self.ui = Ui_EffectDialog()
        self.ui.setupUi(self)
        self.options = options
        self.ui.EffectSettingValueComboBox.addItems(options)
        self.ui.label.setText(name)
        self.setWindowTitle(name)


class EffectsUI(UI):
    def __init__(self, mod, parent=None):
        super().__init__(mod, parent)
        from BaseMod.baseMod import BaseMod
        self.ui = Ui_Effects()
        self.ui.setupUi(self)
        mod: BaseMod
        self.editor = mod.effecteditor
        self.editor.effectui = self
        self.explorer = self.editor.effect_explorer
        self.ui.EffectsTree.setAlternatingRowColors(True)

        self.effectup_key = KeyConfigurable(mod, "EDIT_effect.effectup", "w", "Previous effect")
        self.effectdown_key = KeyConfigurable(mod, "EDIT_effect.effectdown", "s", "Next effect")
        self.effectmoveup_key = KeyConfigurable(mod, "EDIT_effect.effectmoveup", "Shift+w", "Move effect back")
        self.effectmovedown_key = KeyConfigurable(mod, "EDIT_effect.effectmovedown", "Shift+s", "Move effect forward")
        self.duplicate_key = KeyConfigurable(mod, "EDIT_effect.duplicate", "Ctrl+d", "Duplicate effect")
        self.delete_key = KeyConfigurable(mod, "EDIT_effect.delete", "Delete", "Delete effect")
        self.explorer_key = KeyConfigurable(mod, "EDIT_effect.explorer_key", "Ctrl+e", "Open Effect Explorer")

        self.brushup_key = KeyConfigurable(mod, "EDIT_effect.brushup", "Ctrl+Shift+=", "Brush Size +")
        self.brushdown_key = KeyConfigurable(mod, "EDIT_effect.brushdown", "Ctrl+Shift+-", "Brush Size -")

        self.explorer_key.link_button(self.ui.Explorer)
        self.ui.Explorer.clicked.connect(self.open_explorer)

        self.effectup_key.link_button(self.ui.Up)
        self.effectdown_key.link_button(self.ui.Down)
        self.effectmoveup_key.link_button(self.ui.MoveUp)
        self.effectmovedown_key.link_button(self.ui.MoveDown)
        self.delete_key.link_button(self.ui.DeleteEffect)
        self.duplicate_key.link_button(self.ui.DuplicateEffect)
        self.ui.EffectsTree.itemClicked.connect(self.effect_pressed)

        self.explorer.ui.AddEffect.clicked.connect(self.add_effects)
        self.editor.effectindex.valueChanged.connect(self.effect_select)
        self.ui.Up.clicked.connect(self.effect_up)
        self.ui.Down.clicked.connect(self.effect_down)
        self.ui.DeleteEffect.clicked.connect(self.delete_effect)
        self.ui.MoveUp.clicked.connect(self.effect_move_up)
        self.ui.MoveDown.clicked.connect(self.effect_move_down)
        self.ui.DuplicateEffect.clicked.connect(self.duplicate_effect)

        self.ui.OptionsTree.itemDoubleClicked.connect(self.effect_settings_double_click)
        self.ui.OptionsTree.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.OptionsTree.customContextMenuRequested.connect(self.settings_context_menu)

        self.brushup_key.link_button(self.ui.BrushSizeUp)
        self.brushdown_key.link_button(self.ui.BrushSizeDown)
        self.ui.BrushSizeUp.clicked.connect(self.brushup)
        self.ui.BrushSizeDown.clicked.connect(self.brushdown)

    def brushup(self):
        self.editor.brushsize.update_value(self.editor.brushsize.value + 1)
        self.editor.update_brush()

    def brushdown(self):
        self.editor.brushsize.update_value(max(1, self.editor.brushsize.value - 1))
        self.editor.update_brush()

    def delete_effect(self):
        if 0 <= self.editor.effectindex.value < len(self.level.l_effects):
            self.level.add_history(EffectRemove, self.editor.effectindex.value)

    def open_explorer(self):
        self.explorer.change_visibility(True)
        #self.explorer.focussearch()

    def effect_up(self):
        if len(self.level.l_effects) == 0:
            return
        self.editor.effectindex.update_value((self.editor.effectindex.value - 1) % len(self.level.l_effects))

    def effect_down(self):
        if len(self.level.l_effects) == 0:
            return
        self.editor.effectindex.update_value((self.editor.effectindex.value + 1) % len(self.level.l_effects))

    def effect_move_up(self):
        if len(self.level.l_effects) == 0:
            return
        if self.editor.effectindex.value > 0:
            self.level.add_history(EffectMove, self.editor.effectindex.value, -1)

    def effect_move_down(self):
        if len(self.level.l_effects) == 0:
            return
        if self.editor.effectindex.value < len(self.level.l_effects) - 1:
            self.level.add_history(EffectMove, self.editor.effectindex.value, 1)

    def duplicate_effect(self):
        if len(self.level.l_effects) == 0:
            return
        if 0 <= self.editor.effectindex.value < len(self.level.l_effects):
            self.level.add_history(EffectDuplicate, self.editor.effectindex.value)

    def add_effects(self):
        self.ui.EffectsTree.clear()
        if not self.level_loaded:
            return
        for i, effect in enumerate(self.mod.manager.selected_viewport.level.l_effects):
            item = QTreeWidgetItem([str(i), effect["nm"]])
            item.setData(0, Qt.ItemDataRole.UserRole, i)
            item.setData(1, Qt.ItemDataRole.UserRole, effect)
            e = self.mod.manager.effects.find_effect(effect["nm"])
            if e is not None:
                icon = QPixmap(20, 20)
                icon.fill(e.color)
                item.setIcon(0, icon)
            self.ui.EffectsTree.addTopLevelItem(item)
        self.ui.EffectsTree.resizeColumnToContents(0)
        self.effect_settings()

    def effect_pressed(self, item: QTreeWidgetItem, column: int):
        self.editor.effectindex.update_value(item.data(0, Qt.ItemDataRole.UserRole))

    def effect_select(self, row):
        item = self.ui.EffectsTree.topLevelItem(row)
        # print(item, self.ui.EffectsTree.currentItem(), row)
        if self.ui.EffectsTree.currentItem() != item:
            self.ui.EffectsTree.setCurrentItem(item, 1, QItemSelectionModel.SelectionFlag.ClearAndSelect)
        self.effect_settings()

    def effect_settings(self):
        self.ui.OptionsTree.clear()
        self.ui.OptionsTree.setAlternatingRowColors(True)
        self.ui.OptionsTree.setColumnCount(2)
        self.ui.OptionsTree.setHeaderLabels(['Setting', 'Value'])
        if not self.level_loaded or len(self.level.l_effects) == 0:
            return
        effect = self.level.l_effects[self.editor.effectindex.value]

        for index, i in enumerate(effect["options"]):
            if i[0].lower() == "delete/move":
                continue
            item = QTreeWidgetItem([i[0], str(i[2])])
            item.setData(0, Qt.ItemDataRole.UserRole, index)
            self.ui.OptionsTree.addTopLevelItem(item)
        self.ui.OptionsTree.resizeColumnToContents(0)

    def effect_settings_double_click(self, item: QTreeWidgetItem, column):
        if column == 1:
            index = item.data(0, Qt.ItemDataRole.UserRole)
            options = self.level.l_effects[self.editor.effectindex.value]["options"][index]
            if item.text(0).lower() == "seed":
                value, ok = QInputDialog.getInt(self, f"Enter Seed", f"Seed:", int(options[2]))

                if ok:
                    self.level.add_history(EffectOptionChange, self.editor.effectindex.value, index, str(value))
                return
            d = EffectDialog(options[1], options[0])
            value = d.exec()
            if value == QDialog.DialogCode.Accepted:
                self.level.add_history(EffectOptionChange, self.editor.effectindex.value, index, d.ui.EffectSettingValueComboBox.currentText())

    def settings_context_menu(self, pos: QPoint):
        if len(self.ui.OptionsTree.selectedItems()) == 0:
            return
        item = self.ui.OptionsTree.selectedItems()[0]
        index = item.data(0, Qt.ItemDataRole.UserRole)
        menu = QMenu("Options", self.ui.OptionsTree)
        if item.text(0).lower() == "seed":
            menu.addAction("Randomize", self.setoption(index, str(randint(0, 100))))
            menu.popup(self.ui.OptionsTree.mapToGlobal(pos))
            return
        defaultaction = None
        for i in self.level.l_effects[self.editor.effectindex.value]["options"][index][1]:
            menu.addAction(i, self.setoption(index, i))
            if i == self.level.l_effects[self.editor.effectindex.value]["options"][index][2]:
                defaultaction = menu.actions()[-1]
        menu.popup(self.ui.OptionsTree.mapToGlobal(pos), defaultaction)

    def setoption(self, index, value):
        def callback():
            self.level.add_history(EffectOptionChange, self.editor.effectindex.value, index, value)
        return callback
