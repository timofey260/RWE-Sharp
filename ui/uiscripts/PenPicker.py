# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PenPicker.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QSizePolicy, QWidget)

from RWESharpWidgets import ColorPicker

class Ui_Penpicker(object):
    def setupUi(self, Penpicker):
        if not Penpicker.objectName():
            Penpicker.setObjectName(u"Penpicker")
        Penpicker.resize(400, 28)
        self.gridLayout = QGridLayout(Penpicker)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Style = QComboBox(Penpicker)
        self.Style.addItem("")
        self.Style.addItem("")
        self.Style.addItem("")
        self.Style.addItem("")
        self.Style.addItem("")
        self.Style.addItem("")
        self.Style.setObjectName(u"Style")

        self.horizontalLayout.addWidget(self.Style)

        self.toolButton = ColorPicker(Penpicker)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout.addWidget(self.toolButton)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.retranslateUi(Penpicker)

        QMetaObject.connectSlotsByName(Penpicker)
    # setupUi

    def retranslateUi(self, Penpicker):
        Penpicker.setWindowTitle(QCoreApplication.translate("Penpicker", u"Form", None))
        self.Style.setItemText(0, QCoreApplication.translate("Penpicker", u"Solid Line _____", None))
        self.Style.setItemText(1, QCoreApplication.translate("Penpicker", u"No Pen", None))
        self.Style.setItemText(2, QCoreApplication.translate("Penpicker", u"Dash Dot Line ._._._", None))
        self.Style.setItemText(3, QCoreApplication.translate("Penpicker", u"Dash Dot Dot Line .._.._", None))
        self.Style.setItemText(4, QCoreApplication.translate("Penpicker", u"Dot Line ......", None))
        self.Style.setItemText(5, QCoreApplication.translate("Penpicker", u"Dash Line -----", None))

        self.toolButton.setText("")
    # retranslateUi

