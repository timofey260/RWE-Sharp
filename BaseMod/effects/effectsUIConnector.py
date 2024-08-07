from RWESharp.Ui import UI
from BaseMod.effects.ui.effects_ui import Ui_Effects
from PySide6.QtWidgets import QTreeWidgetItem
from PySide6.QtCore import Qt


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
        self.add_effects()

    def add_effects(self):
        self.ui.EffectsTree.clear()
        for i, effect in enumerate(self.mod.manager.level.effects):
            item = QTreeWidgetItem([str(i), effect["nm"]])
            item.setData(0, Qt.ItemDataRole.UserRole, i)
            item.setData(1, Qt.ItemDataRole.UserRole, effect)
            self.ui.EffectsTree.addTopLevelItem(item)
        self.ui.EffectsTree.resizeColumnToContents(0)

    def effect_pressed(self, item: QTreeWidgetItem, column: int):
        self.editor.select_effect(item.data(0, Qt.ItemDataRole.UserRole))

