# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'explorer2.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QDockWidget, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListView, QListWidget, QListWidgetItem,
    QSizePolicy, QSpacerItem, QSplitter, QTableWidget,
    QTableWidgetItem, QToolButton, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

from RWESharpWidgets import SimpleViewport
import ui.res_rc

class Ui_Explorer(object):
    def setupUi(self, Explorer):
        if not Explorer.objectName():
            Explorer.setObjectName(u"Explorer")
        Explorer.resize(907, 606)
        Explorer.setFloating(False)
        Explorer.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetClosable|QDockWidget.DockWidgetFeature.DockWidgetFloatable|QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout_7 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.SearchBar = QLineEdit(self.dockWidgetContents)
        self.SearchBar.setObjectName(u"SearchBar")
        self.SearchBar.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.SearchBar.setClearButtonEnabled(True)

        self.verticalLayout_7.addWidget(self.SearchBar)

        self.splitter_3 = QSplitter(self.dockWidgetContents)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Orientation.Horizontal)
        self.splitter = QSplitter(self.splitter_3)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.CatsTab = QWidget(self.splitter)
        self.CatsTab.setObjectName(u"CatsTab")
        self.verticalLayout_2 = QVBoxLayout(self.CatsTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.LCategories = QLabel(self.CatsTab)
        self.LCategories.setObjectName(u"LCategories")

        self.verticalLayout_2.addWidget(self.LCategories)

        self.Categories = QTreeWidget(self.CatsTab)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.Categories.setHeaderItem(__qtreewidgetitem)
        self.Categories.setObjectName(u"Categories")
        self.Categories.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.Categories.setAlternatingRowColors(True)
        self.Categories.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.Categories.header().setVisible(False)

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

        self.CatPrev = QToolButton(self.CatsTab)
        self.CatPrev.setObjectName(u"CatPrev")
        self.CatPrev.setArrowType(Qt.ArrowType.LeftArrow)

        self.horizontalLayout.addWidget(self.CatPrev)

        self.CatNext = QToolButton(self.CatsTab)
        self.CatNext.setObjectName(u"CatNext")
        self.CatNext.setArrowType(Qt.ArrowType.RightArrow)

        self.horizontalLayout.addWidget(self.CatNext)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.splitter.addWidget(self.CatsTab)
        self.ItemsTab = QWidget(self.splitter)
        self.ItemsTab.setObjectName(u"ItemsTab")
        self.verticalLayout_3 = QVBoxLayout(self.ItemsTab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.LItems = QLabel(self.ItemsTab)
        self.LItems.setObjectName(u"LItems")

        self.verticalLayout_3.addWidget(self.LItems)

        self.Items = QListWidget(self.ItemsTab)
        self.Items.setObjectName(u"Items")
        self.Items.setMouseTracking(True)
        self.Items.setAutoFillBackground(True)
        self.Items.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.Items.setAlternatingRowColors(True)
        self.Items.setResizeMode(QListView.ResizeMode.Fixed)
        self.Items.setLayoutMode(QListView.LayoutMode.SinglePass)
        self.Items.setSpacing(10)
        self.Items.setViewMode(QListView.ViewMode.IconMode)

        self.verticalLayout_3.addWidget(self.Items)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.TilesListView = QToolButton(self.ItemsTab)
        self.TilesListView.setObjectName(u"TilesListView")
        icon2 = QIcon()
        icon2.addFile(u":/grids/grid/list.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.TilesListView.setIcon(icon2)
        self.TilesListView.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout_2.addWidget(self.TilesListView)

        self.TilesGridViewBig = QToolButton(self.ItemsTab)
        self.TilesGridViewBig.setObjectName(u"TilesGridViewBig")
        icon3 = QIcon()
        icon3.addFile(u":/grids/grid/mediumgrid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.TilesGridViewBig.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.TilesGridViewBig)

        self.TilesGridViewSmall = QToolButton(self.ItemsTab)
        self.TilesGridViewSmall.setObjectName(u"TilesGridViewSmall")
        icon4 = QIcon()
        icon4.addFile(u":/grids/grid/smallgrid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.TilesGridViewSmall.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.TilesGridViewSmall)

        self.TilesIconView = QToolButton(self.ItemsTab)
        self.TilesIconView.setObjectName(u"TilesIconView")
        icon5 = QIcon()
        icon5.addFile(u":/grids/grid/smallgrid2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.TilesIconView.setIcon(icon5)

        self.horizontalLayout_2.addWidget(self.TilesIconView)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.TilePrev = QToolButton(self.ItemsTab)
        self.TilePrev.setObjectName(u"TilePrev")
        self.TilePrev.setArrowType(Qt.ArrowType.UpArrow)

        self.horizontalLayout_2.addWidget(self.TilePrev)

        self.TileNext = QToolButton(self.ItemsTab)
        self.TileNext.setObjectName(u"TileNext")
        self.TileNext.setArrowType(Qt.ArrowType.DownArrow)

        self.horizontalLayout_2.addWidget(self.TileNext)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.splitter.addWidget(self.ItemsTab)
        self.splitter_3.addWidget(self.splitter)
        self.splitter_2 = QSplitter(self.splitter_3)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Vertical)
        self.ItemTab = QWidget(self.splitter_2)
        self.ItemTab.setObjectName(u"ItemTab")
        self.verticalLayout_4 = QVBoxLayout(self.ItemTab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.LItem = QLabel(self.ItemTab)
        self.LItem.setObjectName(u"LItem")

        self.verticalLayout_4.addWidget(self.LItem)

        self.Preview = SimpleViewport(self.ItemTab)
        self.Preview.setObjectName(u"Preview")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.Preview.sizePolicy().hasHeightForWidth())
        self.Preview.setSizePolicy(sizePolicy)
        self.Preview.setMouseTracking(True)

        self.verticalLayout_4.addWidget(self.Preview)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.OnetoOne = QToolButton(self.ItemTab)
        self.OnetoOne.setObjectName(u"OnetoOne")
        self.OnetoOne.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout_6.addWidget(self.OnetoOne)

        self.FitInScreen = QToolButton(self.ItemTab)
        self.FitInScreen.setObjectName(u"FitInScreen")
        self.FitInScreen.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout_6.addWidget(self.FitInScreen)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        self.ToggleCollisions = QToolButton(self.ItemTab)
        self.ToggleCollisions.setObjectName(u"ToggleCollisions")
        self.ToggleCollisions.setCheckable(True)
        self.ToggleCollisions.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout_6.addWidget(self.ToggleCollisions)

        self.TogglePreview = QToolButton(self.ItemTab)
        self.TogglePreview.setObjectName(u"TogglePreview")
        self.TogglePreview.setCheckable(True)
        self.TogglePreview.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout_6.addWidget(self.TogglePreview)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.splitter_2.addWidget(self.ItemTab)
        self.ItemInfo = QWidget(self.splitter_2)
        self.ItemInfo.setObjectName(u"ItemInfo")
        self.verticalLayout_6 = QVBoxLayout(self.ItemInfo)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, 0, -1)
        self.LItem_2 = QLabel(self.ItemInfo)
        self.LItem_2.setObjectName(u"LItem_2")

        self.verticalLayout_6.addWidget(self.LItem_2)

        self.Properties = QTableWidget(self.ItemInfo)
        if (self.Properties.columnCount() < 1):
            self.Properties.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.Properties.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.Properties.setObjectName(u"Properties")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
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

        self.verticalLayout_6.addWidget(self.Properties)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.Favourite = QToolButton(self.ItemInfo)
        self.Favourite.setObjectName(u"Favourite")
        icon6 = QIcon(QIcon.fromTheme(u"emblem-favorite"))
        self.Favourite.setIcon(icon6)
        self.Favourite.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout_9.addWidget(self.Favourite)

        self.Pin = QToolButton(self.ItemInfo)
        self.Pin.setObjectName(u"Pin")
        icon7 = QIcon()
        icon7.addFile(u":/special/special/pin.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Pin.setIcon(icon7)
        self.Pin.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout_9.addWidget(self.Pin)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)

        self.RenderOption = QComboBox(self.ItemInfo)
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.setObjectName(u"RenderOption")

        self.horizontalLayout_9.addWidget(self.RenderOption)

        self.LayerBox = QComboBox(self.ItemInfo)
        self.LayerBox.addItem("")
        self.LayerBox.addItem("")
        self.LayerBox.addItem("")
        self.LayerBox.setObjectName(u"LayerBox")

        self.horizontalLayout_9.addWidget(self.LayerBox)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.splitter_2.addWidget(self.ItemInfo)
        self.splitter_3.addWidget(self.splitter_2)

        self.verticalLayout_7.addWidget(self.splitter_3)

        Explorer.setWidget(self.dockWidgetContents)

        self.retranslateUi(Explorer)

        QMetaObject.connectSlotsByName(Explorer)
    # setupUi

    def retranslateUi(self, Explorer):
        Explorer.setWindowTitle(QCoreApplication.translate("Explorer", u"Explorer", None))
        self.SearchBar.setInputMask("")
        self.SearchBar.setPlaceholderText(QCoreApplication.translate("Explorer", u"Search", None))
        self.LCategories.setText(QCoreApplication.translate("Explorer", u"Categories", None))
        self.CatsAddCC.setText("")
        self.CatsRemoveCC.setText("")
        self.CatPrev.setText(QCoreApplication.translate("Explorer", u"...", None))
        self.CatNext.setText(QCoreApplication.translate("Explorer", u"...", None))
        self.LItems.setText(QCoreApplication.translate("Explorer", u"Items", None))
        self.TilesListView.setText("")
        self.TilesGridViewBig.setText("")
        self.TilesGridViewSmall.setText("")
        self.TilesIconView.setText("")
        self.TilePrev.setText(QCoreApplication.translate("Explorer", u"...", None))
        self.TileNext.setText(QCoreApplication.translate("Explorer", u"...", None))
        self.LItem.setText(QCoreApplication.translate("Explorer", u"Item", None))
        self.OnetoOne.setText(QCoreApplication.translate("Explorer", u"1:1", None))
        self.FitInScreen.setText(QCoreApplication.translate("Explorer", u"Fit", None))
        self.ToggleCollisions.setText(QCoreApplication.translate("Explorer", u"Collisions", None))
        self.TogglePreview.setText(QCoreApplication.translate("Explorer", u"Preview", None))
        self.LItem_2.setText(QCoreApplication.translate("Explorer", u"Item Info", None))
        ___qtablewidgetitem = self.Properties.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Explorer", u"Value", None));
        self.Favourite.setText("")
        self.Pin.setText(QCoreApplication.translate("Explorer", u"Pin", None))
        self.RenderOption.setItemText(0, QCoreApplication.translate("Explorer", u"Classic", None))
        self.RenderOption.setItemText(1, QCoreApplication.translate("Explorer", u"Tile image", None))
        self.RenderOption.setItemText(2, QCoreApplication.translate("Explorer", u"Henry", None))
        self.RenderOption.setItemText(3, QCoreApplication.translate("Explorer", u"Unrendered", None))
        self.RenderOption.setItemText(4, QCoreApplication.translate("Explorer", u"Rendered (sun)", None))
        self.RenderOption.setItemText(5, QCoreApplication.translate("Explorer", u"Rendered (shaded)", None))
        self.RenderOption.setItemText(6, QCoreApplication.translate("Explorer", u"Rendered (rain)", None))
        self.RenderOption.setItemText(7, QCoreApplication.translate("Explorer", u"Sync", None))

        self.LayerBox.setItemText(0, QCoreApplication.translate("Explorer", u"1", None))
        self.LayerBox.setItemText(1, QCoreApplication.translate("Explorer", u"2", None))
        self.LayerBox.setItemText(2, QCoreApplication.translate("Explorer", u"3", None))

    # retranslateUi

