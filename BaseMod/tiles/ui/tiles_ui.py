# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tiles.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDockWidget,
    QGraphicsView, QGridLayout, QHeaderView, QLabel,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)
import ui.res_rc

class Ui_Tiles(object):
    def setupUi(self, Tiles):
        if not Tiles.objectName():
            Tiles.setObjectName(u"Tiles")
        Tiles.resize(319, 785)
        self.gridLayout_2 = QGridLayout(Tiles)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(Tiles)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 317, 783))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.ToolTilesM1Select = QComboBox(self.scrollAreaWidgetContents)
        icon = QIcon()
        icon.addFile(u":/geoIcons/geo/pen.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ToolTilesM1Select.addItem(icon, "")
        self.ToolTilesM1Select.addItem("")
        self.ToolTilesM1Select.addItem("")
        self.ToolTilesM1Select.addItem("")
        self.ToolTilesM1Select.addItem("")
        self.ToolTilesM1Select.addItem("")
        self.ToolTilesM1Select.addItem("")
        self.ToolTilesM1Select.addItem("")
        self.ToolTilesM1Select.setObjectName(u"ToolTilesM1Select")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToolTilesM1Select.sizePolicy().hasHeightForWidth())
        self.ToolTilesM1Select.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.ToolTilesM1Select, 0, 1, 1, 1)

        self.checkBox = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 0, 2, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.spinBox = QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimum(1)

        self.gridLayout.addWidget(self.spinBox, 3, 1, 1, 1)

        self.checkBox_2 = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout.addWidget(self.checkBox_2, 2, 2, 1, 1)

        self.ToolTilesM1Select_2 = QComboBox(self.scrollAreaWidgetContents)
        self.ToolTilesM1Select_2.addItem("")
        self.ToolTilesM1Select_2.addItem("")
        self.ToolTilesM1Select_2.addItem("")
        self.ToolTilesM1Select_2.addItem("")
        self.ToolTilesM1Select_2.addItem("")
        self.ToolTilesM1Select_2.addItem("")
        self.ToolTilesM1Select_2.addItem("")
        self.ToolTilesM1Select_2.addItem("")
        self.ToolTilesM1Select_2.addItem("")
        self.ToolTilesM1Select_2.setObjectName(u"ToolTilesM1Select_2")
        sizePolicy.setHeightForWidth(self.ToolTilesM1Select_2.sizePolicy().hasHeightForWidth())
        self.ToolTilesM1Select_2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.ToolTilesM1Select_2, 2, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_2.addWidget(self.label_6)

        self.graphicsView = QGraphicsView(self.scrollAreaWidgetContents)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_2.addWidget(self.graphicsView)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.treeWidget = QTreeWidget(self.scrollAreaWidgetContents)
        self.treeWidget.setObjectName(u"treeWidget")

        self.verticalLayout_2.addWidget(self.treeWidget)

        self.verticalSpacer = QSpacerItem(20, 103, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.dockWidget = QDockWidget(self.scrollAreaWidgetContents)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidget.setFloating(False)
        self.dockWidget.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetClosable|QDockWidget.DockWidgetFeature.DockWidgetFloatable|QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.dockWidget.setWidget(self.dockWidgetContents)

        self.verticalLayout_2.addWidget(self.dockWidget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.retranslateUi(Tiles)
        self.checkBox.pressed.connect(self.dockWidget.show)

        QMetaObject.connectSlotsByName(Tiles)
    # setupUi

    def retranslateUi(self, Tiles):
        Tiles.setWindowTitle(QCoreApplication.translate("Tiles", u"Tiles", None))
        self.label_3.setText(QCoreApplication.translate("Tiles", u"Place:", None))
        self.label.setText(QCoreApplication.translate("Tiles", u"Left Mouse:", None))
        self.label_2.setText(QCoreApplication.translate("Tiles", u"Right Mouse", None))
        self.ToolTilesM1Select.setItemText(0, QCoreApplication.translate("Tiles", u"Pen", None))
        self.ToolTilesM1Select.setItemText(1, QCoreApplication.translate("Tiles", u"Brush", None))
        self.ToolTilesM1Select.setItemText(2, QCoreApplication.translate("Tiles", u"Bucket", None))
        self.ToolTilesM1Select.setItemText(3, QCoreApplication.translate("Tiles", u"Line", None))
        self.ToolTilesM1Select.setItemText(4, QCoreApplication.translate("Tiles", u"Rectangle", None))
        self.ToolTilesM1Select.setItemText(5, QCoreApplication.translate("Tiles", u"Hollow Rectangle", None))
        self.ToolTilesM1Select.setItemText(6, QCoreApplication.translate("Tiles", u"Circle", None))
        self.ToolTilesM1Select.setItemText(7, QCoreApplication.translate("Tiles", u"Hollow Circle", None))

        self.checkBox.setText(QCoreApplication.translate("Tiles", u"Delete", None))
        self.label_4.setText(QCoreApplication.translate("Tiles", u"Brush size:", None))
        self.checkBox_2.setText(QCoreApplication.translate("Tiles", u"Delete", None))
        self.ToolTilesM1Select_2.setItemText(0, QCoreApplication.translate("Tiles", u"Pen", None))
        self.ToolTilesM1Select_2.setItemText(1, QCoreApplication.translate("Tiles", u"Delete", None))
        self.ToolTilesM1Select_2.setItemText(2, QCoreApplication.translate("Tiles", u"Brush", None))
        self.ToolTilesM1Select_2.setItemText(3, QCoreApplication.translate("Tiles", u"Bucket", None))
        self.ToolTilesM1Select_2.setItemText(4, QCoreApplication.translate("Tiles", u"Line", None))
        self.ToolTilesM1Select_2.setItemText(5, QCoreApplication.translate("Tiles", u"Rectangle", None))
        self.ToolTilesM1Select_2.setItemText(6, QCoreApplication.translate("Tiles", u"Hollow Rectangle", None))
        self.ToolTilesM1Select_2.setItemText(7, QCoreApplication.translate("Tiles", u"Circle", None))
        self.ToolTilesM1Select_2.setItemText(8, QCoreApplication.translate("Tiles", u"Hollow Circle", None))

        self.label_6.setText(QCoreApplication.translate("Tiles", u"Tile Preview:", None))
        self.label_5.setText(QCoreApplication.translate("Tiles", u"Recent Tiles:", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Tiles", u"Category", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Tiles", u"Tile", None));
        self.dockWidget.setWindowTitle(QCoreApplication.translate("Tiles", u"Tile Browser", None))
    # retranslateUi

