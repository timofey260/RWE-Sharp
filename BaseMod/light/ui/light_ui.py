# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'light.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QFrame, QGridLayout, QLabel,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_Light(object):
    def setupUi(self, Light):
        if not Light.objectName():
            Light.setObjectName(u"Light")
        Light.resize(423, 427)
        self.verticalLayout = QVBoxLayout(Light)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(Light)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 407, 411))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)

        self.Width = QDoubleSpinBox(self.frame)
        self.Width.setObjectName(u"Width")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Width.sizePolicy().hasHeightForWidth())
        self.Width.setSizePolicy(sizePolicy)
        self.Width.setMinimum(-1000.000000000000000)
        self.Width.setMaximum(1000.000000000000000)

        self.gridLayout_2.addWidget(self.Width, 1, 1, 1, 1)

        self.Rotation = QDoubleSpinBox(self.frame)
        self.Rotation.setObjectName(u"Rotation")
        sizePolicy.setHeightForWidth(self.Rotation.sizePolicy().hasHeightForWidth())
        self.Rotation.setSizePolicy(sizePolicy)
        self.Rotation.setMinimum(-1000.000000000000000)
        self.Rotation.setMaximum(1000.000000000000000)
        self.Rotation.setSingleStep(15.000000000000000)

        self.gridLayout_2.addWidget(self.Rotation, 3, 1, 1, 1)

        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_2.addWidget(self.label_14, 1, 0, 1, 1)

        self.Height = QDoubleSpinBox(self.frame)
        self.Height.setObjectName(u"Height")
        sizePolicy.setHeightForWidth(self.Height.sizePolicy().hasHeightForWidth())
        self.Height.setSizePolicy(sizePolicy)
        self.Height.setMinimum(-1000.000000000000000)
        self.Height.setMaximum(1000.000000000000000)

        self.gridLayout_2.addWidget(self.Height, 2, 1, 1, 1)

        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_2.addWidget(self.label_15, 3, 0, 1, 1)

        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_2.addWidget(self.label_16, 0, 0, 1, 1)

        self.Shape = QComboBox(self.frame)
        self.Shape.setObjectName(u"Shape")

        self.gridLayout_2.addWidget(self.Shape, 0, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_2)

        self.DrawOnMoved = QCheckBox(self.frame)
        self.DrawOnMoved.setObjectName(u"DrawOnMoved")

        self.verticalLayout_4.addWidget(self.DrawOnMoved)


        self.verticalLayout_2.addWidget(self.frame)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_7.addWidget(self.label_12, 0, 0, 1, 1)

        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_7.addWidget(self.label_13, 0, 1, 1, 1)

        self.Flatness = QSpinBox(self.frame_2)
        self.Flatness.setObjectName(u"Flatness")
        self.Flatness.setMinimum(1)
        self.Flatness.setMaximum(10)

        self.gridLayout_7.addWidget(self.Flatness, 1, 1, 1, 1)

        self.Angle = QDoubleSpinBox(self.frame_2)
        self.Angle.setObjectName(u"Angle")
        self.Angle.setWrapping(True)
        self.Angle.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.Angle.setDecimals(1)
        self.Angle.setMinimum(-360.000000000000000)
        self.Angle.setMaximum(360.000000000000000)
        self.Angle.setSingleStep(15.000000000000000)

        self.gridLayout_7.addWidget(self.Angle, 1, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_7)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.verticalSpacer_5 = QSpacerItem(273, 175, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(Light)

        QMetaObject.connectSlotsByName(Light)
    # setupUi

    def retranslateUi(self, Light):
        Light.setWindowTitle(QCoreApplication.translate("Light", u"Light", None))
        self.label_2.setText(QCoreApplication.translate("Light", u"Brush Settings:", None))
        self.label_11.setText(QCoreApplication.translate("Light", u"Height:", None))
        self.Rotation.setSuffix(QCoreApplication.translate("Light", u"\u00b0", None))
        self.label_14.setText(QCoreApplication.translate("Light", u"Width:", None))
        self.label_15.setText(QCoreApplication.translate("Light", u"Rotation:", None))
        self.label_16.setText(QCoreApplication.translate("Light", u"Shape:", None))
        self.DrawOnMoved.setText(QCoreApplication.translate("Light", u"Draw on Moved Light", None))
        self.label.setText(QCoreApplication.translate("Light", u"Light Image Settings:", None))
        self.label_12.setText(QCoreApplication.translate("Light", u"Angle:", None))
        self.label_13.setText(QCoreApplication.translate("Light", u"Flatness:", None))
        self.Angle.setSuffix(QCoreApplication.translate("Light", u"\u00b0", None))
    # retranslateUi

