# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'geometryVSciJI.ui'
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
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)


class Ui_Geo(object):
    def setupUi(self, Geo):
        if not Geo.objectName():
            Geo.setObjectName(u"Geo")
        Geo.resize(477, 804)
        Geo.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(Geo)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(Geo)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 460, 862))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(9, -1, -1, -1)
        self.ToolGeoaApply_to_Label = QLabel(self.scrollAreaWidgetContents)
        self.ToolGeoaApply_to_Label.setObjectName(u"ToolGeoaApply_to_Label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ToolGeoaApply_to_Label.sizePolicy().hasHeightForWidth())
        self.ToolGeoaApply_to_Label.setSizePolicy(sizePolicy1)
        self.ToolGeoaApply_to_Label.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.verticalLayout_7.addWidget(self.ToolGeoaApply_to_Label)

        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.ToolGeoApplyToL1 = QCheckBox(self.frame)
        self.ToolGeoApplyToL1.setObjectName(u"ToolGeoApplyToL1")
        self.ToolGeoApplyToL1.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.verticalLayout_4.addWidget(self.ToolGeoApplyToL1)

        self.ToolGeoApplyToL2 = QCheckBox(self.frame)
        self.ToolGeoApplyToL2.setObjectName(u"ToolGeoApplyToL2")
        self.ToolGeoApplyToL2.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.verticalLayout_4.addWidget(self.ToolGeoApplyToL2)

        self.ToolGeoApplyToL3 = QCheckBox(self.frame)
        self.ToolGeoApplyToL3.setObjectName(u"ToolGeoApplyToL3")
        self.ToolGeoApplyToL3.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.verticalLayout_4.addWidget(self.ToolGeoApplyToL3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.NextLayer = QPushButton(self.frame)
        self.NextLayer.setObjectName(u"NextLayer")

        self.horizontalLayout_2.addWidget(self.NextLayer)

        self.PreviousLayer = QPushButton(self.frame)
        self.PreviousLayer.setObjectName(u"PreviousLayer")

        self.horizontalLayout_2.addWidget(self.PreviousLayer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout_7.addWidget(self.frame)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 10))

        self.verticalLayout_7.addWidget(self.label)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_7.addWidget(self.label_4)

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
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ToolGeoLabelPipes = QLabel(self.ToolMassEditFrame)
        self.ToolGeoLabelPipes.setObjectName(u"ToolGeoLabelPipes")
        sizePolicy1.setHeightForWidth(self.ToolGeoLabelPipes.sizePolicy().hasHeightForWidth())
        self.ToolGeoLabelPipes.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.ToolGeoLabelPipes)

        self.ToolGeoShortcutEntrance = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoShortcutEntrance.setObjectName(u"ToolGeoShortcutEntrance")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ToolGeoShortcutEntrance.sizePolicy().hasHeightForWidth())
        self.ToolGeoShortcutEntrance.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.ToolGeoShortcutEntrance)

        self.ToolGeoShortcut = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoShortcut.setObjectName(u"ToolGeoShortcut")
        sizePolicy3.setHeightForWidth(self.ToolGeoShortcut.sizePolicy().hasHeightForWidth())
        self.ToolGeoShortcut.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.ToolGeoShortcut)

        self.ToolGeoDen = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoDen.setObjectName(u"ToolGeoDen")
        sizePolicy3.setHeightForWidth(self.ToolGeoDen.sizePolicy().hasHeightForWidth())
        self.ToolGeoDen.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.ToolGeoDen)

        self.ToolGeoEntrance = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoEntrance.setObjectName(u"ToolGeoEntrance")
        sizePolicy3.setHeightForWidth(self.ToolGeoEntrance.sizePolicy().hasHeightForWidth())
        self.ToolGeoEntrance.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.ToolGeoEntrance)

        self.ToolGeoWraykAMoleHole = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoWraykAMoleHole.setObjectName(u"ToolGeoWraykAMoleHole")
        sizePolicy3.setHeightForWidth(self.ToolGeoWraykAMoleHole.sizePolicy().hasHeightForWidth())
        self.ToolGeoWraykAMoleHole.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.ToolGeoWraykAMoleHole)

        self.ToolGeoGarbageWorm = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoGarbageWorm.setObjectName(u"ToolGeoGarbageWorm")
        sizePolicy3.setHeightForWidth(self.ToolGeoGarbageWorm.sizePolicy().hasHeightForWidth())
        self.ToolGeoGarbageWorm.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.ToolGeoGarbageWorm)

        self.ToolGeoScavHole = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoScavHole.setObjectName(u"ToolGeoScavHole")
        sizePolicy3.setHeightForWidth(self.ToolGeoScavHole.sizePolicy().hasHeightForWidth())
        self.ToolGeoScavHole.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.ToolGeoScavHole)


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

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
        sizePolicy3.setHeightForWidth(self.ToolGeoWall.sizePolicy().hasHeightForWidth())
        self.ToolGeoWall.setSizePolicy(sizePolicy3)
        self.ToolGeoWall.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.ToolGeoWall.setIconSize(QSize(16, 16))
        self.ToolGeoWall.setCheckable(False)

        self.geolayout.addWidget(self.ToolGeoWall)

        self.ToolGeoAir = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoAir.setObjectName(u"ToolGeoAir")
        sizePolicy3.setHeightForWidth(self.ToolGeoAir.sizePolicy().hasHeightForWidth())
        self.ToolGeoAir.setSizePolicy(sizePolicy3)
        self.ToolGeoAir.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.ToolGeoAir.setIconSize(QSize(32, 16))

        self.geolayout.addWidget(self.ToolGeoAir)

        self.ToolGeoSlope = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoSlope.setObjectName(u"ToolGeoSlope")
        sizePolicy3.setHeightForWidth(self.ToolGeoSlope.sizePolicy().hasHeightForWidth())
        self.ToolGeoSlope.setSizePolicy(sizePolicy3)
        self.ToolGeoSlope.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.geolayout.addWidget(self.ToolGeoSlope)

        self.ToolGeoGlass = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoGlass.setObjectName(u"ToolGeoGlass")
        sizePolicy3.setHeightForWidth(self.ToolGeoGlass.sizePolicy().hasHeightForWidth())
        self.ToolGeoGlass.setSizePolicy(sizePolicy3)
        self.ToolGeoGlass.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.geolayout.addWidget(self.ToolGeoGlass)

        self.ToolGeoFloor = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoFloor.setObjectName(u"ToolGeoFloor")
        sizePolicy3.setHeightForWidth(self.ToolGeoFloor.sizePolicy().hasHeightForWidth())
        self.ToolGeoFloor.setSizePolicy(sizePolicy3)
        self.ToolGeoFloor.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.ToolGeoFloor.setAutoRepeat(False)

        self.geolayout.addWidget(self.ToolGeoFloor)

        self.ToolGeoLabelDeltieTools = QLabel(self.ToolMassEditFrame)
        self.ToolGeoLabelDeltieTools.setObjectName(u"ToolGeoLabelDeltieTools")
        sizePolicy1.setHeightForWidth(self.ToolGeoLabelDeltieTools.sizePolicy().hasHeightForWidth())
        self.ToolGeoLabelDeltieTools.setSizePolicy(sizePolicy1)

        self.geolayout.addWidget(self.ToolGeoLabelDeltieTools)

        self.ToolGeoClearAll = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoClearAll.setObjectName(u"ToolGeoClearAll")
        sizePolicy3.setHeightForWidth(self.ToolGeoClearAll.sizePolicy().hasHeightForWidth())
        self.ToolGeoClearAll.setSizePolicy(sizePolicy3)

        self.geolayout.addWidget(self.ToolGeoClearAll)

        self.ToolGeoClearStackabls = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoClearStackabls.setObjectName(u"ToolGeoClearStackabls")
        sizePolicy3.setHeightForWidth(self.ToolGeoClearStackabls.sizePolicy().hasHeightForWidth())
        self.ToolGeoClearStackabls.setSizePolicy(sizePolicy3)

        self.geolayout.addWidget(self.ToolGeoClearStackabls)

        self.ToolGeoClearBlocks = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoClearBlocks.setObjectName(u"ToolGeoClearBlocks")
        sizePolicy3.setHeightForWidth(self.ToolGeoClearBlocks.sizePolicy().hasHeightForWidth())
        self.ToolGeoClearBlocks.setSizePolicy(sizePolicy3)

        self.geolayout.addWidget(self.ToolGeoClearBlocks)

        self.ToolGeoClearLayer = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoClearLayer.setObjectName(u"ToolGeoClearLayer")
        sizePolicy3.setHeightForWidth(self.ToolGeoClearLayer.sizePolicy().hasHeightForWidth())
        self.ToolGeoClearLayer.setSizePolicy(sizePolicy3)

        self.geolayout.addWidget(self.ToolGeoClearLayer)

        self.ToolGeoLabel = QLabel(self.ToolMassEditFrame)
        self.ToolGeoLabel.setObjectName(u"ToolGeoLabel")
        sizePolicy1.setHeightForWidth(self.ToolGeoLabel.sizePolicy().hasHeightForWidth())
        self.ToolGeoLabel.setSizePolicy(sizePolicy1)
        self.ToolGeoLabel.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.geolayout.addWidget(self.ToolGeoLabel)

        self.ToolGeoPaste = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoPaste.setObjectName(u"ToolGeoPaste")
        sizePolicy3.setHeightForWidth(self.ToolGeoPaste.sizePolicy().hasHeightForWidth())
        self.ToolGeoPaste.setSizePolicy(sizePolicy3)
        self.ToolGeoPaste.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.ToolGeoPaste.setIconSize(QSize(16, 16))
        self.ToolGeoPaste.setCheckable(False)

        self.geolayout.addWidget(self.ToolGeoPaste)

        self.ToolGeoCopy = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoCopy.setObjectName(u"ToolGeoCopy")
        sizePolicy3.setHeightForWidth(self.ToolGeoCopy.sizePolicy().hasHeightForWidth())
        self.ToolGeoCopy.setSizePolicy(sizePolicy3)
        self.ToolGeoCopy.setMinimumSize(QSize(0, 0))
        self.ToolGeoCopy.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.geolayout.addWidget(self.ToolGeoCopy)

        self.ToolGeoMove = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoMove.setObjectName(u"ToolGeoMove")
        sizePolicy3.setHeightForWidth(self.ToolGeoMove.sizePolicy().hasHeightForWidth())
        self.ToolGeoMove.setSizePolicy(sizePolicy3)
        self.ToolGeoMove.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.ToolGeoMove.setAutoRepeat(False)

        self.geolayout.addWidget(self.ToolGeoMove)

        self.ToolGeoMirror = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoMirror.setObjectName(u"ToolGeoMirror")
        sizePolicy3.setHeightForWidth(self.ToolGeoMirror.sizePolicy().hasHeightForWidth())
        self.ToolGeoMirror.setSizePolicy(sizePolicy3)
        self.ToolGeoMirror.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.geolayout.addWidget(self.ToolGeoMirror)

        self.ToolGeoInvert = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoInvert.setObjectName(u"ToolGeoInvert")
        sizePolicy3.setHeightForWidth(self.ToolGeoInvert.sizePolicy().hasHeightForWidth())
        self.ToolGeoInvert.setSizePolicy(sizePolicy3)
        self.ToolGeoInvert.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.geolayout.addWidget(self.ToolGeoInvert)


        self.gridLayout.addLayout(self.geolayout, 0, 0, 2, 1)

        self.deletelayout = QVBoxLayout()
        self.deletelayout.setObjectName(u"deletelayout")
        self.label_Blocks_2 = QLabel(self.ToolMassEditFrame)
        self.label_Blocks_2.setObjectName(u"label_Blocks_2")
        sizePolicy1.setHeightForWidth(self.label_Blocks_2.sizePolicy().hasHeightForWidth())
        self.label_Blocks_2.setSizePolicy(sizePolicy1)
        self.label_Blocks_2.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.deletelayout.addWidget(self.label_Blocks_2)

        self.ToolGeoCrack = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoCrack.setObjectName(u"ToolGeoCrack")
        sizePolicy3.setHeightForWidth(self.ToolGeoCrack.sizePolicy().hasHeightForWidth())
        self.ToolGeoCrack.setSizePolicy(sizePolicy3)
        self.ToolGeoCrack.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.deletelayout.addWidget(self.ToolGeoCrack)

        self.ToolGeoWormGrass = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoWormGrass.setObjectName(u"ToolGeoWormGrass")
        sizePolicy3.setHeightForWidth(self.ToolGeoWormGrass.sizePolicy().hasHeightForWidth())
        self.ToolGeoWormGrass.setSizePolicy(sizePolicy3)
        self.ToolGeoWormGrass.setFlat(False)

        self.deletelayout.addWidget(self.ToolGeoWormGrass)

        self.ToolGeoForbidChains = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoForbidChains.setObjectName(u"ToolGeoForbidChains")
        sizePolicy3.setHeightForWidth(self.ToolGeoForbidChains.sizePolicy().hasHeightForWidth())
        self.ToolGeoForbidChains.setSizePolicy(sizePolicy3)
        self.ToolGeoForbidChains.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.deletelayout.addWidget(self.ToolGeoForbidChains)

        self.ToolGeoSpear = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoSpear.setObjectName(u"ToolGeoSpear")
        sizePolicy3.setHeightForWidth(self.ToolGeoSpear.sizePolicy().hasHeightForWidth())
        self.ToolGeoSpear.setSizePolicy(sizePolicy3)
        self.ToolGeoSpear.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.deletelayout.addWidget(self.ToolGeoSpear)

        self.ToolGeoRock = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoRock.setObjectName(u"ToolGeoRock")
        sizePolicy3.setHeightForWidth(self.ToolGeoRock.sizePolicy().hasHeightForWidth())
        self.ToolGeoRock.setSizePolicy(sizePolicy3)
        self.ToolGeoRock.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.deletelayout.addWidget(self.ToolGeoRock)

        self.ToolGeoHive = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoHive.setObjectName(u"ToolGeoHive")
        sizePolicy3.setHeightForWidth(self.ToolGeoHive.sizePolicy().hasHeightForWidth())
        self.ToolGeoHive.setSizePolicy(sizePolicy3)
        self.ToolGeoHive.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.deletelayout.addWidget(self.ToolGeoHive)

        self.ToolGeoBeam = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoBeam.setObjectName(u"ToolGeoBeam")
        sizePolicy3.setHeightForWidth(self.ToolGeoBeam.sizePolicy().hasHeightForWidth())
        self.ToolGeoBeam.setSizePolicy(sizePolicy3)
        self.ToolGeoBeam.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.deletelayout.addWidget(self.ToolGeoBeam)

        self.ToolGeoWaterfall = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoWaterfall.setObjectName(u"ToolGeoWaterfall")
        sizePolicy3.setHeightForWidth(self.ToolGeoWaterfall.sizePolicy().hasHeightForWidth())
        self.ToolGeoWaterfall.setSizePolicy(sizePolicy3)
        self.ToolGeoWaterfall.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.deletelayout.addWidget(self.ToolGeoWaterfall)


        self.gridLayout.addLayout(self.deletelayout, 1, 1, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout, 4, 0, 1, 1)

        self.frame_2 = QFrame(self.ToolMassEditFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.ToolGeoM1Select = QComboBox(self.frame_2)
        icon = QIcon()
        icon.addFile(u":/geoIcons/geo/pen.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ToolGeoM1Select.addItem(icon, "")
        icon1 = QIcon()
        icon1.addFile(u":/geoIcons/geo/brush.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ToolGeoM1Select.addItem(icon1, "")
        icon2 = QIcon()
        icon2.addFile(u":/geoIcons/geo/bucket.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ToolGeoM1Select.addItem(icon2, "")
        icon3 = QIcon()
        icon3.addFile(u":/geoIcons/geo/line.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ToolGeoM1Select.addItem(icon3, "")
        icon4 = QIcon()
        icon4.addFile(u":/geoIcons/geo/rect.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ToolGeoM1Select.addItem(icon4, "")
        icon5 = QIcon()
        icon5.addFile(u":/geoIcons/geo/rect_hollow.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ToolGeoM1Select.addItem(icon5, "")
        icon6 = QIcon()
        icon6.addFile(u":/geoIcons/geo/circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ToolGeoM1Select.addItem(icon6, "")
        icon7 = QIcon()
        icon7.addFile(u":/geoIcons/geo/circle_hollow.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ToolGeoM1Select.addItem(icon7, "")
        self.ToolGeoM1Select.setObjectName(u"ToolGeoM1Select")
        sizePolicy3.setHeightForWidth(self.ToolGeoM1Select.sizePolicy().hasHeightForWidth())
        self.ToolGeoM1Select.setSizePolicy(sizePolicy3)

        self.gridLayout_8.addWidget(self.ToolGeoM1Select, 1, 1, 1, 1)

        self.ToolGeoM2Select = QComboBox(self.frame_2)
        self.ToolGeoM2Select.addItem(icon, "")
        self.ToolGeoM2Select.addItem(icon1, "")
        self.ToolGeoM2Select.addItem(icon2, "")
        self.ToolGeoM2Select.addItem(icon3, "")
        self.ToolGeoM2Select.addItem(icon4, "")
        self.ToolGeoM2Select.addItem(icon5, "")
        self.ToolGeoM2Select.addItem(icon6, "")
        self.ToolGeoM2Select.addItem(icon7, "")
        self.ToolGeoM2Select.setObjectName(u"ToolGeoM2Select")
        sizePolicy3.setHeightForWidth(self.ToolGeoM2Select.sizePolicy().hasHeightForWidth())
        self.ToolGeoM2Select.setSizePolicy(sizePolicy3)

        self.gridLayout_8.addWidget(self.ToolGeoM2Select, 2, 1, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)

        self.gridLayout_8.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)

        self.gridLayout_8.addWidget(self.label_2, 2, 0, 1, 1)

        self.Brushsize = QSpinBox(self.frame_2)
        self.Brushsize.setObjectName(u"Brushsize")
        self.Brushsize.setMinimum(1)

        self.gridLayout_8.addWidget(self.Brushsize, 3, 1, 1, 1)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_8.addWidget(self.label_5, 3, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_8)


        self.gridLayout_11.addWidget(self.frame_2, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.RotateLeft = QPushButton(self.ToolMassEditFrame)
        self.RotateLeft.setObjectName(u"RotateLeft")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.RotateLeft.sizePolicy().hasHeightForWidth())
        self.RotateLeft.setSizePolicy(sizePolicy4)
        icon8 = QIcon()
        icon8.addFile(u":/special/special/rotatel.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.RotateLeft.setIcon(icon8)

        self.gridLayout_2.addWidget(self.RotateLeft, 0, 3, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.BrushSizeUp = QPushButton(self.ToolMassEditFrame)
        self.BrushSizeUp.setObjectName(u"BrushSizeUp")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.BrushSizeUp.sizePolicy().hasHeightForWidth())
        self.BrushSizeUp.setSizePolicy(sizePolicy5)
        self.BrushSizeUp.setBaseSize(QSize(16, 16))

        self.gridLayout_3.addWidget(self.BrushSizeUp, 0, 0, 1, 1)

        self.BrushSizeDown = QPushButton(self.ToolMassEditFrame)
        self.BrushSizeDown.setObjectName(u"BrushSizeDown")
        sizePolicy5.setHeightForWidth(self.BrushSizeDown.sizePolicy().hasHeightForWidth())
        self.BrushSizeDown.setSizePolicy(sizePolicy5)
        self.BrushSizeDown.setBaseSize(QSize(16, 16))

        self.gridLayout_3.addWidget(self.BrushSizeDown, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 5, 1, 1)

        self.RotateRight = QPushButton(self.ToolMassEditFrame)
        self.RotateRight.setObjectName(u"RotateRight")
        sizePolicy5.setHeightForWidth(self.RotateRight.sizePolicy().hasHeightForWidth())
        self.RotateRight.setSizePolicy(sizePolicy5)
        icon9 = QIcon()
        icon9.addFile(u":/special/special/rotater.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.RotateRight.setIcon(icon9)

        self.gridLayout_2.addWidget(self.RotateRight, 0, 4, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_2, 1, 0, 1, 1)


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
        self.NextLayer.setText(QCoreApplication.translate("Geo", u"Next", None))
        self.PreviousLayer.setText(QCoreApplication.translate("Geo", u"Previous", None))
        self.label.setText(QCoreApplication.translate("Geo", u"Place:", None))
        self.label_4.setText(QCoreApplication.translate("Geo", u"Blocks:", None))
        self.ToolGeoLabelPipes.setText(QCoreApplication.translate("Geo", u"Pipes", None))
        self.ToolGeoShortcutEntrance.setText(QCoreApplication.translate("Geo", u"Sh. Entrance", None))
        self.ToolGeoShortcut.setText(QCoreApplication.translate("Geo", u"Shortcut Path", None))
        self.ToolGeoDen.setText(QCoreApplication.translate("Geo", u"Dragon Den", None))
        self.ToolGeoEntrance.setText(QCoreApplication.translate("Geo", u"Room Entrance", None))
#if QT_CONFIG(tooltip)
        self.ToolGeoWraykAMoleHole.setToolTip(QCoreApplication.translate("Geo", u"Whack a mole hole", None))
#endif // QT_CONFIG(tooltip)
        self.ToolGeoWraykAMoleHole.setText(QCoreApplication.translate("Geo", u"Wrayk a mole", None))
#if QT_CONFIG(tooltip)
        self.ToolGeoGarbageWorm.setToolTip(QCoreApplication.translate("Geo", u"Garbage worm den", None))
#endif // QT_CONFIG(tooltip)
        self.ToolGeoGarbageWorm.setText(QCoreApplication.translate("Geo", u"Wrom den", None))
        self.ToolGeoScavHole.setText(QCoreApplication.translate("Geo", u"Scav Hole", None))
        self.label_Blocks.setText(QCoreApplication.translate("Geo", u"Geomentry", None))
        self.ToolGeoWall.setText(QCoreApplication.translate("Geo", u"Wall", None))
        self.ToolGeoAir.setText(QCoreApplication.translate("Geo", u"Air", None))
        self.ToolGeoSlope.setText(QCoreApplication.translate("Geo", u"Slope", None))
        self.ToolGeoGlass.setText(QCoreApplication.translate("Geo", u"Glass", None))
        self.ToolGeoFloor.setText(QCoreApplication.translate("Geo", u"Floor", None))
        self.ToolGeoLabelDeltieTools.setText(QCoreApplication.translate("Geo", u"Delete tools", None))
        self.ToolGeoClearAll.setText(QCoreApplication.translate("Geo", u"Clear all", None))
        self.ToolGeoClearStackabls.setText(QCoreApplication.translate("Geo", u"Clear Stackables", None))
        self.ToolGeoClearBlocks.setText(QCoreApplication.translate("Geo", u"Clear Blocks", None))
        self.ToolGeoClearLayer.setText(QCoreApplication.translate("Geo", u"Clear Layer", None))
        self.ToolGeoLabel.setText(QCoreApplication.translate("Geo", u"Mass edit", None))
        self.ToolGeoPaste.setText(QCoreApplication.translate("Geo", u"Paste", None))
#if QT_CONFIG(tooltip)
        self.ToolGeoCopy.setToolTip(QCoreApplication.translate("Geo", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ToolGeoCopy.setText(QCoreApplication.translate("Geo", u"Copy", None))
        self.ToolGeoMove.setText(QCoreApplication.translate("Geo", u"Move", None))
        self.ToolGeoMirror.setText(QCoreApplication.translate("Geo", u"Mirror", None))
        self.ToolGeoInvert.setText(QCoreApplication.translate("Geo", u"Invert", None))
        self.label_Blocks_2.setText(QCoreApplication.translate("Geo", u"Stackables", None))
        self.ToolGeoCrack.setText(QCoreApplication.translate("Geo", u"Crack", None))
        self.ToolGeoWormGrass.setText(QCoreApplication.translate("Geo", u"Worm grass", None))
#if QT_CONFIG(tooltip)
        self.ToolGeoForbidChains.setToolTip(QCoreApplication.translate("Geo", u"Forbid fly chains", None))
#endif // QT_CONFIG(tooltip)
        self.ToolGeoForbidChains.setText(QCoreApplication.translate("Geo", u"Forbid Chains", None))
        self.ToolGeoSpear.setText(QCoreApplication.translate("Geo", u"Spear", None))
        self.ToolGeoRock.setText(QCoreApplication.translate("Geo", u"Rock", None))
        self.ToolGeoHive.setText(QCoreApplication.translate("Geo", u"Fly hive", None))
        self.ToolGeoBeam.setText(QCoreApplication.translate("Geo", u"Beam", None))
        self.ToolGeoWaterfall.setText(QCoreApplication.translate("Geo", u"Waterfall", None))
        self.ToolGeoM1Select.setItemText(0, QCoreApplication.translate("Geo", u"Pencil", None))
        self.ToolGeoM1Select.setItemText(1, QCoreApplication.translate("Geo", u"Brush", None))
        self.ToolGeoM1Select.setItemText(2, QCoreApplication.translate("Geo", u"Bucket", None))
        self.ToolGeoM1Select.setItemText(3, QCoreApplication.translate("Geo", u"Line", None))
        self.ToolGeoM1Select.setItemText(4, QCoreApplication.translate("Geo", u"Rectangle", None))
        self.ToolGeoM1Select.setItemText(5, QCoreApplication.translate("Geo", u"Hollow Rectanlge", None))
        self.ToolGeoM1Select.setItemText(6, QCoreApplication.translate("Geo", u"Circle", None))
        self.ToolGeoM1Select.setItemText(7, QCoreApplication.translate("Geo", u"Hollow Circle", None))

        self.ToolGeoM2Select.setItemText(0, QCoreApplication.translate("Geo", u"Pencil", None))
        self.ToolGeoM2Select.setItemText(1, QCoreApplication.translate("Geo", u"Brush", None))
        self.ToolGeoM2Select.setItemText(2, QCoreApplication.translate("Geo", u"Bucket", None))
        self.ToolGeoM2Select.setItemText(3, QCoreApplication.translate("Geo", u"Line", None))
        self.ToolGeoM2Select.setItemText(4, QCoreApplication.translate("Geo", u"Rectangle", None))
        self.ToolGeoM2Select.setItemText(5, QCoreApplication.translate("Geo", u"Hollow Rectanlge", None))
        self.ToolGeoM2Select.setItemText(6, QCoreApplication.translate("Geo", u"Circle", None))
        self.ToolGeoM2Select.setItemText(7, QCoreApplication.translate("Geo", u"Hollow Circle", None))

        self.label_3.setText(QCoreApplication.translate("Geo", u"Left Mouse:", None))
        self.label_2.setText(QCoreApplication.translate("Geo", u"Right Mouse:", None))
        self.label_5.setText(QCoreApplication.translate("Geo", u"Brush Size:", None))
        self.RotateLeft.setText("")
        self.BrushSizeUp.setText(QCoreApplication.translate("Geo", u"+", None))
        self.BrushSizeDown.setText(QCoreApplication.translate("Geo", u"-", None))
        self.RotateRight.setText("")
    # retranslateUi

