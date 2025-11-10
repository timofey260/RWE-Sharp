# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'keydialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QKeySequenceEdit, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_keyDialog(object):
    def setupUi(self, keyDialog):
        if not keyDialog.objectName():
            keyDialog.setObjectName(u"keyDialog")
        keyDialog.resize(248, 72)
        keyDialog.setSizeGripEnabled(False)
        keyDialog.setModal(False)
        self.verticalLayout = QVBoxLayout(keyDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(keyDialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.keySequenceEdit = QKeySequenceEdit(keyDialog)
        self.keySequenceEdit.setObjectName(u"keySequenceEdit")
        self.keySequenceEdit.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.keySequenceEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(keyDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(keyDialog)
        self.buttonBox.accepted.connect(keyDialog.accept)
        self.buttonBox.rejected.connect(keyDialog.reject)

        QMetaObject.connectSlotsByName(keyDialog)
    # setupUi

    def retranslateUi(self, keyDialog):
        keyDialog.setWindowTitle(QCoreApplication.translate("keyDialog", u"Pick a Key", None))
        self.label.setText(QCoreApplication.translate("keyDialog", u"Fucking text", None))
    # retranslateUi

