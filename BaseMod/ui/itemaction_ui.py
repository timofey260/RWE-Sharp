# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'itemaction.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
    QDialogButtonBox, QFrame, QGridLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_ItemAction(object):
    def setupUi(self, ItemAction):
        if not ItemAction.objectName():
            ItemAction.setObjectName(u"ItemAction")
        ItemAction.resize(300, 145)
        self.verticalLayout = QVBoxLayout(ItemAction)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(ItemAction)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.Action = QComboBox(self.frame)
        self.Action.addItem("")
        self.Action.addItem("")
        self.Action.setObjectName(u"Action")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Action.sizePolicy().hasHeightForWidth())
        self.Action.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.Action, 1, 1, 1, 1)

        self.ItemName = QLabel(self.frame)
        self.ItemName.setObjectName(u"ItemName")

        self.gridLayout.addWidget(self.ItemName, 0, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(ItemAction)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(ItemAction)
        self.buttonBox.accepted.connect(ItemAction.accept)
        self.buttonBox.rejected.connect(ItemAction.reject)

        QMetaObject.connectSlotsByName(ItemAction)
    # setupUi

    def retranslateUi(self, ItemAction):
        ItemAction.setWindowTitle(QCoreApplication.translate("ItemAction", u"Item Action", None))
        self.label.setText(QCoreApplication.translate("ItemAction", u"What Action do you wanna do?", None))
        self.label_2.setText(QCoreApplication.translate("ItemAction", u"Name:", None))
        self.label_3.setText(QCoreApplication.translate("ItemAction", u"Action:", None))
        self.Action.setItemText(0, QCoreApplication.translate("ItemAction", u"Add to \"AAAA\"", None))
        self.Action.setItemText(1, QCoreApplication.translate("ItemAction", u"Remove from \"BBBB\"", None))

        self.ItemName.setText(QCoreApplication.translate("ItemAction", u"TextLabel", None))
    # retranslateUi

