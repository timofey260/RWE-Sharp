# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'grid.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_GridView(object):
    def setupUi(self, GridView):
        if not GridView.objectName():
            GridView.setObjectName(u"GridView")
        GridView.resize(310, 430)
        self.verticalLayout = QVBoxLayout(GridView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(GridView)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 290, 410))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ShowGrid = QCheckBox(self.scrollAreaWidgetContents)
        self.ShowGrid.setObjectName(u"ShowGrid")

        self.verticalLayout_2.addWidget(self.ShowGrid)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(8)
        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)

        self.ScaleY = QSpinBox(self.scrollAreaWidgetContents)
        self.ScaleY.setObjectName(u"ScaleY")
        self.ScaleY.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ScaleY.sizePolicy().hasHeightForWidth())
        self.ScaleY.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.ScaleY, 1, 4, 1, 1)

        self.OffsetX = QSpinBox(self.scrollAreaWidgetContents)
        self.OffsetX.setObjectName(u"OffsetX")
        self.OffsetX.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.OffsetX.sizePolicy().hasHeightForWidth())
        self.OffsetX.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.OffsetX, 2, 2, 1, 1)

        self.OffsetY = QSpinBox(self.scrollAreaWidgetContents)
        self.OffsetY.setObjectName(u"OffsetY")
        self.OffsetY.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.OffsetY.sizePolicy().hasHeightForWidth())
        self.OffsetY.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.OffsetY, 2, 4, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 1, 3, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.ScaleX = QSpinBox(self.scrollAreaWidgetContents)
        self.ScaleX.setObjectName(u"ScaleX")
        self.ScaleX.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.ScaleX.sizePolicy().hasHeightForWidth())
        self.ScaleX.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.ScaleX, 1, 2, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 2, 3, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.ShowBorder = QCheckBox(self.scrollAreaWidgetContents)
        self.ShowBorder.setObjectName(u"ShowBorder")

        self.verticalLayout_2.addWidget(self.ShowBorder)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(GridView)
        self.ShowGrid.toggled.connect(self.ScaleX.setEnabled)
        self.ShowGrid.toggled.connect(self.ScaleY.setEnabled)
        self.ShowGrid.toggled.connect(self.OffsetX.setEnabled)
        self.ShowGrid.toggled.connect(self.OffsetY.setEnabled)

        QMetaObject.connectSlotsByName(GridView)
    # setupUi

    def retranslateUi(self, GridView):
        GridView.setWindowTitle(QCoreApplication.translate("GridView", u"Grid", None))
        self.ShowGrid.setText(QCoreApplication.translate("GridView", u"Show grid", None))
        self.label_5.setText(QCoreApplication.translate("GridView", u"X:", None))
        self.label_3.setText(QCoreApplication.translate("GridView", u"X:", None))
        self.label_6.setText(QCoreApplication.translate("GridView", u"Y:", None))
        self.label_2.setText(QCoreApplication.translate("GridView", u"Scale", None))
        self.label.setText(QCoreApplication.translate("GridView", u"Offset", None))
        self.label_4.setText(QCoreApplication.translate("GridView", u"Y:", None))
        self.ShowBorder.setText(QCoreApplication.translate("GridView", u"Border", None))
    # retranslateUi

