# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'light.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            Qt)
from PySide6.QtWidgets import (QCheckBox, QLabel, QScrollArea,
                               QSizePolicy, QSlider, QSpacerItem, QVBoxLayout,
                               QWidget)

class Ui_LightView(object):
    def setupUi(self, LightView):
        if not LightView.objectName():
            LightView.setObjectName(u"LightView")
        LightView.resize(381, 378)
        self.verticalLayout = QVBoxLayout(LightView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(LightView)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 365, 362))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.ShowLight = QCheckBox(self.scrollAreaWidgetContents)
        self.ShowLight.setObjectName(u"ShowLight")
        self.ShowLight.setChecked(True)

        self.verticalLayout_2.addWidget(self.ShowLight)

        self.ShowMoved = QCheckBox(self.scrollAreaWidgetContents)
        self.ShowMoved.setObjectName(u"ShowMoved")

        self.verticalLayout_2.addWidget(self.ShowMoved)

        self.MovedSlider = QSlider(self.scrollAreaWidgetContents)
        self.MovedSlider.setObjectName(u"MovedSlider")
        self.MovedSlider.setMaximum(100)
        self.MovedSlider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_2.addWidget(self.MovedSlider)

        self.ShowStatic = QCheckBox(self.scrollAreaWidgetContents)
        self.ShowStatic.setObjectName(u"ShowStatic")

        self.verticalLayout_2.addWidget(self.ShowStatic)

        self.StaticSlider = QSlider(self.scrollAreaWidgetContents)
        self.StaticSlider.setObjectName(u"StaticSlider")
        self.StaticSlider.setMaximum(100)
        self.StaticSlider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_2.addWidget(self.StaticSlider)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(LightView)
        self.ShowLight.toggled.connect(self.ShowMoved.setEnabled)
        self.ShowLight.toggled.connect(self.ShowStatic.setEnabled)
        self.ShowLight.toggled.connect(self.MovedSlider.setEnabled)
        self.ShowLight.toggled.connect(self.StaticSlider.setEnabled)

        QMetaObject.connectSlotsByName(LightView)
    # setupUi

    def retranslateUi(self, LightView):
        LightView.setWindowTitle(QCoreApplication.translate("LightView", u"LightView", None))
        self.label.setText(QCoreApplication.translate("LightView", u"Light settings:", None))
        self.ShowLight.setText(QCoreApplication.translate("LightView", u"Show Light", None))
        self.ShowMoved.setText(QCoreApplication.translate("LightView", u"Show Moved Light", None))
        self.ShowStatic.setText(QCoreApplication.translate("LightView", u"Show Static Light", None))
    # retranslateUi

