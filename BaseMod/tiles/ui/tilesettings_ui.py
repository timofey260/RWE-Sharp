# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tiles.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QLabel, QScrollArea, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

from BaseModWidgets import TileSettingsViewport

class Ui_TileSettings(object):
    def setupUi(self, TileSettings):
        if not TileSettings.objectName():
            TileSettings.setObjectName(u"TileSettings")
        TileSettings.resize(572, 457)
        self.gridLayout = QGridLayout(TileSettings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(TileSettings)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 552, 437))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.L1show = QCheckBox(self.scrollAreaWidgetContents)
        self.L1show.setObjectName(u"L1show")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.L1show.sizePolicy().hasHeightForWidth())
        self.L1show.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.L1show)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.L1opn = QSlider(self.scrollAreaWidgetContents)
        self.L1opn.setObjectName(u"L1opn")
        self.L1opn.setMaximum(255)
        self.L1opn.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.L1opn, 1, 1, 1, 1)

        self.L1opr_2 = QSpinBox(self.scrollAreaWidgetContents)
        self.L1opr_2.setObjectName(u"L1opr_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.L1opr_2.sizePolicy().hasHeightForWidth())
        self.L1opr_2.setSizePolicy(sizePolicy1)
        self.L1opr_2.setMaximum(255)

        self.gridLayout_2.addWidget(self.L1opr_2, 0, 2, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.L1opn_2 = QSpinBox(self.scrollAreaWidgetContents)
        self.L1opn_2.setObjectName(u"L1opn_2")
        sizePolicy1.setHeightForWidth(self.L1opn_2.sizePolicy().hasHeightForWidth())
        self.L1opn_2.setSizePolicy(sizePolicy1)
        self.L1opn_2.setMaximum(255)

        self.gridLayout_2.addWidget(self.L1opn_2, 1, 2, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.L1opr = QSlider(self.scrollAreaWidgetContents)
        self.L1opr.setObjectName(u"L1opr")
        self.L1opr.setMaximum(255)
        self.L1opr.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.L1opr, 0, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.L2show = QCheckBox(self.scrollAreaWidgetContents)
        self.L2show.setObjectName(u"L2show")
        sizePolicy.setHeightForWidth(self.L2show.sizePolicy().hasHeightForWidth())
        self.L2show.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.L2show)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.L2opn = QSlider(self.scrollAreaWidgetContents)
        self.L2opn.setObjectName(u"L2opn")
        self.L2opn.setMaximum(255)
        self.L2opn.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_3.addWidget(self.L2opn, 1, 1, 1, 1)

        self.L2opr_2 = QSpinBox(self.scrollAreaWidgetContents)
        self.L2opr_2.setObjectName(u"L2opr_2")
        sizePolicy1.setHeightForWidth(self.L2opr_2.sizePolicy().hasHeightForWidth())
        self.L2opr_2.setSizePolicy(sizePolicy1)
        self.L2opr_2.setMaximum(255)

        self.gridLayout_3.addWidget(self.L2opr_2, 0, 2, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)

        self.L2opn_2 = QSpinBox(self.scrollAreaWidgetContents)
        self.L2opn_2.setObjectName(u"L2opn_2")
        sizePolicy1.setHeightForWidth(self.L2opn_2.sizePolicy().hasHeightForWidth())
        self.L2opn_2.setSizePolicy(sizePolicy1)
        self.L2opn_2.setMaximum(255)

        self.gridLayout_3.addWidget(self.L2opn_2, 1, 2, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)

        self.L2opr = QSlider(self.scrollAreaWidgetContents)
        self.L2opr.setObjectName(u"L2opr")
        self.L2opr.setMaximum(255)
        self.L2opr.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_3.addWidget(self.L2opr, 0, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.L3show = QCheckBox(self.scrollAreaWidgetContents)
        self.L3show.setObjectName(u"L3show")
        sizePolicy.setHeightForWidth(self.L3show.sizePolicy().hasHeightForWidth())
        self.L3show.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.L3show)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_9)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.L3opn = QSlider(self.scrollAreaWidgetContents)
        self.L3opn.setObjectName(u"L3opn")
        self.L3opn.setMaximum(255)
        self.L3opn.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_4.addWidget(self.L3opn, 1, 1, 1, 1)

        self.L3opr_2 = QSpinBox(self.scrollAreaWidgetContents)
        self.L3opr_2.setObjectName(u"L3opr_2")
        sizePolicy1.setHeightForWidth(self.L3opr_2.sizePolicy().hasHeightForWidth())
        self.L3opr_2.setSizePolicy(sizePolicy1)
        self.L3opr_2.setMaximum(255)

        self.gridLayout_4.addWidget(self.L3opr_2, 0, 2, 1, 1)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 1, 0, 1, 1)

        self.L3opn_2 = QSpinBox(self.scrollAreaWidgetContents)
        self.L3opn_2.setObjectName(u"L3opn_2")
        sizePolicy1.setHeightForWidth(self.L3opn_2.sizePolicy().hasHeightForWidth())
        self.L3opn_2.setSizePolicy(sizePolicy1)
        self.L3opn_2.setMaximum(255)

        self.gridLayout_4.addWidget(self.L3opn_2, 1, 2, 1, 1)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)

        self.L3opr = QSlider(self.scrollAreaWidgetContents)
        self.L3opr.setObjectName(u"L3opr")
        self.L3opr.setMaximum(255)
        self.L3opr.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_4.addWidget(self.L3opr, 0, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_4)

        self.Opacityshift = QCheckBox(self.scrollAreaWidgetContents)
        self.Opacityshift.setObjectName(u"Opacityshift")

        self.verticalLayout_3.addWidget(self.Opacityshift)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_10)

        self.RenderOption = QComboBox(self.scrollAreaWidgetContents)
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.addItem("")
        self.RenderOption.setObjectName(u"RenderOption")

        self.verticalLayout_3.addWidget(self.RenderOption)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.TilePreview = TileSettingsViewport(self.scrollAreaWidgetContents)
        self.TilePreview.setObjectName(u"TilePreview")

        self.horizontalLayout.addWidget(self.TilePreview)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

