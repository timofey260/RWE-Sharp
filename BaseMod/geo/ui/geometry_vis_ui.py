# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'geometry.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtWidgets import (QCheckBox, QLabel, QRadioButton,
                               QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
                               QWidget)

class Ui_GeoView(object):
    def setupUi(self, GeoView):
        if not GeoView.objectName():
            GeoView.setObjectName(u"GeoView")
        GeoView.resize(348, 390)
        self.verticalLayout = QVBoxLayout(GeoView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(GeoView)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 328, 370))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.VGeolabel = QLabel(self.scrollAreaWidgetContents)
        self.VGeolabel.setObjectName(u"VGeolabel")

        self.verticalLayout_2.addWidget(self.VGeolabel)

        self.VGeoAll = QCheckBox(self.scrollAreaWidgetContents)
        self.VGeoAll.setObjectName(u"VGeoAll")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VGeoAll.sizePolicy().hasHeightForWidth())
        self.VGeoAll.setSizePolicy(sizePolicy)
        self.VGeoAll.setChecked(True)

        self.verticalLayout_2.addWidget(self.VGeoAll)

        self.VGeoLayer1 = QCheckBox(self.scrollAreaWidgetContents)
        self.VGeoLayer1.setObjectName(u"VGeoLayer1")
        self.VGeoLayer1.setEnabled(False)
        sizePolicy.setHeightForWidth(self.VGeoLayer1.sizePolicy().hasHeightForWidth())
        self.VGeoLayer1.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.VGeoLayer1)

        self.VGeoLayer2 = QCheckBox(self.scrollAreaWidgetContents)
        self.VGeoLayer2.setObjectName(u"VGeoLayer2")
        self.VGeoLayer2.setEnabled(False)
        sizePolicy.setHeightForWidth(self.VGeoLayer2.sizePolicy().hasHeightForWidth())
        self.VGeoLayer2.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.VGeoLayer2)

        self.VGeoLayer3 = QCheckBox(self.scrollAreaWidgetContents)
        self.VGeoLayer3.setObjectName(u"VGeoLayer3")
        self.VGeoLayer3.setEnabled(False)
        sizePolicy.setHeightForWidth(self.VGeoLayer3.sizePolicy().hasHeightForWidth())
        self.VGeoLayer3.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.VGeoLayer3)

        self.VGeoBeams = QCheckBox(self.scrollAreaWidgetContents)
        self.VGeoBeams.setObjectName(u"VGeoBeams")
        self.VGeoBeams.setEnabled(False)
        sizePolicy.setHeightForWidth(self.VGeoBeams.sizePolicy().hasHeightForWidth())
        self.VGeoBeams.setSizePolicy(sizePolicy)
        self.VGeoBeams.setChecked(False)

        self.verticalLayout_2.addWidget(self.VGeoBeams)

        self.VGeoPipes = QCheckBox(self.scrollAreaWidgetContents)
        self.VGeoPipes.setObjectName(u"VGeoPipes")
        self.VGeoPipes.setEnabled(False)
        sizePolicy.setHeightForWidth(self.VGeoPipes.sizePolicy().hasHeightForWidth())
        self.VGeoPipes.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.VGeoPipes)

        self.VGeoMisc = QCheckBox(self.scrollAreaWidgetContents)
        self.VGeoMisc.setObjectName(u"VGeoMisc")
        self.VGeoMisc.setEnabled(False)
        sizePolicy.setHeightForWidth(self.VGeoMisc.sizePolicy().hasHeightForWidth())
        self.VGeoMisc.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.VGeoMisc)

        self.VGeoRWEstyle = QRadioButton(self.scrollAreaWidgetContents)
        self.VGeoRWEstyle.setObjectName(u"VGeoRWEstyle")
        sizePolicy.setHeightForWidth(self.VGeoRWEstyle.sizePolicy().hasHeightForWidth())
        self.VGeoRWEstyle.setSizePolicy(sizePolicy)
        self.VGeoRWEstyle.setChecked(True)

        self.verticalLayout_2.addWidget(self.VGeoRWEstyle)

        self.VGeoOldStyle = QRadioButton(self.scrollAreaWidgetContents)
        self.VGeoOldStyle.setObjectName(u"VGeoOldStyle")
        sizePolicy.setHeightForWidth(self.VGeoOldStyle.sizePolicy().hasHeightForWidth())
        self.VGeoOldStyle.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.VGeoOldStyle)

        self.verticalSpacer_2 = QSpacerItem(273, 93, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(GeoView)
        self.VGeoAll.toggled.connect(self.VGeoLayer1.setDisabled)
        self.VGeoAll.toggled.connect(self.VGeoLayer2.setDisabled)
        self.VGeoAll.toggled.connect(self.VGeoLayer3.setDisabled)
        self.VGeoAll.toggled.connect(self.VGeoBeams.setDisabled)
        self.VGeoAll.toggled.connect(self.VGeoPipes.setDisabled)
        self.VGeoAll.toggled.connect(self.VGeoMisc.setDisabled)

        QMetaObject.connectSlotsByName(GeoView)
    # setupUi

    def retranslateUi(self, GeoView):
        GeoView.setWindowTitle(QCoreApplication.translate("GeoView", u"Geo", None))
        self.VGeolabel.setText(QCoreApplication.translate("GeoView", u"Toggle visibility of:", None))
        self.VGeoAll.setText(QCoreApplication.translate("GeoView", u"All geo", None))
        self.VGeoLayer1.setText(QCoreApplication.translate("GeoView", u"Layer 1", None))
        self.VGeoLayer2.setText(QCoreApplication.translate("GeoView", u"Layer 2", None))
        self.VGeoLayer3.setText(QCoreApplication.translate("GeoView", u"Layer 3", None))
        self.VGeoBeams.setText(QCoreApplication.translate("GeoView", u"Beams", None))
        self.VGeoPipes.setText(QCoreApplication.translate("GeoView", u"Pipes", None))
        self.VGeoMisc.setText(QCoreApplication.translate("GeoView", u"misc", None))
        self.VGeoRWEstyle.setText(QCoreApplication.translate("GeoView", u"RWE+ geo view", None))
        self.VGeoOldStyle.setText(QCoreApplication.translate("GeoView", u"Old style view", None))
    # retranslateUi

