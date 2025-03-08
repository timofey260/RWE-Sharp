# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'explorerqSmnDM.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
    QDockWidget, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListView,
    QListWidget, QListWidgetItem, QSizePolicy, QSpacerItem,
    QSplitter, QTableWidget, QTableWidgetItem, QToolButton,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

from RWESharpWidgets import SimpleViewport


class Ui_Explorer(object):
    def setupUi(self, Explorer):
        if not Explorer.objectName():
            Explorer.setObjectName(u"Explorer")
        Explorer.resize(421, 666)
        Explorer.setFloating(False)
        Explorer.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetClosable|QDockWidget.DockWidgetFeature.DockWidgetFloatable|QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout = QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.LCategories = QLabel(self.dockWidgetContents)
        self.LCategories.setObjectName(u"LCategories")

        self.gridLayout.addWidget(self.LCategories, 1, 0, 1, 1)

        self.frame = QFrame(self.dockWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(250, 16777215))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.CatsAddCC = QToolButton(self.frame)
        self.CatsAddCC.setObjectName(u"CatsAddCC")
        icon = QIcon(QIcon.fromTheme(u"list-add"))
        self.CatsAddCC.setIcon(icon)
        self.CatsAddCC.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout_3.addWidget(self.CatsAddCC)

        self.CatsRemoveCC = QToolButton(self.frame)
        self.CatsRemoveCC.setObjectName(u"CatsRemoveCC")
        icon1 = QIcon(QIcon.fromTheme(u"list-remove"))
        self.CatsRemoveCC.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.CatsRemoveCC)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.CatPrev = QToolButton(self.frame)
        self.CatPrev.setObjectName(u"CatPrev")
        self.CatPrev.setArrowType(Qt.ArrowType.LeftArrow)

        self.horizontalLayout_3.addWidget(self.CatPrev)

        self.CatNext = QToolButton(self.frame)
        self.CatNext.setObjectName(u"CatNext")
        self.CatNext.setArrowType(Qt.ArrowType.RightArrow)

        self.horizontalLayout_3.addWidget(self.CatNext)


        self.gridLayout.addWidget(self.frame, 4, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.OnetoOne = QToolButton(self.dockWidgetContents)
        self.OnetoOne.setObjectName(u"OnetoOne")
        self.OnetoOne.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout_6.addWidget(self.OnetoOne)

        self.FitInScreen = QToolButton(self.dockWidgetContents)
        self.FitInScreen.setObjectName(u"FitInScreen")
        self.FitInScreen.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout_6.addWidget(self.FitInScreen)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        self.ToggleCollisions = QToolButton(self.dockWidgetContents)
        self.ToggleCollisions.setObjectName(u"ToggleCollisions")
        self.ToggleCollisions.setCheckable(True)
        self.ToggleCollisions.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout_6.addWidget(self.ToggleCollisions)

        self.TogglePreview = QToolButton(self.dockWidgetContents)
        self.TogglePreview.setObjectName(u"TogglePreview")
        self.TogglePreview.setCheckable(True)
        self.TogglePreview.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout_6.addWidget(self.TogglePreview)


        self.gridLayout.addLayout(self.horizontalLayout_6, 4, 1, 1, 1)

        self.SearchBar = QLineEdit(self.dockWidgetContents)
        self.SearchBar.setObjectName(u"SearchBar")
        self.SearchBar.setMaximumSize(QSize(250, 16777215))
        self.SearchBar.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.SearchBar.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.SearchBar, 2, 0, 1, 1)

        self.Categories = QTreeWidget(self.dockWidgetContents)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.Categories.setHeaderItem(__qtreewidgetitem)
        self.Categories.setObjectName(u"Categories")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Categories.sizePolicy().hasHeightForWidth())
        self.Categories.setSizePolicy(sizePolicy)
        self.Categories.setMinimumSize(QSize(100, 0))
        self.Categories.setMaximumSize(QSize(250, 16777215))
        self.Categories.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.Categories.setAlternatingRowColors(True)
        self.Categories.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.Categories.header().setVisible(False)

        self.gridLayout.addWidget(self.Categories, 3, 0, 1, 1)

        self.splitter = QSplitter(self.dockWidgetContents)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.CatsTab = QWidget(self.splitter)
        self.CatsTab.setObjectName(u"CatsTab")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.CatsTab.sizePolicy().hasHeightForWidth())
        self.CatsTab.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.CatsTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.splitter.addWidget(self.CatsTab)
        self.ItemsTab = QWidget(self.splitter)
        self.ItemsTab.setObjectName(u"ItemsTab")
        self.gridLayout_2 = QGridLayout(self.ItemsTab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Favourite = QToolButton(self.ItemsTab)
        self.Favourite.setObjectName(u"Favourite")
        icon2 = QIcon(QIcon.fromTheme(u"emblem-favorite"))
        self.Favourite.setIcon(icon2)
        self.Favourite.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout_5.addWidget(self.Favourite)

        self.Pin = QToolButton(self.ItemsTab)
        self.Pin.setObjectName(u"Pin")
        icon3 = QIcon()
        icon3.addFile(u":/special/special/pin.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Pin.setIcon(icon3)
        self.Pin.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout_5.addWidget(self.Pin)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.RenderOption = QComboBox(self.ItemsTab)
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.setObjectName(u"RenderOption")

        self.horizontalLayout_5.addWidget(self.RenderOption)

        self.LayerBox = QComboBox(self.ItemsTab)
        self.LayerBox.addItem("")
        self.LayerBox.addItem("")
        self.LayerBox.addItem("")
        self.LayerBox.setObjectName(u"LayerBox")

        self.horizontalLayout_5.addWidget(self.LayerBox)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 7, 0, 1, 1)

        self.LItems = QLabel(self.ItemsTab)
        self.LItems.setObjectName(u"LItems")

        self.gridLayout_2.addWidget(self.LItems, 0, 0, 1, 1)

        self.LItem = QLabel(self.ItemsTab)
        self.LItem.setObjectName(u"LItem")

        self.gridLayout_2.addWidget(self.LItem, 3, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.TilesListView = QToolButton(self.ItemsTab)
        self.TilesListView.setObjectName(u"TilesListView")
        icon4 = QIcon()
        icon4.addFile(u":/grids/grid/list.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.TilesListView.setIcon(icon4)
        self.TilesListView.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout_2.addWidget(self.TilesListView)

        self.TilesGridViewBig = QToolButton(self.ItemsTab)
        self.TilesGridViewBig.setObjectName(u"TilesGridViewBig")
        icon5 = QIcon()
        icon5.addFile(u":/grids/grid/mediumgrid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.TilesGridViewBig.setIcon(icon5)

        self.horizontalLayout_2.addWidget(self.TilesGridViewBig)

        self.TilesGridViewSmall = QToolButton(self.ItemsTab)
        self.TilesGridViewSmall.setObjectName(u"TilesGridViewSmall")
        icon6 = QIcon()
        icon6.addFile(u":/grids/grid/smallgrid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.TilesGridViewSmall.setIcon(icon6)

        self.horizontalLayout_2.addWidget(self.TilesGridViewSmall)

        self.TilesIconView = QToolButton(self.ItemsTab)
        self.TilesIconView.setObjectName(u"TilesIconView")
        icon7 = QIcon()
        icon7.addFile(u":/grids/grid/smallgrid2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.TilesIconView.setIcon(icon7)

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


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.Items = QListWidget(self.ItemsTab)
        self.Items.setObjectName(u"Items")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.Items.sizePolicy().hasHeightForWidth())
        self.Items.setSizePolicy(sizePolicy2)
        self.Items.setMouseTracking(True)
        self.Items.setAutoFillBackground(True)
        self.Items.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.Items.setAlternatingRowColors(True)
        self.Items.setResizeMode(QListView.ResizeMode.Fixed)
        self.Items.setLayoutMode(QListView.LayoutMode.SinglePass)
        self.Items.setSpacing(10)
        self.Items.setViewMode(QListView.ViewMode.IconMode)

        self.gridLayout_2.addWidget(self.Items, 1, 0, 1, 1)

        self.Preview = SimpleViewport(self.ItemsTab)
        self.Preview.setObjectName(u"Preview")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Preview.sizePolicy().hasHeightForWidth())
        self.Preview.setSizePolicy(sizePolicy3)
        self.Preview.setMinimumSize(QSize(0, 150))
        self.Preview.setMouseTracking(True)

        self.gridLayout_2.addWidget(self.Preview, 4, 0, 1, 1)

        self.Properties = QTableWidget(self.ItemsTab)
        self.Properties.setObjectName(u"Properties")
        sizePolicy3.setHeightForWidth(self.Properties.sizePolicy().hasHeightForWidth())
        self.Properties.setSizePolicy(sizePolicy3)
        self.Properties.setMinimumSize(QSize(0, 100))
        self.Properties.setSizeIncrement(QSize(0, 0))
        self.Properties.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.Properties.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.Properties.setAlternatingRowColors(True)
        self.Properties.setShowGrid(False)
        self.Properties.setGridStyle(Qt.PenStyle.NoPen)
        self.Properties.setSortingEnabled(True)
        self.Properties.setWordWrap(False)
        self.Properties.setCornerButtonEnabled(True)
        self.Properties.horizontalHeader().setVisible(False)
        self.Properties.horizontalHeader().setCascadingSectionResizes(True)
        self.Properties.horizontalHeader().setHighlightSections(True)
        self.Properties.verticalHeader().setCascadingSectionResizes(True)
        self.Properties.verticalHeader().setMinimumSectionSize(20)
        self.Properties.verticalHeader().setDefaultSectionSize(20)
        self.Properties.verticalHeader().setHighlightSections(True)

        self.gridLayout_2.addWidget(self.Properties, 6, 0, 1, 1)

        self.splitter.addWidget(self.ItemsTab)

        self.gridLayout.addWidget(self.splitter, 1, 1, 3, 1)

        Explorer.setWidget(self.dockWidgetContents)

        self.retranslateUi(Explorer)

        QMetaObject.connectSlotsByName(Explorer)
    # setupUi

    def retranslateUi(self, Explorer):
        Explorer.setWindowTitle(QCoreApplication.translate("Explorer", u"Explorer", None))
        self.LCategories.setText(QCoreApplication.translate("Explorer", u"Categories", None))
        self.CatsAddCC.setText("")
        self.CatsRemoveCC.setText("")
        self.CatPrev.setText(QCoreApplication.translate("Explorer", u"...", None))
        self.CatNext.setText(QCoreApplication.translate("Explorer", u"...", None))
        self.OnetoOne.setText(QCoreApplication.translate("Explorer", u"1:1", None))
        self.FitInScreen.setText(QCoreApplication.translate("Explorer", u"Fit", None))
        self.ToggleCollisions.setText(QCoreApplication.translate("Explorer", u"Collisions", None))
        self.TogglePreview.setText(QCoreApplication.translate("Explorer", u"Preview", None))
        self.SearchBar.setInputMask("")
        self.SearchBar.setPlaceholderText(QCoreApplication.translate("Explorer", u"Search", None))
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

        self.LItems.setText(QCoreApplication.translate("Explorer", u"Items", None))
        self.LItem.setText(QCoreApplication.translate("Explorer", u"Item", None))
        self.TilesListView.setText("")
        self.TilesGridViewBig.setText("")
        self.TilesGridViewSmall.setText("")
        self.TilesIconView.setText("")
        self.TilePrev.setText(QCoreApplication.translate("Explorer", u"...", None))
        self.TileNext.setText(QCoreApplication.translate("Explorer", u"...", None))
    # retranslateUi

