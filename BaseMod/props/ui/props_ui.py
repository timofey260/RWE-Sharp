# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'props_A_T.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
        Props.resize(590, 985)
        self.gridLayout_2 = QGridLayout(Props)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scrollArea = QScrollArea(Props)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 570, 965))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.PropOptions = QTreeWidget(self.scrollAreaWidgetContents)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.PropOptions.setHeaderItem(__qtreewidgetitem)
        self.PropOptions.setObjectName(u"PropOptions")
        self.PropOptions.header().setVisible(False)

        self.gridLayout_3.addWidget(self.PropOptions, 12, 0, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 11, 0, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 14, 0, 1, 1)

        self.ResetTransform = QPushButton(self.scrollAreaWidgetContents)
        self.ResetTransform.setObjectName(u"ResetTransform")

        self.gridLayout_3.addWidget(self.ResetTransform, 4, 0, 1, 1)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Notes = QLabel(self.frame_2)
        self.Notes.setObjectName(u"Notes")
        self.Notes.setWordWrap(True)

        self.verticalLayout.addWidget(self.Notes)


        self.gridLayout_3.addWidget(self.frame_2, 15, 0, 1, 1)

        self.FreeTransform = QPushButton(self.scrollAreaWidgetContents)
        self.FreeTransform.setObjectName(u"FreeTransform")

        self.gridLayout_3.addWidget(self.FreeTransform, 6, 0, 1, 1)

        self.FreeRotate = QPushButton(self.scrollAreaWidgetContents)
        self.FreeRotate.setObjectName(u"FreeRotate")

        self.gridLayout_3.addWidget(self.FreeRotate, 2, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.CatPrev = QPushButton(self.scrollAreaWidgetContents)
        self.CatPrev.setObjectName(u"CatPrev")

        self.gridLayout_5.addWidget(self.CatPrev, 1, 0, 1, 1)

        self.FindPE = QPushButton(self.scrollAreaWidgetContents)
        self.FindPE.setObjectName(u"FindPE")

        self.gridLayout_5.addWidget(self.FindPE, 2, 0, 1, 1)

        self.PropNext = QPushButton(self.scrollAreaWidgetContents)
        self.PropNext.setObjectName(u"PropNext")

        self.gridLayout_5.addWidget(self.PropNext, 0, 2, 1, 1)

        self.CatNext = QPushButton(self.scrollAreaWidgetContents)
        self.CatNext.setObjectName(u"CatNext")

        self.gridLayout_5.addWidget(self.CatNext, 0, 0, 1, 1)

        self.PropPrev = QPushButton(self.scrollAreaWidgetContents)
        self.PropPrev.setObjectName(u"PropPrev")

        self.gridLayout_5.addWidget(self.PropPrev, 1, 2, 1, 1)

        self.Explorer = QPushButton(self.scrollAreaWidgetContents)
        self.Explorer.setObjectName(u"Explorer")

        self.gridLayout_5.addWidget(self.Explorer, 2, 2, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_5, 10, 0, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 9, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.rotateby = QPushButton(self.scrollAreaWidgetContents)
        self.rotateby.setObjectName(u"rotateby")

        self.gridLayout_4.addWidget(self.rotateby, 1, 1, 1, 1)

        self.degreeamount = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.degreeamount.setObjectName(u"degreeamount")
        self.degreeamount.setDecimals(4)
        self.degreeamount.setMinimum(-360.000000000000000)
        self.degreeamount.setMaximum(360.000000000000000)
        self.degreeamount.setSingleStep(0.500000000000000)

        self.gridLayout_4.addWidget(self.degreeamount, 1, 3, 1, 1)

        self.sub15 = QPushButton(self.scrollAreaWidgetContents)
        self.sub15.setObjectName(u"sub15")

        self.gridLayout_4.addWidget(self.sub15, 0, 1, 1, 1)

        self.add15 = QPushButton(self.scrollAreaWidgetContents)
        self.add15.setObjectName(u"add15")

        self.gridLayout_4.addWidget(self.add15, 0, 3, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_4, 1, 0, 1, 1)

        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")

        self.gridLayout_3.addWidget(self.frame, 12, 1, 1, 1)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line, 8, 0, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 16, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.retranslateUi(Props)

        QMetaObject.connectSlotsByName(Props)
    # setupUi

    def retranslateUi(self, Props):
        Props.setWindowTitle(QCoreApplication.translate("Props", u"Props", None))
        self.label.setText(QCoreApplication.translate("Props", u"Prop Options:", None))
        self.label_2.setText(QCoreApplication.translate("Props", u"Notes:", None))
        self.ResetTransform.setText(QCoreApplication.translate("Props", u"Reset Transform", None))
        self.Notes.setText(QCoreApplication.translate("Props", u"TextLabel", None))
        self.FreeTransform.setText(QCoreApplication.translate("Props", u"Free Transform", None))
        self.FreeRotate.setText(QCoreApplication.translate("Props", u"Free Rotate", None))
        self.CatPrev.setText(QCoreApplication.translate("Props", u"Category-", None))
        self.FindPE.setText(QCoreApplication.translate("Props", u"Find", None))
        self.PropNext.setText(QCoreApplication.translate("Props", u"Prop+", None))
        self.CatNext.setText(QCoreApplication.translate("Props", u"Category+", None))
        self.PropPrev.setText(QCoreApplication.translate("Props", u"Prop-", None))
        self.Explorer.setText(QCoreApplication.translate("Props", u"Open Explorer", None))
        self.label_3.setText(QCoreApplication.translate("Props", u"Prop Explorer:", None))
        self.rotateby.setText(QCoreApplication.translate("Props", u"rotate by:", None))
        self.degreeamount.setSuffix(QCoreApplication.translate("Props", u"\u00ba", None))
        self.sub15.setText(QCoreApplication.translate("Props", u"-15\u00ba", None))
        self.add15.setText(QCoreApplication.translate("Props", u"+15\u00ba", None))
        self.label_4.setText(QCoreApplication.translate("Props", u"Transform:", None))
    # retranslateUi

