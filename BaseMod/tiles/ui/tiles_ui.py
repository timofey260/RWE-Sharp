# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tiles.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
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
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QSpinBox,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)
import ui.res_rc

class Ui_Tiles(object):
    def setupUi(self, Tiles):
        if not Tiles.objectName():
            Tiles.setObjectName(u"Tiles")
        Tiles.resize(379, 700)
        self.gridLayout_2 = QGridLayout(Tiles)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(Tiles)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 377, 698))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.DeleteM1 = QCheckBox(self.scrollAreaWidgetContents)
        self.DeleteM1.setObjectName(u"DeleteM1")

        self.gridLayout.addWidget(self.DeleteM1, 0, 2, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.ToolTilesM1Select = QComboBox(self.scrollAreaWidgetContents)
        icon = QIcon()
        icon.addFile(u":/geoIcons/geo/pen.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ToolTilesM1Select.addItem(icon, "")
        icon1 = QIcon()
        icon1.addFile(u":/geoIcons/geo/brush.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ToolTilesM1Select.addItem(icon1, "")
        icon2 = QIcon()
        icon2.addFile(u":/geoIcons/geo/bucket.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ToolTilesM1Select.addItem(icon2, "")
        icon3 = QIcon()
        icon3.addFile(u":/geoIcons/geo/line.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ToolTilesM1Select.addItem(icon3, "")
        icon4 = QIcon()
        icon4.addFile(u":/geoIcons/geo/rect.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ToolTilesM1Select.addItem(icon4, "")
        icon5 = QIcon()
        icon5.addFile(u":/geoIcons/geo/rect_hollow.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ToolTilesM1Select.addItem(icon5, "")
        icon6 = QIcon()
        icon6.addFile(u":/geoIcons/geo/circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ToolTilesM1Select.addItem(icon6, "")
        icon7 = QIcon()
        icon7.addFile(u":/geoIcons/geo/circle_hollow.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ToolTilesM1Select.addItem(icon7, "")
        self.ToolTilesM1Select.setObjectName(u"ToolTilesM1Select")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToolTilesM1Select.sizePolicy().hasHeightForWidth())
        self.ToolTilesM1Select.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.ToolTilesM1Select, 0, 1, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.BrushSize = QSpinBox(self.scrollAreaWidgetContents)
        self.BrushSize.setObjectName(u"BrushSize")
        self.BrushSize.setMinimum(1)

        self.gridLayout.addWidget(self.BrushSize, 3, 1, 1, 1)

        self.DeleteM2 = QCheckBox(self.scrollAreaWidgetContents)
        self.DeleteM2.setObjectName(u"DeleteM2")

        self.gridLayout.addWidget(self.DeleteM2, 2, 2, 1, 1)

        self.ToolTilesM2Select = QComboBox(self.scrollAreaWidgetContents)
        self.ToolTilesM2Select.addItem(icon, "")
        self.ToolTilesM2Select.addItem(icon1, "")
        self.ToolTilesM2Select.addItem(icon2, "")
        self.ToolTilesM2Select.addItem(icon3, "")
        self.ToolTilesM2Select.addItem(icon4, "")
        self.ToolTilesM2Select.addItem(icon5, "")
        self.ToolTilesM2Select.addItem(icon6, "")
        self.ToolTilesM2Select.addItem(icon7, "")
        self.ToolTilesM2Select.setObjectName(u"ToolTilesM2Select")
        sizePolicy.setHeightForWidth(self.ToolTilesM2Select.sizePolicy().hasHeightForWidth())
        self.ToolTilesM2Select.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.ToolTilesM2Select, 2, 1, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)

        self.Layer = QSpinBox(self.scrollAreaWidgetContents)
        self.Layer.setObjectName(u"Layer")
        self.Layer.setWrapping(True)
        self.Layer.setCorrectionMode(QAbstractSpinBox.CorrectionMode.CorrectToPreviousValue)
        self.Layer.setMinimum(1)
        self.Layer.setMaximum(3)

        self.gridLayout.addWidget(self.Layer, 4, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout.addWidget(self.label_9)

        self.StrictMode = QComboBox(self.scrollAreaWidgetContents)
        self.StrictMode.addItem("")
        self.StrictMode.addItem("")
        self.StrictMode.setObjectName(u"StrictMode")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.StrictMode.sizePolicy().hasHeightForWidth())
        self.StrictMode.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.StrictMode)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.ForceGeo = QCheckBox(self.scrollAreaWidgetContents)
        self.ForceGeo.setObjectName(u"ForceGeo")

        self.verticalLayout_2.addWidget(self.ForceGeo)

        self.ForcePlace = QCheckBox(self.scrollAreaWidgetContents)
        self.ForcePlace.setObjectName(u"ForcePlace")

        self.verticalLayout_2.addWidget(self.ForcePlace)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_2.addWidget(self.label_8)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.CatPrev = QPushButton(self.scrollAreaWidgetContents)
        self.CatPrev.setObjectName(u"CatPrev")

        self.gridLayout_4.addWidget(self.CatPrev, 1, 0, 1, 1)

        self.FindTE = QPushButton(self.scrollAreaWidgetContents)
        self.FindTE.setObjectName(u"FindTE")

        self.gridLayout_4.addWidget(self.FindTE, 0, 2, 1, 1)

        self.CatNext = QPushButton(self.scrollAreaWidgetContents)
        self.CatNext.setObjectName(u"CatNext")

        self.gridLayout_4.addWidget(self.CatNext, 1, 2, 1, 1)

        self.TileNext = QPushButton(self.scrollAreaWidgetContents)
        self.TileNext.setObjectName(u"TileNext")

        self.gridLayout_4.addWidget(self.TileNext, 1, 1, 1, 1)

        self.OpenExplorer = QPushButton(self.scrollAreaWidgetContents)
        self.OpenExplorer.setObjectName(u"OpenExplorer")

        self.gridLayout_4.addWidget(self.OpenExplorer, 0, 0, 1, 1)

        self.TilePrev = QPushButton(self.scrollAreaWidgetContents)
        self.TilePrev.setObjectName(u"TilePrev")

        self.gridLayout_4.addWidget(self.TilePrev, 0, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_4)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_2.addWidget(self.label_6)

        self.ToggleCollisions = QCheckBox(self.scrollAreaWidgetContents)
        self.ToggleCollisions.setObjectName(u"ToggleCollisions")

        self.verticalLayout_2.addWidget(self.ToggleCollisions)

        self.RenderOption = QComboBox(self.scrollAreaWidgetContents)
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.setObjectName(u"RenderOption")

        self.verticalLayout_2.addWidget(self.RenderOption)

        self.PalleteSelect = QPushButton(self.scrollAreaWidgetContents)
        self.PalleteSelect.setObjectName(u"PalleteSelect")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.PalleteSelect.sizePolicy().hasHeightForWidth())
        self.PalleteSelect.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.PalleteSelect)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.RecentTiles = QTreeWidget(self.scrollAreaWidgetContents)
        self.RecentTiles.setObjectName(u"RecentTiles")

        self.verticalLayout_2.addWidget(self.RecentTiles)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.retranslateUi(Tiles)

        QMetaObject.connectSlotsByName(Tiles)
    # setupUi

    def retranslateUi(self, Tiles):
        Tiles.setWindowTitle(QCoreApplication.translate("Tiles", u"Tiles", None))
        self.label_3.setText(QCoreApplication.translate("Tiles", u"Place:", None))
        self.DeleteM1.setText(QCoreApplication.translate("Tiles", u"Delete", None))
        self.label_4.setText(QCoreApplication.translate("Tiles", u"Brush size:", None))
        self.ToolTilesM1Select.setItemText(0, QCoreApplication.translate("Tiles", u"Pen", None))
        self.ToolTilesM1Select.setItemText(1, QCoreApplication.translate("Tiles", u"Brush", None))
        self.ToolTilesM1Select.setItemText(2, QCoreApplication.translate("Tiles", u"Bucket", None))
        self.ToolTilesM1Select.setItemText(3, QCoreApplication.translate("Tiles", u"Line", None))
        self.ToolTilesM1Select.setItemText(4, QCoreApplication.translate("Tiles", u"Rectangle", None))
        self.ToolTilesM1Select.setItemText(5, QCoreApplication.translate("Tiles", u"Hollow Rectangle", None))
        self.ToolTilesM1Select.setItemText(6, QCoreApplication.translate("Tiles", u"Circle", None))
        self.ToolTilesM1Select.setItemText(7, QCoreApplication.translate("Tiles", u"Hollow Circle", None))

        self.label.setText(QCoreApplication.translate("Tiles", u"Left Mouse:", None))
        self.DeleteM2.setText(QCoreApplication.translate("Tiles", u"Delete", None))
        self.ToolTilesM2Select.setItemText(0, QCoreApplication.translate("Tiles", u"Pen", None))
        self.ToolTilesM2Select.setItemText(1, QCoreApplication.translate("Tiles", u"Brush", None))
        self.ToolTilesM2Select.setItemText(2, QCoreApplication.translate("Tiles", u"Bucket", None))
        self.ToolTilesM2Select.setItemText(3, QCoreApplication.translate("Tiles", u"Line", None))
        self.ToolTilesM2Select.setItemText(4, QCoreApplication.translate("Tiles", u"Rectangle", None))
        self.ToolTilesM2Select.setItemText(5, QCoreApplication.translate("Tiles", u"Hollow Rectangle", None))
        self.ToolTilesM2Select.setItemText(6, QCoreApplication.translate("Tiles", u"Circle", None))
        self.ToolTilesM2Select.setItemText(7, QCoreApplication.translate("Tiles", u"Hollow Circle", None))

        self.label_2.setText(QCoreApplication.translate("Tiles", u"Right Mouse", None))
        self.label_7.setText(QCoreApplication.translate("Tiles", u"Layer", None))
        self.label_9.setText(QCoreApplication.translate("Tiles", u"Tile Remove Strategy:", None))
        self.StrictMode.setItemText(0, QCoreApplication.translate("Tiles", u"Strict", None))
        self.StrictMode.setItemText(1, QCoreApplication.translate("Tiles", u"Full", None))

        self.ForceGeo.setText(QCoreApplication.translate("Tiles", u"Force Geometry", None))
        self.ForcePlace.setText(QCoreApplication.translate("Tiles", u"Force Place", None))
        self.label_8.setText(QCoreApplication.translate("Tiles", u"Tile Explorer:", None))
        self.CatPrev.setText(QCoreApplication.translate("Tiles", u"Category-", None))
        self.FindTE.setText(QCoreApplication.translate("Tiles", u"Find", None))
        self.CatNext.setText(QCoreApplication.translate("Tiles", u"Category+", None))
        self.TileNext.setText(QCoreApplication.translate("Tiles", u"Tile+", None))
        self.OpenExplorer.setText(QCoreApplication.translate("Tiles", u"Open Explorer", None))
        self.TilePrev.setText(QCoreApplication.translate("Tiles", u"Tile-", None))
        self.label_6.setText(QCoreApplication.translate("Tiles", u"Tile Preview:", None))
        self.ToggleCollisions.setText(QCoreApplication.translate("Tiles", u"Collisions", None))
        self.RenderOption.setItemText(0, QCoreApplication.translate("Tiles", u"Classic", None))
        self.RenderOption.setItemText(1, QCoreApplication.translate("Tiles", u"Tile image", None))
        self.RenderOption.setItemText(2, QCoreApplication.translate("Tiles", u"Henry", None))
        self.RenderOption.setItemText(3, QCoreApplication.translate("Tiles", u"Unrendered", None))
        self.RenderOption.setItemText(4, QCoreApplication.translate("Tiles", u"Rendered (sun)", None))
        self.RenderOption.setItemText(5, QCoreApplication.translate("Tiles", u"Rendered (shaded)", None))
        self.RenderOption.setItemText(6, QCoreApplication.translate("Tiles", u"Rendered (rain)", None))
        self.RenderOption.setItemText(7, QCoreApplication.translate("Tiles", u"Sync", None))

        self.PalleteSelect.setText(QCoreApplication.translate("Tiles", u"Select Palette", None))
        self.label_5.setText(QCoreApplication.translate("Tiles", u"Recent Tiles:", None))
        ___qtreewidgetitem = self.RecentTiles.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Tiles", u"Category", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Tiles", u"Tile", None));
    # retranslateUi

