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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QRadioButton, QScrollArea,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

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
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
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
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.L1show.sizePolicy().hasHeightForWidth())
        self.L1show.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.L1show)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label)

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

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_2)

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

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_3)

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
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.RGBop2.sizePolicy().hasHeightForWidth())
        self.RGBop2.setSizePolicy(sizePolicy2)
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

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.RWEpreview = QRadioButton(self.scrollAreaWidgetContents)
        self.RWEpreview.setObjectName(u"RWEpreview")

        self.horizontalLayout_3.addWidget(self.RWEpreview)

        self.Leditorpreview = QRadioButton(self.scrollAreaWidgetContents)
        self.Leditorpreview.setObjectName(u"Leditorpreview")

        self.horizontalLayout_3.addWidget(self.Leditorpreview)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.graphicsView = SimpleGeoViewport(self.scrollAreaWidgetContents)
        self.graphicsView.setObjectName(u"graphicsView")

        self.horizontalLayout.addWidget(self.graphicsView)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.L1show)
        self.label_2.setBuddy(self.L2show)
        self.label_3.setBuddy(self.L3show)
#endif // QT_CONFIG(shortcut)
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
        self.L1show.setText("")
        self.label.setText(QCoreApplication.translate("Geometry", u"Layer 1", None))
        self.L2show.setText("")
        self.label_2.setText(QCoreApplication.translate("Geometry", u"Layer 2", None))
        self.L3show.setText("")
        self.label_3.setText(QCoreApplication.translate("Geometry", u"Layer 3", None))
        self.OPshift.setText(QCoreApplication.translate("Geometry", u"Opacity Shift", None))
        self.label_5.setText(QCoreApplication.translate("Geometry", u"Old(Leditor) view layers opacity", None))
        self.label_6.setText(QCoreApplication.translate("Geometry", u"Preview", None))
        self.RWEpreview.setText(QCoreApplication.translate("Geometry", u"RWE+", None))
        self.Leditorpreview.setText(QCoreApplication.translate("Geometry", u"Leditor", None))
    # retranslateUi

