# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tilessxnFkf.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QRadioButton, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

from BaseModWidgets import SimpleGeoViewport

class Ui_TileSettings(object):
    def setupUi(self, TileSettings):
        if not TileSettings.objectName():
            TileSettings.setObjectName(u"TileSettings")
        TileSettings.resize(572, 457)
        self.gridLayout = QGridLayout(TileSettings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.graphicsView = SimpleGeoViewport(TileSettings)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout.addWidget(self.graphicsView, 0, 1, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(TileSettings)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.L1show = QCheckBox(TileSettings)
        self.L1show.setObjectName(u"L1show")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.L1show.sizePolicy().hasHeightForWidth())
        self.L1show.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.L1show)

        self.L1op2 = QSpinBox(TileSettings)
        self.L1op2.setObjectName(u"L1op2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.L1op2.sizePolicy().hasHeightForWidth())
        self.L1op2.setSizePolicy(sizePolicy1)
        self.L1op2.setMaximum(255)

        self.horizontalLayout_2.addWidget(self.L1op2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.L1op = QSlider(TileSettings)
        self.L1op.setObjectName(u"L1op")
        self.L1op.setMaximum(255)
        self.L1op.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_2.addWidget(self.L1op)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.L2show = QCheckBox(TileSettings)
        self.L2show.setObjectName(u"L2show")
        sizePolicy.setHeightForWidth(self.L2show.sizePolicy().hasHeightForWidth())
        self.L2show.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.L2show)

        self.L2op2 = QSpinBox(TileSettings)
        self.L2op2.setObjectName(u"L2op2")
        sizePolicy1.setHeightForWidth(self.L2op2.sizePolicy().hasHeightForWidth())
        self.L2op2.setSizePolicy(sizePolicy1)
        self.L2op2.setMaximum(255)

        self.horizontalLayout_4.addWidget(self.L2op2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.L2op = QSlider(TileSettings)
        self.L2op.setObjectName(u"L2op")
        self.L2op.setMaximum(255)
        self.L2op.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_2.addWidget(self.L2op)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.L3show = QCheckBox(TileSettings)
        self.L3show.setObjectName(u"L3show")
        sizePolicy.setHeightForWidth(self.L3show.sizePolicy().hasHeightForWidth())
        self.L3show.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.L3show)

        self.L3op2 = QSpinBox(TileSettings)
        self.L3op2.setObjectName(u"L3op2")
        sizePolicy1.setHeightForWidth(self.L3op2.sizePolicy().hasHeightForWidth())
        self.L3op2.setSizePolicy(sizePolicy1)
        self.L3op2.setMaximum(255)

        self.horizontalLayout_5.addWidget(self.L3op2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.L3op = QSlider(TileSettings)
        self.L3op.setObjectName(u"L3op")
        self.L3op.setMaximum(255)
        self.L3op.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_2.addWidget(self.L3op)

        self.OPshift = QCheckBox(TileSettings)
        self.OPshift.setObjectName(u"OPshift")

        self.verticalLayout_2.addWidget(self.OPshift)

        self.line = QFrame(TileSettings)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.label_5 = QLabel(TileSettings)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)

        self.RGBop2 = QSpinBox(TileSettings)
        self.RGBop2.setObjectName(u"RGBop2")
        sizePolicy.setHeightForWidth(self.RGBop2.sizePolicy().hasHeightForWidth())
        self.RGBop2.setSizePolicy(sizePolicy)
        self.RGBop2.setMaximum(255)

        self.horizontalLayout_9.addWidget(self.RGBop2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.RGBop = QSlider(TileSettings)
        self.RGBop.setObjectName(u"RGBop")
        self.RGBop.setMaximum(255)
        self.RGBop.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_2.addWidget(self.RGBop)

        self.line_2 = QFrame(TileSettings)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.label_6 = QLabel(TileSettings)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.RWEpreview = QRadioButton(TileSettings)
        self.RWEpreview.setObjectName(u"RWEpreview")

        self.horizontalLayout_3.addWidget(self.RWEpreview)

        self.Leditorpreview = QRadioButton(TileSettings)
        self.Leditorpreview.setObjectName(u"Leditorpreview")

        self.horizontalLayout_3.addWidget(self.Leditorpreview)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(TileSettings)

        QMetaObject.connectSlotsByName(TileSettings)
    # setupUi

    def retranslateUi(self, TileSettings):
        TileSettings.setWindowTitle(QCoreApplication.translate("TileSettings", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("TileSettings", u"RWE+ view layer opacity", None))
        self.L1show.setText(QCoreApplication.translate("TileSettings", u"Layer 1", None))
        self.L2show.setText(QCoreApplication.translate("TileSettings", u"Layer 2", None))
        self.L3show.setText(QCoreApplication.translate("TileSettings", u"Layer 3", None))
        self.OPshift.setText(QCoreApplication.translate("TileSettings", u"Opacity Shift", None))
        self.label_5.setText(QCoreApplication.translate("TileSettings", u"Old(Leditor) view layers opacity", None))
        self.label_6.setText(QCoreApplication.translate("TileSettings", u"Preview", None))
        self.RWEpreview.setText(QCoreApplication.translate("TileSettings", u"RWE+", None))
        self.Leditorpreview.setText(QCoreApplication.translate("TileSettings", u"Leditor", None))
    # retranslateUi

