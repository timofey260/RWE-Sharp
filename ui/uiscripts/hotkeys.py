# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hotkeys.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGridLayout, QHBoxLayout, QKeySequenceEdit,
    QLabel, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Hotkeys(object):
    def setupUi(self, Hotkeys):
        if not Hotkeys.objectName():
            Hotkeys.setObjectName(u"Hotkeys")
        Hotkeys.resize(795, 542)
        self.verticalLayout_2 = QVBoxLayout(Hotkeys)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBox = QComboBox(Hotkeys)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.scrollArea = QScrollArea(Hotkeys)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 775, 462))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.keySequenceEdit = QKeySequenceEdit(self.scrollAreaWidgetContents)
        self.keySequenceEdit.setObjectName(u"keySequenceEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.keySequenceEdit.sizePolicy().hasHeightForWidth())
        self.keySequenceEdit.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.keySequenceEdit, 0, 2, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.keySequenceEdit_2 = QKeySequenceEdit(self.scrollAreaWidgetContents)
        self.keySequenceEdit_2.setObjectName(u"keySequenceEdit_2")
        sizePolicy1.setHeightForWidth(self.keySequenceEdit_2.sizePolicy().hasHeightForWidth())
        self.keySequenceEdit_2.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.keySequenceEdit_2, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 383, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.buttonBox = QDialogButtonBox(Hotkeys)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(Hotkeys)
        self.buttonBox.accepted.connect(Hotkeys.accept)
        self.buttonBox.rejected.connect(Hotkeys.reject)

        self.comboBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Hotkeys)
    # setupUi

    def retranslateUi(self, Hotkeys):
        Hotkeys.setWindowTitle(QCoreApplication.translate("Hotkeys", u"Hotkeys", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Hotkeys", u"set", None))

        self.label_2.setText(QCoreApplication.translate("Hotkeys", u"option2", None))
        self.label.setText(QCoreApplication.translate("Hotkeys", u"option", None))
    # retranslateUi

