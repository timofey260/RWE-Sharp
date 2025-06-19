import math
from PySide6.QtCore import QPointF, QRectF, QPoint
from BaseMod.LevelParts import GeoLevelPart
from RWESharp.Loaders import Prop

def Diag(point1: QPointF, point2: QPointF):
    RectHeight = abs(point1.y() - point2.y())
    RectWidth = abs(point1.x() - point2.x())
    diagonal = math.sqrt((RectHeight * RectHeight) + (RectWidth * RectWidth))
    return diagonal

def DiagWI(point1: QPointF, point2: QPointF, dig):
    RectHeight = abs(point1.y() - point2.y())
    RectWidth = abs(point1.x() - point2.x())
    return (RectHeight * RectHeight) + (RectWidth * RectWidth) < dig*dig


def MoveToPoint(pointA: QPointF, pointB: QPointF, theMovement):
    pointB = pointB - pointA
    diag = Diag(QPointF(0, 0), pointB)
    if diag > 0:
        dirVec = pointB * (1 / diag)
    else:
        dirVec = QPointF(0, 1)
    return dirVec * theMovement


def lerp(a, b, t):
    return (1 - t) * a + t * b


def restrict(a, minimum, maximum):
    return max(min(a, maximum), minimum)


class RopeModel:
    def __init__(self, data: GeoLevelPart, pA: QPointF, pB: QPointF, prop: Prop, lengthFac, lr, rel):
        self.data: GeoLevelPart = data
        self.prop = prop.copy()
        self.lengthFac = lengthFac
        self.release = rel
        self.layer = lr

        self.posA: QPointF = pA
        self.posB: QPointF = pB
        self.segmentLength: int = prop["segmentLength"]
        self.grav = prop["grav"]
        self.stiff = prop["stiff"]
        self.segments = []
        self.friction = prop["friction"]
        self.airFric = prop["airFric"]
        self.segRad = prop["segRad"]
        self.rigid = prop["rigid"]
        self.edgeDirection = prop["edgeDirection"]
        self.selfPush = prop["selfPush"]
        self.sourcePush = prop["sourcePush"]

        numberOfSegments = int(max((Diag(pA, pB) / self.segmentLength) * lengthFac, 3))
        step = Diag(pA, pB) / numberOfSegments
        for i in range(1, numberOfSegments):
            self.segments.append({"pos": pA + MoveToPoint(pA, pB, (i - 0.5) * step),
                                  "lastPos": pA + MoveToPoint(pA, pB, (i - 0.5) * step),
                                  "vel": QPointF(0, 0)
                                  })

    def modelRopeUpdate(self, collision=True):
        if self.edgeDirection > 0:
            dir = MoveToPoint(self.posA, self.posB, 1)
            if self.release > -1:
                for A in range(int(len(self.segments) / 2)):
                    fac = pow(1 - ((A - 1) / (len(self.segments) / 2)), 2)
                    self.segments[A]["vel"] += dir * fac * self.edgeDirection
                idealFirstPos = self.posA + dir * self.segmentLength
                self.segments[0]["pos"] = QPointF(
                    lerp(self.segments[0]["pos"].x(), idealFirstPos.x(), self.edgeDirection),
                    lerp(self.segments[0]["pos"].y(), idealFirstPos.y(), self.edgeDirection))
            if self.release < 1:
                for A1 in range(1, int(len(self.segments) / 2)):
                    fac = pow(1 - ((A1 - 1) / (len(self.segments) / 2)), 2)
                    A = len(self.segments) - A1
                    self.segments[A]["vel"] -= dir * fac * self.edgeDirection
                idealFirstPos = self.posB - dir * self.segmentLength
                self.segments[-1]["pos"] = QPointF(
                    lerp(self.segments[-1]["pos"].x(), idealFirstPos.x(), self.edgeDirection),
                    lerp(self.segments[-1]["pos"].y(), idealFirstPos.y(), self.edgeDirection))
        if self.release > -1:
            self.segments[0]["pos"] = self.posA.__copy__()
            self.segments[0]["vel"] = QPointF(0, 0)
        if self.release < 1:
            self.segments[-1]["pos"] = self.posB.__copy__()
            self.segments[-1]["vel"] = QPointF(0, 0)
        for i in range(len(self.segments)):
            self.segments[i]["lastPos"] = self.segments[i]["pos"]
            self.segments[i]["pos"] += self.segments[i]["vel"]
            self.segments[i]["vel"] *= self.airFric
            self.segments[i]["vel"] += QPointF(0, self.grav)

        for i in range(1, len(self.segments)):
            self.ConnectRopePoints(i, i-1)
            if self.rigid > 0:
                self.ApplyRigidity(i)
        for i in range(len(self.segments), 0):
            self.ConnectRopePoints(i, i+1)
            if self.rigid > 0:
                self.ApplyRigidity(i)

        if self.selfPush > 0:
            for A in range(len(self.segments)):
                for B in range(len(self.segments)):
                    if A != B and DiagWI(self.segments[A]["pos"], self.segments[B]["pos"], self.selfPush):
                        dir = MoveToPoint(self.segments[A]["pos"], self.segments[B]["pos"], 1)
                        dist = Diag(self.segments[A]["pos"], self.segments[B]["pos"])
                        mov = dir * (dist-self.selfPush)

                        self.segments[A]['pos'] += mov * 0.5
                        self.segments[A]['vel'] += mov * 0.5
                        self.segments[B]['pos'] -= mov * 0.5
                        self.segments[B]['vel'] -= mov * 0.5
        if self.sourcePush > 0:
            for A in range(len(self.segments)):
                self.segments[A]["vel"] += MoveToPoint(self.posA, self.segments[A]["pos"], self.sourcePush) * restrict(((A - 1) / (len(self.segments) - 1)) - 0.7, 0, 1)
                self.segments[A]["vel"] += MoveToPoint(self.posB, self.segments[A]["pos"], self.sourcePush) * restrict((1 - ((A - 1) / (len(self.segments) - 1))) - 0.7, 0, 1)
        if collision:
            for i in range(int(self.release > -1), len(self.segments) - int(self.release < 1)):
                self.PushRopePointOutOfTerrain(i)


    def ApplyRigidity(self, A):
        for B2 in [-2, 2, -3, 3, -4, 4]:
            B = A + B2
            if 0 < B < len(self.segments):
                dir = MoveToPoint(self.segments[A]["pos"], self.segments[B]["pos"], 1)
                self.segments[A]["vel"] -= (dir * self.rigid * self.segmentLength) / (Diag(self.segments[A]["pos"], self.segments[B]["pos"]) + 0.1 + abs(B2))
                self.segments[B]["vel"] += (dir * self.rigid * self.segmentLength) / (Diag(self.segments[A]["pos"], self.segments[B]["pos"]) + 0.1 + abs(B2))

    def ConnectRopePoints(self, A, B):
        dir = MoveToPoint(self.segments[A]["pos"], self.segments[B]["pos"], 1)
        dist = Diag(self.segments[A]["pos"], self.segments[B]["pos"])
        if self.stiff == 1 or dist > self.segmentLength:
            mov = dir * (dist - self.segmentLength)

            self.segments[A]['pos'] += mov * 0.5
            self.segments[A]['vel'] += mov * 0.5
            self.segments[B]['pos'] -= mov * 0.5
            self.segments[B]['vel'] -= mov * 0.5

    def PushRopePointOutOfTerrain(self, A):
        p = {
            "Loc": self.segments[A]["pos"].__copy__(),
            "LastLoc": self.segments[A]["lastPos"].__copy__(),
            "Frc": self.segments[A]["vel"].__copy__(),
            "SizePnt": QPointF(self.segRad, self.segRad).__copy__()
        }
        p = self.sharedCheckVCollision(p, self.friction, self.layer)

        self.segments[A]["pos"] = p["Loc"].__copy__()
        self.segments[A]["vel"] = p["Frc"].__copy__()

        gridPos = self.giveGridPos(self.segments[A]["pos"])
        for dir in [QPointF(0, 0), QPointF(-1, 0), QPointF(-1, -1), QPointF(0, -1), QPointF(1, -1),
                    QPointF(1, 0), QPointF(1, 1), QPointF(0, 1), QPointF(-1, 1)]:
            if self.afaMvLvlEdit(gridPos + dir, self.layer) == 1:
                midPos = self.giveMiddleOfTile(gridPos + dir)
                terrainPos = QPointF(restrict(self.segments[A]["pos"].x(), midPos.x() - 10, midPos.x() + 10),
                                     restrict(self.segments[A]["pos"].y(), midPos.y() - 10, midPos.y() + 10))
                terrainPos = ((terrainPos * 10) + midPos) * (1 / 11)

                dir = MoveToPoint(self.segments[A]["pos"], terrainPos, 1)
                dist = Diag(self.segments[A]["pos"], terrainPos) - 1
                if dist < self.segRad:
                    mov = dir * (dist - self.segRad)
                    self.segments[A]["pos"] += mov
                    self.segments[A]["vel"] = QPointF(0, 0) # not a total fix

    def giveMiddleOfTile(self, pos):
        return QPointF((pos.x() * 20) - 10, (pos.y() * 20) - 10)

    def sharedCheckVCollision(self, p, friction, layer):
        bounce = 0

        if p["Frc"].y() > 0:
            lastGridPos = self.giveGridPos(p["LastLoc"])
            feetPos = self.giveGridPos(p["Loc"] + QPointF(0, p["SizePnt"].y() + 0.01))
            lastFeetPos = self.giveGridPos(p["LastLoc"] + QPointF(0, p["SizePnt"].y()))
            leftPos = self.giveGridPos(p["Loc"] + QPointF(-p["SizePnt"].x() + 1, p["SizePnt"].y() + 0.01))
            rightPos = self.giveGridPos(p["Loc"] + QPointF(p["SizePnt"].x() - 1, p["SizePnt"].y() + 0.01))
            for q in range(int(lastFeetPos.y()), int(feetPos.y()) + 1):
                for c in range(int(leftPos.x()), int(rightPos.x()) + 1):
                    if self.afaMvLvlEdit(QPointF(c, q), layer) == 1 and self.afaMvLvlEdit(QPointF(c, q-1), layer) != 1:
                        if lastGridPos.y() >= q and self.afaMvLvlEdit(lastGridPos, layer) == 1:
                            pass
                        else:
                            p["Loc"].setY(((q-1) * 20) - p["SizePnt"].y())
                            p["Frc"].setX(friction * p["Frc"].x())
                            p["Frc"].setY(-p["Frc"].y() * bounce)
                            return p
        elif p["Frc"].y() < 0:
            lastGridPos = self.giveGridPos(p["LastLoc"])
            headPos = self.giveGridPos(p["Loc"] - QPointF(0, p["SizePnt"].y() + 0.01))
            lastHeadPos = self.giveGridPos(p["LastLoc"] - QPointF(0, p["SizePnt"].y()))
            leftPos = self.giveGridPos(p["Loc"] + QPointF(-p["SizePnt"].x() + 1, p["SizePnt"].y() + 0.01))
            rightPos = self.giveGridPos(p["Loc"] + QPointF(p["SizePnt"].x() - 1, p["SizePnt"].y() + 0.01))
            for d in range(int(lastHeadPos.y()), int(headPos.y()) + 1):
                q = (lastHeadPos.y()) - (d - headPos.y())
                for c in range(int(leftPos.x()), int(rightPos.x()) + 1):
                    if self.afaMvLvlEdit(QPointF(c, q), layer) == 1 and self.afaMvLvlEdit(QPointF(c, q+1), layer) != 1:
                        if lastGridPos.y() <= q and self.afaMvLvlEdit(lastGridPos, layer) != 1:
                            pass
                        else:
                            p["Loc"].setY((q * 20) + p["SizePnt"].y())
                            p["Frc"].setX(friction * p["Frc"].x())
                            p["Frc"].setY(-p["Frc"].y() * bounce)
                            return p
        return p

    def giveGridPos(self, pos: QPointF):
        return QPointF(int((pos.x() / 20) + 0.4999), int((pos.y() / 20) + 0.4999))

    def afaMvLvlEdit(self, pos: QPointF, layer):
        # if __name__ == "__main__":
        #     if pos.y > 11:
        #         return 1
        #     return 0
        if QRectF(0, 0, self.levelwidth - 1, self.levelheight - 1).contains(pos.toPoint() - QPoint(1, 1)):
            return self.data.getlevelgeo(int(pos.x() - 1), int(pos.y() - 1), layer)[0]
        return 1

    @property
    def levelwidth(self):
        return self.data.width

    @property
    def levelheight(self):
        return self.data.height


