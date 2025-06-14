# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cameras.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

from RWESharpWidgets import (ColorPicker, PenPicker)

class Ui_Cameras(object):
    def setupUi(self, Cameras):
        if not Cameras.objectName():
            Cameras.setObjectName(u"Cameras")
        Cameras.resize(616, 482)
        self.gridLayout = QGridLayout(Cameras)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(Cameras)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 614, 480))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.rect1 = PenPicker(self.scrollAreaWidgetContents)
        self.rect1.setObjectName(u"rect1")

        self.verticalLayout.addWidget(self.rect1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.rect2 = PenPicker(self.scrollAreaWidgetContents)
        self.rect2.setObjectName(u"rect2")

        self.verticalLayout.addWidget(self.rect2)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.rect3 = PenPicker(self.scrollAreaWidgetContents)
        self.rect3.setObjectName(u"rect3")

        self.verticalLayout.addWidget(self.rect3)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.circle = PenPicker(self.scrollAreaWidgetContents)
        self.circle.setObjectName(u"circle")

        self.verticalLayout.addWidget(self.circle)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.center = PenPicker(self.scrollAreaWidgetContents)
        self.center.setObjectName(u"center")

        self.verticalLayout.addWidget(self.center)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.poly = PenPicker(self.scrollAreaWidgetContents)
        self.poly.setObjectName(u"poly")

        self.verticalLayout.addWidget(self.poly)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.Index = ColorPicker(self.scrollAreaWidgetContents)
        self.Index.setObjectName(u"Index")
        self.Index.setEnabled(True)

        self.verticalLayout.addWidget(self.Index)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.retranslateUi(Cameras)

        QMetaObject.connectSlotsByName(Cameras)
    # setupUi

    def retranslateUi(self, Cameras):
        Cameras.setWindowTitle(QCoreApplication.translate("Cameras", u"Cameras", None))
        self.label.setText(QCoreApplication.translate("Cameras", u"Outer Rectangle:", None))
        self.label_2.setText(QCoreApplication.translate("Cameras", u"Inner Rectangle:", None))
        self.label_3.setText(QCoreApplication.translate("Cameras", u"Inner Rectangle 4:3", None))
        self.label_4.setText(QCoreApplication.translate("Cameras", u"Edge Circles:", None))
        self.label_5.setText(QCoreApplication.translate("Cameras", u"Center:", None))
        self.label_7.setText(QCoreApplication.translate("Cameras", u"Camera shape:", None))
        self.label_6.setText(QCoreApplication.translate("Cameras", u"Index:", None))
        self.Index.setText("")
    # retranslateUi

