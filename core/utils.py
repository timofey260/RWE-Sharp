import datetime
import os
from PySide6.QtGui import QColor, QIcon
from core.info import PATH, PATH_FILES_CACHE
from PySide6.QtCore import QPoint, QFile, QByteArray
from collections.abc import Callable


def log_to_load_log(message, error=False):
    with open(os.path.join(PATH, "loadLog.txt"), "a") as file:
        msg = f"[{datetime.datetime.now().strftime('%H:%M')}; {'ERROR' if error else ' INFO'}]: {message}\n"
        file.write(msg)
        print(msg, end="")


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


def draw_line(pointa: QPoint, pointb: QPoint, callback: Callable):
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
