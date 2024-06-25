# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tileexplorer.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListView,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QSizePolicy, QSpacerItem, QSplitter, QStatusBar,
    QTableWidget, QTableWidgetItem, QToolButton, QVBoxLayout,
    QWidget)

from BaseModWidgets import TilePreview
import ui.res_rc

class Ui_TileExplorer(object):
    def setupUi(self, TileExplorer):
        if not TileExplorer.objectName():
            TileExplorer.setObjectName(u"TileExplorer")
        TileExplorer.resize(800, 600)
        self.centralwidget = QWidget(TileExplorer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.SearchBar = QLineEdit(self.centralwidget)
        self.SearchBar.setObjectName(u"SearchBar")
        self.SearchBar.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.SearchBar.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.SearchBar)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.CatsTab = QWidget(self.splitter)
        self.CatsTab.setObjectName(u"CatsTab")
        self.verticalLayout_2 = QVBoxLayout(self.CatsTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.label = QLabel(self.CatsTab)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.Categories = QListWidget(self.CatsTab)
        self.Categories.setObjectName(u"Categories")
        self.Categories.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.Categories.setAlternatingRowColors(True)
        self.Categories.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.Categories.setMovement(QListView.Movement.Static)
        self.Categories.setFlow(QListView.Flow.TopToBottom)
        self.Categories.setResizeMode(QListView.ResizeMode.Adjust)
        self.Categories.setLayoutMode(QListView.LayoutMode.SinglePass)
        self.Categories.setViewMode(QListView.ViewMode.ListMode)
        self.Categories.setUniformItemSizes(True)
        self.Categories.setSelectionRectVisible(False)

        self.verticalLayout_2.addWidget(self.Categories)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.CatsAddCC = QToolButton(self.CatsTab)
        self.CatsAddCC.setObjectName(u"CatsAddCC")
        icon = QIcon(QIcon.fromTheme(u"list-add"))
        self.CatsAddCC.setIcon(icon)
        self.CatsAddCC.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout.addWidget(self.CatsAddCC)

        self.CatsRemoveCC = QToolButton(self.CatsTab)
        self.CatsRemoveCC.setObjectName(u"CatsRemoveCC")
        icon1 = QIcon(QIcon.fromTheme(u"list-remove"))
        self.CatsRemoveCC.setIcon(icon1)

        self.horizontalLayout.addWidget(self.CatsRemoveCC)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.splitter.addWidget(self.CatsTab)
        self.TilesTab = QWidget(self.splitter)
        self.TilesTab.setObjectName(u"TilesTab")
        self.verticalLayout_3 = QVBoxLayout(self.TilesTab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.label_2 = QLabel(self.TilesTab)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.Tiles = QListWidget(self.TilesTab)
        self.Tiles.setObjectName(u"Tiles")
        self.Tiles.setMouseTracking(True)
        self.Tiles.setAutoFillBackground(True)
        self.Tiles.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.Tiles.setAlternatingRowColors(True)
        self.Tiles.setResizeMode(QListView.ResizeMode.Fixed)
        self.Tiles.setLayoutMode(QListView.LayoutMode.SinglePass)
        self.Tiles.setSpacing(10)
        self.Tiles.setViewMode(QListView.ViewMode.IconMode)

        self.verticalLayout_3.addWidget(self.Tiles)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.TilesListView = QToolButton(self.TilesTab)
        self.TilesListView.setObjectName(u"TilesListView")
        icon2 = QIcon()
        icon2.addFile(u":/grids/grid/list.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.TilesListView.setIcon(icon2)
        self.TilesListView.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout_2.addWidget(self.TilesListView)

        self.TilesGridViewBig = QToolButton(self.TilesTab)
        self.TilesGridViewBig.setObjectName(u"TilesGridViewBig")
        icon3 = QIcon()
        icon3.addFile(u":/grids/grid/mediumgrid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.TilesGridViewBig.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.TilesGridViewBig)

        self.TilesGridViewSmall = QToolButton(self.TilesTab)
        self.TilesGridViewSmall.setObjectName(u"TilesGridViewSmall")
        icon4 = QIcon()
        icon4.addFile(u":/grids/grid/smallgrid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.TilesGridViewSmall.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.TilesGridViewSmall)

        self.TilesIconView = QToolButton(self.TilesTab)
        self.TilesIconView.setObjectName(u"TilesIconView")
        icon5 = QIcon()
        icon5.addFile(u":/grids/grid/smallgrid2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.TilesIconView.setIcon(icon5)

        self.horizontalLayout_2.addWidget(self.TilesIconView)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.TilesClassic = QToolButton(self.TilesTab)
        self.TilesClassic.setObjectName(u"TilesClassic")

        self.horizontalLayout_2.addWidget(self.TilesClassic)

        self.TilesImage = QToolButton(self.TilesTab)
        self.TilesImage.setObjectName(u"TilesImage")

        self.horizontalLayout_2.addWidget(self.TilesImage)

        self.TilesUnrendered = QToolButton(self.TilesTab)
        self.TilesUnrendered.setObjectName(u"TilesUnrendered")

        self.horizontalLayout_2.addWidget(self.TilesUnrendered)

        self.TilesRendered = QToolButton(self.TilesTab)
        self.TilesRendered.setObjectName(u"TilesRendered")

        self.horizontalLayout_2.addWidget(self.TilesRendered)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.splitter.addWidget(self.TilesTab)
        self.TileTab = QWidget(self.splitter)
        self.TileTab.setObjectName(u"TileTab")
        self.verticalLayout_4 = QVBoxLayout(self.TileTab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.label_3 = QLabel(self.TileTab)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.Preview = TilePreview(self.TileTab)
        self.Preview.setObjectName(u"Preview")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.Preview.sizePolicy().hasHeightForWidth())
        self.Preview.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.Preview)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.OnetoOne = QToolButton(self.TileTab)
        self.OnetoOne.setObjectName(u"OnetoOne")
        self.OnetoOne.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout_6.addWidget(self.OnetoOne)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.Properties = QTableWidget(self.TileTab)
        if (self.Properties.columnCount() < 1):
            self.Properties.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.Properties.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.Properties.rowCount() < 3):
            self.Properties.setRowCount(3)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.Properties.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.Properties.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.Properties.setVerticalHeaderItem(2, __qtablewidgetitem3)
        self.Properties.setObjectName(u"Properties")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Properties.sizePolicy().hasHeightForWidth())
        self.Properties.setSizePolicy(sizePolicy1)
        self.Properties.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.Properties.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.Properties.setAlternatingRowColors(False)
        self.Properties.setShowGrid(False)
        self.Properties.setGridStyle(Qt.PenStyle.NoPen)
        self.Properties.setSortingEnabled(False)
        self.Properties.setCornerButtonEnabled(True)
        self.Properties.horizontalHeader().setVisible(False)
        self.Properties.horizontalHeader().setHighlightSections(True)
        self.Properties.verticalHeader().setMinimumSectionSize(20)
        self.Properties.verticalHeader().setDefaultSectionSize(20)
        self.Properties.verticalHeader().setHighlightSections(True)

        self.verticalLayout_4.addWidget(self.Properties)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.toolButton_9 = QToolButton(self.TileTab)
        self.toolButton_9.setObjectName(u"toolButton_9")
        icon6 = QIcon(QIcon.fromTheme(u"emblem-favorite"))
        self.toolButton_9.setIcon(icon6)
        self.toolButton_9.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout_5.addWidget(self.toolButton_9)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.splitter.addWidget(self.TileTab)

        self.verticalLayout.addWidget(self.splitter)

        TileExplorer.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(TileExplorer)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        TileExplorer.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(TileExplorer)
        self.statusbar.setObjectName(u"statusbar")
        TileExplorer.setStatusBar(self.statusbar)

        self.retranslateUi(TileExplorer)

        QMetaObject.connectSlotsByName(TileExplorer)
    # setupUi

    def retranslateUi(self, TileExplorer):
        TileExplorer.setWindowTitle(QCoreApplication.translate("TileExplorer", u"Tile Explorer", None))
        self.SearchBar.setInputMask("")
        self.SearchBar.setPlaceholderText(QCoreApplication.translate("TileExplorer", u"Search", None))
        self.label.setText(QCoreApplication.translate("TileExplorer", u"Categories", None))
        self.CatsAddCC.setText("")
        self.CatsRemoveCC.setText("")
        self.label_2.setText(QCoreApplication.translate("TileExplorer", u"Tiles", None))
        self.TilesListView.setText("")
        self.TilesGridViewBig.setText("")
        self.TilesGridViewSmall.setText("")
        self.TilesIconView.setText("")
        self.TilesClassic.setText(QCoreApplication.translate("TileExplorer", u"C", None))
        self.TilesImage.setText(QCoreApplication.translate("TileExplorer", u"T", None))
        self.TilesUnrendered.setText(QCoreApplication.translate("TileExplorer", u"U", None))
        self.TilesRendered.setText(QCoreApplication.translate("TileExplorer", u"R", None))
        self.label_3.setText(QCoreApplication.translate("TileExplorer", u"Tile", None))
        self.OnetoOne.setText(QCoreApplication.translate("TileExplorer", u"1:1", None))
        ___qtablewidgetitem = self.Properties.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("TileExplorer", u"Value", None));
        ___qtablewidgetitem1 = self.Properties.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("TileExplorer", u"Name", None));
        ___qtablewidgetitem2 = self.Properties.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("TileExplorer", u"Size", None));
        ___qtablewidgetitem3 = self.Properties.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("TileExplorer", u"Category", None));
        self.toolButton_9.setText("")
    # retranslateUi

