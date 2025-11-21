# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'effects.ui'
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
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

from RWS.Widgets import ColorPicker

class Ui_EffectsView(object):
    def setupUi(self, EffectsView):
        if not EffectsView.objectName():
            EffectsView.setObjectName(u"EffectsView")
        EffectsView.resize(375, 441)
        self.verticalLayout = QVBoxLayout(EffectsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(EffectsView)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 355, 421))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ShowAddEffect = QCheckBox(self.scrollAreaWidgetContents)
        self.ShowAddEffect.setObjectName(u"ShowAddEffect")
        self.ShowAddEffect.setChecked(True)

        self.verticalLayout_2.addWidget(self.ShowAddEffect)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.Color100 = ColorPicker(self.scrollAreaWidgetContents)
        self.Color100.setObjectName(u"Color100")

        self.horizontalLayout.addWidget(self.Color100)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.Color0 = ColorPicker(self.scrollAreaWidgetContents)
        self.Color0.setObjectName(u"Color0")

        self.horizontalLayout_2.addWidget(self.Color0)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.EffectIndex = QSpinBox(self.scrollAreaWidgetContents)
        self.EffectIndex.setObjectName(u"EffectIndex")

        self.horizontalLayout_3.addWidget(self.EffectIndex)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 257, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(EffectsView)
        self.ShowAddEffect.toggled.connect(self.label.setEnabled)
        self.ShowAddEffect.toggled.connect(self.Color100.setEnabled)
        self.ShowAddEffect.toggled.connect(self.label_2.setEnabled)
        self.ShowAddEffect.toggled.connect(self.Color0.setEnabled)
        self.ShowAddEffect.toggled.connect(self.EffectIndex.setEnabled)
        self.ShowAddEffect.toggled.connect(self.label_3.setEnabled)

        QMetaObject.connectSlotsByName(EffectsView)
    # setupUi

    def retranslateUi(self, EffectsView):
        EffectsView.setWindowTitle(QCoreApplication.translate("EffectsView", u"Effects", None))
        self.ShowAddEffect.setText(QCoreApplication.translate("EffectsView", u"Show Additional Effect", None))
        self.label.setText(QCoreApplication.translate("EffectsView", u"100% Color:", None))
        self.Color100.setText("")
        self.label_2.setText(QCoreApplication.translate("EffectsView", u"0% Color:", None))
        self.Color0.setText("")
        self.label_3.setText(QCoreApplication.translate("EffectsView", u"Index:", None))
    # retranslateUi

