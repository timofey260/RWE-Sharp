# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PenPicker.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDoubleSpinBox,
    QGridLayout, QHBoxLayout, QLayout, QSizePolicy,
    QWidget)

from RWESharp.Core.RWESharpWidgets import ColorPicker

class Ui_Penpicker(object):
    def setupUi(self, Penpicker):
        if not Penpicker.objectName():
            Penpicker.setObjectName(u"Penpicker")
        Penpicker.resize(548, 186)
        self.gridLayout = QGridLayout(Penpicker)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.Style = QComboBox(Penpicker)
        self.Style.addItem("")
        self.Style.addItem("")
        self.Style.addItem("")
        self.Style.addItem("")
        self.Style.addItem("")
        self.Style.addItem("")
        self.Style.setObjectName(u"Style")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Style.sizePolicy().hasHeightForWidth())
        self.Style.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.Style)

        self.Width = QDoubleSpinBox(Penpicker)
        self.Width.setObjectName(u"Width")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Width.sizePolicy().hasHeightForWidth())
        self.Width.setSizePolicy(sizePolicy1)
        self.Width.setWrapping(False)
        self.Width.setFrame(True)
        self.Width.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.Width.setAccelerated(False)
        self.Width.setProperty(u"showGroupSeparator", False)
        self.Width.setDecimals(1)
        self.Width.setMinimum(1.000000000000000)
        self.Width.setSingleStep(0.500000000000000)

        self.horizontalLayout.addWidget(self.Width)

        self.Color = ColorPicker(Penpicker)
        self.Color.setObjectName(u"Color")

        self.horizontalLayout.addWidget(self.Color)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.retranslateUi(Penpicker)

        QMetaObject.connectSlotsByName(Penpicker)
    # setupUi

    def retranslateUi(self, Penpicker):
        Penpicker.setWindowTitle(QCoreApplication.translate("Penpicker", u"Form", None))
        self.Style.setItemText(0, QCoreApplication.translate("Penpicker", u"Solid Line _____", None))
        self.Style.setItemText(1, QCoreApplication.translate("Penpicker", u"No Pen", None))
        self.Style.setItemText(2, QCoreApplication.translate("Penpicker", u"Dash Line -----", None))
        self.Style.setItemText(3, QCoreApplication.translate("Penpicker", u"Dot Line ......", None))
        self.Style.setItemText(4, QCoreApplication.translate("Penpicker", u"Dash Dot Line ._._._", None))
        self.Style.setItemText(5, QCoreApplication.translate("Penpicker", u"Dash Dot Dot Line .._.._", None))

        self.Width.setPrefix("")
        self.Width.setSuffix(QCoreApplication.translate("Penpicker", u" px", None))
        self.Color.setText("")
    # retranslateUi

