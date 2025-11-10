# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tiles.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_TilesView(object):
    def setupUi(self, TilesView):
        if not TilesView.objectName():
            TilesView.setObjectName(u"TilesView")
        TilesView.resize(380, 741)
        self.verticalLayout = QVBoxLayout(TilesView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(TilesView)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 360, 721))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.VTilesMaterialsLabel = QLabel(self.scrollAreaWidgetContents)
        self.VTilesMaterialsLabel.setObjectName(u"VTilesMaterialsLabel")

        self.verticalLayout_2.addWidget(self.VTilesMaterialsLabel)

        self.VTilesAllTiles = QCheckBox(self.scrollAreaWidgetContents)
        self.VTilesAllTiles.setObjectName(u"VTilesAllTiles")
        self.VTilesAllTiles.setCheckable(True)
        self.VTilesAllTiles.setChecked(True)

        self.verticalLayout_2.addWidget(self.VTilesAllTiles)

        self.VTilesLayer1 = QCheckBox(self.scrollAreaWidgetContents)
        self.VTilesLayer1.setObjectName(u"VTilesLayer1")
        self.VTilesLayer1.setEnabled(False)

        self.verticalLayout_2.addWidget(self.VTilesLayer1)

        self.VTilesLayer2 = QCheckBox(self.scrollAreaWidgetContents)
        self.VTilesLayer2.setObjectName(u"VTilesLayer2")
        self.VTilesLayer2.setEnabled(False)

        self.verticalLayout_2.addWidget(self.VTilesLayer2)

        self.VTilesLayer3 = QCheckBox(self.scrollAreaWidgetContents)
        self.VTilesLayer3.setObjectName(u"VTilesLayer3")
        self.VTilesLayer3.setEnabled(False)

        self.verticalLayout_2.addWidget(self.VTilesLayer3)

        self.VTilesMaterials = QCheckBox(self.scrollAreaWidgetContents)
        self.VTilesMaterials.setObjectName(u"VTilesMaterials")
        self.VTilesMaterials.setEnabled(False)
        self.VTilesMaterials.setChecked(True)

        self.verticalLayout_2.addWidget(self.VTilesMaterials)

        self.VTilesHeads = QCheckBox(self.scrollAreaWidgetContents)
        self.VTilesHeads.setObjectName(u"VTilesHeads")
        self.VTilesHeads.setEnabled(True)
        self.VTilesHeads.setChecked(False)

        self.verticalLayout_2.addWidget(self.VTilesHeads)

        self.VTilesBodies = QCheckBox(self.scrollAreaWidgetContents)
        self.VTilesBodies.setObjectName(u"VTilesBodies")
        self.VTilesBodies.setEnabled(True)
        self.VTilesBodies.setChecked(False)

        self.verticalLayout_2.addWidget(self.VTilesBodies)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.VTilesClassic = QRadioButton(self.scrollAreaWidgetContents)
        self.VTilesClassic.setObjectName(u"VTilesClassic")
        self.VTilesClassic.setChecked(True)

        self.verticalLayout_2.addWidget(self.VTilesClassic)

        self.VTilesImage = QRadioButton(self.scrollAreaWidgetContents)
        self.VTilesImage.setObjectName(u"VTilesImage")

        self.verticalLayout_2.addWidget(self.VTilesImage)

        self.VTilesHenry = QRadioButton(self.scrollAreaWidgetContents)
        self.VTilesHenry.setObjectName(u"VTilesHenry")

        self.verticalLayout_2.addWidget(self.VTilesHenry)

        self.VTilesUnrendered = QRadioButton(self.scrollAreaWidgetContents)
        self.VTilesUnrendered.setObjectName(u"VTilesUnrendered")

        self.verticalLayout_2.addWidget(self.VTilesUnrendered)

        self.VTilesRendered = QRadioButton(self.scrollAreaWidgetContents)
        self.VTilesRendered.setObjectName(u"VTilesRendered")

        self.verticalLayout_2.addWidget(self.VTilesRendered)

        self.VTilesRendered_shade = QRadioButton(self.scrollAreaWidgetContents)
        self.VTilesRendered_shade.setObjectName(u"VTilesRendered_shade")

        self.verticalLayout_2.addWidget(self.VTilesRendered_shade)

        self.VTilesRendered_rain = QRadioButton(self.scrollAreaWidgetContents)
        self.VTilesRendered_rain.setObjectName(u"VTilesRendered_rain")

        self.verticalLayout_2.addWidget(self.VTilesRendered_rain)

        self.PaletteSelectButton = QPushButton(self.scrollAreaWidgetContents)
        self.PaletteSelectButton.setObjectName(u"PaletteSelectButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PaletteSelectButton.sizePolicy().hasHeightForWidth())
        self.PaletteSelectButton.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.PaletteSelectButton)

        self.verticalSpacer = QSpacerItem(273, 103, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(TilesView)
        self.VTilesAllTiles.toggled.connect(self.VTilesLayer3.setDisabled)
        self.VTilesAllTiles.toggled.connect(self.VTilesLayer2.setDisabled)
        self.VTilesAllTiles.toggled.connect(self.VTilesLayer1.setDisabled)
        self.VTilesAllTiles.toggled.connect(self.VTilesMaterials.setDisabled)

        QMetaObject.connectSlotsByName(TilesView)
    # setupUi

    def retranslateUi(self, TilesView):
        TilesView.setWindowTitle(QCoreApplication.translate("TilesView", u"Tiles", None))
        self.VTilesMaterialsLabel.setText(QCoreApplication.translate("TilesView", u"Toggle visibility of:", None))
        self.VTilesAllTiles.setText(QCoreApplication.translate("TilesView", u"All tiles", None))
        self.VTilesLayer1.setText(QCoreApplication.translate("TilesView", u"Layer 1", None))
        self.VTilesLayer2.setText(QCoreApplication.translate("TilesView", u"Layer 2", None))
        self.VTilesLayer3.setText(QCoreApplication.translate("TilesView", u"Layer 3", None))
        self.VTilesMaterials.setText(QCoreApplication.translate("TilesView", u"Materials", None))
        self.VTilesHeads.setText(QCoreApplication.translate("TilesView", u"Tile heads", None))
        self.VTilesBodies.setText(QCoreApplication.translate("TilesView", u"Tile bodies", None))
        self.label.setText(QCoreApplication.translate("TilesView", u"Preview:", None))
        self.VTilesClassic.setText(QCoreApplication.translate("TilesView", u"Classic tile preview", None))
        self.VTilesImage.setText(QCoreApplication.translate("TilesView", u"Tile image preview", None))
        self.VTilesHenry.setText(QCoreApplication.translate("TilesView", u"Henry's category colors", None))
        self.VTilesUnrendered.setText(QCoreApplication.translate("TilesView", u"Unrendered tiles", None))
        self.VTilesRendered.setText(QCoreApplication.translate("TilesView", u"Rendered Tiles (sun)", None))
        self.VTilesRendered_shade.setText(QCoreApplication.translate("TilesView", u"Rendered Tiles (shaded)", None))
        self.VTilesRendered_rain.setText(QCoreApplication.translate("TilesView", u"Rendered Tiles (rain)", None))
        self.PaletteSelectButton.setText(QCoreApplication.translate("TilesView", u"Select Palette", None))
    # retranslateUi

