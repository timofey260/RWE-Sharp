from __future__ import annotations
from PySide6.QtGui import QMoveEvent, QMouseEvent, QWheelEvent, QGuiApplication
from PySide6.QtCore import QPoint, Qt
from PySide6.QtWidgets import QGraphicsScene
from typing import TYPE_CHECKING
from abc import ABC
from core.Modify.baseModule import Module
if TYPE_CHECKING:
    from core.Renderable.Renderable import Renderable


class Editor(Module, ABC):
    """
    Base for creating custom viewport editors
    """
    def __init__(self, mod):
        super().__init__(mod)

    def mouse_move_event(self, event: QMoveEvent):
        pass

    def mouse_press_event(self, event: QMouseEvent):
        pass

    def mouse_release_event(self, event: QMouseEvent):
        pass

    def mouse_wheel_event(self, event: QWheelEvent):
        pass

    @property
    def workscene(self) -> QGraphicsScene:
        return self.viewport.workscene

    @property
    def mouse_left(self) -> bool:
        return self.viewport.mouse_left

    @property
    def mouse_right(self) -> bool:
        return self.viewport.mouse_right

    @property
    def mouse_pos(self) -> QPoint:
        """
        last mouse location on viewport coordinates
        :return:
        """
        return self.viewport.mouse_pos

    @property
    def shift(self):
        return bool(QGuiApplication.keyboardModifiers() & Qt.KeyboardModifier.ShiftModifier)

    @property
    def control(self):
        return bool(QGuiApplication.keyboardModifiers() & Qt.KeyboardModifier.ControlModifier)

    @property
    def alt(self):
        return bool(QGuiApplication.keyboardModifiers() & Qt.KeyboardModifier.AltModifier)

    @property
    def level(self):
        return self.viewport.level

    def add_myself(self, ui, viewport=None, name=None):
        self.mod.add_editor(self, ui)
        ui.begin_recording()
        return self

    def mouse_left_release(self):
        pass

    def mouse_right_release(self):
        pass

    def mouse_middle_release(self):
        pass

    def mouse_left_press(self):
        pass

    def mouse_right_press(self):
        pass

    def mouse_middle_press(self):
        pass

    @property
    def modifiers(self):
        return QGuiApplication.keyboardModifiers()
