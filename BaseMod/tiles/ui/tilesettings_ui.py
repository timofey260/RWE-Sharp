# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tiles.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QScrollArea, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

from BaseMod.BaseModWidgets import TileSettingsViewport

class Ui_TileSettings(object):
    def setupUi(self, TileSettings):
        if not TileSettings.objectName():
            TileSettings.setObjectName(u"TileSettings")
        TileSettings.resize(572, 457)
        self.gridLayout = QGridLayout(TileSettings)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(TileSettings)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setEnabled(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 570, 455))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Pshow = QCheckBox(self.scrollAreaWidgetContents)
        self.Pshow.setObjectName(u"Pshow")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Pshow.sizePolicy().hasHeightForWidth())
        self.Pshow.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.Pshow)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Popr = QSlider(self.scrollAreaWidgetContents)
        self.Popr.setObjectName(u"Popr")
        self.Popr.setMaximum(255)
        self.Popr.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.Popr, 2, 1, 1, 1)

        self.Popn = QSlider(self.scrollAreaWidgetContents)
        self.Popn.setObjectName(u"Popn")
        self.Popn.setMaximum(255)
        self.Popn.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.Popn, 3, 1, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)

        self.Popr_2 = QSpinBox(self.scrollAreaWidgetContents)
        self.Popr_2.setObjectName(u"Popr_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Popr_2.sizePolicy().hasHeightForWidth())
        self.Popr_2.setSizePolicy(sizePolicy1)
        self.Popr_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Popr_2.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.Popr_2.setMaximum(255)

        self.gridLayout_2.addWidget(self.Popr_2, 2, 2, 1, 1)

        self.Popn_2 = QSpinBox(self.scrollAreaWidgetContents)
        self.Popn_2.setObjectName(u"Popn_2")
        sizePolicy1.setHeightForWidth(self.Popn_2.sizePolicy().hasHeightForWidth())
        self.Popn_2.setSizePolicy(sizePolicy1)
        self.Popn_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Popn_2.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.Popn_2.setMaximum(255)

        self.gridLayout_2.addWidget(self.Popn_2, 3, 2, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_2)

        self.Sshow = QCheckBox(self.scrollAreaWidgetContents)
        self.Sshow.setObjectName(u"Sshow")
        sizePolicy.setHeightForWidth(self.Sshow.sizePolicy().hasHeightForWidth())
        self.Sshow.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.Sshow)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Sopn = QSlider(self.scrollAreaWidgetContents)
        self.Sopn.setObjectName(u"Sopn")
        self.Sopn.setMaximum(255)
        self.Sopn.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_3.addWidget(self.Sopn, 1, 1, 1, 1)

        self.Sopr_2 = QSpinBox(self.scrollAreaWidgetContents)
        self.Sopr_2.setObjectName(u"Sopr_2")
        sizePolicy1.setHeightForWidth(self.Sopr_2.sizePolicy().hasHeightForWidth())
        self.Sopr_2.setSizePolicy(sizePolicy1)
        self.Sopr_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Sopr_2.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.Sopr_2.setMaximum(255)

        self.gridLayout_3.addWidget(self.Sopr_2, 0, 2, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)

        self.Sopn_2 = QSpinBox(self.scrollAreaWidgetContents)
        self.Sopn_2.setObjectName(u"Sopn_2")
        sizePolicy1.setHeightForWidth(self.Sopn_2.sizePolicy().hasHeightForWidth())
        self.Sopn_2.setSizePolicy(sizePolicy1)
        self.Sopn_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.Sopn_2.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.Sopn_2.setMaximum(255)

        self.gridLayout_3.addWidget(self.Sopn_2, 1, 2, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)

        self.Sopr = QSlider(self.scrollAreaWidgetContents)
        self.Sopr.setObjectName(u"Sopr")
        self.Sopr.setMaximum(255)
        self.Sopr.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_3.addWidget(self.Sopr, 0, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Rall = QCheckBox(self.scrollAreaWidgetContents)
        self.Rall.setObjectName(u"Rall")

        self.horizontalLayout_2.addWidget(self.Rall)

        self.MatBorder = QCheckBox(self.scrollAreaWidgetContents)
        self.MatBorder.setObjectName(u"MatBorder")

        self.horizontalLayout_2.addWidget(self.MatBorder)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_10)

        self.RenderOption = QComboBox(self.scrollAreaWidgetContents)
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.setObjectName(u"RenderOption")

        self.verticalLayout_3.addWidget(self.RenderOption)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.LayerSlider = QSlider(self.scrollAreaWidgetContents)
        self.LayerSlider.setObjectName(u"LayerSlider")
        self.LayerSlider.setMaximum(2)
        self.LayerSlider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_3.addWidget(self.LayerSlider)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.TilePreview = TileSettingsViewport(self.scrollAreaWidgetContents)
        self.TilePreview.setObjectName(u"TilePreview")

        self.horizontalLayout.addWidget(self.TilePreview)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.retranslateUi(TileSettings)

        QMetaObject.connectSlotsByName(TileSettings)
    # setupUi

    def retranslateUi(self, TileSettings):
        TileSettings.setWindowTitle(QCoreApplication.translate("TileSettings", u"Form", None))
        self.Pshow.setText(QCoreApplication.translate("TileSettings", u"Primary", None))
        self.label_2.setText(QCoreApplication.translate("TileSettings", u"Not Rendered", None))
        self.label.setText(QCoreApplication.translate("TileSettings", u"Rendered", None))
        self.Sshow.setText(QCoreApplication.translate("TileSettings", u"Secondary", None))
        self.label_3.setText(QCoreApplication.translate("TileSettings", u"Not Rendered", None))
        self.label_4.setText(QCoreApplication.translate("TileSettings", u"Rendered", None))
        self.Rall.setText(QCoreApplication.translate("TileSettings", u"Render All", None))
        self.MatBorder.setText(QCoreApplication.translate("TileSettings", u"Material Border", None))
        self.label_10.setText(QCoreApplication.translate("TileSettings", u"Preview", None))
        self.RenderOption.setItemText(0, QCoreApplication.translate("TileSettings", u"Classic", None))
        self.RenderOption.setItemText(1, QCoreApplication.translate("TileSettings", u"Tile image", None))
        self.RenderOption.setItemText(2, QCoreApplication.translate("TileSettings", u"Henry", None))
        self.RenderOption.setItemText(3, QCoreApplication.translate("TileSettings", u"Unrendered", None))
        self.RenderOption.setItemText(4, QCoreApplication.translate("TileSettings", u"Rendered (sun)", None))
        self.RenderOption.setItemText(5, QCoreApplication.translate("TileSettings", u"Rendered (shaded)", None))
        self.RenderOption.setItemText(6, QCoreApplication.translate("TileSettings", u"Rendered (rain)", None))

        self.label_5.setText(QCoreApplication.translate("TileSettings", u"Layer:", None))
    # retranslateUi

