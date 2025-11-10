# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Preferences.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Preferences(object):
    def setupUi(self, Preferences):
        if not Preferences.objectName():
            Preferences.setObjectName(u"Preferences")
        Preferences.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Preferences)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Preferences)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.Theme = QComboBox(Preferences)
        self.Theme.setObjectName(u"Theme")

        self.horizontalLayout.addWidget(self.Theme)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(Preferences)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.ThemeUI = QFrame(Preferences)
        self.ThemeUI.setObjectName(u"ThemeUI")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ThemeUI.sizePolicy().hasHeightForWidth())
        self.ThemeUI.setSizePolicy(sizePolicy)
        self.ThemeUI.setFrameShape(QFrame.Shape.StyledPanel)
        self.ThemeUI.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.ThemeUI)


        self.retranslateUi(Preferences)

        QMetaObject.connectSlotsByName(Preferences)
    # setupUi

    def retranslateUi(self, Preferences):
        Preferences.setWindowTitle(QCoreApplication.translate("Preferences", u"Preferences", None))
        self.label.setText(QCoreApplication.translate("Preferences", u"Theme", None))
        self.label_2.setText(QCoreApplication.translate("Preferences", u"Theme ui:", None))
    # retranslateUi

