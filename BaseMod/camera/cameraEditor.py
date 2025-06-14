from RWESharp.Modify import Editor
from RWESharp.Renderable import Handle, RenderList, RenderRect
from RWESharp.Core import camw, camh, CELLSIZE
from BaseMod.camera.cameraRenderable import RenderCamera
from BaseMod.camera.cameraHistory import AddCamera, RemoveCamera, CameraMove, CameraQuadMove, MoveCameraOrder
from BaseMod.LevelParts import CameraLevelPart
from PySide6.QtCore import QPointF, QRect, Qt, QPoint
from PySide6.QtGui import QPen, QColor
import random


"""class CameraHandles(RenderList):
    def __init__(self, module, depth, rendercamera: RenderCamera):
        super().__init__(module, depth)
        self.camera = rendercamera.camera
        self.rendercamera = rendercamera

        self.poshandle = Handle(module)
        self.renderables.append(self.poshandle)
        self.poshandle.setPos(self.camera.pos)
        self.poshandle.handle_offset = QPointF(camw / 2 * CELLSIZE, camh / 2 * CELLSIZE)
        self.poshandle.posChangedRelative.connect(self.movepos)
        self.poshandle.mouseReleased.connect(self.changepos)  # todo add history, make selection grouping

    def changepos(self, x):
        # when we finish moving
        index = self.viewport.level.l_cameras.index(self.camera)
        if self not in self.module.selected:
            self.module.cameraui.select_camera(index)
            return
        self.module.level.add_history(CameraMove(self.module.level.history, self.module, self.rendercamera.module,
                                                 self.module.selected, x - self.poshandle.handle.reserved_pos))
        self.camera.pos = x

    def movepos(self, x):
        # when we move
        self.rendercamera.setPos(x + self.poshandle.offset)
        for i in self.module.selected:
            if i == self:
                continue
            i: CameraHandles
            i.rendercamera.setPos(x + i.poshandle.offset)
            i.poshandle.handle.movehandle(x)
"""

"""
class CameraGroup(QGraphicsItemGroup):
    def __init__(self, module, handles: list[CameraHandles], parent=None):
        super().__init__(parent)
        self.handles = handles
        self.module = module
        for i in self.handles:
            self.addToGroup(i.poshandle.handle)
        self.setAcceptTouchEvents(True)
        self.setAcceptHoverEvents(True)
        self.setAcceptedMouseButtons(Qt.MouseButton.LeftButton)
            
    def mouseMoveEvent(self, event):
        for i in self.handles:
            i.poshandle.setPos(i.poshandle.offset + event.pos())

    def mousePressEvent(self, event):
        event.accept()
        for i in self.handles:
            i.poshandle.handle.mousePressEvent(event)
"""


