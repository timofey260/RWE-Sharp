# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_tim.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDial,
    QDockWidget, QDoubleSpinBox, QFrame, QGridLayout,
    QGroupBox, QHeaderView, QLCDNumber, QLabel,
    QMainWindow, QMenu, QMenuBar, QProgressBar,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QStatusBar,
    QTabWidget, QTableView, QTableWidget, QTableWidgetItem,
    QUndoView, QVBoxLayout, QWidget)

from RWESharpWidgets import ViewPort
import ui.res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1351, 968)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1, 400))
        icon = QIcon()
        icon.addFile(u":/icons/icon_small.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon1 = QIcon(QIcon.fromTheme(u"document-open"))
        self.actionOpen.setIcon(icon1)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        icon2 = QIcon(QIcon.fromTheme(u"document-new"))
        self.actionNew.setIcon(icon2)
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        icon3 = QIcon(QIcon.fromTheme(u"application-exit"))
        self.actionClose.setIcon(icon3)
        self.actionClose.setMenuRole(QAction.MenuRole.QuitRole)
        self.actionlevel1 = QAction(MainWindow)
        self.actionlevel1.setObjectName(u"actionlevel1")
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        icon4 = QIcon(QIcon.fromTheme(u"edit-undo"))
        self.actionUndo.setIcon(icon4)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon5 = QIcon(QIcon.fromTheme(u"document-save"))
        self.actionSave.setIcon(icon5)
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        icon6 = QIcon(QIcon.fromTheme(u"document-save-as"))
        self.actionSave_As.setIcon(icon6)
        self.actionRedo = QAction(MainWindow)
        self.actionRedo.setObjectName(u"actionRedo")
        icon7 = QIcon(QIcon.fromTheme(u"edit-redo"))
        self.actionRedo.setIcon(icon7)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon8 = QIcon(QIcon.fromTheme(u"help-about"))
        self.actionAbout.setIcon(icon8)
        self.actionAbout.setMenuRole(QAction.MenuRole.AboutRole)
        self.actionWiki_window = QAction(MainWindow)
        self.actionWiki_window.setObjectName(u"actionWiki_window")
        self.actionWiki_window.setCheckable(True)
        icon9 = QIcon(QIcon.fromTheme(u"accessories-dictionary"))
        self.actionWiki_window.setIcon(icon9)
        self.actionAbout_Qt = QAction(MainWindow)
        self.actionAbout_Qt.setObjectName(u"actionAbout_Qt")
        self.actionAbout_Qt.setIcon(icon8)
        self.actionAbout_Qt.setMenuRole(QAction.MenuRole.AboutQtRole)
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        icon10 = QIcon(QIcon.fromTheme(u"document-properties"))
        self.actionPreferences.setIcon(icon10)
        self.actionPreferences.setMenuRole(QAction.MenuRole.PreferencesRole)
        self.actionRender = QAction(MainWindow)
        self.actionRender.setObjectName(u"actionRender")
        self.actionexplode_leditor = QAction(MainWindow)
        self.actionexplode_leditor.setObjectName(u"actionexplode_leditor")
        self.actionLediting_help = QAction(MainWindow)
        self.actionLediting_help.setObjectName(u"actionLediting_help")
        self.actionRender_2 = QAction(MainWindow)
        self.actionRender_2.setObjectName(u"actionRender_2")
        self.actionHotkeys = QAction(MainWindow)
        self.actionHotkeys.setObjectName(u"actionHotkeys")
        icon11 = QIcon(QIcon.fromTheme(u"input-keyboard"))
        self.actionHotkeys.setIcon(icon11)
        self.actionOpen_2 = QAction(MainWindow)
        self.actionOpen_2.setObjectName(u"actionOpen_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_6 = QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.viewPort = ViewPort(self.centralwidget)
        self.viewPort.setObjectName(u"viewPort")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(2)
        sizePolicy1.setHeightForWidth(self.viewPort.sizePolicy().hasHeightForWidth())
        self.viewPort.setSizePolicy(sizePolicy1)
        self.viewPort.setMouseTracking(True)
        self.viewPort.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout_6.addWidget(self.viewPort, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        MainWindow.setStatusBar(self.statusbar)
        self.DockTools = QDockWidget(MainWindow)
        self.DockTools.setObjectName(u"DockTools")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(3)
        sizePolicy2.setHeightForWidth(self.DockTools.sizePolicy().hasHeightForWidth())
        self.DockTools.setSizePolicy(sizePolicy2)
        self.DockTools.setMinimumSize(QSize(238, 571))
        self.DockTools.setMaximumSize(QSize(524287, 524287))
        self.DockTools.setWindowIcon(icon)
        self.DockTools.setStyleSheet(u"")
        self.DockTools.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.spacer = QWidget()
        self.spacer.setObjectName(u"spacer")
        self.gridLayout_2 = QGridLayout(self.spacer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.ToolsTabs = QTabWidget(self.spacer)
        self.ToolsTabs.setObjectName(u"ToolsTabs")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ToolsTabs.sizePolicy().hasHeightForWidth())
        self.ToolsTabs.setSizePolicy(sizePolicy3)
        self.ToolsTabs.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ToolsTabs.setAutoFillBackground(False)
        self.ToolsTabs.setStyleSheet(u"")
        self.ToolsTabs.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.ToolsGeo = QWidget()
        self.ToolsGeo.setObjectName(u"ToolsGeo")
        self.verticalLayout_3 = QVBoxLayout(self.ToolsGeo)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea = QScrollArea(self.ToolsGeo)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy3.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy3)
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 259, 782))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.ToolGeoaApply_to_Label = QLabel(self.scrollAreaWidgetContents)
        self.ToolGeoaApply_to_Label.setObjectName(u"ToolGeoaApply_to_Label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.ToolGeoaApply_to_Label.sizePolicy().hasHeightForWidth())
        self.ToolGeoaApply_to_Label.setSizePolicy(sizePolicy4)
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
        sizePolicy3.setHeightForWidth(self.ToolGeoM2Select.sizePolicy().hasHeightForWidth())
        self.ToolGeoM2Select.setSizePolicy(sizePolicy3)

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
        sizePolicy3.setHeightForWidth(self.ToolGeoM1Select.sizePolicy().hasHeightForWidth())
        self.ToolGeoM1Select.setSizePolicy(sizePolicy3)

        self.gridLayout_8.addWidget(self.ToolGeoM1Select, 2, 1, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)

        self.gridLayout_8.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)

        self.gridLayout_8.addWidget(self.label_3, 2, 0, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 10))

        self.gridLayout_8.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_8)

        self.ToolMassEditFrame = QGroupBox(self.scrollAreaWidgetContents)
        self.ToolMassEditFrame.setObjectName(u"ToolMassEditFrame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.ToolMassEditFrame.sizePolicy().hasHeightForWidth())
        self.ToolMassEditFrame.setSizePolicy(sizePolicy5)
        self.ToolMassEditFrame.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_11 = QGridLayout(self.ToolMassEditFrame)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.geolayout = QVBoxLayout()
        self.geolayout.setObjectName(u"geolayout")
        self.label_Blocks = QLabel(self.ToolMassEditFrame)
        self.label_Blocks.setObjectName(u"label_Blocks")
        sizePolicy4.setHeightForWidth(self.label_Blocks.sizePolicy().hasHeightForWidth())
        self.label_Blocks.setSizePolicy(sizePolicy4)
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

        self.ToolGeoSlope = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoSlope.setObjectName(u"ToolGeoSlope")
        sizePolicy3.setHeightForWidth(self.ToolGeoSlope.sizePolicy().hasHeightForWidth())
        self.ToolGeoSlope.setSizePolicy(sizePolicy3)
        self.ToolGeoSlope.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.geolayout.addWidget(self.ToolGeoSlope)

        self.ToolGeoAir = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoAir.setObjectName(u"ToolGeoAir")
        sizePolicy3.setHeightForWidth(self.ToolGeoAir.sizePolicy().hasHeightForWidth())
        self.ToolGeoAir.setSizePolicy(sizePolicy3)
        self.ToolGeoAir.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.ToolGeoAir.setIconSize(QSize(32, 16))

        self.geolayout.addWidget(self.ToolGeoAir)

        self.ToolGeoBeam = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoBeam.setObjectName(u"ToolGeoBeam")
        sizePolicy3.setHeightForWidth(self.ToolGeoBeam.sizePolicy().hasHeightForWidth())
        self.ToolGeoBeam.setSizePolicy(sizePolicy3)
        self.ToolGeoBeam.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.geolayout.addWidget(self.ToolGeoBeam)

        self.ToolGeoFloor = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoFloor.setObjectName(u"ToolGeoFloor")
        sizePolicy3.setHeightForWidth(self.ToolGeoFloor.sizePolicy().hasHeightForWidth())
        self.ToolGeoFloor.setSizePolicy(sizePolicy3)
        self.ToolGeoFloor.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.ToolGeoFloor.setAutoRepeat(False)

        self.geolayout.addWidget(self.ToolGeoFloor)

        self.ToolGeoCrack = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoCrack.setObjectName(u"ToolGeoCrack")
        sizePolicy3.setHeightForWidth(self.ToolGeoCrack.sizePolicy().hasHeightForWidth())
        self.ToolGeoCrack.setSizePolicy(sizePolicy3)
        self.ToolGeoCrack.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.geolayout.addWidget(self.ToolGeoCrack)

        self.ToolGeoSpear = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoSpear.setObjectName(u"ToolGeoSpear")
        sizePolicy3.setHeightForWidth(self.ToolGeoSpear.sizePolicy().hasHeightForWidth())
        self.ToolGeoSpear.setSizePolicy(sizePolicy3)
        self.ToolGeoSpear.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.geolayout.addWidget(self.ToolGeoSpear)

        self.ToolGeoRock = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoRock.setObjectName(u"ToolGeoRock")
        sizePolicy3.setHeightForWidth(self.ToolGeoRock.sizePolicy().hasHeightForWidth())
        self.ToolGeoRock.setSizePolicy(sizePolicy3)
        self.ToolGeoRock.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.geolayout.addWidget(self.ToolGeoRock)

        self.ToolGeoGlass = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoGlass.setObjectName(u"ToolGeoGlass")
        sizePolicy3.setHeightForWidth(self.ToolGeoGlass.sizePolicy().hasHeightForWidth())
        self.ToolGeoGlass.setSizePolicy(sizePolicy3)
        self.ToolGeoGlass.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.geolayout.addWidget(self.ToolGeoGlass)

        self.ToolGeoHive = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoHive.setObjectName(u"ToolGeoHive")
        sizePolicy3.setHeightForWidth(self.ToolGeoHive.sizePolicy().hasHeightForWidth())
        self.ToolGeoHive.setSizePolicy(sizePolicy3)
        self.ToolGeoHive.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.geolayout.addWidget(self.ToolGeoHive)

        self.ToolGeoForbidChains = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoForbidChains.setObjectName(u"ToolGeoForbidChains")
        sizePolicy3.setHeightForWidth(self.ToolGeoForbidChains.sizePolicy().hasHeightForWidth())
        self.ToolGeoForbidChains.setSizePolicy(sizePolicy3)
        self.ToolGeoForbidChains.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.geolayout.addWidget(self.ToolGeoForbidChains)

        self.pushButton_8 = QPushButton(self.ToolMassEditFrame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy3.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy3)
        self.pushButton_8.setFlat(False)

        self.geolayout.addWidget(self.pushButton_8)


        self.gridLayout.addLayout(self.geolayout, 0, 0, 2, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ToolGeoLabelPipes = QLabel(self.ToolMassEditFrame)
        self.ToolGeoLabelPipes.setObjectName(u"ToolGeoLabelPipes")
        sizePolicy4.setHeightForWidth(self.ToolGeoLabelPipes.sizePolicy().hasHeightForWidth())
        self.ToolGeoLabelPipes.setSizePolicy(sizePolicy4)

        self.verticalLayout.addWidget(self.ToolGeoLabelPipes)

        self.ToolGeoShortcutEnterance = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoShortcutEnterance.setObjectName(u"ToolGeoShortcutEnterance")
        sizePolicy3.setHeightForWidth(self.ToolGeoShortcutEnterance.sizePolicy().hasHeightForWidth())
        self.ToolGeoShortcutEnterance.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.ToolGeoShortcutEnterance)

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

        self.ToolGeoEnterance = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoEnterance.setObjectName(u"ToolGeoEnterance")
        sizePolicy3.setHeightForWidth(self.ToolGeoEnterance.sizePolicy().hasHeightForWidth())
        self.ToolGeoEnterance.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.ToolGeoEnterance)

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

        self.deletelayout = QVBoxLayout()
        self.deletelayout.setObjectName(u"deletelayout")
        self.ToolGeoLabelDeltieTools = QLabel(self.ToolMassEditFrame)
        self.ToolGeoLabelDeltieTools.setObjectName(u"ToolGeoLabelDeltieTools")
        sizePolicy4.setHeightForWidth(self.ToolGeoLabelDeltieTools.sizePolicy().hasHeightForWidth())
        self.ToolGeoLabelDeltieTools.setSizePolicy(sizePolicy4)

        self.deletelayout.addWidget(self.ToolGeoLabelDeltieTools)

        self.ToolGeoClearUpperLayer = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoClearUpperLayer.setObjectName(u"ToolGeoClearUpperLayer")
        sizePolicy3.setHeightForWidth(self.ToolGeoClearUpperLayer.sizePolicy().hasHeightForWidth())
        self.ToolGeoClearUpperLayer.setSizePolicy(sizePolicy3)

        self.deletelayout.addWidget(self.ToolGeoClearUpperLayer)

        self.ToolGeoClearLayer = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoClearLayer.setObjectName(u"ToolGeoClearLayer")
        sizePolicy3.setHeightForWidth(self.ToolGeoClearLayer.sizePolicy().hasHeightForWidth())
        self.ToolGeoClearLayer.setSizePolicy(sizePolicy3)

        self.deletelayout.addWidget(self.ToolGeoClearLayer)

        self.ToolGeoClearAll = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoClearAll.setObjectName(u"ToolGeoClearAll")
        sizePolicy3.setHeightForWidth(self.ToolGeoClearAll.sizePolicy().hasHeightForWidth())
        self.ToolGeoClearAll.setSizePolicy(sizePolicy3)

        self.deletelayout.addWidget(self.ToolGeoClearAll)


        self.gridLayout.addLayout(self.deletelayout, 1, 1, 1, 1)

        self.masslayout = QVBoxLayout()
        self.masslayout.setObjectName(u"masslayout")
        self.ToolGeoLabel = QLabel(self.ToolMassEditFrame)
        self.ToolGeoLabel.setObjectName(u"ToolGeoLabel")
        sizePolicy4.setHeightForWidth(self.ToolGeoLabel.sizePolicy().hasHeightForWidth())
        self.ToolGeoLabel.setSizePolicy(sizePolicy4)
        self.ToolGeoLabel.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.masslayout.addWidget(self.ToolGeoLabel)

        self.ToolGeoCopy = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoCopy.setObjectName(u"ToolGeoCopy")
        sizePolicy3.setHeightForWidth(self.ToolGeoCopy.sizePolicy().hasHeightForWidth())
        self.ToolGeoCopy.setSizePolicy(sizePolicy3)
        self.ToolGeoCopy.setMinimumSize(QSize(0, 0))
        self.ToolGeoCopy.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.masslayout.addWidget(self.ToolGeoCopy)

        self.ToolGeoPaste = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoPaste.setObjectName(u"ToolGeoPaste")
        sizePolicy3.setHeightForWidth(self.ToolGeoPaste.sizePolicy().hasHeightForWidth())
        self.ToolGeoPaste.setSizePolicy(sizePolicy3)
        self.ToolGeoPaste.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.ToolGeoPaste.setIconSize(QSize(16, 16))
        self.ToolGeoPaste.setCheckable(False)

        self.masslayout.addWidget(self.ToolGeoPaste)

        self.ToolGeoMirror = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoMirror.setObjectName(u"ToolGeoMirror")
        sizePolicy3.setHeightForWidth(self.ToolGeoMirror.sizePolicy().hasHeightForWidth())
        self.ToolGeoMirror.setSizePolicy(sizePolicy3)
        self.ToolGeoMirror.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.masslayout.addWidget(self.ToolGeoMirror)

        self.ToolGeoInvert = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoInvert.setObjectName(u"ToolGeoInvert")
        sizePolicy3.setHeightForWidth(self.ToolGeoInvert.sizePolicy().hasHeightForWidth())
        self.ToolGeoInvert.setSizePolicy(sizePolicy3)
        self.ToolGeoInvert.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.masslayout.addWidget(self.ToolGeoInvert)

        self.ToolGeoMove = QPushButton(self.ToolMassEditFrame)
        self.ToolGeoMove.setObjectName(u"ToolGeoMove")
        sizePolicy3.setHeightForWidth(self.ToolGeoMove.sizePolicy().hasHeightForWidth())
        self.ToolGeoMove.setSizePolicy(sizePolicy3)
        self.ToolGeoMove.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.ToolGeoMove.setAutoRepeat(False)

        self.masslayout.addWidget(self.ToolGeoMove)


        self.gridLayout.addLayout(self.masslayout, 2, 0, 1, 2)


        self.gridLayout_11.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.ToolMassEditFrame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.ToolsTabs.addTab(self.ToolsGeo, "")
        self.ToolsTiles = QWidget()
        self.ToolsTiles.setObjectName(u"ToolsTiles")
        self.verticalLayout_16 = QVBoxLayout(self.ToolsTiles)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.ToolTilesSetAsDefault = QPushButton(self.ToolsTiles)
        self.ToolTilesSetAsDefault.setObjectName(u"ToolTilesSetAsDefault")

        self.gridLayout_9.addWidget(self.ToolTilesSetAsDefault, 5, 1, 1, 1)

        self.ToolTilesM1Select = QComboBox(self.ToolsTiles)
        self.ToolTilesM1Select.addItem("")
        self.ToolTilesM1Select.addItem("")
        self.ToolTilesM1Select.addItem("")
        self.ToolTilesM1Select.addItem("")
        self.ToolTilesM1Select.addItem("")
        self.ToolTilesM1Select.addItem("")
        self.ToolTilesM1Select.addItem("")
        self.ToolTilesM1Select.addItem("")
        self.ToolTilesM1Select.addItem("")
        self.ToolTilesM1Select.setObjectName(u"ToolTilesM1Select")

        self.gridLayout_9.addWidget(self.ToolTilesM1Select, 1, 0, 1, 1)

        self.label_4 = QLabel(self.ToolsTiles)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_9.addWidget(self.label_4, 1, 1, 1, 1)

        self.ToolTilesBrushSIzeSelector = QSpinBox(self.ToolsTiles)
        self.ToolTilesBrushSIzeSelector.setObjectName(u"ToolTilesBrushSIzeSelector")

        self.gridLayout_9.addWidget(self.ToolTilesBrushSIzeSelector, 3, 0, 1, 1)

        self.ToolTilesM2Select = QComboBox(self.ToolsTiles)
        self.ToolTilesM2Select.addItem("")
        self.ToolTilesM2Select.addItem("")
        self.ToolTilesM2Select.addItem("")
        self.ToolTilesM2Select.addItem("")
        self.ToolTilesM2Select.addItem("")
        self.ToolTilesM2Select.addItem("")
        self.ToolTilesM2Select.addItem("")
        self.ToolTilesM2Select.addItem("")
        self.ToolTilesM2Select.addItem("")
        self.ToolTilesM2Select.setObjectName(u"ToolTilesM2Select")

        self.gridLayout_9.addWidget(self.ToolTilesM2Select, 2, 0, 1, 1)

        self.label_11 = QLabel(self.ToolsTiles)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_9.addWidget(self.label_11, 3, 1, 1, 1)

        self.ToolTilesPaste = QPushButton(self.ToolsTiles)
        self.ToolTilesPaste.setObjectName(u"ToolTilesPaste")

        self.gridLayout_9.addWidget(self.ToolTilesPaste, 4, 0, 1, 1)

        self.ToolTilesCopy = QPushButton(self.ToolsTiles)
        self.ToolTilesCopy.setObjectName(u"ToolTilesCopy")

        self.gridLayout_9.addWidget(self.ToolTilesCopy, 4, 1, 1, 1)

        self.label_5 = QLabel(self.ToolsTiles)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_9.addWidget(self.label_5, 2, 1, 1, 1)

        self.ToolTilesSelectTool = QPushButton(self.ToolsTiles)
        self.ToolTilesSelectTool.setObjectName(u"ToolTilesSelectTool")

        self.gridLayout_9.addWidget(self.ToolTilesSelectTool, 5, 0, 1, 1)


        self.verticalLayout_16.addLayout(self.gridLayout_9)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_4)

        self.ToolsTabs.addTab(self.ToolsTiles, "")
        self.ToolsProps = QWidget()
        self.ToolsProps.setObjectName(u"ToolsProps")
        self.verticalLayout_17 = QVBoxLayout(self.ToolsProps)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.ToolPropsSelectTool = QPushButton(self.ToolsProps)
        self.ToolPropsSelectTool.setObjectName(u"ToolPropsSelectTool")

        self.verticalLayout_17.addWidget(self.ToolPropsSelectTool)

        self.ToolPropsDelite = QPushButton(self.ToolsProps)
        self.ToolPropsDelite.setObjectName(u"ToolPropsDelite")

        self.verticalLayout_17.addWidget(self.ToolPropsDelite)

        self.ToolPropsMoveSelected = QPushButton(self.ToolsProps)
        self.ToolPropsMoveSelected.setObjectName(u"ToolPropsMoveSelected")

        self.verticalLayout_17.addWidget(self.ToolPropsMoveSelected)

        self.ToolPropsLabel_11 = QLabel(self.ToolsProps)
        self.ToolPropsLabel_11.setObjectName(u"ToolPropsLabel_11")

        self.verticalLayout_17.addWidget(self.ToolPropsLabel_11)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.ToolsPropsSizeY = QSpinBox(self.ToolsProps)
        self.ToolsPropsSizeY.setObjectName(u"ToolsPropsSizeY")
        sizePolicy.setHeightForWidth(self.ToolsPropsSizeY.sizePolicy().hasHeightForWidth())
        self.ToolsPropsSizeY.setSizePolicy(sizePolicy)

        self.gridLayout_12.addWidget(self.ToolsPropsSizeY, 0, 0, 1, 1)

        self.ToolPropsLabel_10 = QLabel(self.ToolsProps)
        self.ToolPropsLabel_10.setObjectName(u"ToolPropsLabel_10")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(4)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.ToolPropsLabel_10.sizePolicy().hasHeightForWidth())
        self.ToolPropsLabel_10.setSizePolicy(sizePolicy6)

        self.gridLayout_12.addWidget(self.ToolPropsLabel_10, 0, 1, 1, 1)

        self.ToolPropsSizeX = QSpinBox(self.ToolsProps)
        self.ToolPropsSizeX.setObjectName(u"ToolPropsSizeX")
        sizePolicy3.setHeightForWidth(self.ToolPropsSizeX.sizePolicy().hasHeightForWidth())
        self.ToolPropsSizeX.setSizePolicy(sizePolicy3)

        self.gridLayout_12.addWidget(self.ToolPropsSizeX, 1, 0, 1, 1)

        self.ToolPropsLabel_9 = QLabel(self.ToolsProps)
        self.ToolPropsLabel_9.setObjectName(u"ToolPropsLabel_9")

        self.gridLayout_12.addWidget(self.ToolPropsLabel_9, 1, 1, 1, 1)

        self.ToolPropsRotation = QSpinBox(self.ToolsProps)
        self.ToolPropsRotation.setObjectName(u"ToolPropsRotation")
        sizePolicy3.setHeightForWidth(self.ToolPropsRotation.sizePolicy().hasHeightForWidth())
        self.ToolPropsRotation.setSizePolicy(sizePolicy3)

        self.gridLayout_12.addWidget(self.ToolPropsRotation, 2, 0, 1, 1)

        self.ToolPropsLabel_8 = QLabel(self.ToolsProps)
        self.ToolPropsLabel_8.setObjectName(u"ToolPropsLabel_8")

        self.gridLayout_12.addWidget(self.ToolPropsLabel_8, 2, 1, 1, 1)

        self.ToolPropsRenderOrder = QSpinBox(self.ToolsProps)
        self.ToolPropsRenderOrder.setObjectName(u"ToolPropsRenderOrder")
        sizePolicy3.setHeightForWidth(self.ToolPropsRenderOrder.sizePolicy().hasHeightForWidth())
        self.ToolPropsRenderOrder.setSizePolicy(sizePolicy3)

        self.gridLayout_12.addWidget(self.ToolPropsRenderOrder, 3, 0, 1, 1)

        self.ToolPropsLabel = QLabel(self.ToolsProps)
        self.ToolPropsLabel.setObjectName(u"ToolPropsLabel")

        self.gridLayout_12.addWidget(self.ToolPropsLabel, 3, 1, 1, 1)

        self.ToolPropsRenderTime = QSpinBox(self.ToolsProps)
        self.ToolPropsRenderTime.setObjectName(u"ToolPropsRenderTime")
        sizePolicy3.setHeightForWidth(self.ToolPropsRenderTime.sizePolicy().hasHeightForWidth())
        self.ToolPropsRenderTime.setSizePolicy(sizePolicy3)

        self.gridLayout_12.addWidget(self.ToolPropsRenderTime, 4, 0, 1, 1)

        self.ToolPropsLabel_2 = QLabel(self.ToolsProps)
        self.ToolPropsLabel_2.setObjectName(u"ToolPropsLabel_2")

        self.gridLayout_12.addWidget(self.ToolPropsLabel_2, 4, 1, 1, 1)

        self.ToolPropsSeed = QSpinBox(self.ToolsProps)
        self.ToolPropsSeed.setObjectName(u"ToolPropsSeed")
        sizePolicy3.setHeightForWidth(self.ToolPropsSeed.sizePolicy().hasHeightForWidth())
        self.ToolPropsSeed.setSizePolicy(sizePolicy3)

        self.gridLayout_12.addWidget(self.ToolPropsSeed, 5, 0, 1, 1)

        self.ToolPropsLabel_3 = QLabel(self.ToolsProps)
        self.ToolPropsLabel_3.setObjectName(u"ToolPropsLabel_3")

        self.gridLayout_12.addWidget(self.ToolPropsLabel_3, 5, 1, 1, 1)

        self.ToolPropsRelease = QComboBox(self.ToolsProps)
        self.ToolPropsRelease.setObjectName(u"ToolPropsRelease")
        sizePolicy3.setHeightForWidth(self.ToolPropsRelease.sizePolicy().hasHeightForWidth())
        self.ToolPropsRelease.setSizePolicy(sizePolicy3)

        self.gridLayout_12.addWidget(self.ToolPropsRelease, 6, 0, 1, 1)

        self.ToolPropsLabel_4 = QLabel(self.ToolsProps)
        self.ToolPropsLabel_4.setObjectName(u"ToolPropsLabel_4")

        self.gridLayout_12.addWidget(self.ToolPropsLabel_4, 6, 1, 1, 1)

        self.ToolPropsVariation = QSpinBox(self.ToolsProps)
        self.ToolPropsVariation.setObjectName(u"ToolPropsVariation")
        sizePolicy3.setHeightForWidth(self.ToolPropsVariation.sizePolicy().hasHeightForWidth())
        self.ToolPropsVariation.setSizePolicy(sizePolicy3)

        self.gridLayout_12.addWidget(self.ToolPropsVariation, 7, 0, 1, 1)

        self.ToolPropsLabel_6 = QLabel(self.ToolsProps)
        self.ToolPropsLabel_6.setObjectName(u"ToolPropsLabel_6")

        self.gridLayout_12.addWidget(self.ToolPropsLabel_6, 7, 1, 1, 1)

        self.ToolPropsCustomDepth = QSpinBox(self.ToolsProps)
        self.ToolPropsCustomDepth.setObjectName(u"ToolPropsCustomDepth")
        sizePolicy3.setHeightForWidth(self.ToolPropsCustomDepth.sizePolicy().hasHeightForWidth())
        self.ToolPropsCustomDepth.setSizePolicy(sizePolicy3)

        self.gridLayout_12.addWidget(self.ToolPropsCustomDepth, 8, 0, 1, 1)

        self.ToolPropsLabel_5 = QLabel(self.ToolsProps)
        self.ToolPropsLabel_5.setObjectName(u"ToolPropsLabel_5")

        self.gridLayout_12.addWidget(self.ToolPropsLabel_5, 8, 1, 1, 1)

        self.ToolPropsApplyColor = QCheckBox(self.ToolsProps)
        self.ToolPropsApplyColor.setObjectName(u"ToolPropsApplyColor")
        sizePolicy3.setHeightForWidth(self.ToolPropsApplyColor.sizePolicy().hasHeightForWidth())
        self.ToolPropsApplyColor.setSizePolicy(sizePolicy3)

        self.gridLayout_12.addWidget(self.ToolPropsApplyColor, 9, 0, 1, 1)

        self.ToolPropsLabel_7 = QLabel(self.ToolsProps)
        self.ToolPropsLabel_7.setObjectName(u"ToolPropsLabel_7")

        self.gridLayout_12.addWidget(self.ToolPropsLabel_7, 9, 1, 1, 1)


        self.verticalLayout_17.addLayout(self.gridLayout_12)

        self.label_16 = QLabel(self.ToolsProps)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_17.addWidget(self.label_16)

        self.tableView = QTableView(self.ToolsProps)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_17.addWidget(self.tableView)

        self.ToolsTabs.addTab(self.ToolsProps, "")
        self.ToolsEffects = QWidget()
        self.ToolsEffects.setObjectName(u"ToolsEffects")
        self.verticalLayout_10 = QVBoxLayout(self.ToolsEffects)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.scrollArea_3 = QScrollArea(self.ToolsEffects)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 274, 480))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_6 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_12.addWidget(self.label_6)

        self.tableWidget = QTableWidget(self.scrollAreaWidgetContents_3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_12.addWidget(self.tableWidget)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_2 = QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_5.addWidget(self.pushButton_2, 1, 2, 1, 1)

        self.pushButton = QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_5.addWidget(self.pushButton, 1, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_5.addWidget(self.pushButton_3, 1, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_5.addWidget(self.pushButton_5, 2, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_5.addWidget(self.pushButton_4, 2, 2, 1, 1)


        self.verticalLayout_12.addLayout(self.gridLayout_5)

        self.label_7 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_12.addWidget(self.label_7)

        self.tableWidget_2 = QTableWidget(self.scrollAreaWidgetContents_3)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.verticalLayout_12.addWidget(self.tableWidget_2)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_10.addWidget(self.scrollArea_3)

        self.ToolsTabs.addTab(self.ToolsEffects, "")
        self.ToolsLight = QWidget()
        self.ToolsLight.setObjectName(u"ToolsLight")
        self.verticalLayout_14 = QVBoxLayout(self.ToolsLight)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_9 = QLabel(self.ToolsLight)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_14.addWidget(self.label_9)

        self.label_10 = QLabel(self.ToolsLight)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_14.addWidget(self.label_10)

        self.label_8 = QLabel(self.ToolsLight)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_14.addWidget(self.label_8)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.ToolsLight)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")

        self.verticalLayout_14.addWidget(self.doubleSpinBox_2)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.ToolsLight)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")

        self.verticalLayout_14.addWidget(self.doubleSpinBox_3)

        self.doubleSpinBox = QDoubleSpinBox(self.ToolsLight)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.verticalLayout_14.addWidget(self.doubleSpinBox)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.spinBox = QSpinBox(self.ToolsLight)
        self.spinBox.setObjectName(u"spinBox")

        self.gridLayout_7.addWidget(self.spinBox, 2, 0, 1, 1)

        self.label_13 = QLabel(self.ToolsLight)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_7.addWidget(self.label_13, 1, 1, 1, 1)

        self.spinBox_2 = QSpinBox(self.ToolsLight)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.gridLayout_7.addWidget(self.spinBox_2, 2, 1, 1, 1)

        self.line_2 = QFrame(self.ToolsLight)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_7.addWidget(self.line_2, 0, 1, 1, 1)

        self.label_12 = QLabel(self.ToolsLight)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_7.addWidget(self.label_12, 1, 0, 1, 1)

        self.line = QFrame(self.ToolsLight)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_7.addWidget(self.line, 0, 0, 1, 1)


        self.verticalLayout_14.addLayout(self.gridLayout_7)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_5)

        self.ToolsTabs.addTab(self.ToolsLight, "")
        self.ToolsProperties = QWidget()
        self.ToolsProperties.setObjectName(u"ToolsProperties")
        self.verticalLayout_18 = QVBoxLayout(self.ToolsProperties)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_15 = QLabel(self.ToolsProperties)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_18.addWidget(self.label_15)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.ToolsPropertiesLabel = QLabel(self.ToolsProperties)
        self.ToolsPropertiesLabel.setObjectName(u"ToolsPropertiesLabel")

        self.gridLayout_10.addWidget(self.ToolsPropertiesLabel, 1, 0, 1, 1)

        self.ToolsPropertiesLabel_3 = QLabel(self.ToolsProperties)
        self.ToolsPropertiesLabel_3.setObjectName(u"ToolsPropertiesLabel_3")

        self.gridLayout_10.addWidget(self.ToolsPropertiesLabel_3, 3, 0, 1, 1)

        self.ToolsPropertiesSizeX = QSpinBox(self.ToolsProperties)
        self.ToolsPropertiesSizeX.setObjectName(u"ToolsPropertiesSizeX")

        self.gridLayout_10.addWidget(self.ToolsPropertiesSizeX, 2, 0, 1, 1)

        self.ToolsPropertiesWaterSettings = QComboBox(self.ToolsProperties)
        self.ToolsPropertiesWaterSettings.addItem("")
        self.ToolsPropertiesWaterSettings.addItem("")
        self.ToolsPropertiesWaterSettings.addItem("")
        self.ToolsPropertiesWaterSettings.setObjectName(u"ToolsPropertiesWaterSettings")
        self.ToolsPropertiesWaterSettings.setFrame(False)

        self.gridLayout_10.addWidget(self.ToolsPropertiesWaterSettings, 8, 1, 1, 1)

        self.ToolsPropertiesLabel_5 = QLabel(self.ToolsProperties)
        self.ToolsPropertiesLabel_5.setObjectName(u"ToolsPropertiesLabel_5")

        self.gridLayout_10.addWidget(self.ToolsPropertiesLabel_5, 7, 0, 1, 1)

        self.ToolsPropertiesSun = QCheckBox(self.ToolsProperties)
        self.ToolsPropertiesSun.setObjectName(u"ToolsPropertiesSun")

        self.gridLayout_10.addWidget(self.ToolsPropertiesSun, 5, 0, 1, 2)

        self.ToolsPropertiesBorderSizeX = QSpinBox(self.ToolsProperties)
        self.ToolsPropertiesBorderSizeX.setObjectName(u"ToolsPropertiesBorderSizeX")

        self.gridLayout_10.addWidget(self.ToolsPropertiesBorderSizeX, 4, 0, 1, 1)

        self.ToolsPropertiesWaterHeight = QSpinBox(self.ToolsProperties)
        self.ToolsPropertiesWaterHeight.setObjectName(u"ToolsPropertiesWaterHeight")

        self.gridLayout_10.addWidget(self.ToolsPropertiesWaterHeight, 8, 0, 1, 1)

        self.ToolsPropertiesSizeY = QSpinBox(self.ToolsProperties)
        self.ToolsPropertiesSizeY.setObjectName(u"ToolsPropertiesSizeY")

        self.gridLayout_10.addWidget(self.ToolsPropertiesSizeY, 2, 1, 1, 1)

        self.ToolsPropertiesLabel_2 = QLabel(self.ToolsProperties)
        self.ToolsPropertiesLabel_2.setObjectName(u"ToolsPropertiesLabel_2")

        self.gridLayout_10.addWidget(self.ToolsPropertiesLabel_2, 1, 1, 1, 1)

        self.ToolsPropertiesBorderSizeY = QSpinBox(self.ToolsProperties)
        self.ToolsPropertiesBorderSizeY.setObjectName(u"ToolsPropertiesBorderSizeY")

        self.gridLayout_10.addWidget(self.ToolsPropertiesBorderSizeY, 4, 1, 1, 1)

        self.ToolsPropertiesLabel_4 = QLabel(self.ToolsProperties)
        self.ToolsPropertiesLabel_4.setObjectName(u"ToolsPropertiesLabel_4")

        self.gridLayout_10.addWidget(self.ToolsPropertiesLabel_4, 3, 1, 1, 1)

        self.ToolsPropertiesLabel_6 = QLabel(self.ToolsProperties)
        self.ToolsPropertiesLabel_6.setObjectName(u"ToolsPropertiesLabel_6")

        self.gridLayout_10.addWidget(self.ToolsPropertiesLabel_6, 7, 1, 1, 1)

        self.ToolsPropertiesLine = QFrame(self.ToolsProperties)
        self.ToolsPropertiesLine.setObjectName(u"ToolsPropertiesLine")
        self.ToolsPropertiesLine.setFrameShape(QFrame.Shape.HLine)
        self.ToolsPropertiesLine.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_10.addWidget(self.ToolsPropertiesLine, 6, 0, 1, 2)


        self.verticalLayout_18.addLayout(self.gridLayout_10)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.ToolsPropertiesLabel_7 = QLabel(self.ToolsProperties)
        self.ToolsPropertiesLabel_7.setObjectName(u"ToolsPropertiesLabel_7")

        self.verticalLayout_13.addWidget(self.ToolsPropertiesLabel_7)

        self.ToolsPropertiesTabel = QTableWidget(self.ToolsProperties)
        self.ToolsPropertiesTabel.setObjectName(u"ToolsPropertiesTabel")

        self.verticalLayout_13.addWidget(self.ToolsPropertiesTabel)

        self.ToolsPropertiesLabel_9 = QLabel(self.ToolsProperties)
        self.ToolsPropertiesLabel_9.setObjectName(u"ToolsPropertiesLabel_9")

        self.verticalLayout_13.addWidget(self.ToolsPropertiesLabel_9)

        self.ToolsPropertiesSeed = QSlider(self.ToolsProperties)
        self.ToolsPropertiesSeed.setObjectName(u"ToolsPropertiesSeed")
        self.ToolsPropertiesSeed.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_13.addWidget(self.ToolsPropertiesSeed)


        self.verticalLayout_18.addLayout(self.verticalLayout_13)

        self.ToolsTabs.addTab(self.ToolsProperties, "")

        self.gridLayout_2.addWidget(self.ToolsTabs, 0, 1, 1, 1)

        self.DockTools.setWidget(self.spacer)
        MainWindow.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.DockTools)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1351, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuRecent = QMenu(self.menuFile)
        self.menuRecent.setObjectName(u"menuRecent")
        icon12 = QIcon(QIcon.fromTheme(u"document-open-recent"))
        self.menuRecent.setIcon(icon12)
        self.menuWindow = QMenu(self.menubar)
        self.menuWindow.setObjectName(u"menuWindow")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menutools = QMenu(self.menubar)
        self.menutools.setObjectName(u"menutools")
        self.menuDrizzle = QMenu(self.menubar)
        self.menuDrizzle.setObjectName(u"menuDrizzle")
        self.menuMods = QMenu(self.menubar)
        self.menuMods.setObjectName(u"menuMods")
        self.menuConfigure = QMenu(self.menuMods)
        self.menuConfigure.setObjectName(u"menuConfigure")
        MainWindow.setMenuBar(self.menubar)
        self.DockView = QDockWidget(MainWindow)
        self.DockView.setObjectName(u"DockView")
        self.DockView.setEnabled(True)
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(1)
        sizePolicy7.setHeightForWidth(self.DockView.sizePolicy().hasHeightForWidth())
        self.DockView.setSizePolicy(sizePolicy7)
        self.DockView.setMinimumSize(QSize(167, 371))
        self.DockView.setMaximumSize(QSize(524287, 524287))
        self.DockView.setBaseSize(QSize(200, 300))
        self.DockView.setAcceptDrops(True)
        self.DockView.setWindowIcon(icon)
        self.ViewDock = QWidget()
        self.ViewDock.setObjectName(u"ViewDock")
        self.verticalLayout_2 = QVBoxLayout(self.ViewDock)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ViewTab = QTabWidget(self.ViewDock)
        self.ViewTab.setObjectName(u"ViewTab")
        self.VQuick = QWidget()
        self.VQuick.setObjectName(u"VQuick")
        self.verticalLayout_8 = QVBoxLayout(self.VQuick)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.scrollArea_4 = QScrollArea(self.VQuick)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 274, 280))
        self.gridLayout_13 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.VQuickLabel = QLabel(self.scrollAreaWidgetContents_4)
        self.VQuickLabel.setObjectName(u"VQuickLabel")

        self.verticalLayout_4.addWidget(self.VQuickLabel)

        self.VQuickGeo = QCheckBox(self.scrollAreaWidgetContents_4)
        self.VQuickGeo.setObjectName(u"VQuickGeo")
        self.VQuickGeo.setChecked(True)

        self.verticalLayout_4.addWidget(self.VQuickGeo)

        self.VQuickTiles = QCheckBox(self.scrollAreaWidgetContents_4)
        self.VQuickTiles.setObjectName(u"VQuickTiles")
        self.VQuickTiles.setChecked(True)

        self.verticalLayout_4.addWidget(self.VQuickTiles)

        self.VQuickProps = QCheckBox(self.scrollAreaWidgetContents_4)
        self.VQuickProps.setObjectName(u"VQuickProps")
        self.VQuickProps.setChecked(True)

        self.verticalLayout_4.addWidget(self.VQuickProps)

        self.VQuickCammeras = QCheckBox(self.scrollAreaWidgetContents_4)
        self.VQuickCammeras.setObjectName(u"VQuickCammeras")
        self.VQuickCammeras.setChecked(False)

        self.verticalLayout_4.addWidget(self.VQuickCammeras)

        self.VQuickEffects = QCheckBox(self.scrollAreaWidgetContents_4)
        self.VQuickEffects.setObjectName(u"VQuickEffects")
        self.VQuickEffects.setChecked(False)

        self.verticalLayout_4.addWidget(self.VQuickEffects)

        self.VQuickWater = QCheckBox(self.scrollAreaWidgetContents_4)
        self.VQuickWater.setObjectName(u"VQuickWater")
        self.VQuickWater.setChecked(False)

        self.verticalLayout_4.addWidget(self.VQuickWater)

        self.VQuickLightmap = QCheckBox(self.scrollAreaWidgetContents_4)
        self.VQuickLightmap.setObjectName(u"VQuickLightmap")
        self.VQuickLightmap.setChecked(False)

        self.verticalLayout_4.addWidget(self.VQuickLightmap)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_11)


        self.gridLayout_13.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_8.addWidget(self.scrollArea_4)

        self.ViewTab.addTab(self.VQuick, "")
        self.VGeo = QWidget()
        self.VGeo.setObjectName(u"VGeo")
        self.gridLayout_3 = QGridLayout(self.VGeo)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.VGeoBeams = QCheckBox(self.VGeo)
        self.VGeoBeams.setObjectName(u"VGeoBeams")
        self.VGeoBeams.setEnabled(True)
        self.VGeoBeams.setChecked(False)

        self.gridLayout_3.addWidget(self.VGeoBeams, 5, 0, 1, 1)

        self.VGeoRWEstyle = QRadioButton(self.VGeo)
        self.VGeoRWEstyle.setObjectName(u"VGeoRWEstyle")
        self.VGeoRWEstyle.setChecked(True)

        self.gridLayout_3.addWidget(self.VGeoRWEstyle, 8, 0, 1, 1)

        self.VGeolabel = QLabel(self.VGeo)
        self.VGeolabel.setObjectName(u"VGeolabel")

        self.gridLayout_3.addWidget(self.VGeolabel, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 10, 0, 1, 1)

        self.VGeoMisc = QCheckBox(self.VGeo)
        self.VGeoMisc.setObjectName(u"VGeoMisc")

        self.gridLayout_3.addWidget(self.VGeoMisc, 7, 0, 1, 1)

        self.VGeoAll = QCheckBox(self.VGeo)
        self.VGeoAll.setObjectName(u"VGeoAll")
        self.VGeoAll.setChecked(True)

        self.gridLayout_3.addWidget(self.VGeoAll, 1, 0, 1, 1)

        self.VGeoLayer2 = QCheckBox(self.VGeo)
        self.VGeoLayer2.setObjectName(u"VGeoLayer2")

        self.gridLayout_3.addWidget(self.VGeoLayer2, 3, 0, 1, 1)

        self.VGeoLayer1 = QCheckBox(self.VGeo)
        self.VGeoLayer1.setObjectName(u"VGeoLayer1")

        self.gridLayout_3.addWidget(self.VGeoLayer1, 2, 0, 1, 1)

        self.VGeoThrowables = QCheckBox(self.VGeo)
        self.VGeoThrowables.setObjectName(u"VGeoThrowables")

        self.gridLayout_3.addWidget(self.VGeoThrowables, 6, 0, 1, 1)

        self.VGeoLayer3 = QCheckBox(self.VGeo)
        self.VGeoLayer3.setObjectName(u"VGeoLayer3")

        self.gridLayout_3.addWidget(self.VGeoLayer3, 4, 0, 1, 1)

        self.VGeoOldStyle = QRadioButton(self.VGeo)
        self.VGeoOldStyle.setObjectName(u"VGeoOldStyle")

        self.gridLayout_3.addWidget(self.VGeoOldStyle, 9, 0, 1, 1)

        self.ViewTab.addTab(self.VGeo, "")
        self.VTiles = QWidget()
        self.VTiles.setObjectName(u"VTiles")
        self.verticalLayout_5 = QVBoxLayout(self.VTiles)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.VTilesMaterialsLabel = QLabel(self.VTiles)
        self.VTilesMaterialsLabel.setObjectName(u"VTilesMaterialsLabel")

        self.verticalLayout_5.addWidget(self.VTilesMaterialsLabel)

        self.VTilesAllTiles = QCheckBox(self.VTiles)
        self.VTilesAllTiles.setObjectName(u"VTilesAllTiles")

        self.verticalLayout_5.addWidget(self.VTilesAllTiles)

        self.VTilesLayer1 = QCheckBox(self.VTiles)
        self.VTilesLayer1.setObjectName(u"VTilesLayer1")

        self.verticalLayout_5.addWidget(self.VTilesLayer1)

        self.VTilesLayer2 = QCheckBox(self.VTiles)
        self.VTilesLayer2.setObjectName(u"VTilesLayer2")

        self.verticalLayout_5.addWidget(self.VTilesLayer2)

        self.VTilesLayer3 = QCheckBox(self.VTiles)
        self.VTilesLayer3.setObjectName(u"VTilesLayer3")

        self.verticalLayout_5.addWidget(self.VTilesLayer3)

        self.VTilesMaterials = QCheckBox(self.VTiles)
        self.VTilesMaterials.setObjectName(u"VTilesMaterials")

        self.verticalLayout_5.addWidget(self.VTilesMaterials)

        self.VTilesMaterialsOldPreview = QRadioButton(self.VTiles)
        self.VTilesMaterialsOldPreview.setObjectName(u"VTilesMaterialsOldPreview")

        self.verticalLayout_5.addWidget(self.VTilesMaterialsOldPreview)

        self.VTilesMaterialBetterPreview = QRadioButton(self.VTiles)
        self.VTilesMaterialBetterPreview.setObjectName(u"VTilesMaterialBetterPreview")

        self.verticalLayout_5.addWidget(self.VTilesMaterialBetterPreview)

        self.VTilesHeads = QCheckBox(self.VTiles)
        self.VTilesHeads.setObjectName(u"VTilesHeads")

        self.verticalLayout_5.addWidget(self.VTilesHeads)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.ViewTab.addTab(self.VTiles, "")
        self.VProps_2 = QWidget()
        self.VProps_2.setObjectName(u"VProps_2")
        self.gridLayout_4 = QGridLayout(self.VProps_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.VPropsLabel = QLabel(self.VProps_2)
        self.VPropsLabel.setObjectName(u"VPropsLabel")

        self.gridLayout_4.addWidget(self.VPropsLabel, 0, 0, 1, 1)

        self.VPropsHead = QCheckBox(self.VProps_2)
        self.VPropsHead.setObjectName(u"VPropsHead")

        self.gridLayout_4.addWidget(self.VPropsHead, 6, 0, 1, 1)

        self.VPropsAllProps = QCheckBox(self.VProps_2)
        self.VPropsAllProps.setObjectName(u"VPropsAllProps")

        self.gridLayout_4.addWidget(self.VPropsAllProps, 1, 0, 1, 1)

        self.VPropsLayer3 = QCheckBox(self.VProps_2)
        self.VPropsLayer3.setObjectName(u"VPropsLayer3")

        self.gridLayout_4.addWidget(self.VPropsLayer3, 4, 0, 1, 1)

        self.VPropsDestructionProps = QCheckBox(self.VProps_2)
        self.VPropsDestructionProps.setObjectName(u"VPropsDestructionProps")

        self.gridLayout_4.addWidget(self.VPropsDestructionProps, 10, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 15, 0, 1, 1)

        self.VPropsLayer1 = QCheckBox(self.VProps_2)
        self.VPropsLayer1.setObjectName(u"VPropsLayer1")

        self.gridLayout_4.addWidget(self.VPropsLayer1, 2, 0, 1, 1)

        self.VPropsLongProps = QCheckBox(self.VProps_2)
        self.VPropsLongProps.setObjectName(u"VPropsLongProps")

        self.gridLayout_4.addWidget(self.VPropsLongProps, 7, 0, 1, 1)

        self.VPropsSoftProps = QCheckBox(self.VProps_2)
        self.VPropsSoftProps.setObjectName(u"VPropsSoftProps")

        self.gridLayout_4.addWidget(self.VPropsSoftProps, 11, 0, 1, 1)

        self.VPropsLayer2 = QCheckBox(self.VProps_2)
        self.VPropsLayer2.setObjectName(u"VPropsLayer2")
        self.VPropsLayer2.setEnabled(True)

        self.gridLayout_4.addWidget(self.VPropsLayer2, 3, 0, 1, 1)

        self.VPropsRopeProps = QCheckBox(self.VProps_2)
        self.VPropsRopeProps.setObjectName(u"VPropsRopeProps")

        self.gridLayout_4.addWidget(self.VPropsRopeProps, 5, 0, 1, 1)

        self.ViewTab.addTab(self.VProps_2, "")
        self.VEffects = QWidget()
        self.VEffects.setObjectName(u"VEffects")
        self.verticalLayout_9 = QVBoxLayout(self.VEffects)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.VEffectsLabel3 = QLabel(self.VEffects)
        self.VEffectsLabel3.setObjectName(u"VEffectsLabel3")

        self.verticalLayout_9.addWidget(self.VEffectsLabel3)

        self.VEffectsList = QGridLayout()
        self.VEffectsList.setObjectName(u"VEffectsList")
        self.VEffectsLabel2 = QLabel(self.VEffects)
        self.VEffectsLabel2.setObjectName(u"VEffectsLabel2")

        self.VEffectsList.addWidget(self.VEffectsLabel2, 1, 0, 1, 1)

        self.VEffectsStrengthIndicator = QProgressBar(self.VEffects)
        self.VEffectsStrengthIndicator.setObjectName(u"VEffectsStrengthIndicator")
        self.VEffectsStrengthIndicator.setValue(23)
        self.VEffectsStrengthIndicator.setFormat(u"%p%")

        self.VEffectsList.addWidget(self.VEffectsStrengthIndicator, 2, 0, 1, 1)

        self.VEffectsLabel = QLabel(self.VEffects)
        self.VEffectsLabel.setObjectName(u"VEffectsLabel")

        self.VEffectsList.addWidget(self.VEffectsLabel, 5, 0, 1, 1)

        self.VEffectsDropdown = QComboBox(self.VEffects)
        self.VEffectsDropdown.setObjectName(u"VEffectsDropdown")

        self.VEffectsList.addWidget(self.VEffectsDropdown, 0, 0, 1, 1)

        self.VEffectsDial = QDial(self.VEffects)
        self.VEffectsDial.setObjectName(u"VEffectsDial")

        self.VEffectsList.addWidget(self.VEffectsDial, 3, 0, 1, 1)


        self.verticalLayout_9.addLayout(self.VEffectsList)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_9)

        self.ViewTab.addTab(self.VEffects, "")
        self.VMisc = QWidget()
        self.VMisc.setObjectName(u"VMisc")
        self.verticalLayout_11 = QVBoxLayout(self.VMisc)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.scrollArea_2 = QScrollArea(self.VMisc)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 257, 311))
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.VMiscLabel2 = QLabel(self.scrollAreaWidgetContents_2)
        self.VMiscLabel2.setObjectName(u"VMiscLabel2")

        self.verticalLayout_15.addWidget(self.VMiscLabel2)

        self.VMiscWater = QCheckBox(self.scrollAreaWidgetContents_2)
        self.VMiscWater.setObjectName(u"VMiscWater")

        self.verticalLayout_15.addWidget(self.VMiscWater)

        self.VMiscLightMap = QCheckBox(self.scrollAreaWidgetContents_2)
        self.VMiscLightMap.setObjectName(u"VMiscLightMap")

        self.verticalLayout_15.addWidget(self.VMiscLightMap)

        self.VMiscLabel1 = QLabel(self.scrollAreaWidgetContents_2)
        self.VMiscLabel1.setObjectName(u"VMiscLabel1")

        self.verticalLayout_15.addWidget(self.VMiscLabel1)

        self.VMiscLabelSessionTime = QLabel(self.scrollAreaWidgetContents_2)
        self.VMiscLabelSessionTime.setObjectName(u"VMiscLabelSessionTime")

        self.verticalLayout_15.addWidget(self.VMiscLabelSessionTime)

        self.VMiscLabelTotalTime = QLabel(self.scrollAreaWidgetContents_2)
        self.VMiscLabelTotalTime.setObjectName(u"VMiscLabelTotalTime")

        self.verticalLayout_15.addWidget(self.VMiscLabelTotalTime)

        self.VMiscLCDSessionTime = QLCDNumber(self.scrollAreaWidgetContents_2)
        self.VMiscLCDSessionTime.setObjectName(u"VMiscLCDSessionTime")

        self.verticalLayout_15.addWidget(self.VMiscLCDSessionTime)

        self.lcdNumber = QLCDNumber(self.scrollAreaWidgetContents_2)
        self.lcdNumber.setObjectName(u"lcdNumber")

        self.verticalLayout_15.addWidget(self.lcdNumber)

        self.VMiscLabel3 = QLabel(self.scrollAreaWidgetContents_2)
        self.VMiscLabel3.setObjectName(u"VMiscLabel3")

        self.verticalLayout_15.addWidget(self.VMiscLabel3)

        self.VMiscUndoTimeline = QUndoView(self.scrollAreaWidgetContents_2)
        self.VMiscUndoTimeline.setObjectName(u"VMiscUndoTimeline")

        self.verticalLayout_15.addWidget(self.VMiscUndoTimeline)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_11.addWidget(self.scrollArea_2)

        self.ViewTab.addTab(self.VMisc, "")

        self.verticalLayout_2.addWidget(self.ViewTab)

        self.DockView.setWidget(self.ViewDock)
        MainWindow.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.DockView)
        self.dockWidget_2 = QDockWidget(MainWindow)
        self.dockWidget_2.setObjectName(u"dockWidget_2")
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.label_14 = QLabel(self.dockWidgetContents_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 10, 131, 16))
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dockWidget_2)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menutools.menuAction())
        self.menubar.addAction(self.menuDrizzle.menuAction())
        self.menubar.addAction(self.menuMods.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.menuRecent.menuAction())
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuSettings.addAction(self.actionPreferences)
        self.menuSettings.addAction(self.actionHotkeys)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAbout_Qt)
        self.menuHelp.addAction(self.actionWiki_window)
        self.menuHelp.addAction(self.actionLediting_help)
        self.menuDrizzle.addAction(self.actionRender_2)
        self.menuDrizzle.addAction(self.actionOpen_2)
        self.menuMods.addAction(self.menuConfigure.menuAction())

        self.retranslateUi(MainWindow)

        self.ToolsTabs.setCurrentIndex(0)
        self.ViewTab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RWE#", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
