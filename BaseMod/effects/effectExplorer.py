from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QAction, QColor
from PySide6.QtWidgets import QTreeWidgetItem

from BaseMod.effects.effectHistory import EffectAdd
from BaseMod.effects.ui.effectexplorer_ui import Ui_EffectExplorer
from RWESharp2.Core import ViewDockWidget
from RWESharp2.Loaders import Effect, EffectCategory
from RWESharp2.Utils import color_lerp


class EffectExplorer(ViewDockWidget):
    def __init__(self, editor, parent=None):
        super().__init__(parent)
        self.mod = editor.mod
        parent.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self)
        self.setFloating(True)
        self.ui = Ui_EffectExplorer()
        self.ui.setupUi(self)
        self.load_effects()
        self.ui.Effects.itemClicked.connect(self.effect_pressed)
        self.ui.Effects.itemSelectionChanged.connect(self.selection_changed)
        self.ui.Effects.itemDoubleClicked.connect(self.add_effect)
        self.ui.AddEffect.clicked.connect(self.add_effect)
        # self.ui.splitter.widget(0)
        self.ui.splitter.setSizes([2, 5])
        self.ui.Search.textChanged.connect(self.search)
        # self.ui.splitter.splitterMoved.connect(self.moved)
        self.effect = None
        self.image = self.ui.Effectpreview.workscene.addPixmap(QPixmap(1, 1))
        self.ui.Effectpreview.items.append(self.image)

        self.effect_explorer_action = QAction("Effect Explorer")
        self.mod.manager.window_menu.addAction(self.effect_explorer_action)
        self.link_action(self.effect_explorer_action)
        self.change_visibility(False)
        self.mod.bmconfig.effectexplorer_key.link_action(self.effect_explorer_action)

    def resizeEvent(self, event):
        if hasattr(self, 'ui') and self.ui:
            width,  height = self.width(), self.height()
            aspect_ratio = width / height if height else 1
            if hasattr(self.ui, "splitter") and self.ui.splitter:
                self.ui.splitter.setOrientation(Qt.Orientation.Horizontal if aspect_ratio > 1.45 else Qt.Orientation.Vertical)
        super().resizeEvent(event)

    def search(self):
        self.load_effects()

    def add_effect(self):
        self.mod.manager.selected_viewport.level.add_history(EffectAdd, self.effect)
        if len(self.mod.manager.selected_viewport.level.l_effects) == 1:
            self.mod.effecteditor.select_effect(0)

    def load_effects(self):
        filter = self.ui.Search.text()
        self.ui.Effects.clear()
        for i in self.mod.manager.effects.categories:
            item = QTreeWidgetItem([i.name])
            item.setData(0, Qt.ItemDataRole.UserRole, i)
            icon = QPixmap(20, 20)
            icon.fill(i.color)
            item.setIcon(0, icon)
            for indx, e in enumerate(i.effects):
                if filter != "" and filter.lower() not in e.name.lower():
                    continue
                icon2 = QPixmap(20, 20)
                icon2.fill(color_lerp(i.color, QColor(0, 0, 0), indx / 15))
                effect = QTreeWidgetItem([e.name])
                effect.setData(0, Qt.ItemDataRole.UserRole, e)
                effect.setIcon(0, icon2)
                item.addChild(effect)
            if filter != "" and item.childCount() == 0:
                continue
            self.ui.Effects.addTopLevelItem(item)
        if filter != "":
            self.ui.Effects.expandAll()

    def selection_changed(self):
        items = self.ui.Effects.selectedItems()
        if len(items) == 0:
            return
        self.set_preview(items[0])

    def effect_pressed(self, item: QTreeWidgetItem, column: int):
        self.set_preview(item)

    def set_preview(self, item: QTreeWidgetItem):
        if isinstance(item.data(0, Qt.ItemDataRole.UserRole), Effect):
            self.effect = item.data(0, Qt.ItemDataRole.UserRole)
            self.image.setPixmap(self.effect.preview)
            self.ui.Description.setText(item.data(0, Qt.ItemDataRole.UserRole).description)
        elif isinstance(item.data(0, Qt.ItemDataRole.UserRole), EffectCategory):
            self.ui.Effects.expand(self.ui.Effects.indexFromItem(item, 0))
            self.ui.Description.setText(item.data(0, Qt.ItemDataRole.UserRole).name)


