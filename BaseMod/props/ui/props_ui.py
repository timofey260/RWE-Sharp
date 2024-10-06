# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'props.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QLabel, QScrollArea, QSizePolicy, QSpacerItem,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_Props(object):
    def setupUi(self, Props):
        if not Props.objectName():
            Props.setObjectName(u"Props")
        Props.resize(398, 550)
        self.verticalLayout = QVBoxLayout(Props)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(Props)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 378, 530))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Notes = QLabel(self.frame)
        self.Notes.setObjectName(u"Notes")
        self.Notes.setWordWrap(True)

        self.gridLayout.addWidget(self.Notes, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.PropOptions = QTreeWidget(self.scrollAreaWidgetContents)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.PropOptions.setHeaderItem(__qtreewidgetitem)
        self.PropOptions.setObjectName(u"PropOptions")

        self.verticalLayout_2.addWidget(self.PropOptions)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(Props)

        QMetaObject.connectSlotsByName(Props)
    # setupUi

    def retranslateUi(self, Props):
        Props.setWindowTitle(QCoreApplication.translate("Props", u"Props", None))
        self.label_2.setText(QCoreApplication.translate("Props", u"Notes:", None))
        self.Notes.setText(QCoreApplication.translate("Props", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("Props", u"Options:", None))
    # retranslateUi

