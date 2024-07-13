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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHeaderView, QSizePolicy, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Hotkeys(object):
    def setupUi(self, Hotkeys):
        if not Hotkeys.objectName():
            Hotkeys.setObjectName(u"Hotkeys")
        Hotkeys.resize(795, 542)
        self.verticalLayout_2 = QVBoxLayout(Hotkeys)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.treeWidget = QTreeWidget(Hotkeys)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.header().setDefaultSectionSize(200)

        self.verticalLayout_2.addWidget(self.treeWidget)

        self.buttonBox = QDialogButtonBox(Hotkeys)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(Hotkeys)
        self.buttonBox.accepted.connect(Hotkeys.accept)
        self.buttonBox.rejected.connect(Hotkeys.reject)

        QMetaObject.connectSlotsByName(Hotkeys)
    # setupUi

    def retranslateUi(self, Hotkeys):
        Hotkeys.setWindowTitle(QCoreApplication.translate("Hotkeys", u"Hotkeys", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Hotkeys", u"Key", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Hotkeys", u"Name", None));
    # retranslateUi

