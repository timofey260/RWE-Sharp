# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'props.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtWidgets import (QDoubleSpinBox, QFrame, QGridLayout,
                               QLabel, QPushButton, QScrollArea,
                               QSizePolicy, QSpacerItem, QTreeWidget, QTreeWidgetItem,
                               QVBoxLayout, QWidget)

class Ui_Props(object):
    def setupUi(self, Props):
        if not Props.objectName():
            Props.setObjectName(u"Props")
        Props.resize(290, 985)
        self.gridLayout_2 = QGridLayout(Props)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scrollArea = QScrollArea(Props)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 287, 955))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.FreeTransform = QPushButton(self.scrollAreaWidgetContents)
        self.FreeTransform.setObjectName(u"FreeTransform")

        self.gridLayout_3.addWidget(self.FreeTransform, 3, 0, 1, 1)

        self.Explorer = QPushButton(self.scrollAreaWidgetContents)
        self.Explorer.setObjectName(u"Explorer")

        self.gridLayout_3.addWidget(self.Explorer, 11, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.Rotateby = QPushButton(self.scrollAreaWidgetContents)
        self.Rotateby.setObjectName(u"Rotateby")

        self.gridLayout_4.addWidget(self.Rotateby, 1, 0, 1, 1)

        self.degreeamount = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.degreeamount.setObjectName(u"degreeamount")
        self.degreeamount.setDecimals(4)
        self.degreeamount.setMinimum(-360.000000000000000)
        self.degreeamount.setMaximum(360.000000000000000)
        self.degreeamount.setSingleStep(0.500000000000000)

        self.gridLayout_4.addWidget(self.degreeamount, 1, 1, 1, 1)

        self.sub15 = QPushButton(self.scrollAreaWidgetContents)
        self.sub15.setObjectName(u"sub15")

        self.gridLayout_4.addWidget(self.sub15, 0, 0, 1, 1)

        self.add15 = QPushButton(self.scrollAreaWidgetContents)
        self.add15.setObjectName(u"add15")

        self.gridLayout_4.addWidget(self.add15, 0, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_4, 1, 0, 1, 1)

        self.FreeRotate = QPushButton(self.scrollAreaWidgetContents)
        self.FreeRotate.setObjectName(u"FreeRotate")

        self.gridLayout_3.addWidget(self.FreeRotate, 2, 0, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)

        self.ResetTransform = QPushButton(self.scrollAreaWidgetContents)
        self.ResetTransform.setObjectName(u"ResetTransform")

        self.gridLayout_3.addWidget(self.ResetTransform, 5, 0, 1, 1)

        self.PropOptions = QTreeWidget(self.scrollAreaWidgetContents)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.PropOptions.setHeaderItem(__qtreewidgetitem)
        self.PropOptions.setObjectName(u"PropOptions")
        self.PropOptions.header().setVisible(False)

        self.gridLayout_3.addWidget(self.PropOptions, 13, 0, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 8, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.CatPrev = QPushButton(self.scrollAreaWidgetContents)
        self.CatPrev.setObjectName(u"CatPrev")

        self.gridLayout_5.addWidget(self.CatPrev, 1, 0, 1, 1)

        self.PropPrev = QPushButton(self.scrollAreaWidgetContents)
        self.PropPrev.setObjectName(u"PropPrev")

        self.gridLayout_5.addWidget(self.PropPrev, 0, 1, 1, 1)

        self.CatNext = QPushButton(self.scrollAreaWidgetContents)
        self.CatNext.setObjectName(u"CatNext")

        self.gridLayout_5.addWidget(self.CatNext, 1, 2, 1, 1)

        self.PropNext = QPushButton(self.scrollAreaWidgetContents)
        self.PropNext.setObjectName(u"PropNext")

        self.gridLayout_5.addWidget(self.PropNext, 1, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_5, 9, 0, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 15, 0, 1, 1)

        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")

        self.gridLayout_3.addWidget(self.frame, 13, 1, 1, 1)

        self.FindPE = QPushButton(self.scrollAreaWidgetContents)
        self.FindPE.setObjectName(u"FindPE")

        self.gridLayout_3.addWidget(self.FindPE, 10, 0, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 12, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 17, 0, 1, 1)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Notes = QLabel(self.frame_2)
        self.Notes.setObjectName(u"Notes")
        self.Notes.setWordWrap(True)

        self.verticalLayout.addWidget(self.Notes)


        self.gridLayout_3.addWidget(self.frame_2, 16, 0, 1, 1)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line, 7, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.retranslateUi(Props)

        QMetaObject.connectSlotsByName(Props)
    # setupUi

    def retranslateUi(self, Props):
        Props.setWindowTitle(QCoreApplication.translate("Props", u"Props", None))
        self.FreeTransform.setText(QCoreApplication.translate("Props", u"Free Transform", None))
        self.Explorer.setText(QCoreApplication.translate("Props", u"Open explorer", None))
        self.Rotateby.setText(QCoreApplication.translate("Props", u"Rotate by:", None))
        self.degreeamount.setSuffix(QCoreApplication.translate("Props", u"\u00ba", None))
        self.sub15.setText(QCoreApplication.translate("Props", u"-15\u00ba", None))
        self.add15.setText(QCoreApplication.translate("Props", u"+15\u00ba", None))
        self.FreeRotate.setText(QCoreApplication.translate("Props", u"Free rotate", None))
        self.label_4.setText(QCoreApplication.translate("Props", u"Transform:", None))
        self.ResetTransform.setText(QCoreApplication.translate("Props", u"Reset Transform", None))
        self.label_3.setText(QCoreApplication.translate("Props", u"Prop Explorer:", None))
        self.CatPrev.setText(QCoreApplication.translate("Props", u"Category-", None))
        self.PropPrev.setText(QCoreApplication.translate("Props", u"Prop-", None))
        self.CatNext.setText(QCoreApplication.translate("Props", u"Category+", None))
        self.PropNext.setText(QCoreApplication.translate("Props", u"Prop+", None))
        self.label_2.setText(QCoreApplication.translate("Props", u"Notes:", None))
        self.FindPE.setText(QCoreApplication.translate("Props", u"Find", None))
        self.label.setText(QCoreApplication.translate("Props", u"Prop Options:", None))
        self.Notes.setText(QCoreApplication.translate("Props", u"TextLabel", None))
    # retranslateUi