class CameraEditor(Editor):
    def __init__(self, mod):
        super().__init__(mod)
        self.cameraui = None
        self.selectrect = RenderRect(self, 0, QRect(), pen=QPen(QColor(255, 255, 255), 3, Qt.PenStyle.DashLine))
        self.selectrect.drawrect.setOpacity(0)
        self.selectpos = QPoint()
        self.selected: list[RenderCamera] = []

    def init_scene_items(self, viewport):
        self.reset_selection()
        self.add_handles()
        super().init_scene_items(viewport)
        # module = self.viewport.modulenames["cameras"]
        # for i in range(40000):
        #     print(i)
        #     module.add_new_camera(0, QPointF(random.randrange(0, 4000), random.randrange(0, 4000)))
        #     #self.add_camera()
        # self.add_handles()

    def remove_items_from_scene(self, viewport):
        self.reset_selection()
        self.clear_handles()
        super().remove_items_from_scene(viewport)

    def clear_handles(self):
        # for i in self.handles:
        #     i.remove_graphics(self.viewport)
        #     i.remove_myself()
        # self.handles.clear()
        if self.viewport is None:
            return
        for i in self.cameras:
            i.edit_camera(False)

    def move_up(self, selection):
        self.level.add_history(MoveCameraOrder, self, self.viewport.modulenames["cameras"], True, selection)

    def move_down(self, selection):
        self.level.add_history(MoveCameraOrder, self, self.viewport.modulenames["cameras"], False, selection)

    def move_event(self):
        super().move_event()
        if self.control and self.selectpos != QPoint(0, 0):
            self.selectrect.setRect(QRect.span(self.selectpos, self.editor_pos))
            self.selectrect.drawrect.setOpacity(1)
            self.reset_selection()
            for i in self.cameras:
                if self.selectrect.rect.contains(i.camera.pos.toPoint() + QPoint(camw / 2 * CELLSIZE, camh / 2 * CELLSIZE)):
                    self.selected.append(i)
                    i.paintselected()
            for i in self.selected:
                indx = self.cameras.index(i)
                self.cameraui.select_camera(indx, False)

    def mouse_left_release(self):
        self.selectpos = QPoint()
        self.selectrect.drawrect.setOpacity(0)

    def mouse_left_press(self):
        if self.control:
            self.selectpos = self.editor_pos
            self.reset_selection()

    def reset_selection(self, reset_ui=True):
        self.selected = []
        if self.viewport is None:
            return
        for i in self.cameras:
            i.paintselected(False)
        if reset_ui:
            self.cameraui.reset_selection()

    def select_indexes(self, selection):
        for i, v in enumerate(self.cameras):
            if i in selection:
                self.selected.append(v)
                v.paintselected()

    def add_camera(self):
        module = self.viewport.modulenames["cameras"]
        self.level.add_history(AddCamera, self, module, len(module.cameras),
                                         self.editor_pos.toPointF() - QPointF(camw / 2 * CELLSIZE, camh / 2 * CELLSIZE))
        self.add_handles()

    def remove_cameras(self, cameras: list[int]):
        module = self.viewport.modulenames["cameras"]
        self.level.add_history(RemoveCamera, self, module, cameras)
        self.add_handles()
        # group = CameraGroup(self, self.handles)
        # self.viewport.scene().addItem(group)

    def add_handles(self):
        # for i, v in enumerate(self.level.l_cameras):
        #     self.handles.append(CameraHandles(self, 0, self.viewport.modulenames["cameras"].cameras[i]))
        # if init:
        #     for i in self.handles:
        #         i.init_graphics(self.viewport)
        if self.viewport is None:  # for the undo/redo stuff
            return
        for i in self.cameras:
            i.edit_camera()
            i.poshandle.posChangedRelative.connect(self.move_selected(i))
            i.poshandle.mouseReleased.connect(self.finishmove(i))
            for k in range(4):
                i.quadhandles[k].posChangedRelative.connect(self.quad_moved(i, k))
                i.quadhandles[k].mouseReleased.connect(self.finishmovequad(i, k))
        self.cameraui.add_cameras()

    def quad_moved(self, camera, quad):
        if camera not in self.selected:
            self.reset_selection()
            self.selected = [camera]
            camera.paintselected()

        def move(x):
            if camera not in self.selected:
                self.reset_selection()
                self.selected = [camera]
                camera.paintselected()
                self.cameraui.select_camera(self.cameras.index(camera), False)
            for i in self.selected:
                if i == camera:
                    continue
                i.quadhandles[quad].handle.movehandle(x, True)
        return move

    def finishmovequad(self, camera, quad):
        module = self.viewport.modulenames["cameras"]

        def move(x):
            self.level.add_history(CameraQuadMove, self, module, quad, self.cameraindexes)
        return move

    def move_selected(self, camera: RenderCamera):
        if camera not in self.selected:
            self.reset_selection()
            self.selected = [camera]
            camera.paintselected()

        def move(x):
            if camera not in self.selected:
                self.reset_selection()
                self.selected = [camera]
                camera.paintselected()
                self.cameraui.select_camera(self.cameras.index(camera), False)
            for i in self.selected:
                if i == camera:
                    continue
                i.poshandle.handle.movehandle(x, True)
        return move

    def finishmove(self, camera):
        module = self.viewport.modulenames["cameras"]

        def move(x):
            self.level.add_history(CameraMove, self, module, self.cameraindexes, x - camera.poshandle.previous_pos)
        return move

    @property
    def cameras(self) -> list[RenderCamera]:
        return self.viewport.modulenames["cameras"].cameras

    @property
    def cameraindexes(self) -> list[int]:
        return [self.viewport.modulenames["cameras"].cameras.index(i) for i in self.selected]
