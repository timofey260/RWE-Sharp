# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'geo.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGridLayout, QHBoxLayout,
    QLabel, QRadioButton, QScrollArea, QSizePolicy,
    QSlider, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Geometry(object):
    def setupUi(self, Geometry):
        if not Geometry.objectName():
            Geometry.setObjectName(u"Geometry")
        Geometry.resize(616, 482)
        self.gridLayout = QGridLayout(Geometry)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(Geometry)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 596, 462))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalSlider = QSlider(self.scrollAreaWidgetContents)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalSlider_2 = QSlider(self.scrollAreaWidgetContents)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider_2)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalSlider_3 = QSlider(self.scrollAreaWidgetContents)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        self.horizontalSlider_3.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider_3)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.horizontalSlider_4 = QSlider(self.scrollAreaWidgetContents)
        self.horizontalSlider_4.setObjectName(u"horizontalSlider_4")
        self.horizontalSlider_4.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.radioButton = QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_3.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_3.addWidget(self.radioButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.graphicsView = QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView.setObjectName(u"graphicsView")

        self.horizontalLayout.addWidget(self.graphicsView)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.retranslateUi(Geometry)

        QMetaObject.connectSlotsByName(Geometry)
    # setupUi

    def retranslateUi(self, Geometry):
        Geometry.setWindowTitle(QCoreApplication.translate("Geometry", u"Geometry", None))
        self.label_4.setText(QCoreApplication.translate("Geometry", u"RWE+ view layer opacity", None))
        self.label.setText(QCoreApplication.translate("Geometry", u"Layer 1", None))
        self.label_2.setText(QCoreApplication.translate("Geometry", u"Layer 2", None))
        self.label_3.setText(QCoreApplication.translate("Geometry", u"Layer 3", None))
        self.label_5.setText(QCoreApplication.translate("Geometry", u"Old(Leditor) view layers opacity", None))
        self.radioButton.setText(QCoreApplication.translate("Geometry", u"RWE+", None))
        self.radioButton_2.setText(QCoreApplication.translate("Geometry", u"Leditor", None))
    # retranslateUi