#if QT_CONFIG(tooltip)
        self.actionNew.setToolTip(QCoreApplication.translate("MainWindow", u"New level", None))
#endif // QT_CONFIG(tooltip)
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionlevel1.setText(QCoreApplication.translate("MainWindow", u"level1", None))
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(tooltip)
        self.actionSave.setToolTip(QCoreApplication.translate("MainWindow", u"Save the level", None))
#endif // QT_CONFIG(tooltip)
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save As...", None))
        self.actionRedo.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionWiki_window.setText(QCoreApplication.translate("MainWindow", u"Wiki", None))
        self.actionAbout_Qt.setText(QCoreApplication.translate("MainWindow", u"About Qt", None))
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"Preferences...", None))
        self.actionRender.setText(QCoreApplication.translate("MainWindow", u"Render", None))
        self.actionexplode_leditor.setText(QCoreApplication.translate("MainWindow", u"explode leditor", None))
        self.actionLediting_help.setText(QCoreApplication.translate("MainWindow", u"Lediting help", None))
        self.actionRender_2.setText(QCoreApplication.translate("MainWindow", u"Render", None))
        self.actionHotkeys.setText(QCoreApplication.translate("MainWindow", u"Hotkeys", None))
        self.actionOpen_2.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.DockTools.setWindowTitle(QCoreApplication.translate("MainWindow", u"Editors", None))
