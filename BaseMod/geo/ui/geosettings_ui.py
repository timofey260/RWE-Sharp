# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'geoFFBtLl.ui'
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
    QHBoxLayout, QLabel, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

from BaseModWidgets import SimpleGeoViewport

class Ui_Geometry(object):
    def setupUi(self, Geometry):
        if not Geometry.objectName():
            Geometry.setObjectName(u"Geometry")
        Geometry.resize(616, 482)
        self.gridLayout = QGridLayout(Geometry)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(Geometry)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 614, 480))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.graphicsView = SimpleGeoViewport(self.scrollAreaWidgetContents)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_2.addWidget(self.graphicsView, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.L1show = QCheckBox(self.scrollAreaWidgetContents)
        self.L1show.setObjectName(u"L1show")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.L1show.sizePolicy().hasHeightForWidth())
        self.L1show.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.L1show)

        self.L1op2 = QSpinBox(self.scrollAreaWidgetContents)
        self.L1op2.setObjectName(u"L1op2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.L1op2.sizePolicy().hasHeightForWidth())
        self.L1op2.setSizePolicy(sizePolicy1)
        self.L1op2.setMaximum(255)

        self.horizontalLayout_2.addWidget(self.L1op2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.L1op = QSlider(self.scrollAreaWidgetContents)
        self.L1op.setObjectName(u"L1op")
        self.L1op.setMaximum(255)
        self.L1op.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout.addWidget(self.L1op)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.L2show = QCheckBox(self.scrollAreaWidgetContents)
        self.L2show.setObjectName(u"L2show")
        sizePolicy.setHeightForWidth(self.L2show.sizePolicy().hasHeightForWidth())
        self.L2show.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.L2show)

        self.L2op2 = QSpinBox(self.scrollAreaWidgetContents)
        self.L2op2.setObjectName(u"L2op2")
        sizePolicy1.setHeightForWidth(self.L2op2.sizePolicy().hasHeightForWidth())
        self.L2op2.setSizePolicy(sizePolicy1)
        self.L2op2.setMaximum(255)

        self.horizontalLayout_4.addWidget(self.L2op2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.L2op = QSlider(self.scrollAreaWidgetContents)
        self.L2op.setObjectName(u"L2op")
        self.L2op.setMaximum(255)
        self.L2op.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout.addWidget(self.L2op)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.L3show = QCheckBox(self.scrollAreaWidgetContents)
        self.L3show.setObjectName(u"L3show")
        sizePolicy.setHeightForWidth(self.L3show.sizePolicy().hasHeightForWidth())
        self.L3show.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.L3show)

        self.L3op2 = QSpinBox(self.scrollAreaWidgetContents)
        self.L3op2.setObjectName(u"L3op2")
        sizePolicy1.setHeightForWidth(self.L3op2.sizePolicy().hasHeightForWidth())
        self.L3op2.setSizePolicy(sizePolicy1)
        self.L3op2.setMaximum(255)

        self.horizontalLayout_5.addWidget(self.L3op2)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.L3op = QSlider(self.scrollAreaWidgetContents)
        self.L3op.setObjectName(u"L3op")
        self.L3op.setMaximum(255)
        self.L3op.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout.addWidget(self.L3op)

        self.OPshift = QCheckBox(self.scrollAreaWidgetContents)
        self.OPshift.setObjectName(u"OPshift")

        self.verticalLayout.addWidget(self.OPshift)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)

        self.RGBop2 = QSpinBox(self.scrollAreaWidgetContents)
        self.RGBop2.setObjectName(u"RGBop2")
        sizePolicy.setHeightForWidth(self.RGBop2.sizePolicy().hasHeightForWidth())
        self.RGBop2.setSizePolicy(sizePolicy)
        self.RGBop2.setMaximum(255)

        self.horizontalLayout_9.addWidget(self.RGBop2)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.RGBop = QSlider(self.scrollAreaWidgetContents)
        self.RGBop.setObjectName(u"RGBop")
        self.RGBop.setMaximum(255)
        self.RGBop.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout.addWidget(self.RGBop)

        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.RWEpreview = QRadioButton(self.scrollAreaWidgetContents)
        self.RWEpreview.setObjectName(u"RWEpreview")

        self.gridLayout_3.addWidget(self.RWEpreview, 1, 0, 1, 1)

        self.Leditorpreview = QRadioButton(self.scrollAreaWidgetContents)
        self.Leditorpreview.setObjectName(u"Leditorpreview")

        self.gridLayout_3.addWidget(self.Leditorpreview, 1, 1, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 3, 1)

        self.ChangeImage = QPushButton(self.scrollAreaWidgetContents)
        self.ChangeImage.setObjectName(u"ChangeImage")

        self.gridLayout_2.addWidget(self.ChangeImage, 2, 1, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        QWidget.setTabOrder(self.scrollArea, self.L1show)
        QWidget.setTabOrder(self.L1show, self.L2show)
        QWidget.setTabOrder(self.L2show, self.L3show)
        QWidget.setTabOrder(self.L3show, self.RWEpreview)
        QWidget.setTabOrder(self.RWEpreview, self.Leditorpreview)

        self.retranslateUi(Geometry)

        QMetaObject.connectSlotsByName(Geometry)
    # setupUi

    def retranslateUi(self, Geometry):
        Geometry.setWindowTitle(QCoreApplication.translate("Geometry", u"Geometry", None))
        self.label_4.setText(QCoreApplication.translate("Geometry", u"RWE+ view layer opacity", None))
        self.L1show.setText(QCoreApplication.translate("Geometry", u"Layer 1", None))
        self.L2show.setText(QCoreApplication.translate("Geometry", u"Layer 2", None))
        self.L3show.setText(QCoreApplication.translate("Geometry", u"Layer 3", None))
        self.OPshift.setText(QCoreApplication.translate("Geometry", u"Opacity Shift", None))
        self.label_5.setText(QCoreApplication.translate("Geometry", u"Old(Leditor) view layers opacity", None))
        self.RWEpreview.setText(QCoreApplication.translate("Geometry", u"RWE+", None))
        self.Leditorpreview.setText(QCoreApplication.translate("Geometry", u"Leditor", None))
        self.label_6.setText(QCoreApplication.translate("Geometry", u"Preview", None))
        self.ChangeImage.setText(QCoreApplication.translate("Geometry", u"Change Geometry Image", None))
    # retranslateUi

