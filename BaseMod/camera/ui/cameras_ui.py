# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cameras.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QScrollArea, QSizePolicy,
    QSpacerItem, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Cameras(object):
    def setupUi(self, Cameras):
        if not Cameras.objectName():
            Cameras.setObjectName(u"Cameras")
        Cameras.resize(388, 547)
        self.verticalLayout = QVBoxLayout(Cameras)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(Cameras)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 368, 527))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.treeWidget = QTreeWidget(self.scrollAreaWidgetContents_3)
        self.treeWidget.setObjectName(u"treeWidget")

        self.verticalLayout_12.addWidget(self.treeWidget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(Cameras)

        QMetaObject.connectSlotsByName(Cameras)
    # setupUi

    def retranslateUi(self, Cameras):
        Cameras.setWindowTitle(QCoreApplication.translate("Cameras", u"Cameras", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Cameras", u"Pos", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Cameras", u"Order", None));
    # retranslateUi

