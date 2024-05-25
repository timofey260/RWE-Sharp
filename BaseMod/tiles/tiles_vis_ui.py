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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_TilesView(object):
    def setupUi(self, TilesView):
        if not TilesView.objectName():
            TilesView.setObjectName(u"TilesView")
        TilesView.resize(380, 374)
        self.verticalLayout = QVBoxLayout(TilesView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(TilesView)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 360, 354))
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
        self.VTilesMaterials.setChecked(True)

        self.verticalLayout_2.addWidget(self.VTilesMaterials)

        self.VTilesHeads = QCheckBox(self.scrollAreaWidgetContents)
        self.VTilesHeads.setObjectName(u"VTilesHeads")
        self.VTilesHeads.setChecked(True)

        self.verticalLayout_2.addWidget(self.VTilesHeads)

        self.VTilesMaterialClassic = QRadioButton(self.scrollAreaWidgetContents)
        self.VTilesMaterialClassic.setObjectName(u"VTilesMaterialClassic")
        self.VTilesMaterialClassic.setChecked(True)

        self.verticalLayout_2.addWidget(self.VTilesMaterialClassic)

        self.VTilesMaterialHenry = QRadioButton(self.scrollAreaWidgetContents)
        self.VTilesMaterialHenry.setObjectName(u"VTilesMaterialHenry")

        self.verticalLayout_2.addWidget(self.VTilesMaterialHenry)

        self.VTilesMaterialUnrendered = QRadioButton(self.scrollAreaWidgetContents)
        self.VTilesMaterialUnrendered.setObjectName(u"VTilesMaterialUnrendered")

        self.verticalLayout_2.addWidget(self.VTilesMaterialUnrendered)

        self.VTilesMaterialRendered = QRadioButton(self.scrollAreaWidgetContents)
        self.VTilesMaterialRendered.setObjectName(u"VTilesMaterialRendered")

        self.verticalLayout_2.addWidget(self.VTilesMaterialRendered)

        self.PalleteSelectButton = QPushButton(self.scrollAreaWidgetContents)
        self.PalleteSelectButton.setObjectName(u"PalleteSelectButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PalleteSelectButton.sizePolicy().hasHeightForWidth())
        self.PalleteSelectButton.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.PalleteSelectButton)

        self.verticalSpacer = QSpacerItem(273, 103, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(TilesView)
        self.VTilesAllTiles.clicked["bool"].connect(self.VTilesLayer1.setDisabled)
        self.VTilesAllTiles.clicked["bool"].connect(self.VTilesLayer2.setDisabled)
        self.VTilesAllTiles.clicked["bool"].connect(self.VTilesLayer3.setDisabled)
        self.VTilesAllTiles.clicked["bool"].connect(self.VTilesMaterials.setDisabled)
        self.VTilesAllTiles.clicked["bool"].connect(self.VTilesHeads.setDisabled)

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
        self.VTilesMaterialClassic.setText(QCoreApplication.translate("TilesView", u"Classic tile preview", None))
        self.VTilesMaterialHenry.setText(QCoreApplication.translate("TilesView", u"Henry's category colors", None))
        self.VTilesMaterialUnrendered.setText(QCoreApplication.translate("TilesView", u"Unrendered tiles", None))
        self.VTilesMaterialRendered.setText(QCoreApplication.translate("TilesView", u"Render preview", None))
        self.PalleteSelectButton.setText(QCoreApplication.translate("TilesView", u"Select Pallete", None))
    # retranslateUi

