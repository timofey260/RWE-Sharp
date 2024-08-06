from RWESharp.Core import ViewDockWidget
from PySide6.QtWidgets import QTreeWidgetItem
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from BaseMod.effects.ui.effectexplorer_ui import Ui_EffectExplorer
from RWESharp.Loaders import Effect


class EffectExplorer(ViewDockWidget):
    def __init__(self, mod, parent=None):
        super().__init__(parent)
        self.mod = mod
        parent.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self)
        self.setFloating(True)
        self.ui = Ui_EffectExplorer()
        self.ui.setupUi(self)
        self.load_effects()
        self.ui.Effects.itemClicked.connect(self.effect_pressed)

    def load_effects(self):
        for i in self.mod.manager.effects.categories:
            item = QTreeWidgetItem([i.name])
            item.setData(0, Qt.ItemDataRole.UserRole, i)
            icon = QPixmap(20, 20)
            icon.fill(i.color)
            item.setIcon(0, icon)
            for e in i.effects:
                effect = QTreeWidgetItem([e.name])
                effect.setData(0, Qt.ItemDataRole.UserRole, e)
                effect.setIcon(0, icon)
                item.addChild(effect)
            self.ui.Effects.addTopLevelItem(item)

    def effect_pressed(self, item: QTreeWidgetItem, column: int):
        if isinstance(item.data(0, Qt.ItemDataRole.UserRole), Effect):
            self.ui.Effectpreview.load_effect(item.data(0, Qt.ItemDataRole.UserRole))
