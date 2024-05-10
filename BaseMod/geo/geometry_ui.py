# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'geometry.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Geo(object):
    def setupUi(self, Geo):
        if not Geo.objectName():
            Geo.setObjectName(u"Geo")
        Geo.resize(338, 551)
        self.verticalLayout_2 = QVBoxLayout(Geo)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(Geo)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 303, 782))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.ToolGeoaApply_to_Label = QLabel(self.scrollAreaWidgetContents)
        self.ToolGeoaApply_to_Label.setObjectName(u"ToolGeoaApply_to_Label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ToolGeoaApply_to_Label.sizePolicy().hasHeightForWidth())
        self.ToolGeoaApply_to_Label.setSizePolicy(sizePolicy1)
        self.ToolGeoaApply_to_Label.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.verticalLayout_7.addWidget(self.ToolGeoaApply_to_Label)

        self.ToolGeoApplyToL1 = QCheckBox(self.scrollAreaWidgetContents)
        self.ToolGeoApplyToL1.setObjectName(u"ToolGeoApplyToL1")
        self.ToolGeoApplyToL1.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.verticalLayout_7.addWidget(self.ToolGeoApplyToL1)

        self.ToolGeoApplyToL2 = QCheckBox(self.scrollAreaWidgetContents)
        self.ToolGeoApplyToL2.setObjectName(u"ToolGeoApplyToL2")
        self.ToolGeoApplyToL2.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.verticalLayout_7.addWidget(self.ToolGeoApplyToL2)

        self.ToolGeoApplyToL3 = QCheckBox(self.scrollAreaWidgetContents)
        self.ToolGeoApplyToL3.setObjectName(u"ToolGeoApplyToL3")
        self.ToolGeoApplyToL3.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.verticalLayout_7.addWidget(self.ToolGeoApplyToL3)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.ToolGeoM2Select = QComboBox(self.scrollAreaWidgetContents)
        self.ToolGeoM2Select.addItem("")
        self.ToolGeoM2Select.addItem("")
        self.ToolGeoM2Select.addItem("")
        self.ToolGeoM2Select.addItem("")
        self.ToolGeoM2Select.addItem("")
        self.ToolGeoM2Select.addItem("")
        self.ToolGeoM2Select.addItem("")
        self.ToolGeoM2Select.addItem("")
        self.ToolGeoM2Select.setObjectName(u"ToolGeoM2Select")
        sizePolicy.setHeightForWidth(self.ToolGeoM2Select.sizePolicy().hasHeightForWidth())
        self.ToolGeoM2Select.setSizePolicy(sizePolicy)

        self.gridLayout_8.addWidget(self.ToolGeoM2Select, 1, 1, 1, 1)

        self.ToolGeoM1Select = QComboBox(self.scrollAreaWidgetContents)
        self.ToolGeoM1Select.addItem("")
        self.ToolGeoM1Select.addItem("")
        self.ToolGeoM1Select.addItem("")
        self.ToolGeoM1Select.addItem("")
        self.ToolGeoM1Select.addItem("")
        self.ToolGeoM1Select.addItem("")
        self.ToolGeoM1Select.addItem("")
        self.ToolGeoM1Select.addItem("")
        self.ToolGeoM1Select.setObjectName(u"ToolGeoM1Select")
        sizePolicy.setHeightForWidth(self.ToolGeoM1Select.sizePolicy().hasHeightForWidth())
        self.ToolGeoM1Select.setSizePolicy(sizePolicy)

        self.gridLayout_8.addWidget(self.ToolGeoM1Select, 2, 1, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.gridLayout_8.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.gridLayout_8.addWidget(self.label_3, 2, 0, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 10))

        self.gridLayout_8.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_8)

        self.ToolMassEditFrame = QGroupBox(self.scrollAreaWidgetContents)
        self.ToolMassEditFrame.setObjectName(u"ToolMassEditFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.ToolMassEditFrame.sizePolicy().hasHeightForWidth())
        self.ToolMassEditFrame.setSizePolicy(sizePolicy2)
        self.ToolMassEditFrame.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_11 = QGridLayout(self.ToolMassEditFrame)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.geolayout = QVBoxLayout()
        self.geolayout.setObjectName(u"geolayout")
        self.label_Blocks = QLabel(self.ToolMassEditFrame)
        self.label_Blocks.setObjectName(u"label_Blocks")
        sizePolicy1.setHeightForWidth(self.label_Blocks.sizePolicy().hasHeightForWidth())
        self.label_Blocks.setSizePolicy(sizePolicy1)
        self.label_Blocks.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.geolayout.addWidget(self.label_Blocks)

        self.ToolGeoWall = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoWall.setObjectName(u"ToolGeoWall")
        sizePolicy.setHeightForWidth(self.ToolGeoWall.sizePolicy().hasHeightForWidth())
        self.ToolGeoWall.setSizePolicy(sizePolicy)
        self.ToolGeoWall.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.ToolGeoWall.setIconSize(QSize(16, 16))
        self.ToolGeoWall.setCheckable(False)

        self.geolayout.addWidget(self.ToolGeoWall)

        self.ToolGeoSlope = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoSlope.setObjectName(u"ToolGeoSlope")
        sizePolicy.setHeightForWidth(self.ToolGeoSlope.sizePolicy().hasHeightForWidth())
        self.ToolGeoSlope.setSizePolicy(sizePolicy)
        self.ToolGeoSlope.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.geolayout.addWidget(self.ToolGeoSlope)

        self.ToolGeoAir = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoAir.setObjectName(u"ToolGeoAir")
        sizePolicy.setHeightForWidth(self.ToolGeoAir.sizePolicy().hasHeightForWidth())
        self.ToolGeoAir.setSizePolicy(sizePolicy)
        self.ToolGeoAir.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.ToolGeoAir.setIconSize(QSize(32, 16))

        self.geolayout.addWidget(self.ToolGeoAir)

        self.ToolGeoBeam = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoBeam.setObjectName(u"ToolGeoBeam")
        sizePolicy.setHeightForWidth(self.ToolGeoBeam.sizePolicy().hasHeightForWidth())
        self.ToolGeoBeam.setSizePolicy(sizePolicy)
        self.ToolGeoBeam.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.geolayout.addWidget(self.ToolGeoBeam)

        self.ToolGeoFloor = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoFloor.setObjectName(u"ToolGeoFloor")
        sizePolicy.setHeightForWidth(self.ToolGeoFloor.sizePolicy().hasHeightForWidth())
        self.ToolGeoFloor.setSizePolicy(sizePolicy)
        self.ToolGeoFloor.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.ToolGeoFloor.setAutoRepeat(False)

        self.geolayout.addWidget(self.ToolGeoFloor)

        self.ToolGeoCrack = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoCrack.setObjectName(u"ToolGeoCrack")
        sizePolicy.setHeightForWidth(self.ToolGeoCrack.sizePolicy().hasHeightForWidth())
        self.ToolGeoCrack.setSizePolicy(sizePolicy)
        self.ToolGeoCrack.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.geolayout.addWidget(self.ToolGeoCrack)

        self.ToolGeoSpear = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoSpear.setObjectName(u"ToolGeoSpear")
        sizePolicy.setHeightForWidth(self.ToolGeoSpear.sizePolicy().hasHeightForWidth())
        self.ToolGeoSpear.setSizePolicy(sizePolicy)
        self.ToolGeoSpear.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.geolayout.addWidget(self.ToolGeoSpear)

        self.ToolGeoRock = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoRock.setObjectName(u"ToolGeoRock")
        sizePolicy.setHeightForWidth(self.ToolGeoRock.sizePolicy().hasHeightForWidth())
        self.ToolGeoRock.setSizePolicy(sizePolicy)
        self.ToolGeoRock.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.geolayout.addWidget(self.ToolGeoRock)

        self.ToolGeoGlass = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoGlass.setObjectName(u"ToolGeoGlass")
        sizePolicy.setHeightForWidth(self.ToolGeoGlass.sizePolicy().hasHeightForWidth())
        self.ToolGeoGlass.setSizePolicy(sizePolicy)
        self.ToolGeoGlass.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.geolayout.addWidget(self.ToolGeoGlass)

        self.ToolGeoHive = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoHive.setObjectName(u"ToolGeoHive")
        sizePolicy.setHeightForWidth(self.ToolGeoHive.sizePolicy().hasHeightForWidth())
        self.ToolGeoHive.setSizePolicy(sizePolicy)
        self.ToolGeoHive.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.geolayout.addWidget(self.ToolGeoHive)

        self.ToolGeoForbidChains = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoForbidChains.setObjectName(u"ToolGeoForbidChains")
        sizePolicy.setHeightForWidth(self.ToolGeoForbidChains.sizePolicy().hasHeightForWidth())
        self.ToolGeoForbidChains.setSizePolicy(sizePolicy)
        self.ToolGeoForbidChains.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.geolayout.addWidget(self.ToolGeoForbidChains)

        self.pushButton_8 = QPushButton(self.ToolMassEditFrame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setFlat(False)

        self.geolayout.addWidget(self.pushButton_8)


        self.gridLayout.addLayout(self.geolayout, 0, 0, 2, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ToolGeoLabelPipes = QLabel(self.ToolMassEditFrame)
        self.ToolGeoLabelPipes.setObjectName(u"ToolGeoLabelPipes")
        sizePolicy1.setHeightForWidth(self.ToolGeoLabelPipes.sizePolicy().hasHeightForWidth())
        self.ToolGeoLabelPipes.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.ToolGeoLabelPipes)

        self.ToolGeoShortcutEnterance = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoShortcutEnterance.setObjectName(u"ToolGeoShortcutEnterance")
        sizePolicy.setHeightForWidth(self.ToolGeoShortcutEnterance.sizePolicy().hasHeightForWidth())
        self.ToolGeoShortcutEnterance.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.ToolGeoShortcutEnterance)

        self.ToolGeoShortcut = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoShortcut.setObjectName(u"ToolGeoShortcut")
        sizePolicy.setHeightForWidth(self.ToolGeoShortcut.sizePolicy().hasHeightForWidth())
        self.ToolGeoShortcut.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.ToolGeoShortcut)

        self.ToolGeoDen = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoDen.setObjectName(u"ToolGeoDen")
        sizePolicy.setHeightForWidth(self.ToolGeoDen.sizePolicy().hasHeightForWidth())
        self.ToolGeoDen.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.ToolGeoDen)

        self.ToolGeoEnterance = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoEnterance.setObjectName(u"ToolGeoEnterance")
        sizePolicy.setHeightForWidth(self.ToolGeoEnterance.sizePolicy().hasHeightForWidth())
        self.ToolGeoEnterance.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.ToolGeoEnterance)

        self.ToolGeoWraykAMoleHole = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoWraykAMoleHole.setObjectName(u"ToolGeoWraykAMoleHole")
        sizePolicy.setHeightForWidth(self.ToolGeoWraykAMoleHole.sizePolicy().hasHeightForWidth())
        self.ToolGeoWraykAMoleHole.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.ToolGeoWraykAMoleHole)

        self.ToolGeoGarbageWorm = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoGarbageWorm.setObjectName(u"ToolGeoGarbageWorm")
        sizePolicy.setHeightForWidth(self.ToolGeoGarbageWorm.sizePolicy().hasHeightForWidth())
        self.ToolGeoGarbageWorm.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.ToolGeoGarbageWorm)

        self.ToolGeoScavHole = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoScavHole.setObjectName(u"ToolGeoScavHole")
        sizePolicy.setHeightForWidth(self.ToolGeoScavHole.sizePolicy().hasHeightForWidth())
        self.ToolGeoScavHole.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.ToolGeoScavHole)


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.deletelayout = QVBoxLayout()
        self.deletelayout.setObjectName(u"deletelayout")
        self.ToolGeoLabelDeltieTools = QLabel(self.ToolMassEditFrame)
        self.ToolGeoLabelDeltieTools.setObjectName(u"ToolGeoLabelDeltieTools")
        sizePolicy1.setHeightForWidth(self.ToolGeoLabelDeltieTools.sizePolicy().hasHeightForWidth())
        self.ToolGeoLabelDeltieTools.setSizePolicy(sizePolicy1)

        self.deletelayout.addWidget(self.ToolGeoLabelDeltieTools)

        self.ToolGeoClearUpperLayer = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoClearUpperLayer.setObjectName(u"ToolGeoClearUpperLayer")
        sizePolicy.setHeightForWidth(self.ToolGeoClearUpperLayer.sizePolicy().hasHeightForWidth())
        self.ToolGeoClearUpperLayer.setSizePolicy(sizePolicy)

        self.deletelayout.addWidget(self.ToolGeoClearUpperLayer)

        self.ToolGeoClearLayer = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoClearLayer.setObjectName(u"ToolGeoClearLayer")
        sizePolicy.setHeightForWidth(self.ToolGeoClearLayer.sizePolicy().hasHeightForWidth())
        self.ToolGeoClearLayer.setSizePolicy(sizePolicy)

        self.deletelayout.addWidget(self.ToolGeoClearLayer)

        self.ToolGeoClearAll = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoClearAll.setObjectName(u"ToolGeoClearAll")
        sizePolicy.setHeightForWidth(self.ToolGeoClearAll.sizePolicy().hasHeightForWidth())
        self.ToolGeoClearAll.setSizePolicy(sizePolicy)

        self.deletelayout.addWidget(self.ToolGeoClearAll)


        self.gridLayout.addLayout(self.deletelayout, 1, 1, 1, 1)

        self.masslayout = QVBoxLayout()
        self.masslayout.setObjectName(u"masslayout")
        self.ToolGeoLabel = QLabel(self.ToolMassEditFrame)
        self.ToolGeoLabel.setObjectName(u"ToolGeoLabel")
        sizePolicy1.setHeightForWidth(self.ToolGeoLabel.sizePolicy().hasHeightForWidth())
        self.ToolGeoLabel.setSizePolicy(sizePolicy1)
        self.ToolGeoLabel.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.masslayout.addWidget(self.ToolGeoLabel)

        self.ToolGeoCopy = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoCopy.setObjectName(u"ToolGeoCopy")
        sizePolicy.setHeightForWidth(self.ToolGeoCopy.sizePolicy().hasHeightForWidth())
        self.ToolGeoCopy.setSizePolicy(sizePolicy)
        self.ToolGeoCopy.setMinimumSize(QSize(0, 0))
        self.ToolGeoCopy.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.masslayout.addWidget(self.ToolGeoCopy)

        self.ToolGeoPaste = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoPaste.setObjectName(u"ToolGeoPaste")
        sizePolicy.setHeightForWidth(self.ToolGeoPaste.sizePolicy().hasHeightForWidth())
        self.ToolGeoPaste.setSizePolicy(sizePolicy)
        self.ToolGeoPaste.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.ToolGeoPaste.setIconSize(QSize(16, 16))
        self.ToolGeoPaste.setCheckable(False)

        self.masslayout.addWidget(self.ToolGeoPaste)

        self.ToolGeoMirror = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoMirror.setObjectName(u"ToolGeoMirror")
        sizePolicy.setHeightForWidth(self.ToolGeoMirror.sizePolicy().hasHeightForWidth())
        self.ToolGeoMirror.setSizePolicy(sizePolicy)
        self.ToolGeoMirror.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.masslayout.addWidget(self.ToolGeoMirror)

        self.ToolGeoInvert = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoInvert.setObjectName(u"ToolGeoInvert")
        sizePolicy.setHeightForWidth(self.ToolGeoInvert.sizePolicy().hasHeightForWidth())
        self.ToolGeoInvert.setSizePolicy(sizePolicy)
        self.ToolGeoInvert.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.masslayout.addWidget(self.ToolGeoInvert)

        self.ToolGeoMove = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoMove.setObjectName(u"ToolGeoMove")
        sizePolicy.setHeightForWidth(self.ToolGeoMove.sizePolicy().hasHeightForWidth())
        self.ToolGeoMove.setSizePolicy(sizePolicy)
        self.ToolGeoMove.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.ToolGeoMove.setAutoRepeat(False)

        self.masslayout.addWidget(self.ToolGeoMove)


        self.gridLayout.addLayout(self.masslayout, 2, 0, 1, 2)


        self.gridLayout_11.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.ToolMassEditFrame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.retranslateUi(Geo)

        QMetaObject.connectSlotsByName(Geo)
    # setupUi

    def retranslateUi(self, Geo):
        Geo.setWindowTitle(QCoreApplication.translate("Geo", u"Geo", None))
        self.ToolGeoaApply_to_Label.setText(QCoreApplication.translate("Geo", u"Apply to:", None))
        self.ToolGeoApplyToL1.setText(QCoreApplication.translate("Geo", u"Layer 1", None))
        self.ToolGeoApplyToL2.setText(QCoreApplication.translate("Geo", u"Layer 2", None))
        self.ToolGeoApplyToL3.setText(QCoreApplication.translate("Geo", u"Layer 3", None))
        self.ToolGeoM2Select.setItemText(0, QCoreApplication.translate("Geo", u"pencil", None))
        self.ToolGeoM2Select.setItemText(1, QCoreApplication.translate("Geo", u"brush", None))
        self.ToolGeoM2Select.setItemText(2, QCoreApplication.translate("Geo", u"bucket", None))
        self.ToolGeoM2Select.setItemText(3, QCoreApplication.translate("Geo", u"line", None))
        self.ToolGeoM2Select.setItemText(4, QCoreApplication.translate("Geo", u"rectangle tool", None))
        self.ToolGeoM2Select.setItemText(5, QCoreApplication.translate("Geo", u"hollow rectanlge", None))
        self.ToolGeoM2Select.setItemText(6, QCoreApplication.translate("Geo", u"circle", None))
        self.ToolGeoM2Select.setItemText(7, QCoreApplication.translate("Geo", u"hollow circle", None))

        self.ToolGeoM1Select.setItemText(0, QCoreApplication.translate("Geo", u"pencil", None))
        self.ToolGeoM1Select.setItemText(1, QCoreApplication.translate("Geo", u"brush", None))
        self.ToolGeoM1Select.setItemText(2, QCoreApplication.translate("Geo", u"bucket", None))
        self.ToolGeoM1Select.setItemText(3, QCoreApplication.translate("Geo", u"line", None))
        self.ToolGeoM1Select.setItemText(4, QCoreApplication.translate("Geo", u"rectangle tool", None))
        self.ToolGeoM1Select.setItemText(5, QCoreApplication.translate("Geo", u"hollow rectanlge", None))
        self.ToolGeoM1Select.setItemText(6, QCoreApplication.translate("Geo", u"circle", None))
        self.ToolGeoM1Select.setItemText(7, QCoreApplication.translate("Geo", u"hollow circle", None))

        self.label_2.setText(QCoreApplication.translate("Geo", u"Right mouse:", None))
        self.label_3.setText(QCoreApplication.translate("Geo", u"Left mouse:", None))
        self.label.setText(QCoreApplication.translate("Geo", u"Mouse mode:", None))
        self.label_Blocks.setText(QCoreApplication.translate("Geo", u"Geomentry", None))
        self.ToolGeoWall.setText(QCoreApplication.translate("Geo", u"Wall", None))
        self.ToolGeoSlope.setText(QCoreApplication.translate("Geo", u"Slope", None))
        self.ToolGeoAir.setText(QCoreApplication.translate("Geo", u"Air", None))
        self.ToolGeoBeam.setText(QCoreApplication.translate("Geo", u"Beam", None))
        self.ToolGeoFloor.setText(QCoreApplication.translate("Geo", u"Floor", None))
        self.ToolGeoCrack.setText(QCoreApplication.translate("Geo", u"Crack", None))
        self.ToolGeoSpear.setText(QCoreApplication.translate("Geo", u"Spear", None))
        self.ToolGeoRock.setText(QCoreApplication.translate("Geo", u"Rock", None))
        self.ToolGeoGlass.setText(QCoreApplication.translate("Geo", u"Glass", None))
        self.ToolGeoHive.setText(QCoreApplication.translate("Geo", u"Fly hive", None))
        self.ToolGeoForbidChains.setText(QCoreApplication.translate("Geo", u"Forbid Fly\n"
"Chains", None))
        self.pushButton_8.setText(QCoreApplication.translate("Geo", u"Worm grass", None))
        self.ToolGeoLabelPipes.setText(QCoreApplication.translate("Geo", u"Pipes", None))
        self.ToolGeoShortcutEnterance.setText(QCoreApplication.translate("Geo", u"Shortcut Enterance", None))
        self.ToolGeoShortcut.setText(QCoreApplication.translate("Geo", u"Shortcut", None))
        self.ToolGeoDen.setText(QCoreApplication.translate("Geo", u"Den", None))
        self.ToolGeoEnterance.setText(QCoreApplication.translate("Geo", u"Enterance", None))
        self.ToolGeoWraykAMoleHole.setText(QCoreApplication.translate("Geo", u"Wrayk a mole hole", None))
        self.ToolGeoGarbageWorm.setText(QCoreApplication.translate("Geo", u"Garbage wrom den", None))
        self.ToolGeoScavHole.setText(QCoreApplication.translate("Geo", u"Scavanger Hole", None))
        self.ToolGeoLabelDeltieTools.setText(QCoreApplication.translate("Geo", u"Delete tools", None))
        self.ToolGeoClearUpperLayer.setText(QCoreApplication.translate("Geo", u"Clear upper layer", None))
        self.ToolGeoClearLayer.setText(QCoreApplication.translate("Geo", u"Clear layer", None))
        self.ToolGeoClearAll.setText(QCoreApplication.translate("Geo", u"Clear all", None))
        self.ToolGeoLabel.setText(QCoreApplication.translate("Geo", u"mass edit", None))
#if QT_CONFIG(tooltip)
        self.ToolGeoCopy.setToolTip(QCoreApplication.translate("Geo", u"<html><head/><body><p>copy</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ToolGeoCopy.setText(QCoreApplication.translate("Geo", u"Copy tool", None))
        self.ToolGeoPaste.setText(QCoreApplication.translate("Geo", u"Paste", None))
        self.ToolGeoMirror.setText(QCoreApplication.translate("Geo", u"Mirror", None))
        self.ToolGeoInvert.setText(QCoreApplication.translate("Geo", u"Invert", None))
        self.ToolGeoMove.setText(QCoreApplication.translate("Geo", u"Move", None))
    # retranslateUi

