# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cameras.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from RWS.Widgets import (ColorPicker, PenPicker)

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
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.rect1 = PenPicker(self.scrollAreaWidgetContents)
        self.rect1.setObjectName(u"rect1")

        self.horizontalLayout_2.addWidget(self.rect1)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.rect2 = PenPicker(self.scrollAreaWidgetContents)
        self.rect2.setObjectName(u"rect2")

        self.horizontalLayout_3.addWidget(self.rect2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.rect3 = PenPicker(self.scrollAreaWidgetContents)
        self.rect3.setObjectName(u"rect3")

        self.horizontalLayout_4.addWidget(self.rect3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.circle = PenPicker(self.scrollAreaWidgetContents)
        self.circle.setObjectName(u"circle")

        self.horizontalLayout_5.addWidget(self.circle)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.center = PenPicker(self.scrollAreaWidgetContents)
        self.center.setObjectName(u"center")

        self.horizontalLayout_6.addWidget(self.center)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.poly = PenPicker(self.scrollAreaWidgetContents)
        self.poly.setObjectName(u"poly")

        self.horizontalLayout_7.addWidget(self.poly)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_8.addWidget(self.label_6)

        self.Index = ColorPicker(self.scrollAreaWidgetContents)
        self.Index.setObjectName(u"Index")
        self.Index.setEnabled(True)

        self.horizontalLayout_8.addWidget(self.Index)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


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
        self.label_3.setText(QCoreApplication.translate("Cameras", u"Inner Rectangle 4:3:", None))
        self.label_4.setText(QCoreApplication.translate("Cameras", u"Edge Circles:", None))
        self.label_5.setText(QCoreApplication.translate("Cameras", u"Center:", None))
        self.label_7.setText(QCoreApplication.translate("Cameras", u"Camera shape:", None))
        self.label_6.setText(QCoreApplication.translate("Cameras", u"Index(text color):", None))
        self.Index.setText("")
    # retranslateUi