#if QT_CONFIG(tooltip)
        self.ToolsTabs.setToolTip(QCoreApplication.translate("MainWindow", u"Toggle view for ceirtain objects", None))
#endif // QT_CONFIG(tooltip)
        self.ToolGeoaApply_to_Label.setText(QCoreApplication.translate("MainWindow", u"Apply to:", None))
        self.ToolGeoApplyToL1.setText(QCoreApplication.translate("MainWindow", u"Layer 1", None))
        self.ToolGeoApplyToL2.setText(QCoreApplication.translate("MainWindow", u"Layer 2", None))
        self.ToolGeoApplyToL3.setText(QCoreApplication.translate("MainWindow", u"Layer 3", None))
        self.ToolGeoM2Select.setItemText(0, QCoreApplication.translate("MainWindow", u"pencil", None))
        self.ToolGeoM2Select.setItemText(1, QCoreApplication.translate("MainWindow", u"brush", None))
        self.ToolGeoM2Select.setItemText(2, QCoreApplication.translate("MainWindow", u"bucket", None))
        self.ToolGeoM2Select.setItemText(3, QCoreApplication.translate("MainWindow", u"line", None))
        self.ToolGeoM2Select.setItemText(4, QCoreApplication.translate("MainWindow", u"rectangle tool", None))
        self.ToolGeoM2Select.setItemText(5, QCoreApplication.translate("MainWindow", u"hollow rectanlge", None))
        self.ToolGeoM2Select.setItemText(6, QCoreApplication.translate("MainWindow", u"circle", None))
        self.ToolGeoM2Select.setItemText(7, QCoreApplication.translate("MainWindow", u"hollow circle", None))

        self.ToolGeoM1Select.setItemText(0, QCoreApplication.translate("MainWindow", u"pencil", None))
        self.ToolGeoM1Select.setItemText(1, QCoreApplication.translate("MainWindow", u"brush", None))
        self.ToolGeoM1Select.setItemText(2, QCoreApplication.translate("MainWindow", u"bucket", None))
        self.ToolGeoM1Select.setItemText(3, QCoreApplication.translate("MainWindow", u"line", None))
        self.ToolGeoM1Select.setItemText(4, QCoreApplication.translate("MainWindow", u"rectangle tool", None))
        self.ToolGeoM1Select.setItemText(5, QCoreApplication.translate("MainWindow", u"hollow rectanlge", None))
        self.ToolGeoM1Select.setItemText(6, QCoreApplication.translate("MainWindow", u"circle", None))
        self.ToolGeoM1Select.setItemText(7, QCoreApplication.translate("MainWindow", u"hollow circle", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Right mouse:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Left mouse:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Mouse mode:", None))
        self.label_Blocks.setText(QCoreApplication.translate("MainWindow", u"Geomentry", None))
        self.ToolGeoWall.setText(QCoreApplication.translate("MainWindow", u"Wall", None))
        self.ToolGeoSlope.setText(QCoreApplication.translate("MainWindow", u"Slope", None))
        self.ToolGeoAir.setText(QCoreApplication.translate("MainWindow", u"Air", None))
        self.ToolGeoBeam.setText(QCoreApplication.translate("MainWindow", u"Beam", None))
        self.ToolGeoFloor.setText(QCoreApplication.translate("MainWindow", u"Floor", None))
        self.ToolGeoCrack.setText(QCoreApplication.translate("MainWindow", u"Crack", None))
        self.ToolGeoSpear.setText(QCoreApplication.translate("MainWindow", u"Spear", None))
        self.ToolGeoRock.setText(QCoreApplication.translate("MainWindow", u"Rock", None))
        self.ToolGeoGlass.setText(QCoreApplication.translate("MainWindow", u"Glass", None))
        self.ToolGeoHive.setText(QCoreApplication.translate("MainWindow", u"Fly hive", None))
        self.ToolGeoForbidChains.setText(QCoreApplication.translate("MainWindow", u"Forbid Fly\n"
"Chains", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Worm grass", None))
        self.ToolGeoLabelPipes.setText(QCoreApplication.translate("MainWindow", u"Pipes", None))
        self.ToolGeoShortcutEnterance.setText(QCoreApplication.translate("MainWindow", u"Shortcut Enterance", None))
        self.ToolGeoShortcut.setText(QCoreApplication.translate("MainWindow", u"Shortcut", None))
        self.ToolGeoDen.setText(QCoreApplication.translate("MainWindow", u"Den", None))
        self.ToolGeoEnterance.setText(QCoreApplication.translate("MainWindow", u"Enterance", None))
        self.ToolGeoWraykAMoleHole.setText(QCoreApplication.translate("MainWindow", u"Wrayk a mole hole", None))
        self.ToolGeoGarbageWorm.setText(QCoreApplication.translate("MainWindow", u"Garbage wrom den", None))
        self.ToolGeoScavHole.setText(QCoreApplication.translate("MainWindow", u"Scavanger Hole", None))
        self.ToolGeoLabelDeltieTools.setText(QCoreApplication.translate("MainWindow", u"Delete tools", None))
        self.ToolGeoClearUpperLayer.setText(QCoreApplication.translate("MainWindow", u"Clear upper layer", None))
        self.ToolGeoClearLayer.setText(QCoreApplication.translate("MainWindow", u"Clear layer", None))
        self.ToolGeoClearAll.setText(QCoreApplication.translate("MainWindow", u"Clear all", None))
        self.ToolGeoLabel.setText(QCoreApplication.translate("MainWindow", u"mass edit", None))
#if QT_CONFIG(tooltip)
        self.ToolGeoCopy.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>copy</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ToolGeoCopy.setText(QCoreApplication.translate("MainWindow", u"Copy tool", None))
        self.ToolGeoPaste.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
        self.ToolGeoMirror.setText(QCoreApplication.translate("MainWindow", u"Mirror", None))
        self.ToolGeoInvert.setText(QCoreApplication.translate("MainWindow", u"Invert", None))
        self.ToolGeoMove.setText(QCoreApplication.translate("MainWindow", u"Move", None))
        self.ToolsTabs.setTabText(self.ToolsTabs.indexOf(self.ToolsGeo), QCoreApplication.translate("MainWindow", u"Geo", None))
        self.ToolTilesSetAsDefault.setText(QCoreApplication.translate("MainWindow", u"Set default", None))
        self.ToolTilesM1Select.setItemText(0, QCoreApplication.translate("MainWindow", u"pencil", None))
        self.ToolTilesM1Select.setItemText(1, QCoreApplication.translate("MainWindow", u"Delite", None))
        self.ToolTilesM1Select.setItemText(2, QCoreApplication.translate("MainWindow", u"brush", None))
        self.ToolTilesM1Select.setItemText(3, QCoreApplication.translate("MainWindow", u"bucket", None))
        self.ToolTilesM1Select.setItemText(4, QCoreApplication.translate("MainWindow", u"line", None))
        self.ToolTilesM1Select.setItemText(5, QCoreApplication.translate("MainWindow", u"rectangle tool", None))
        self.ToolTilesM1Select.setItemText(6, QCoreApplication.translate("MainWindow", u"hollow rectanlge", None))
        self.ToolTilesM1Select.setItemText(7, QCoreApplication.translate("MainWindow", u"circle", None))
        self.ToolTilesM1Select.setItemText(8, QCoreApplication.translate("MainWindow", u"hollow circle", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Right mouse ", None))
        self.ToolTilesM2Select.setItemText(0, QCoreApplication.translate("MainWindow", u"Delite", None))
        self.ToolTilesM2Select.setItemText(1, QCoreApplication.translate("MainWindow", u"pencil", None))
        self.ToolTilesM2Select.setItemText(2, QCoreApplication.translate("MainWindow", u"brush", None))
        self.ToolTilesM2Select.setItemText(3, QCoreApplication.translate("MainWindow", u"bucket", None))
        self.ToolTilesM2Select.setItemText(4, QCoreApplication.translate("MainWindow", u"line", None))
        self.ToolTilesM2Select.setItemText(5, QCoreApplication.translate("MainWindow", u"rectangle tool", None))
        self.ToolTilesM2Select.setItemText(6, QCoreApplication.translate("MainWindow", u"hollow rectanlge", None))
        self.ToolTilesM2Select.setItemText(7, QCoreApplication.translate("MainWindow", u"circle", None))
        self.ToolTilesM2Select.setItemText(8, QCoreApplication.translate("MainWindow", u"hollow circle", None))

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Brush size", None))
        self.ToolTilesPaste.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
        self.ToolTilesCopy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Left mouse", None))
        self.ToolTilesSelectTool.setText(QCoreApplication.translate("MainWindow", u"Selection tool", None))
        self.ToolsTabs.setTabText(self.ToolsTabs.indexOf(self.ToolsTiles), QCoreApplication.translate("MainWindow", u"Tiles", None))
        self.ToolPropsSelectTool.setText(QCoreApplication.translate("MainWindow", u"Select tool", None))
        self.ToolPropsDelite.setText(QCoreApplication.translate("MainWindow", u"Delite selected", None))
        self.ToolPropsMoveSelected.setText(QCoreApplication.translate("MainWindow", u"Move selected", None))
        self.ToolPropsLabel_11.setText(QCoreApplication.translate("MainWindow", u"Prop properties", None))
        self.ToolPropsLabel_10.setText(QCoreApplication.translate("MainWindow", u"Size Y", None))
        self.ToolPropsLabel_9.setText(QCoreApplication.translate("MainWindow", u"Size X", None))
        self.ToolPropsLabel_8.setText(QCoreApplication.translate("MainWindow", u"Rotation", None))
        self.ToolPropsLabel.setText(QCoreApplication.translate("MainWindow", u"Render order", None))
        self.ToolPropsLabel_2.setText(QCoreApplication.translate("MainWindow", u"Render time ", None))
        self.ToolPropsLabel_3.setText(QCoreApplication.translate("MainWindow", u"Seed", None))
        self.ToolPropsLabel_4.setText(QCoreApplication.translate("MainWindow", u"Release", None))
        self.ToolPropsLabel_6.setText(QCoreApplication.translate("MainWindow", u"Variation", None))
        self.ToolPropsLabel_5.setText(QCoreApplication.translate("MainWindow", u"Custom depth", None))
        self.ToolPropsApplyColor.setText("")
        self.ToolPropsLabel_7.setText(QCoreApplication.translate("MainWindow", u"Apply colour", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Props:", None))
        self.ToolsTabs.setTabText(self.ToolsTabs.indexOf(self.ToolsProps), QCoreApplication.translate("MainWindow", u"Props", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Layers", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Move down", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Move up", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Delite current", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Coppy area", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Duplicate", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Layer properties", None))
        self.ToolsTabs.setTabText(self.ToolsTabs.indexOf(self.ToolsEffects), QCoreApplication.translate("MainWindow", u"Effects", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Scale y", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Rotation", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Scale x", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Distance", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Angle", None))
        self.ToolsTabs.setTabText(self.ToolsTabs.indexOf(self.ToolsLight), QCoreApplication.translate("MainWindow", u"light", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Level size ", None))
        self.ToolsPropertiesLabel.setText(QCoreApplication.translate("MainWindow", u"Size x", None))
        self.ToolsPropertiesLabel_3.setText(QCoreApplication.translate("MainWindow", u"Border size x", None))
        self.ToolsPropertiesWaterSettings.setItemText(0, QCoreApplication.translate("MainWindow", u"No water", None))
        self.ToolsPropertiesWaterSettings.setItemText(1, QCoreApplication.translate("MainWindow", u"infront ", None))
        self.ToolsPropertiesWaterSettings.setItemText(2, QCoreApplication.translate("MainWindow", u"behind", None))

        self.ToolsPropertiesLabel_5.setText(QCoreApplication.translate("MainWindow", u"Water height", None))
        self.ToolsPropertiesSun.setText(QCoreApplication.translate("MainWindow", u"Sunlight", None))
        self.ToolsPropertiesLabel_2.setText(QCoreApplication.translate("MainWindow", u"Size y", None))
        self.ToolsPropertiesLabel_4.setText(QCoreApplication.translate("MainWindow", u"Border size", None))
        self.ToolsPropertiesLabel_6.setText(QCoreApplication.translate("MainWindow", u"Water Properties", None))
        self.ToolsPropertiesLabel_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ToolsPropertiesLabel_9.setText(QCoreApplication.translate("MainWindow", u"Tile seed", None))
        self.ToolsTabs.setTabText(self.ToolsTabs.indexOf(self.ToolsProperties), QCoreApplication.translate("MainWindow", u"Properties", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuRecent.setTitle(QCoreApplication.translate("MainWindow", u"Recent...", None))
        self.menuWindow.setTitle(QCoreApplication.translate("MainWindow", u"Window", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menutools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.menuDrizzle.setTitle(QCoreApplication.translate("MainWindow", u"Drizzle", None))
        self.menuMods.setTitle(QCoreApplication.translate("MainWindow", u"Mods", None))
        self.menuConfigure.setTitle(QCoreApplication.translate("MainWindow", u"Configure", None))
        self.DockView.setWindowTitle(QCoreApplication.translate("MainWindow", u"VIew", None))
        self.VQuickLabel.setText(QCoreApplication.translate("MainWindow", u"Overlay of layers:", None))
        self.VQuickGeo.setText(QCoreApplication.translate("MainWindow", u"Geo", None))
        self.VQuickTiles.setText(QCoreApplication.translate("MainWindow", u"Tiles", None))
        self.VQuickProps.setText(QCoreApplication.translate("MainWindow", u"props", None))
        self.VQuickCammeras.setText(QCoreApplication.translate("MainWindow", u"Cameras", None))
        self.VQuickEffects.setText(QCoreApplication.translate("MainWindow", u"Effects", None))
        self.VQuickWater.setText(QCoreApplication.translate("MainWindow", u"Water", None))
        self.VQuickLightmap.setText(QCoreApplication.translate("MainWindow", u"Lightmap", None))
        self.ViewTab.setTabText(self.ViewTab.indexOf(self.VQuick), QCoreApplication.translate("MainWindow", u"Quick", None))
        self.VGeoBeams.setText(QCoreApplication.translate("MainWindow", u"Beams", None))
        self.VGeoRWEstyle.setText(QCoreApplication.translate("MainWindow", u"RWE+ geo view", None))
        self.VGeolabel.setText(QCoreApplication.translate("MainWindow", u"Toggle visibility of:", None))
        self.VGeoMisc.setText(QCoreApplication.translate("MainWindow", u"misc", None))
        self.VGeoAll.setText(QCoreApplication.translate("MainWindow", u"All geo", None))
        self.VGeoLayer2.setText(QCoreApplication.translate("MainWindow", u"Layer 2", None))
        self.VGeoLayer1.setText(QCoreApplication.translate("MainWindow", u"Layer 1", None))
        self.VGeoThrowables.setText(QCoreApplication.translate("MainWindow", u"Pipes", None))
        self.VGeoLayer3.setText(QCoreApplication.translate("MainWindow", u"Layer 3", None))
        self.VGeoOldStyle.setText(QCoreApplication.translate("MainWindow", u"Old style view", None))
        self.ViewTab.setTabText(self.ViewTab.indexOf(self.VGeo), QCoreApplication.translate("MainWindow", u"Geo", None))
        self.VTilesMaterialsLabel.setText(QCoreApplication.translate("MainWindow", u"Toggle visibility of:", None))
        self.VTilesAllTiles.setText(QCoreApplication.translate("MainWindow", u"All tiles", None))
        self.VTilesLayer1.setText(QCoreApplication.translate("MainWindow", u"Layer 1", None))
        self.VTilesLayer2.setText(QCoreApplication.translate("MainWindow", u"Layer 2", None))
        self.VTilesLayer3.setText(QCoreApplication.translate("MainWindow", u"Layer 3", None))
        self.VTilesMaterials.setText(QCoreApplication.translate("MainWindow", u"Materials", None))
        self.VTilesMaterialsOldPreview.setText(QCoreApplication.translate("MainWindow", u"Classic tile preview", None))
        self.VTilesMaterialBetterPreview.setText(QCoreApplication.translate("MainWindow", u"Better tile preview", None))
        self.VTilesHeads.setText(QCoreApplication.translate("MainWindow", u"Tile heads", None))
        self.ViewTab.setTabText(self.ViewTab.indexOf(self.VTiles), QCoreApplication.translate("MainWindow", u"Tiles", None))
        self.VPropsLabel.setText(QCoreApplication.translate("MainWindow", u"Toggle visibility of:", None))
        self.VPropsHead.setText(QCoreApplication.translate("MainWindow", u"Prop headers", None))
        self.VPropsAllProps.setText(QCoreApplication.translate("MainWindow", u"All props", None))
        self.VPropsLayer3.setText(QCoreApplication.translate("MainWindow", u"Layer 3", None))
        self.VPropsDestructionProps.setText(QCoreApplication.translate("MainWindow", u"Destruction Props", None))
        self.VPropsLayer1.setText(QCoreApplication.translate("MainWindow", u"Layer 1", None))
        self.VPropsLongProps.setText(QCoreApplication.translate("MainWindow", u"Long type props", None))
        self.VPropsSoftProps.setText(QCoreApplication.translate("MainWindow", u"Soft props", None))
        self.VPropsLayer2.setText(QCoreApplication.translate("MainWindow", u"Layer 2", None))
        self.VPropsRopeProps.setText(QCoreApplication.translate("MainWindow", u"Rope props", None))
        self.ViewTab.setTabText(self.ViewTab.indexOf(self.VProps_2), QCoreApplication.translate("MainWindow", u"Props", None))
        self.VEffectsLabel3.setText(QCoreApplication.translate("MainWindow", u"Select Effects layer", None))
        self.VEffectsLabel2.setText(QCoreApplication.translate("MainWindow", u"Overlay strength", None))
        self.VEffectsLabel.setText(QCoreApplication.translate("MainWindow", u"Usless knob lives", None))
        self.ViewTab.setTabText(self.ViewTab.indexOf(self.VEffects), QCoreApplication.translate("MainWindow", u"Effects", None))
        self.VMiscLabel2.setText(QCoreApplication.translate("MainWindow", u"Toggle view of:", None))
        self.VMiscWater.setText(QCoreApplication.translate("MainWindow", u"Water", None))
        self.VMiscLightMap.setText(QCoreApplication.translate("MainWindow", u"Light map", None))
        self.VMiscLabel1.setText(QCoreApplication.translate("MainWindow", u"More will come", None))
        self.VMiscLabelSessionTime.setText(QCoreApplication.translate("MainWindow", u"Session time", None))
        self.VMiscLabelTotalTime.setText(QCoreApplication.translate("MainWindow", u"Total level file time", None))
        self.VMiscLabel3.setText(QCoreApplication.translate("MainWindow", u"Undo history:", None))
        self.ViewTab.setTabText(self.ViewTab.indexOf(self.VMisc), QCoreApplication.translate("MainWindow", u"Misc", None))
        self.dockWidget_2.setWindowTitle(QCoreApplication.translate("MainWindow", u"Prefabs", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Prefabs idk", None))
    # retranslateUi

