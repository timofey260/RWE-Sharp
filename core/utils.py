import datetime
import os
import math
from core.info import PATH_FILES_CACHE, LOG
from PySide6.QtGui import QColor, QIcon, QPixmap
from PySide6.QtCore import QPoint, QPointF, QFile, QByteArray, QRect, QLineF, QRectF
from collections.abc import Callable


def log(message, error=False) -> None:
    """
    Logs a message in both terminal and log file
    :param message: message to log
    :param error: Whether it's error or not
    :return: None
    """
    s = f"[{datetime.datetime.now().strftime('%H:%M')}; {'ERROR' if error else ' INFO'}]: {message}\n"
    print(s, end="", file=LOG, flush=True)
    print(s, end="")


def draw_line(pointa: QPoint, pointb: QPoint, callback: Callable) -> None:
    """
    Calls callback function for each point line intersected with
    :param pointa: Line point a
    :param pointb: Line point b
    :param callback: Callback function(lambda QPoint:)
    :return: None
    """
    def plotLineLow(pointa: QPoint, pointb: QPoint, callback: Callable):
        if pointa.x() > pointb.x():
            pointa, pointb = pointb, pointa
        d = pointb - pointa
        yi = 1
        if d.y() < 0:
            yi = -1
            d.setY(-d.y())
        D = (2 * d.y()) - d.x()
        y = pointa.y()

        for x in range(pointa.x(), pointb.x()):
            callback(QPoint(x, y))
            if D > 0:
                y = y + yi
                D = D + (2 * (d.y() - d.x()))
            else:
                D = D + 2 * d.y()

    def plotLineHigh(pointa: QPoint, pointb: QPoint, callback: Callable):
        if pointa.y() > pointb.y():
            pointa, pointb = pointb, pointa
        d = pointb - pointa
        xi = 1
        if d.x() < 0:
            xi = -1
            d.setX(-d.x())
        D = (2 * d.x()) - d.y()
        x = pointa.x()

        for y in range(pointa.y(), pointb.y()):
            callback(QPoint(x, y))
            if D > 0:
                x = x + xi
                D = D + (2 * (d.x() - d.y()))
            else:
                D = D + 2 * d.x()
    # callback(pointa)
    if abs(pointb.y() - pointa.y()) < abs(pointb.x() - pointa.x()):
        plotLineLow(pointa, pointb, callback)
    else:
        plotLineHigh(pointa, pointb, callback)
    callback(pointb)


def insensitive_path(path) -> str | None:
    """
    returns path to case-insensitive file(not path to it)
    :param path: path to file
    :return: str
    """
    if os.path.exists(path):
        return path
    dir, name = os.path.split(path)
    for dir, d2, a in os.walk(dir):
        for i in a:
            if os.path.join(dir, i).lower() == path.lower():
                return os.path.join(dir, i)
        break
    return None


def draw_ellipse(rect: QRect, hollow: bool, callback: Callable) -> None:
    """
    Calls callback for each point ellipse intersects with

    NOTE: Callback may be called multiple times on same point
    :param rect:
    :param hollow: call callback only on edges or whole ellipse
    :param callback: callback function(lambda QPoint:)
    :return: None
    """
    width = rect.width() // 2
    height = rect.height() // 2
    origin = rect.center()
    hh = height * height
    ww = width * width
    hhww = hh * ww
    x0 = width
    dx = 0
    for x in range(-width, width + 1):
        if x == -width or x == width or not hollow:
            callback(QPoint(origin.x() + x, origin.y()))
    for y in range(1, height + 1):
        x1 = x0 - (dx - 1)
        while x1 > 0:
            if x1*x1*hh + y*y*ww <= hhww:
                break
            x1 -= 1
        dx = x0 - x1
        x0 = x1
        if hollow:
            callback(QPoint(origin.x() - x0, origin.y() - y))
            callback(QPoint(origin.x() - x0, origin.y() + y))
            callback(QPoint(origin.x() + x0, origin.y() - y))
            callback(QPoint(origin.x() + x0, origin.y() + y))
        else:
            for x in range(-x0, x0 + 1):
                callback(QPoint(origin.x() + x, origin.y() - y))
                callback(QPoint(origin.x() + x, origin.y() + y))

    if not hollow:
        return

    y0 = height
    dy = 0
    callback(QPoint(origin.x(), origin.y() - height))
    callback(QPoint(origin.x(), origin.y() + height))
    for x in range(1, width + 1):
        y1 = y0 - (dy - 1)
        while y1 > 0:
            if y1*y1*ww + x*x*hh <= hhww:
                break
            y1 -= 1
        dy = y0 - y1
        y0 = y1
        callback(QPoint(origin.x() - x, origin.y() - y0))
        callback(QPoint(origin.x() - x, origin.y() + y0))
        callback(QPoint(origin.x() + x, origin.y() - y0))
        callback(QPoint(origin.x() + x, origin.y() + y0))


