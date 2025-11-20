# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createcategory.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QGridLayout, QLabel, QLineEdit,
    QSizePolicy, QVBoxLayout, QWidget)

from RWS.Widgets import ColorPicker

class Ui_CreateCategory(object):
    def setupUi(self, CreateCategory):
        if not CreateCategory.objectName():
            CreateCategory.setObjectName(u"CreateCategory")
        CreateCategory.resize(309, 162)
        self.verticalLayout = QVBoxLayout(CreateCategory)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(CreateCategory)
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
        self.CategoryColor = ColorPicker(self.frame)
        self.CategoryColor.setObjectName(u"CategoryColor")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CategoryColor.sizePolicy().hasHeightForWidth())
        self.CategoryColor.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.CategoryColor, 1, 1, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.CategoryName = QLineEdit(self.frame)
        self.CategoryName.setObjectName(u"CategoryName")

        self.gridLayout.addWidget(self.CategoryName, 0, 1, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(CreateCategory)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(CreateCategory)
        self.buttonBox.accepted.connect(CreateCategory.accept)
        self.buttonBox.rejected.connect(CreateCategory.reject)

        QMetaObject.connectSlotsByName(CreateCategory)
    # setupUi

    def retranslateUi(self, CreateCategory):
        CreateCategory.setWindowTitle(QCoreApplication.translate("CreateCategory", u"Create Category", None))
        self.label.setText(QCoreApplication.translate("CreateCategory", u"Create Category:", None))
        self.CategoryColor.setText("")
        self.label_2.setText(QCoreApplication.translate("CreateCategory", u"Name:", None))
        self.label_3.setText(QCoreApplication.translate("CreateCategory", u"Color:", None))
    # retranslateUi

