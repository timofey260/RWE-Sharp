# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'backup0SZPkye.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QGridLayout,
    QHeaderView, QLabel, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Props(object):
    def setupUi(self, Props):
        if not Props.objectName():
            Props.setObjectName(u"Props")
        Props.resize(649, 882)
        self.gridLayout_2 = QGridLayout(Props)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scrollArea = QScrollArea(Props)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 629, 427))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.NotesLabel = QLabel(self.scrollAreaWidgetContents)
        self.NotesLabel.setObjectName(u"NotesLabel")

        self.gridLayout_3.addWidget(self.NotesLabel, 10, 0, 1, 1)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Notes = QLabel(self.frame_2)
        self.Notes.setObjectName(u"Notes")

        self.verticalLayout.addWidget(self.Notes)


        self.gridLayout_3.addWidget(self.frame_2, 11, 0, 1, 1)

        self.ResetTransform = QPushButton(self.scrollAreaWidgetContents)
        self.ResetTransform.setObjectName(u"ResetTransform")

        self.gridLayout_3.addWidget(self.ResetTransform, 5, 0, 1, 1)

        self.RootateLabel = QLabel(self.scrollAreaWidgetContents)
        self.RootateLabel.setObjectName(u"RootateLabel")

        self.gridLayout_3.addWidget(self.RootateLabel, 0, 0, 1, 1)

        self.FreeTransform = QPushButton(self.scrollAreaWidgetContents)
        self.FreeTransform.setObjectName(u"FreeTransform")

        self.gridLayout_3.addWidget(self.FreeTransform, 7, 0, 1, 1)

        self.Fuckyou = QLabel(self.scrollAreaWidgetContents)
        self.Fuckyou.setObjectName(u"Fuckyou")

        self.gridLayout_3.addWidget(self.Fuckyou, 8, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.RotateMinus15 = QPushButton(self.scrollAreaWidgetContents)
        self.RotateMinus15.setObjectName(u"RotateMinus15")

        self.gridLayout_4.addWidget(self.RotateMinus15, 0, 3, 1, 1)

        self.Rotateplus15 = QPushButton(self.scrollAreaWidgetContents)
        self.Rotateplus15.setObjectName(u"Rotateplus15")

        self.gridLayout_4.addWidget(self.Rotateplus15, 0, 1, 1, 1)

        self.CustomRotateBox = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.CustomRotateBox.setObjectName(u"CustomRotateBox")
        self.CustomRotateBox.setDecimals(4)
        self.CustomRotateBox.setMinimum(-360.000000000000000)
        self.CustomRotateBox.setMaximum(360.000000000000000)
        self.CustomRotateBox.setSingleStep(0.500000000000000)

        self.gridLayout_4.addWidget(self.CustomRotateBox, 1, 3, 1, 1)

        self.CustomRotate = QPushButton(self.scrollAreaWidgetContents)
        self.CustomRotate.setObjectName(u"CustomRotate")

        self.gridLayout_4.addWidget(self.CustomRotate, 1, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_4, 1, 0, 1, 1)

        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")

        self.gridLayout_3.addWidget(self.frame, 9, 1, 1, 1)

        self.PropOptions = QTreeWidget(self.scrollAreaWidgetContents)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.PropOptions.setHeaderItem(__qtreewidgetitem)
        self.PropOptions.setObjectName(u"PropOptions")
        self.PropOptions.header().setVisible(False)

        self.gridLayout_3.addWidget(self.PropOptions, 9, 0, 1, 1)

        self.FreeRotate = QPushButton(self.scrollAreaWidgetContents)
        self.FreeRotate.setObjectName(u"FreeRotate")

        self.gridLayout_3.addWidget(self.FreeRotate, 3, 0, 1, 1)

        self.Transgender = QLabel(self.scrollAreaWidgetContents)
        self.Transgender.setObjectName(u"Transgender")

        self.gridLayout_3.addWidget(self.Transgender, 2, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.retranslateUi(Props)

        QMetaObject.connectSlotsByName(Props)
    # setupUi

    def retranslateUi(self, Props):
        Props.setWindowTitle(QCoreApplication.translate("Props", u"Props", None))
        self.NotesLabel.setText(QCoreApplication.translate("Props", u"Notes:", None))
        self.Notes.setText(QCoreApplication.translate("Props", u"TextLabel", None))
        self.ResetTransform.setText(QCoreApplication.translate("Props", u"Reset Transform", None))
        self.RootateLabel.setText(QCoreApplication.translate("Props", u"Rotate:", None))
        self.FreeTransform.setText(QCoreApplication.translate("Props", u"Free Transform", None))
        self.Fuckyou.setText(QCoreApplication.translate("Props", u"Options:", None))
        self.RotateMinus15.setText(QCoreApplication.translate("Props", u"-15\u00ba", None))
        self.Rotateplus15.setText(QCoreApplication.translate("Props", u"+15\u00ba", None))
        self.CustomRotate.setText(QCoreApplication.translate("Props", u"rotate by:", None))
        self.FreeRotate.setText(QCoreApplication.translate("Props", u"Free Rotate", None))
        self.Transgender.setText(QCoreApplication.translate("Props", u"Transform", None))
    # retranslateUi

