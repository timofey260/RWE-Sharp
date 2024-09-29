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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QScrollArea,
    QSizePolicy, QTableView, QVBoxLayout, QWidget)

class Ui_Props(object):
    def setupUi(self, Props):
        if not Props.objectName():
            Props.setObjectName(u"Props")
        Props.resize(418, 658)
        self.verticalLayout = QVBoxLayout(Props)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(Props)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 386, 924))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.ToolPropsLabel_11 = QLabel(self.scrollAreaWidgetContents)
        self.ToolPropsLabel_11.setObjectName(u"ToolPropsLabel_11")

        self.verticalLayout_2.addWidget(self.ToolPropsLabel_11)

        self.label_16 = QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_2.addWidget(self.label_16)

        self.tableView = QTableView(self.scrollAreaWidgetContents)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_2.addWidget(self.tableView)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(Props)

        QMetaObject.connectSlotsByName(Props)
    # setupUi

    def retranslateUi(self, Props):
        Props.setWindowTitle(QCoreApplication.translate("Props", u"Props", None))
        self.label.setText(QCoreApplication.translate("Props", u"<html><head/><body><p align=\"center\">YOU, ME, Gas station</p><p align=\"center\">what are we getting for dinner?</p><p align=\"center\">Sushi of corse</p><p align=\"center\">Uh oh. there was a roofie inside of our gas station sushi</p><p align=\"center\">We black out and wake up in sewers</p><p align=\"center\">we're surrounded by fish.</p><p align=\"center\">horny fish</p><p align=\"center\">you know what that means: FISH orgy</p><p align=\"center\">the stench drives the bear in</p><p align=\"center\">what are we gonna do?</p><p align=\"center\">we're gonna fight it</p><p align=\"center\">bear fight, bare-handed, bare-NAKED?</p><p align=\"center\">OH YES PLEASE</p><p align=\"center\">we befriend the bear after we beat him in the brawl</p><p align=\"center\">then we ride into the chuckie cheese</p><p align=\"center\">DANCE DANCE REVOLUTION</p><p align=\"center\">REVOLUTION? overthrow the government?</p><p align=\"center\">UH I THINK SO</p><p align=\"center\">next thing you know, i'm reincarnated as jesus chr"
                        "ist</p><p align=\"center\">then i turn into a jet, fly into the sun</p><p align=\"center\">black out again</p><p align=\"center\">wake up then</p><p align=\"center\">i do the bob</p><p align=\"center\">white out, which i didn't know you could do</p><p align=\"center\">then i smoked a joint</p><p align=\"center\">greened out</p><p align=\"center\">then i turned into the sun</p><p align=\"center\">UH OH LOOKS LIKE THE METH IS KICKING IN</p><p align=\"center\">KIJFWOUHAGOWHIGAOIJGAOKMWDWANMFOGJAW</p></body></html>", None))
        self.ToolPropsLabel_11.setText(QCoreApplication.translate("Props", u"Prop properties", None))
        self.label_16.setText(QCoreApplication.translate("Props", u"Props:", None))
    # retranslateUi

