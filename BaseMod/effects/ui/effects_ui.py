# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'effects.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_Effects(object):
    def setupUi(self, Effects):
        if not Effects.objectName():
            Effects.setObjectName(u"Effects")
        Effects.resize(388, 547)
        self.verticalLayout = QVBoxLayout(Effects)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(Effects)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 368, 527))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_6 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_12.addWidget(self.label_6)

        self.EffectsTree = QTreeWidget(self.scrollAreaWidgetContents_3)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.EffectsTree.setHeaderItem(__qtreewidgetitem)
        self.EffectsTree.setObjectName(u"EffectsTree")
        self.EffectsTree.setHeaderHidden(True)

        self.verticalLayout_12.addWidget(self.EffectsTree)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.MoveDown = QPushButton(self.scrollAreaWidgetContents_3)
        self.MoveDown.setObjectName(u"MoveDown")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MoveDown.sizePolicy().hasHeightForWidth())
        self.MoveDown.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.MoveDown, 1, 2, 1, 1)

        self.MoveUp = QPushButton(self.scrollAreaWidgetContents_3)
        self.MoveUp.setObjectName(u"MoveUp")
        sizePolicy.setHeightForWidth(self.MoveUp.sizePolicy().hasHeightForWidth())
        self.MoveUp.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.MoveUp, 1, 0, 1, 1)

        self.DeleteEffect = QPushButton(self.scrollAreaWidgetContents_3)
        self.DeleteEffect.setObjectName(u"DeleteEffect")
        sizePolicy.setHeightForWidth(self.DeleteEffect.sizePolicy().hasHeightForWidth())
        self.DeleteEffect.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.DeleteEffect, 1, 1, 1, 1)

        self.DuplicateEffect = QPushButton(self.scrollAreaWidgetContents_3)
        self.DuplicateEffect.setObjectName(u"DuplicateEffect")
        sizePolicy.setHeightForWidth(self.DuplicateEffect.sizePolicy().hasHeightForWidth())
        self.DuplicateEffect.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.DuplicateEffect, 2, 2, 1, 1)

        self.PasteEffect = QPushButton(self.scrollAreaWidgetContents_3)
        self.PasteEffect.setObjectName(u"PasteEffect")
        sizePolicy.setHeightForWidth(self.PasteEffect.sizePolicy().hasHeightForWidth())
        self.PasteEffect.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.PasteEffect, 2, 1, 1, 1)

        self.CopyEffect = QPushButton(self.scrollAreaWidgetContents_3)
        self.CopyEffect.setObjectName(u"CopyEffect")
        sizePolicy.setHeightForWidth(self.CopyEffect.sizePolicy().hasHeightForWidth())
        self.CopyEffect.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.CopyEffect, 2, 0, 1, 1)


        self.verticalLayout_12.addLayout(self.gridLayout_5)

        self.label_7 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_12.addWidget(self.label_7)

        self.OptionsTree = QTreeWidget(self.scrollAreaWidgetContents_3)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"1");
        self.OptionsTree.setHeaderItem(__qtreewidgetitem1)
        self.OptionsTree.setObjectName(u"OptionsTree")
        self.OptionsTree.setHeaderHidden(False)

        self.verticalLayout_12.addWidget(self.OptionsTree)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(Effects)

        QMetaObject.connectSlotsByName(Effects)
    # setupUi

    def retranslateUi(self, Effects):
        Effects.setWindowTitle(QCoreApplication.translate("Effects", u"Effects", None))
        self.label_6.setText(QCoreApplication.translate("Effects", u"Effects:", None))
        self.MoveDown.setText(QCoreApplication.translate("Effects", u"Move down", None))
        self.MoveUp.setText(QCoreApplication.translate("Effects", u"Move up", None))
        self.DeleteEffect.setText(QCoreApplication.translate("Effects", u"Delete", None))
        self.DuplicateEffect.setText(QCoreApplication.translate("Effects", u"Duplicate", None))
        self.PasteEffect.setText(QCoreApplication.translate("Effects", u"Paste", None))
        self.CopyEffect.setText(QCoreApplication.translate("Effects", u"Copy", None))
        self.label_7.setText(QCoreApplication.translate("Effects", u"Options:", None))
    # retranslateUi

