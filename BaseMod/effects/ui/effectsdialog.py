# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'effectdialogmygHvV.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
    QFontComboBox, QHBoxLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_EffectDialog(object):
    def setupUi(self, EffectDialog):
        if not EffectDialog.objectName():
            EffectDialog.setObjectName(u"EffectDialog")
        EffectDialog.resize(293, 72)
        EffectDialog.setSizeGripEnabled(False)
        EffectDialog.setModal(False)
        self.verticalLayout = QVBoxLayout(EffectDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(EffectDialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.EffectSettingComboBox = QFontComboBox(EffectDialog)
        self.EffectSettingComboBox.setObjectName(u"EffectSettingComboBox")

        self.horizontalLayout.addWidget(self.EffectSettingComboBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(EffectDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(EffectDialog)
        self.buttonBox.accepted.connect(EffectDialog.accept)
        self.buttonBox.rejected.connect(EffectDialog.reject)

        QMetaObject.connectSlotsByName(EffectDialog)
    # setupUi

    def retranslateUi(self, EffectDialog):
        EffectDialog.setWindowTitle(QCoreApplication.translate("EffectDialog", u"Pick a Key", None))
        self.label.setText(QCoreApplication.translate("EffectDialog", u"Eddit value", None))
    # retranslateUi

