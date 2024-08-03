from RWESharp.Ui import UI
from BaseMod.effects.ui.effects_ui import Ui_Effects
from PySide6.QtWidgets import QTreeWidgetItem


class EffectsUI(UI):
    def __init__(self, mod, parent=None):
        super().__init__(mod, parent)
        from BaseMod.baseMod import BaseMod
        self.ui = Ui_Effects()
        self.ui.setupUi(self)
        mod: BaseMod
        self.editor = mod.effecteditor
        self.ui.EffectsTree.setAlternatingRowColors(True)

        self.editor.effectup.link_button(self.ui.Up)
        self.editor.effectdown.link_button(self.ui.Down)
        self.editor.effectmoveup.link_button(self.ui.MoveUp)
        self.editor.effectmovedown.link_button(self.ui.MoveDown)
        self.editor.delete.link_button(self.ui.DeleteEffect)
        self.editor.duplicate.link_button(self.ui.DuplicateEffect)

        self.add_effects()

    def add_effects(self):
        self.ui.EffectsTree.clear()
        for i, effect in enumerate(self.mod.manager.level.effects):
            self.ui.EffectsTree.addTopLevelItem(QTreeWidgetItem([str(i), effect["nm"]]))
        self.ui.EffectsTree.resizeColumnToContents(0)
