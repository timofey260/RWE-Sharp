from RWESharp.Ui import UI
from BaseMod.effects.ui.effects_ui import Ui_Effects
from PySide6.QtWidgets import QTreeWidgetItem, QTreeWidget, QDialog
from PySide6.QtCore import Qt, QPoint, QItemSelectionModel, QRect
from PySide6.QtGui import QPixmap
from BaseMod.effects.ui.effectsdialog import Ui_EffectDialog

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

    # Assuming your effect_settings method generates or fetches the list of settings.
    def effect_settings(self):
        self.ui.OptionsTree.clear()
        self.ui.OptionsTree.setAlternatingRowColors(True)
        self.ui.OptionsTree.setColumnCount(2)
        self.ui.OptionsTree.setColumnWidth(0, 180)
        self.ui.OptionsTree.setHeaderLabels(['Setting', 'Value'])

        effect = self.mod.manager.level.effects[self.editor.effectindex.value]

        settings_list = []  # Initialize a list to store the settings

        for i in effect["options"]:
            item = QTreeWidgetItem([i[0], str(i[1])])
            print(i)
            self.ui.OptionsTree.addTopLevelItem(item)
            settings_list.append(i[0])  # Add each setting to the list

        self.settings_list = settings_list  # Store the list in an instance variable

        return settings_list
    def effect_settings_double_click(self):
        current_item = self.ui.OptionsTree.currentItem()
        if current_item and self.ui.OptionsTree.currentColumn() == 1:
            print(current_item.text(0))
            selected_item = self.ui.EffectsTree.currentItem()
            if selected_item:
                selected_item.setText(0, current_item.text(0))

            effect_dialog = Ui_EffectDialog()
            dialog = QDialog()
            effect_dialog.setupUi(dialog)

            # Show the dialog and wait for the user's input
            result = dialog.exec_()

            # Check the result of the dialog
            if result == QDialog.DialogCode.Accepted:
                # The dialog was accepted
                # Add your code here to handle the accepted dialog
                pass
            elif result == QDialog.DialogCode.Rejected:
                # The dialog was rejected
                # Add your code here to handle the rejected dialog
                pass