# if __name__ == "__main__": # shit no longer works rn
#     import lingotojson
#     import pygame as pg
#
#     data = lingotojson.turntoproject(open(Path("LevelEditorProjects") / "HI_C15.txt", "r").read())
#     #rope = RopeModel(data, QPointF(60, 200), QPointF(60 + 9 * 16, 200),
#     #                 {"nm": "Wire", "tp": "rope", "depth": 4, "tags": [], "notes": [], "segmentLength": 10,
#     #                  "collisionDepth": 2, "segRad": 4.5, "grav": 0.5, "friction": 0.5, "airFric": 0.9, "stiff": 1,
#     #                  "previewColor": [255, 0, 0], "previewEvery": 4, "edgeDirection": 5, "rigid": 1.6, "selfPush": 0,
#     #                  "sourcePush": 0}, 1, 1, 0)
#     rope = RopeModel(data, QPointF(60, 200), QPointF(60 + 9 * 16, 200),
#                      {"nm": "Wire", "tp": "rope", "depth": 0, "tags": [], "notes": [], "segmentLength": 3,
#                       "collisionDepth": 0, "segRad": 1, "grav": 0.5, "friction": 0.5, "airFric": 0.9, "stiff": 0,
#                       "previewColor": [255, 0, 0], "previewEvery": 4, "edgeDirection": 0, "rigid": 0, "selfPush": 0,
#                       "sourcePush": 0}, 1, 1, 0)
#     timer = pg.time.Clock()
#     run = True
#     width = 1280
#     height = 720
#     window = pg.display.set_mode([width, height], flags=pg.RESIZABLE)
#     while run:
#         window.fill([0, 0, 0])
#         for event in pg.event.get():
#             match event.type:
#                 case pg.QUIT:
#                     exit(0)
#         if any(pg.key.get_pressed()):
#             rope.modelRopeUpdate()
#         for segment in rope.segments:
#             pg.draw.circle(window, [255, 0, 0], segment["pos"], 3)
#         pg.draw.line(window, [0, 255, 0], rope.posA, rope.posB)
#         pg.draw.line(window, [0, 0, 255], [0, 11*20], [width, 11*20])
#         pg.display.flip()
#         pg.display.update()
#         timer.tick(20)
#     pg.quit()
#     exit(0)
