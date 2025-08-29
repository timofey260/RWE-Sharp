# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'properties.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_Properties(object):
    def setupUi(self, Properties):
        if not Properties.objectName():
            Properties.setObjectName(u"Properties")
        Properties.resize(400, 727)
        self.verticalLayout = QVBoxLayout(Properties)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(Properties)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 384, 711))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_15 = QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_2.addWidget(self.label_15)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.ToolsPropertiesLabel = QLabel(self.scrollAreaWidgetContents)
        self.ToolsPropertiesLabel.setObjectName(u"ToolsPropertiesLabel")

        self.gridLayout_10.addWidget(self.ToolsPropertiesLabel, 2, 0, 1, 1)

        self.WidthCells = QSpinBox(self.scrollAreaWidgetContents)
        self.WidthCells.setObjectName(u"WidthCells")
        self.WidthCells.setMaximum(1000)

        self.gridLayout_10.addWidget(self.WidthCells, 3, 0, 1, 1)

        self.WidthCams = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.WidthCams.setObjectName(u"WidthCams")

        self.gridLayout_10.addWidget(self.WidthCams, 5, 0, 1, 1)

        self.HeightCams = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.HeightCams.setObjectName(u"HeightCams")

        self.gridLayout_10.addWidget(self.HeightCams, 5, 1, 1, 1)

        self.XOfs = QSpinBox(self.scrollAreaWidgetContents)
        self.XOfs.setObjectName(u"XOfs")
        self.XOfs.setMaximum(1000)

        self.gridLayout_10.addWidget(self.XOfs, 1, 0, 1, 1)

        self.ToolsPropertiesLabel_2 = QLabel(self.scrollAreaWidgetContents)
        self.ToolsPropertiesLabel_2.setObjectName(u"ToolsPropertiesLabel_2")

        self.gridLayout_10.addWidget(self.ToolsPropertiesLabel_2, 2, 1, 1, 1)

        self.YOfs = QSpinBox(self.scrollAreaWidgetContents)
        self.YOfs.setObjectName(u"YOfs")
        self.YOfs.setMaximum(1000)

        self.gridLayout_10.addWidget(self.YOfs, 1, 1, 1, 1)

        self.HeightCells = QSpinBox(self.scrollAreaWidgetContents)
        self.HeightCells.setObjectName(u"HeightCells")
        self.HeightCells.setMaximum(1000)

        self.gridLayout_10.addWidget(self.HeightCells, 3, 1, 1, 1)

        self.ToolsPropertiesLabel_10 = QLabel(self.scrollAreaWidgetContents)
        self.ToolsPropertiesLabel_10.setObjectName(u"ToolsPropertiesLabel_10")

        self.gridLayout_10.addWidget(self.ToolsPropertiesLabel_10, 4, 1, 1, 1)

        self.ToolsPropertiesLabel_8 = QLabel(self.scrollAreaWidgetContents)
        self.ToolsPropertiesLabel_8.setObjectName(u"ToolsPropertiesLabel_8")

        self.gridLayout_10.addWidget(self.ToolsPropertiesLabel_8, 4, 0, 1, 1)

        self.ToolsPropertiesLabel_3 = QLabel(self.scrollAreaWidgetContents)
        self.ToolsPropertiesLabel_3.setObjectName(u"ToolsPropertiesLabel_3")

        self.gridLayout_10.addWidget(self.ToolsPropertiesLabel_3, 0, 0, 1, 1)

        self.ToolsPropertiesLabel_4 = QLabel(self.scrollAreaWidgetContents)
        self.ToolsPropertiesLabel_4.setObjectName(u"ToolsPropertiesLabel_4")

        self.gridLayout_10.addWidget(self.ToolsPropertiesLabel_4, 0, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_10)

        self.AddCameras = QCheckBox(self.scrollAreaWidgetContents)
        self.AddCameras.setObjectName(u"AddCameras")

        self.verticalLayout_2.addWidget(self.AddCameras)

        self.Resize = QPushButton(self.scrollAreaWidgetContents)
        self.Resize.setObjectName(u"Resize")

        self.verticalLayout_2.addWidget(self.Resize)

        self.ToolsPropertiesLabel_11 = QLabel(self.scrollAreaWidgetContents)
        self.ToolsPropertiesLabel_11.setObjectName(u"ToolsPropertiesLabel_11")

        self.verticalLayout_2.addWidget(self.ToolsPropertiesLabel_11)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.BorderTop = QSpinBox(self.scrollAreaWidgetContents)
        self.BorderTop.setObjectName(u"BorderTop")
        self.BorderTop.setMaximum(1000)

        self.gridLayout.addWidget(self.BorderTop, 1, 1, 1, 1)

        self.BorderBottom = QSpinBox(self.scrollAreaWidgetContents)
        self.BorderBottom.setObjectName(u"BorderBottom")
        self.BorderBottom.setMaximum(1000)

        self.gridLayout.addWidget(self.BorderBottom, 3, 1, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.BorderRight = QSpinBox(self.scrollAreaWidgetContents)
        self.BorderRight.setObjectName(u"BorderRight")
        self.BorderRight.setMaximum(1000)

        self.gridLayout.addWidget(self.BorderRight, 3, 0, 1, 1)

        self.BorderLeft = QSpinBox(self.scrollAreaWidgetContents)
        self.BorderLeft.setObjectName(u"BorderLeft")
        self.BorderLeft.setMaximum(1000)

        self.gridLayout.addWidget(self.BorderLeft, 1, 0, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.ToolsPropertiesLabel_6 = QLabel(self.scrollAreaWidgetContents)
        self.ToolsPropertiesLabel_6.setObjectName(u"ToolsPropertiesLabel_6")

        self.verticalLayout_2.addWidget(self.ToolsPropertiesLabel_6)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.WaterState = QComboBox(self.scrollAreaWidgetContents)
        self.WaterState.addItem("")
        self.WaterState.addItem("")
        self.WaterState.addItem("")
        self.WaterState.setObjectName(u"WaterState")

        self.verticalLayout_3.addWidget(self.WaterState)

        self.ToolsPropertiesLabel_5 = QLabel(self.scrollAreaWidgetContents)
        self.ToolsPropertiesLabel_5.setObjectName(u"ToolsPropertiesLabel_5")

        self.verticalLayout_3.addWidget(self.ToolsPropertiesLabel_5)

        self.WaterHeight = QSpinBox(self.scrollAreaWidgetContents)
        self.WaterHeight.setObjectName(u"WaterHeight")
        self.WaterHeight.setEnabled(True)
        self.WaterHeight.setMinimum(-1)
        self.WaterHeight.setMaximum(1000)
        self.WaterHeight.setValue(-1)

        self.verticalLayout_3.addWidget(self.WaterHeight)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ToolsPropertiesLabel_9 = QLabel(self.scrollAreaWidgetContents)
        self.ToolsPropertiesLabel_9.setObjectName(u"ToolsPropertiesLabel_9")

        self.horizontalLayout.addWidget(self.ToolsPropertiesLabel_9)

        self.TileSeedSpin = QSpinBox(self.scrollAreaWidgetContents)
        self.TileSeedSpin.setObjectName(u"TileSeedSpin")
        self.TileSeedSpin.setMaximum(1000)

        self.horizontalLayout.addWidget(self.TileSeedSpin)

        self.TileSeedRandom = QPushButton(self.scrollAreaWidgetContents)
        self.TileSeedRandom.setObjectName(u"TileSeedRandom")

        self.horizontalLayout.addWidget(self.TileSeedRandom)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(Properties)

        QMetaObject.connectSlotsByName(Properties)
    # setupUi

    def retranslateUi(self, Properties):
        Properties.setWindowTitle(QCoreApplication.translate("Properties", u"Properties", None))
        self.label_15.setText(QCoreApplication.translate("Properties", u"Level size:", None))
        self.ToolsPropertiesLabel.setText(QCoreApplication.translate("Properties", u"Width(cells):", None))
        self.ToolsPropertiesLabel_2.setText(QCoreApplication.translate("Properties", u"Height(cells):", None))
        self.ToolsPropertiesLabel_10.setText(QCoreApplication.translate("Properties", u"Height(Cameras):", None))
        self.ToolsPropertiesLabel_8.setText(QCoreApplication.translate("Properties", u"Width(Cameras):", None))
        self.ToolsPropertiesLabel_3.setText(QCoreApplication.translate("Properties", u"X Offset:", None))
        self.ToolsPropertiesLabel_4.setText(QCoreApplication.translate("Properties", u"Y Offset:", None))
        self.AddCameras.setText(QCoreApplication.translate("Properties", u"Add Cameras", None))
        self.Resize.setText(QCoreApplication.translate("Properties", u"Resize", None))
        self.ToolsPropertiesLabel_11.setText(QCoreApplication.translate("Properties", u"Border Tiles:", None))
        self.label.setText(QCoreApplication.translate("Properties", u"Left:", None))
        self.label_2.setText(QCoreApplication.translate("Properties", u"Top:", None))
        self.label_3.setText(QCoreApplication.translate("Properties", u"Bottom:", None))
        self.label_4.setText(QCoreApplication.translate("Properties", u"Right:", None))
        self.ToolsPropertiesLabel_6.setText(QCoreApplication.translate("Properties", u"Water Properties:", None))
        self.WaterState.setItemText(0, QCoreApplication.translate("Properties", u"No water", None))
        self.WaterState.setItemText(1, QCoreApplication.translate("Properties", u"In front", None))
        self.WaterState.setItemText(2, QCoreApplication.translate("Properties", u"Behind", None))

        self.ToolsPropertiesLabel_5.setText(QCoreApplication.translate("Properties", u"Water height:", None))
        self.ToolsPropertiesLabel_9.setText(QCoreApplication.translate("Properties", u"Tile seed:", None))
        self.TileSeedRandom.setText(QCoreApplication.translate("Properties", u"Random", None))
    # retranslateUi

