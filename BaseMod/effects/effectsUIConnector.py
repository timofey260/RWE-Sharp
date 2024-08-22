from RWESharp.Ui import UI
from BaseMod.effects.ui.effects_ui import Ui_Effects
from PySide6.QtWidgets import QTreeWidgetItem, QDialog, QInputDialog
from PySide6.QtCore import Qt, QPoint, QItemSelectionModel
from PySide6.QtGui import QPixmap
from BaseMod.effects.ui.effectsdialog import Ui_EffectDialog


class EffectDialog(QDialog):
    def __init__(self, options: list[str], parent=None):
        super().__init__(parent)
        self.ui = Ui_EffectDialog()
        self.ui.setupUi(self)
        self.options = options
        self.ui.EffectSettingValueComboBox.addItems(options)


class EffectsUI(UI):
    def __init__(self, mod, parent=None):
        super().__init__(mod, parent)
        from BaseMod.baseMod import BaseMod
        self.ui = Ui_Effects()
        self.ui.setupUi(self)
        mod: BaseMod
        self.editor = mod.effecteditor
        self.explorer = mod.effect_explorer
        self.ui.EffectsTree.setAlternatingRowColors(True)

        self.editor.effectup.link_button(self.ui.Up)
        self.editor.effectdown.link_button(self.ui.Down)
        self.editor.effectmoveup.link_button(self.ui.MoveUp)
        self.editor.effectmovedown.link_button(self.ui.MoveDown)
        self.editor.delete.link_button(self.ui.DeleteEffect)
        self.editor.duplicate.link_button(self.ui.DuplicateEffect)
        self.ui.EffectsTree.itemClicked.connect(self.effect_pressed)

        self.explorer.ui.AddEffect.clicked.connect(self.add_effects)
        self.editor.effectindex.valueChanged.connect(self.effect_select)
        self.ui.Up.clicked.connect(self.effect_up)
        self.ui.Down.clicked.connect(self.effect_down)
        self.add_effects()
        self.effect_settings()
        self.ui.OptionsTree.itemDoubleClicked.connect(self.effect_settings_double_click)

    def effect_up(self):
        self.editor.effectindex.update_value((self.editor.effectindex.value - 1) % self.mod.manager.level.effect_len)

    def effect_down(self):
        self.editor.effectindex.update_value((self.editor.effectindex.value + 1) % self.mod.manager.level.effect_len)

    def add_effects(self):
        self.ui.EffectsTree.clear()
        for i, effect in enumerate(self.mod.manager.level.effects):
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

    def effect_pressed(self, item: QTreeWidgetItem, column: int):
        self.editor.effectindex.update_value(item.data(0, Qt.ItemDataRole.UserRole))

    def effect_select(self, row):
        item = self.ui.EffectsTree.itemAt(QPoint(0, row * self.ui.EffectsTree.sizeHintForRow(0)))
        # print(item, self.ui.EffectsTree.currentItem(), row)
        if self.ui.EffectsTree.currentItem() != item:
            self.ui.EffectsTree.setCurrentItem(item, 1, QItemSelectionModel.SelectionFlag.ClearAndSelect)
        self.effect_settings()

    def effect_settings(self):
        self.ui.OptionsTree.clear()
        self.ui.OptionsTree.setAlternatingRowColors(True)
        self.ui.OptionsTree.setColumnCount(2)
        self.ui.OptionsTree.setHeaderLabels(['Setting', 'Value'])

        effect = self.mod.manager.level.effects[self.editor.effectindex.value]

        for index, i in enumerate(effect["options"]):
            if i[0].lower() == "delete/move":
                continue
            item = QTreeWidgetItem([i[0], str(i[2])])
            item.setData(0, Qt.ItemDataRole.UserRole, index)
            self.ui.OptionsTree.addTopLevelItem(item)
        self.ui.OptionsTree.resizeColumnToContents(0)

        return

    def effect_settings_double_click(self, item: QTreeWidgetItem, column):
        if column == 1:
            #todo history thing
            if item.text(0).lower() == "seed":
                d = QInputDialog()
                d.setInputMode(QInputDialog.InputMode.IntInput)
                d.setIntRange(0, 1000)
                d.setLabelText("Seed:")
                value = d.exec()
                print(d.intValue(), value)
                return
            index = item.data(0, Qt.ItemDataRole.UserRole)
            d = EffectDialog(self.mod.manager.level.effects[self.editor.effectindex.value]["options"][index][1])
            result = d.exec()

            print(d.ui.EffectSettingValueComboBox.currentText(), result)
