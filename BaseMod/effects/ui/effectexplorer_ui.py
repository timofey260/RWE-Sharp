# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'effectexplorer.ui'
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
from PySide6.QtWidgets import (QApplication, QDockWidget, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSplitter, QToolButton, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

from RWESharpWidgets import SimpleViewport

class Ui_EffectExplorer(object):
    def setupUi(self, EffectExplorer):
        if not EffectExplorer.objectName():
            EffectExplorer.setObjectName(u"EffectExplorer")
        EffectExplorer.resize(582, 355)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout_3 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Search = QLineEdit(self.dockWidgetContents)
        self.Search.setObjectName(u"Search")

        self.verticalLayout_3.addWidget(self.Search)

        self.splitter = QSplitter(self.dockWidgetContents)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.Effects = QTreeWidget(self.layoutWidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.Effects.setHeaderItem(__qtreewidgetitem)
        self.Effects.setObjectName(u"Effects")
        self.Effects.header().setVisible(False)

        self.verticalLayout.addWidget(self.Effects)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Up = QToolButton(self.layoutWidget)
        self.Up.setObjectName(u"Up")
        self.Up.setArrowType(Qt.ArrowType.UpArrow)

        self.horizontalLayout.addWidget(self.Up)

        self.Down = QToolButton(self.layoutWidget)
        self.Down.setObjectName(u"Down")
        self.Down.setArrowType(Qt.ArrowType.DownArrow)

        self.horizontalLayout.addWidget(self.Down)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.Effectpreview = SimpleViewport(self.layoutWidget1)
        self.Effectpreview.setObjectName(u"Effectpreview")

        self.verticalLayout_2.addWidget(self.Effectpreview)

        self.Description = QLabel(self.layoutWidget1)
        self.Description.setObjectName(u"Description")

        self.verticalLayout_2.addWidget(self.Description)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Favorite = QToolButton(self.layoutWidget1)
        self.Favorite.setObjectName(u"Favorite")
        icon = QIcon(QIcon.fromTheme(u"emblem-favorite"))
        self.Favorite.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.Favorite)

        self.AddEffect = QPushButton(self.layoutWidget1)
        self.AddEffect.setObjectName(u"AddEffect")

        self.horizontalLayout_2.addWidget(self.AddEffect)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.splitter.addWidget(self.layoutWidget1)

        self.verticalLayout_3.addWidget(self.splitter)

        EffectExplorer.setWidget(self.dockWidgetContents)

        self.retranslateUi(EffectExplorer)

        QMetaObject.connectSlotsByName(EffectExplorer)
    # setupUi

    def retranslateUi(self, EffectExplorer):
        EffectExplorer.setWindowTitle(QCoreApplication.translate("EffectExplorer", u"Effect Explorer", None))
        self.Search.setPlaceholderText(QCoreApplication.translate("EffectExplorer", u"Search for effects", None))
        self.label.setText(QCoreApplication.translate("EffectExplorer", u"Effects:", None))
        self.Up.setText(QCoreApplication.translate("EffectExplorer", u"...", None))
        self.Down.setText(QCoreApplication.translate("EffectExplorer", u"...", None))
        self.label_2.setText(QCoreApplication.translate("EffectExplorer", u"Preview:", None))
        self.Description.setText(QCoreApplication.translate("EffectExplorer", u"Description", None))
        self.Favorite.setText("")
        self.AddEffect.setText(QCoreApplication.translate("EffectExplorer", u"Add", None))
    # retranslateUi