#if QT_CONFIG(shortcut)
        self.label_5.setBuddy(self.L1show)
        self.label_6.setBuddy(self.L1show)
        self.label_9.setBuddy(self.L1show)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(TileSettings)

        QMetaObject.connectSlotsByName(TileSettings)
    # setupUi

    def retranslateUi(self, TileSettings):
        TileSettings.setWindowTitle(QCoreApplication.translate("TileSettings", u"Form", None))
        self.L1show.setText("")
        self.label_5.setText(QCoreApplication.translate("TileSettings", u"Layer 1", None))
        self.label_2.setText(QCoreApplication.translate("TileSettings", u"Not Rendered", None))
        self.label.setText(QCoreApplication.translate("TileSettings", u"Rendered", None))
        self.L2show.setText("")
        self.label_6.setText(QCoreApplication.translate("TileSettings", u"Layer 2", None))
        self.label_3.setText(QCoreApplication.translate("TileSettings", u"Not Rendered", None))
        self.label_4.setText(QCoreApplication.translate("TileSettings", u"Rendered", None))
        self.L3show.setText("")
        self.label_9.setText(QCoreApplication.translate("TileSettings", u"Layer 3", None))
        self.label_7.setText(QCoreApplication.translate("TileSettings", u"Not Rendered", None))
        self.label_8.setText(QCoreApplication.translate("TileSettings", u"Rendered", None))
        self.Opacityshift.setText(QCoreApplication.translate("TileSettings", u"Opacity Shift", None))
        self.label_10.setText(QCoreApplication.translate("TileSettings", u"Preview", None))
        self.RenderOption.setItemText(0, QCoreApplication.translate("TileSettings", u"Classic", None))
        self.RenderOption.setItemText(1, QCoreApplication.translate("TileSettings", u"Tile image", None))
        self.RenderOption.setItemText(2, QCoreApplication.translate("TileSettings", u"Henry", None))
        self.RenderOption.setItemText(3, QCoreApplication.translate("TileSettings", u"Unrendered", None))
        self.RenderOption.setItemText(4, QCoreApplication.translate("TileSettings", u"Rendered (sun)", None))
        self.RenderOption.setItemText(5, QCoreApplication.translate("TileSettings", u"Rendered (shaded)", None))
        self.RenderOption.setItemText(6, QCoreApplication.translate("TileSettings", u"Rendered (rain)", None))

    # retranslateUi