def paint_svg(filename: str, color: QColor) -> str:
    """
    Paints svg image with caching and returns path to edited svg in cache

    works with resources too

    if file is already stored in cache, passes it instead
    """

    path, file = os.path.split(filename)
    file, ex = os.path.splitext(file)
    newpath = os.path.join(PATH_FILES_CACHE, f"{file}_{color.red()}_{color.green()}_{color.blue()}{ex}")
    if os.path.exists(newpath):
        return newpath
    file = QFile(filename)
    file.open(QFile.OpenModeFlag.ReadOnly)
    data: QByteArray = file.readAll()
    file.close()
    htindex = data.indexOf(b'"', data.indexOf(b"fill=\"#")) + 1
    data = data.replace(htindex, data.indexOf(b'"', htindex) - htindex, bytearray(color.name(), "utf-8"))
    file = QFile(newpath)
    file.open(QFile.OpenModeFlag.WriteOnly)
    file.write(data)
    file.close()
    return newpath


def paint_svg_qicon(filename: str, color: QColor) -> QIcon:
    return QIcon(paint_svg(filename, color))


def paint_svg_qpixmap(filename: str, color: QColor) -> QPixmap:
    return QPixmap(paint_svg(filename, color))


def remap(x: float, in_min: float, in_max: float, out_min: float, out_max: float) -> float:
    """
    converts value from one range to another
    :param x: value in **in** range
    :param in_min: **in** in start
    :param in_max:  **in** end
    :param out_min: **out** start
    :param out_max:  **out** end
    :return: value in **out** range
    """
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def lerp(a: float, b: float, t: float) -> float:  # laundmo
    """
    linear interpolation or something
    :param a: start
    :param b: end
    :param t: t
    :return: value interpolated between a and b
    """
    return (1 - t) * a + t * b


def color_lerp(c1: QColor, c2: QColor, t: float) -> QColor:
    return QColor.fromRgbF(lerp(c1.redF(), c2.redF(), t),
                           lerp(c1.greenF(), c2.greenF(), t),
                           lerp(c1.blueF(), c2.blueF(), t),
                           lerp(c1.alphaF(), c2.alphaF(), t))


def closest_line(pos, lastpos) -> QLineF:
    """
    Returns the line closest to one in 8 directions

    :param pos: start of line
    :param lastpos: end of line
    :return: closest line to given argument
    """
    magnitude = QLineF(lastpos, pos).length()
    points = [QLineF.fromPolar(magnitude, 0).p2().toPoint(),
              QLineF.fromPolar(magnitude, 45).p2().toPoint(),
              QLineF.fromPolar(magnitude, 90).p2().toPoint(),
              QLineF.fromPolar(magnitude, 135).p2().toPoint(),
              QLineF.fromPolar(magnitude, 180).p2().toPoint(),
              QLineF.fromPolar(magnitude, 225).p2().toPoint(),
              QLineF.fromPolar(magnitude, 270).p2().toPoint(),
              QLineF.fromPolar(magnitude, 315).p2().toPoint()]
    smallest = points[0]
    smallestdis = 9999
    for i in points:
        if QLineF(i, pos - lastpos).length() < smallestdis:
            smallest = i
            smallestdis = QLineF(i, pos - lastpos).length()
    return QLineF(lastpos, lastpos + smallest)


def rotate_point(point: QPointF, angle):
    """
    Rotates point with some angle
    :param point: point to rotate
    :param angle: angle to rotate
    :return: rotated point
    """
    px, py = point.x(), point.y()
    angle = math.radians(angle)
    qx = math.cos(angle) * px - math.sin(angle) * py
    qy = math.sin(angle) * px + math.cos(angle) * py
    return QPointF(qx, qy)


def circle2rect(pos: QPointF, radius: float) -> QRectF:
    return QRectF(pos.x() - radius, pos.y() - radius, radius * 2, radius * 2)


def point2polar(pos: QPointF) -> QPointF:
    """
    :param pos: position in cartesian coordinates
    :return: point in polar coordinates where x is angle and y is distance
    """
    return QPointF(math.degrees(math.atan2(pos.y(), pos.x())), math.dist([0, 0], pos.toTuple()))


def polar2point(pos: QPointF) -> QPointF:
    """
    :param pos: position in polar coordinates where x is angle and y is distance
    :return: point in cartesian coordinates
    """
    nq = math.radians((pos.x() + 90) % 360)
    return QPointF(math.sin(nq) * pos.y(), -math.cos(nq) * pos.y())


def modify_path_url(path: str) -> str:
    """
    converts specified path to file url
    :param path: path to convert
    :return: converted path
    """
    return "file:///" + path.replace("\\", "/").replace("#", "%23")
