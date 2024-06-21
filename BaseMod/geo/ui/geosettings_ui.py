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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QRadioButton, QScrollArea, QSizePolicy,
    QSlider, QSpacerItem, QVBoxLayout, QWidget)

from BaseModWidgets import SimpleGeoViewport

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

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_8)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.L1op = QSlider(self.scrollAreaWidgetContents)
        self.L1op.setObjectName(u"L1op")
        self.L1op.setMaximum(256)
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

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_9)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.L2op = QSlider(self.scrollAreaWidgetContents)
        self.L2op.setObjectName(u"L2op")
        self.L2op.setMaximum(256)
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

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_10)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.L3op = QSlider(self.scrollAreaWidgetContents)
        self.L3op.setObjectName(u"L3op")
        self.L3op.setMaximum(256)
        self.L3op.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout.addWidget(self.L3op)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_11)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.RGBop = QSlider(self.scrollAreaWidgetContents)
        self.RGBop.setObjectName(u"RGBop")
        self.RGBop.setMaximum(256)
        self.RGBop.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout.addWidget(self.RGBop)

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

        self.OPshift = QCheckBox(self.scrollAreaWidgetContents)
        self.OPshift.setObjectName(u"OPshift")

        self.verticalLayout.addWidget(self.OPshift)

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
        self.label_8.setBuddy(self.L1op)
        self.label_2.setBuddy(self.L2show)
        self.label_9.setBuddy(self.L2op)
        self.label_3.setBuddy(self.L3show)
        self.label_10.setBuddy(self.L3op)
        self.label_11.setBuddy(self.RGBop)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.scrollArea, self.L1show)
        QWidget.setTabOrder(self.L1show, self.L2show)
        QWidget.setTabOrder(self.L2show, self.L3show)
        QWidget.setTabOrder(self.L3show, self.RWEpreview)
        QWidget.setTabOrder(self.RWEpreview, self.Leditorpreview)
        QWidget.setTabOrder(self.Leditorpreview, self.OPshift)

        self.retranslateUi(Geometry)
        self.L1op.valueChanged.connect(self.label_8.setNum)
        self.L2op.valueChanged.connect(self.label_9.setNum)
        self.RGBop.valueChanged.connect(self.label_11.setNum)
        self.L3op.valueChanged.connect(self.label_10.setNum)

        QMetaObject.connectSlotsByName(Geometry)
    # setupUi

    def retranslateUi(self, Geometry):
        Geometry.setWindowTitle(QCoreApplication.translate("Geometry", u"Geometry", None))
        self.label_4.setText(QCoreApplication.translate("Geometry", u"RWE+ view layer opacity", None))
        self.L1show.setText("")
        self.label.setText(QCoreApplication.translate("Geometry", u"Layer 1", None))
        self.label_8.setText(QCoreApplication.translate("Geometry", u"100", None))
        self.L2show.setText("")
        self.label_2.setText(QCoreApplication.translate("Geometry", u"Layer 2", None))
        self.label_9.setText(QCoreApplication.translate("Geometry", u"100", None))
        self.L3show.setText("")
        self.label_3.setText(QCoreApplication.translate("Geometry", u"Layer 3", None))
        self.label_10.setText(QCoreApplication.translate("Geometry", u"100", None))
        self.label_5.setText(QCoreApplication.translate("Geometry", u"Old(Leditor) view layers opacity", None))
        self.label_11.setText(QCoreApplication.translate("Geometry", u"100", None))
        self.label_6.setText(QCoreApplication.translate("Geometry", u"Preview", None))
        self.RWEpreview.setText(QCoreApplication.translate("Geometry", u"RWE+", None))
        self.Leditorpreview.setText(QCoreApplication.translate("Geometry", u"Leditor", None))
        self.OPshift.setText(QCoreApplication.translate("Geometry", u"Opacity Shift", None))
    # retranslateUi

