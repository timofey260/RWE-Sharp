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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 366, 624))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.changeTL = QPushButton(self.scrollAreaWidgetContents)
        self.changeTL.setObjectName(u"changeTL")
        self.changeTL.setFlat(False)

        self.horizontalLayout.addWidget(self.changeTL)

        self.changeTR = QPushButton(self.scrollAreaWidgetContents)
        self.changeTR.setObjectName(u"changeTR")

        self.horizontalLayout.addWidget(self.changeTR)

        self.changeBR = QPushButton(self.scrollAreaWidgetContents)
        self.changeBR.setObjectName(u"changeBR")

        self.horizontalLayout.addWidget(self.changeBR)

        self.changeBL = QPushButton(self.scrollAreaWidgetContents)
        self.changeBL.setObjectName(u"changeBL")

        self.horizontalLayout.addWidget(self.changeBL)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_7 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_2.addWidget(self.pushButton_7, 1, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_2.addWidget(self.pushButton_5, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_2.addWidget(self.pushButton_3, 1, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_2.addWidget(self.pushButton_4, 0, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout_2.addWidget(self.pushButton_8, 0, 2, 1, 1)

        self.pushButton_6 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_2.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.pushButton_9 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout_2.addWidget(self.pushButton_9, 2, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout_2.addWidget(self.pushButton_10, 2, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.pushButton_12 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.verticalLayout_2.addWidget(self.pushButton_12)

        self.pushButton_11 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.verticalLayout_2.addWidget(self.pushButton_11)

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

        self.gridLayout.addWidget(self.Notes, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.PropOptions = QTreeWidget(self.scrollAreaWidgetContents)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.PropOptions.setHeaderItem(__qtreewidgetitem)
        self.PropOptions.setObjectName(u"PropOptions")
        self.PropOptions.header().setVisible(False)

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
        self.label_3.setText(QCoreApplication.translate("Props", u"Change Points:", None))
        self.changeTL.setText(QCoreApplication.translate("Props", u"TL", None))
        self.changeTR.setText(QCoreApplication.translate("Props", u"TR", None))
#if QT_CONFIG(shortcut)
        self.changeTR.setShortcut(QCoreApplication.translate("Props", u"A", None))
#endif // QT_CONFIG(shortcut)
        self.changeBR.setText(QCoreApplication.translate("Props", u"BR", None))
        self.changeBL.setText(QCoreApplication.translate("Props", u"BL", None))
        self.label_4.setText(QCoreApplication.translate("Props", u"Rotate:", None))
        self.pushButton.setText(QCoreApplication.translate("Props", u"-15\u00ba", None))
        self.pushButton_2.setText(QCoreApplication.translate("Props", u"+15\u00ba", None))
        self.label_5.setText(QCoreApplication.translate("Props", u"Stretch", None))
        self.pushButton_7.setText(QCoreApplication.translate("Props", u"Right", None))
        self.pushButton_5.setText(QCoreApplication.translate("Props", u"Bottom", None))
        self.pushButton_3.setText(QCoreApplication.translate("Props", u"Left", None))
        self.pushButton_4.setText(QCoreApplication.translate("Props", u"Top", None))
        self.pushButton_8.setText(QCoreApplication.translate("Props", u"TopBottom", None))
        self.pushButton_6.setText(QCoreApplication.translate("Props", u"LeftRight", None))
        self.pushButton_9.setText(QCoreApplication.translate("Props", u"Scale", None))
        self.pushButton_10.setText(QCoreApplication.translate("Props", u"Offset", None))
        self.pushButton_12.setText(QCoreApplication.translate("Props", u"Free Transform", None))
        self.pushButton_11.setText(QCoreApplication.translate("Props", u"Reset Transform", None))
        self.label_2.setText(QCoreApplication.translate("Props", u"Notes:", None))
        self.Notes.setText(QCoreApplication.translate("Props", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("Props", u"Options:", None))
    # retranslateUi

