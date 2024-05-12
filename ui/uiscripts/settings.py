# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QSplitter, QTreeView,
    QVBoxLayout, QWidget)

from RWESharpWidgets import SettingsViewer

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(709, 542)
        icon = QIcon(QIcon.fromTheme(u"document-properties"))
        Settings.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Settings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.treeSettingPair = QSplitter(Settings)
        self.treeSettingPair.setObjectName(u"treeSettingPair")
        self.treeSettingPair.setOrientation(Qt.Orientation.Horizontal)
        self.treeSettingPair.setChildrenCollapsible(False)
        self.settingsTree = QTreeView(self.treeSettingPair)
        self.settingsTree.setObjectName(u"settingsTree")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.settingsTree.sizePolicy().hasHeightForWidth())
        self.settingsTree.setSizePolicy(sizePolicy)
        self.settingsTree.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.treeSettingPair.addWidget(self.settingsTree)
        self.frame = QFrame(self.treeSettingPair)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.SettingsLabel = QLabel(self.frame)
        self.SettingsLabel.setObjectName(u"SettingsLabel")

        self.verticalLayout_2.addWidget(self.SettingsLabel)

        self.SettingsViewer = SettingsViewer(self.frame)
        self.SettingsViewer.setObjectName(u"SettingsViewer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.SettingsViewer.sizePolicy().hasHeightForWidth())
        self.SettingsViewer.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.SettingsViewer)

        self.treeSettingPair.addWidget(self.frame)

        self.verticalLayout.addWidget(self.treeSettingPair)

        self.butons = QHBoxLayout()
        self.butons.setObjectName(u"butons")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.butons.addItem(self.horizontalSpacer)

        self.applyButton = QPushButton(Settings)
        self.applyButton.setObjectName(u"applyButton")
        self.applyButton.setEnabled(False)

        self.butons.addWidget(self.applyButton)

        self.okButton = QPushButton(Settings)
        self.okButton.setObjectName(u"okButton")
        self.okButton.setFlat(False)

        self.butons.addWidget(self.okButton)

        self.cancelButton = QPushButton(Settings)
        self.cancelButton.setObjectName(u"cancelButton")

        self.butons.addWidget(self.cancelButton)


        self.verticalLayout.addLayout(self.butons)


        self.retranslateUi(Settings)

        self.okButton.setDefault(False)


        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Settings", None))
        self.SettingsLabel.setText(QCoreApplication.translate("Settings", u"Settings", None))
        self.applyButton.setText(QCoreApplication.translate("Settings", u"Apply", None))
        self.okButton.setText(QCoreApplication.translate("Settings", u"Ok", None))
        self.cancelButton.setText(QCoreApplication.translate("Settings", u"Cancel", None))
    # retranslateUi

