# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'geo.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QFrame,
    QGridLayout, QLabel, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

from BaseMod.BaseModWidgets import SimpleGeoViewport
import RWESharp.ui.res_rc

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

        self.ChangeImage = QPushButton(self.scrollAreaWidgetContents)
        self.ChangeImage.setObjectName(u"ChangeImage")

        self.gridLayout_2.addWidget(self.ChangeImage, 2, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.Pshow = QCheckBox(self.scrollAreaWidgetContents)
        self.Pshow.setObjectName(u"Pshow")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Pshow.sizePolicy().hasHeightForWidth())
        self.Pshow.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.Pshow)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.Pop = QSpinBox(self.scrollAreaWidgetContents)
        self.Pop.setObjectName(u"Pop")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Pop.sizePolicy().hasHeightForWidth())
        self.Pop.setSizePolicy(sizePolicy1)
        self.Pop.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Pop.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.Pop.setMaximum(255)

        self.gridLayout_4.addWidget(self.Pop, 0, 2, 1, 1)

        self.Pop2 = QSlider(self.scrollAreaWidgetContents)
        self.Pop2.setObjectName(u"Pop2")
        self.Pop2.setMaximum(255)
        self.Pop2.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_4.addWidget(self.Pop2, 0, 1, 1, 1)

        self.PRGBop = QSpinBox(self.scrollAreaWidgetContents)
        self.PRGBop.setObjectName(u"PRGBop")
        sizePolicy1.setHeightForWidth(self.PRGBop.sizePolicy().hasHeightForWidth())
        self.PRGBop.setSizePolicy(sizePolicy1)
        self.PRGBop.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.PRGBop.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.PRGBop.setMaximum(255)

        self.gridLayout_4.addWidget(self.PRGBop, 1, 2, 1, 1)

        self.PRGBop2 = QSlider(self.scrollAreaWidgetContents)
        self.PRGBop2.setObjectName(u"PRGBop2")
        self.PRGBop2.setMaximum(255)
        self.PRGBop2.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_4.addWidget(self.PRGBop2, 1, 1, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_4)

        self.Sshow = QCheckBox(self.scrollAreaWidgetContents)
        self.Sshow.setObjectName(u"Sshow")
        sizePolicy.setHeightForWidth(self.Sshow.sizePolicy().hasHeightForWidth())
        self.Sshow.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.Sshow)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.Sop2 = QSlider(self.scrollAreaWidgetContents)
        self.Sop2.setObjectName(u"Sop2")
        self.Sop2.setMaximum(255)
        self.Sop2.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_5.addWidget(self.Sop2, 0, 1, 1, 1)

        self.SRGBop2 = QSlider(self.scrollAreaWidgetContents)
        self.SRGBop2.setObjectName(u"SRGBop2")
        self.SRGBop2.setMaximum(255)
        self.SRGBop2.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_5.addWidget(self.SRGBop2, 1, 1, 1, 1)

        self.Sop = QSpinBox(self.scrollAreaWidgetContents)
        self.Sop.setObjectName(u"Sop")
        sizePolicy1.setHeightForWidth(self.Sop.sizePolicy().hasHeightForWidth())
        self.Sop.setSizePolicy(sizePolicy1)
        self.Sop.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Sop.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.Sop.setMaximum(255)

        self.gridLayout_5.addWidget(self.Sop, 0, 2, 1, 1)

        self.SRGBop = QSpinBox(self.scrollAreaWidgetContents)
        self.SRGBop.setObjectName(u"SRGBop")
        sizePolicy1.setHeightForWidth(self.SRGBop.sizePolicy().hasHeightForWidth())
        self.SRGBop.setSizePolicy(sizePolicy1)
        self.SRGBop.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.SRGBop.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.SRGBop.setMaximum(255)

        self.gridLayout_5.addWidget(self.SRGBop, 1, 2, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_5.addWidget(self.label_3, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_5)

        self.Rall = QCheckBox(self.scrollAreaWidgetContents)
        self.Rall.setObjectName(u"Rall")

        self.verticalLayout.addWidget(self.Rall)

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

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.LayerSlider = QSlider(self.scrollAreaWidgetContents)
        self.LayerSlider.setObjectName(u"LayerSlider")
        self.LayerSlider.setMaximum(2)
        self.LayerSlider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout.addWidget(self.LayerSlider)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 3, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        QWidget.setTabOrder(self.scrollArea, self.RWEpreview)
        QWidget.setTabOrder(self.RWEpreview, self.Leditorpreview)

        self.retranslateUi(Geometry)

        QMetaObject.connectSlotsByName(Geometry)
    # setupUi

    def retranslateUi(self, Geometry):
        Geometry.setWindowTitle(QCoreApplication.translate("Geometry", u"Geometry", None))
        self.ChangeImage.setText(QCoreApplication.translate("Geometry", u"Change Geometry Image", None))
        self.label_4.setText(QCoreApplication.translate("Geometry", u"RWE+ view layer opacity", None))
        self.Pshow.setText(QCoreApplication.translate("Geometry", u"Primary", None))
        self.label.setText(QCoreApplication.translate("Geometry", u"RWE+", None))
        self.label_5.setText(QCoreApplication.translate("Geometry", u"LEDITOR", None))
        self.Sshow.setText(QCoreApplication.translate("Geometry", u"Secondary", None))
        self.label_2.setText(QCoreApplication.translate("Geometry", u"RWE+", None))
        self.label_3.setText(QCoreApplication.translate("Geometry", u"LEDITOR", None))
        self.Rall.setText(QCoreApplication.translate("Geometry", u"Render All", None))
        self.RWEpreview.setText(QCoreApplication.translate("Geometry", u"RWE+", None))
        self.Leditorpreview.setText(QCoreApplication.translate("Geometry", u"Leditor", None))
        self.label_6.setText(QCoreApplication.translate("Geometry", u"Preview", None))
        self.label_7.setText(QCoreApplication.translate("Geometry", u"Layer:", None))
    # retranslateUi

