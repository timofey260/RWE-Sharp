from __future__ import annotations
from PySide6.QtGui import QColor, QPixmap
from PySide6.QtCore import Qt, QPoint, Slot, QPointF
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QApplication, QFileDialog
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from core.Modify.baseModule import Module
    from core.Manager import Manager
    from core.Level.RWELevel import RWELevel
from core.info import CELLSIZE, PATH_LEVELS


class ViewPort(QGraphicsView):
    """
    Viewport for visualizing level and editors

    :param level: level to load
    :param manager: rwe# manager
    :param parent: widget parent
    """
    def __init__(self, level, manager, parent=None):
        super().__init__(parent)
        self.level: RWELevel = level
        self.level.viewport = self
        self.manager: Manager = manager
        self.workscene: QGraphicsScene = QGraphicsScene(self)
        self.setScene(self.workscene)
        self.zoom = 1
        # self.origin = self.workscene.addEllipse(0, 0, 1, 1, QColor(0, 0, 0, 0))
        self.topleft = self.workscene.addEllipse(0, 0, 1, 1, QColor(0, 0, 0, 0))
        self.uselessthing = self.workscene.addRect(0, 0, 9999, 9999, QColor(0, 0, 0, 0))  # just a big rect to keep shit working
        self.verticalScrollBar().sliderReleased.connect(self.redraw)
        self.horizontalScrollBar().sliderReleased.connect(self.redraw)
        self.setMouseTracking(True)
        self._lmb = False
        self._rmb = False
        self._mmb = False
        self.mouse_pos = QPoint()
        self.modules: list[Module] = []
        self.modulenames: dict[str, Module] = {}
        # self.setBackgroundBrush(QBrush(QColor(30, 30, 30), Qt.BrushStyle.SolidPattern))
        for i in self.manager.mods:
            i.level_opened(self)

    @Slot()
    def redraw(self):
        self.repaint()

    def add_module(self, module: Module, name=None, editor=False):
        if not editor:
            self.modules.append(module)
            if name is not None:
                self.modulenames[name] = module
        module.viewport = self
        module.init_scene_items(self)
        for i in module.renderables:
            i.init_graphics(self)
        for i in module.renderables:
            i.post_init_graphics(self)

        self.repaint()
        module.zoom_event()
        module.move_event()

    def remove_module(self, module: Module):
        if module in self.modules:
            self.modules.remove(module)
        if module in self.modulenames.values():
            del self.modulenames[list(self.modulenames.keys())[list(self.modulenames.values()).index(module)]]
        module.remove_items_from_scene(self)
        module.viewport = None
        for i in module.renderables:
            i.remove_graphics(self)
        self.repaint()

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        if self.scene().mouseGrabberItem() is not None:
            return
        if event.buttons() & self.manager.basemod.bmconfig.main_button.value:
            self._lmb = True
            self.editor.mouse_left_press()
        if event.buttons() & self.manager.basemod.bmconfig.sec_button.value:
            self._rmb = True
            self.editor.mouse_right_press()
        if event.buttons() & self.manager.basemod.bmconfig.movement_button.value:
            self.setCursor(Qt.CursorShape.SizeAllCursor)
            self._mmb = True
            self.editor.mouse_middle_press()
        self.editor.mouse_press_event(event)

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        if self.scene().mouseGrabberItem() is not None:
            return
        if event.button() & self.manager.basemod.bmconfig.main_button.value:
            self._lmb = False
            self.editor.mouse_left_release()
        if event.button() & self.manager.basemod.bmconfig.sec_button.value:
            self._rmb = False
            self.editor.mouse_right_release()
        if event.button() & self.manager.basemod.bmconfig.movement_button.value:
            self.setCursor(Qt.CursorShape.ArrowCursor)
            self._mmb = False
            self.editor.mouse_middle_release()
        self.editor.mouse_release_event(event)

    @property
    def mouse_left(self) -> bool:
        return self._lmb

    @property
    def mouse_right(self) -> bool:
        return self._rmb

    @property
    def mouse_middle(self):
        return self._mmb

    @property
    def editor(self):
        return self.manager.editor

    def clean(self):
        self.workscene.update(0, 0, 10000, 10000)  # that'l do

    def levelchanged(self):
        # for i in self.editor.renderables:
        #     i.level_resized()
        for i in self.modules:
            i.level_resized()
        for i in self.manager.editors:
            i.level_resized()

    def wheelEvent(self, event):
        if self.scene().mouseGrabberItem() is not None:
            super().wheelEvent(event)
            return
        mods = QApplication.keyboardModifiers()
        #print(self.map.scale() + (event.angleDelta().y() / 80))
        if mods == mods.ShiftModifier:
            event.setModifiers(Qt.KeyboardModifier.NoModifier)
            self.verticalScrollBar().wheelEvent(event)
            return
        elif mods == mods.ControlModifier:
            event.setModifiers(Qt.KeyboardModifier.NoModifier)
            self.horizontalScrollBar().wheelEvent(event)
            return
        pointbefore = self.viewport_to_editor_float(self.mouse_pos.toPointF())
        self.zoom = max(0.01, self.zoom + (event.angleDelta().y() * (-1 if event.inverted() else 1) / 800) * self.zoom)
        offset = (self.viewport_to_editor_float(self.mouse_pos.toPointF()) - pointbefore) * CELLSIZE * self.zoom
        self.topleft.setPos(self.topleft.pos() + offset)
        for i in self.modules:
            i.zoom_event()
            i.move_event()
        self.editor.mouse_wheel_event(event)
        self.editor.mouse_move_event(event)
        self.editor.zoom_event()
        self.editor.move_event()
        #self.verticalScrollBar().size
        #self.horizontalScrollBar().adjustSize()

    def mouseMoveEvent(self, event):
        if self.scene().mouseGrabberItem() is not None:
            super().mouseMoveEvent(event)
            return
        offset = event.pos() - self.mouse_pos
        if self.mouse_middle:
            # self.origin.setX(self.origin.x() + offset.x())
            # self.origin.setY(self.origin.y() + offset.y())
            self.topleft.setPos(self.topleft.pos() + offset)
            for i in self.modules:
                i.move_event()
        self.mouse_pos = event.pos()
        self.editor.mouse_move_event(event)
        self.editor.move_event()
        #super().mouseMoveEvent(event)

    def viewport_to_editor(self, point: QPoint) -> QPoint:
        npoint = point.toPointF() + QPointF(self.horizontalScrollBar().value(), self.verticalScrollBar().value()) - self.topleft.pos()
        npoint.setX(npoint.x() / (CELLSIZE * self.zoom))
        npoint.setY(npoint.y() / (CELLSIZE * self.zoom))
        npoint -= QPointF(.5, .5)
        return npoint.toPoint()

    def viewport_to_editor_float(self, point: QPointF) -> QPointF:
        npoint = point + QPointF(self.horizontalScrollBar().value(), self.verticalScrollBar().value()) - self.topleft.pos()
        npoint.setX(npoint.x() / (CELLSIZE * self.zoom))
        npoint.setY(npoint.y() / (CELLSIZE * self.zoom))
        return npoint

    def editor_to_viewport(self, point: QPoint) -> QPoint:
        return (point * CELLSIZE * self.zoom) + self.topleft.pos().toPoint()

    def editor_to_viewport_float(self, point: QPointF) -> QPointF:
        return (point * CELLSIZE * self.zoom) + self.topleft.pos()

    def save_level(self):
        for i in self.manager.mods:
            i.on_save(self)
        if self.level.file is None:
            dialog = QFileDialog.getSaveFileName(self.manager.window, "Save a level...", PATH_LEVELS, "Level files (*.txt *.wep *.rwl)", selectedFilter=".wep")
            if dialog[0] == "":
                return
            self.level.file = dialog[0]
        self.level.save_file()

    def save_level_as(self):
        dialog = QFileDialog.getSaveFileName(self.manager.window, "Save a level...", PATH_LEVELS, "Level files (*.txt *.wep *.rwl)", selectedFilter=".wep")
        if dialog[0] == "":
            return
        self.level.file = dialog[0]
        self.level.save_file()
