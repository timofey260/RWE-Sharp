# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'grid.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            Qt)
from PySide6.QtWidgets import (QCheckBox, QGridLayout, QHBoxLayout,
                               QLabel, QScrollArea, QSizePolicy, QSpacerItem,
                               QSpinBox, QVBoxLayout, QWidget)

from RWESharp.Core.RWESharpWidgets import (ColorPicker, PenPicker)


class Ui_MiscView(object):
    def setupUi(self, MiscView):
        if not MiscView.objectName():
            MiscView.setObjectName(u"MiscView")
        MiscView.resize(389, 478)
        self.verticalLayout = QVBoxLayout(MiscView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(MiscView)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 373, 462))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ShowGrid = QCheckBox(self.scrollAreaWidgetContents)
        self.ShowGrid.setObjectName(u"ShowGrid")

        self.verticalLayout_2.addWidget(self.ShowGrid)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(8)
        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)

        self.ScaleY = QSpinBox(self.scrollAreaWidgetContents)
        self.ScaleY.setObjectName(u"ScaleY")
        self.ScaleY.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ScaleY.sizePolicy().hasHeightForWidth())
        self.ScaleY.setSizePolicy(sizePolicy1)
        self.ScaleY.setMinimum(1)

        self.gridLayout.addWidget(self.ScaleY, 1, 4, 1, 1)

        self.OffsetX = QSpinBox(self.scrollAreaWidgetContents)
        self.OffsetX.setObjectName(u"OffsetX")
        self.OffsetX.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.OffsetX.sizePolicy().hasHeightForWidth())
        self.OffsetX.setSizePolicy(sizePolicy1)
        self.OffsetX.setMinimum(-99)

        self.gridLayout.addWidget(self.OffsetX, 2, 2, 1, 1)

        self.OffsetY = QSpinBox(self.scrollAreaWidgetContents)
        self.OffsetY.setObjectName(u"OffsetY")
        self.OffsetY.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.OffsetY.sizePolicy().hasHeightForWidth())
        self.OffsetY.setSizePolicy(sizePolicy1)
        self.OffsetY.setMinimum(-99)

        self.gridLayout.addWidget(self.OffsetY, 2, 4, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 1, 3, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.ScaleX = QSpinBox(self.scrollAreaWidgetContents)
        self.ScaleX.setObjectName(u"ScaleX")
        self.ScaleX.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.ScaleX.sizePolicy().hasHeightForWidth())
        self.ScaleX.setSizePolicy(sizePolicy1)
        self.ScaleX.setMinimum(1)

        self.gridLayout.addWidget(self.ScaleX, 1, 2, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 2, 3, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_2.addWidget(self.label_7)

        self.GridColor = PenPicker(self.scrollAreaWidgetContents)
        self.GridColor.setObjectName(u"GridColor")

        self.verticalLayout_2.addWidget(self.GridColor)

        self.ShowBorder = QCheckBox(self.scrollAreaWidgetContents)
        self.ShowBorder.setObjectName(u"ShowBorder")

        self.verticalLayout_2.addWidget(self.ShowBorder)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_2.addWidget(self.label_8)

        self.BorderColor = PenPicker(self.scrollAreaWidgetContents)
        self.BorderColor.setObjectName(u"BorderColor")

        self.verticalLayout_2.addWidget(self.BorderColor)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Water = QCheckBox(self.scrollAreaWidgetContents)
        self.Water.setObjectName(u"Water")
        self.Water.setChecked(True)

        self.horizontalLayout.addWidget(self.Water)

        self.WaterColor = ColorPicker(self.scrollAreaWidgetContents)
        self.WaterColor.setObjectName(u"WaterColor")

        self.horizontalLayout.addWidget(self.WaterColor)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(MiscView)
        self.ShowGrid.toggled.connect(self.ScaleX.setEnabled)
        self.ShowGrid.toggled.connect(self.ScaleY.setEnabled)
        self.ShowGrid.toggled.connect(self.OffsetX.setEnabled)
        self.ShowGrid.toggled.connect(self.OffsetY.setEnabled)
        self.Water.toggled.connect(self.WaterColor.setEnabled)

        QMetaObject.connectSlotsByName(MiscView)
    # setupUi

    def retranslateUi(self, MiscView):
        MiscView.setWindowTitle(QCoreApplication.translate("MiscView", u"Misc", None))
        self.ShowGrid.setText(QCoreApplication.translate("MiscView", u"Show grid", None))
        self.label_5.setText(QCoreApplication.translate("MiscView", u"X:", None))
        self.label_3.setText(QCoreApplication.translate("MiscView", u"X:", None))
        self.label_6.setText(QCoreApplication.translate("MiscView", u"Y:", None))
        self.label_2.setText(QCoreApplication.translate("MiscView", u"Scale:", None))
        self.label.setText(QCoreApplication.translate("MiscView", u"Offset:", None))
        self.label_4.setText(QCoreApplication.translate("MiscView", u"Y:", None))
        self.label_7.setText(QCoreApplication.translate("MiscView", u"Grid Style:", None))
        self.ShowBorder.setText(QCoreApplication.translate("MiscView", u"Border", None))
        self.label_8.setText(QCoreApplication.translate("MiscView", u"Border Style:", None))
        self.Water.setText(QCoreApplication.translate("MiscView", u"Water", None))
        self.WaterColor.setText("")
    # retranslateUi

