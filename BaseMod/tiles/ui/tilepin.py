# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tilepin.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize)
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (QCheckBox, QComboBox, QHBoxLayout, QLabel, QPushButton, QSpinBox, QVBoxLayout, QWidget)

from RWESharp.Core.RWESharpWidgets import SimpleViewport


class Ui_TilePin(object):
    def setupUi(self, TilePin):
        if not TilePin.objectName():
            TilePin.setObjectName(u"TilePin")
        TilePin.resize(240, 371)
        icon = QIcon()
        icon.addFile(u":/special/special/pin.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        TilePin.setWindowIcon(icon)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tileLabel = QLabel(self.dockWidgetContents)
        self.tileLabel.setObjectName(u"tileLabel")

        self.verticalLayout.addWidget(self.tileLabel)

        self.Preview = SimpleViewport(self.dockWidgetContents)
        self.Preview.setObjectName(u"Preview")

        self.verticalLayout.addWidget(self.Preview)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Collisions = QCheckBox(self.dockWidgetContents)
        self.Collisions.setObjectName(u"Collisions")

        self.horizontalLayout.addWidget(self.Collisions)

        self.Layer = QSpinBox(self.dockWidgetContents)
        self.Layer.setObjectName(u"Layer")
        self.Layer.setWrapping(True)
        self.Layer.setMinimum(1)
        self.Layer.setMaximum(3)

        self.horizontalLayout.addWidget(self.Layer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.RenderOption = QComboBox(self.dockWidgetContents)
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.setObjectName(u"RenderOption")

        self.verticalLayout.addWidget(self.RenderOption)

        self.Select = QPushButton(self.dockWidgetContents)
        self.Select.setObjectName(u"Select")

        self.verticalLayout.addWidget(self.Select)

        TilePin.setWidget(self.dockWidgetContents)

        self.retranslateUi(TilePin)

        QMetaObject.connectSlotsByName(TilePin)
    # setupUi

    def retranslateUi(self, TilePin):
        TilePin.setWindowTitle(QCoreApplication.translate("TilePin", u"Pinned Tile", None))
        self.tileLabel.setText(QCoreApplication.translate("TilePin", u"Preview:", None))
        self.Collisions.setText(QCoreApplication.translate("TilePin", u"Collisions", None))
        self.RenderOption.setItemText(0, QCoreApplication.translate("TilePin", u"Classic", None))
        self.RenderOption.setItemText(1, QCoreApplication.translate("TilePin", u"Tile image", None))
        self.RenderOption.setItemText(2, QCoreApplication.translate("TilePin", u"Henry", None))
        self.RenderOption.setItemText(3, QCoreApplication.translate("TilePin", u"Unrendered", None))
        self.RenderOption.setItemText(4, QCoreApplication.translate("TilePin", u"Rendered (sun)", None))
        self.RenderOption.setItemText(5, QCoreApplication.translate("TilePin", u"Rendered (shaded)", None))
        self.RenderOption.setItemText(6, QCoreApplication.translate("TilePin", u"Rendered (rain)", None))

        self.Select.setText(QCoreApplication.translate("TilePin", u"Select", None))
    # retranslateUi

