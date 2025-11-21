# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'props.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from RWS.Widgets import ColorPicker

class Ui_PropsView(object):
    def setupUi(self, PropsView):
        if not PropsView.objectName():
            PropsView.setObjectName(u"PropsView")
        PropsView.resize(429, 592)
        self.verticalLayout = QVBoxLayout(PropsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(PropsView)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 409, 572))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ShowProps = QCheckBox(self.scrollAreaWidgetContents)
        self.ShowProps.setObjectName(u"ShowProps")

        self.verticalLayout_2.addWidget(self.ShowProps)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Outline = QCheckBox(self.scrollAreaWidgetContents)
        self.Outline.setObjectName(u"Outline")

        self.horizontalLayout.addWidget(self.Outline)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setEnabled(False)
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label)

        self.OutlineColor = ColorPicker(self.scrollAreaWidgetContents)
        self.OutlineColor.setObjectName(u"OutlineColor")
        self.OutlineColor.setEnabled(False)

        self.horizontalLayout.addWidget(self.OutlineColor)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(PropsView)
        self.Outline.toggled.connect(self.label.setEnabled)
        self.Outline.toggled.connect(self.OutlineColor.setEnabled)

        QMetaObject.connectSlotsByName(PropsView)
    # setupUi

    def retranslateUi(self, PropsView):
        PropsView.setWindowTitle(QCoreApplication.translate("PropsView", u"Props", None))
        self.ShowProps.setText(QCoreApplication.translate("PropsView", u"Show Props", None))
        self.Outline.setText(QCoreApplication.translate("PropsView", u"Outline", None))
        self.label.setText(QCoreApplication.translate("PropsView", u"Color:", None))
        self.OutlineColor.setText("")
    # retranslateUi

