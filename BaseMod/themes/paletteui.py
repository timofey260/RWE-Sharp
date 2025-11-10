# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Palette.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_Paletteui(object):
    def setupUi(self, Paletteui):
        if not Paletteui.objectName():
            Paletteui.setObjectName(u"Paletteui")
        Paletteui.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Paletteui)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Paletteui)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.Style = QComboBox(Paletteui)
        self.Style.addItem("")
        self.Style.addItem("")
        self.Style.setObjectName(u"Style")

        self.horizontalLayout.addWidget(self.Style)

        self.label_2 = QLabel(Paletteui)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.Palette = QComboBox(Paletteui)
        self.Palette.addItem("")
        self.Palette.addItem("")
        self.Palette.setObjectName(u"Palette")

        self.horizontalLayout.addWidget(self.Palette)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lineEdit = QLineEdit(Paletteui)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.lineEdit)

        self.treeWidget = QTreeWidget(Paletteui)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.header().setVisible(False)

        self.verticalLayout.addWidget(self.treeWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Import = QPushButton(Paletteui)
        self.Import.setObjectName(u"Import")

        self.horizontalLayout_2.addWidget(self.Import)

        self.Export = QPushButton(Paletteui)
        self.Export.setObjectName(u"Export")

        self.horizontalLayout_2.addWidget(self.Export)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Paletteui)

        QMetaObject.connectSlotsByName(Paletteui)
    # setupUi

    def retranslateUi(self, Paletteui):
        Paletteui.setWindowTitle(QCoreApplication.translate("Paletteui", u"Palette", None))
        self.label.setText(QCoreApplication.translate("Paletteui", u"Style:", None))
        self.Style.setItemText(0, QCoreApplication.translate("Paletteui", u"Circular", None))
        self.Style.setItemText(1, QCoreApplication.translate("Paletteui", u"Sharp", None))

        self.label_2.setText(QCoreApplication.translate("Paletteui", u"Palette", None))
        self.Palette.setItemText(0, QCoreApplication.translate("Paletteui", u"RaspberryDark", None))
        self.Palette.setItemText(1, QCoreApplication.translate("Paletteui", u"MoonlightDark", None))

        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Paletteui", u"Search", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Paletteui", u"1", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Paletteui", u"Text", None));
        ___qtreewidgetitem2 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("Paletteui", u"other bullshit", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.Import.setText(QCoreApplication.translate("Paletteui", u"Import", None))
        self.Export.setText(QCoreApplication.translate("Paletteui", u"Export", None))
    # retranslateUi

