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
from PySide6.QtWidgets import (QApplication, QDockWidget, QGraphicsView, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSplitter, QToolButton, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_EffectExplorer(object):
    def setupUi(self, EffectExplorer):
        if not EffectExplorer.objectName():
            EffectExplorer.setObjectName(u"EffectExplorer")
        EffectExplorer.resize(582, 355)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.horizontalLayout = QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter = QSplitter(self.dockWidgetContents)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.Effects = QTreeWidget(self.widget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.Effects.setHeaderItem(__qtreewidgetitem)
        self.Effects.setObjectName(u"Effects")
        self.Effects.header().setVisible(False)

        self.verticalLayout.addWidget(self.Effects)

        self.splitter.addWidget(self.widget)
        self.widget1 = QWidget(self.splitter)
        self.widget1.setObjectName(u"widget1")
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.Effectpreview = QGraphicsView(self.widget1)
        self.Effectpreview.setObjectName(u"Effectpreview")

        self.verticalLayout_2.addWidget(self.Effectpreview)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Favorite = QToolButton(self.widget1)
        self.Favorite.setObjectName(u"Favorite")
        icon = QIcon(QIcon.fromTheme(u"emblem-favorite"))
        self.Favorite.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.Favorite)

        self.AddEffect = QPushButton(self.widget1)
        self.AddEffect.setObjectName(u"AddEffect")

        self.horizontalLayout_2.addWidget(self.AddEffect)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.splitter.addWidget(self.widget1)

        self.horizontalLayout.addWidget(self.splitter)

        EffectExplorer.setWidget(self.dockWidgetContents)

        self.retranslateUi(EffectExplorer)

        QMetaObject.connectSlotsByName(EffectExplorer)
    # setupUi

    def retranslateUi(self, EffectExplorer):
        EffectExplorer.setWindowTitle(QCoreApplication.translate("EffectExplorer", u"Effect Explorer", None))
        self.label.setText(QCoreApplication.translate("EffectExplorer", u"Effects:", None))
        self.label_2.setText(QCoreApplication.translate("EffectExplorer", u"Preview:", None))
        self.Favorite.setText("")
        self.AddEffect.setText(QCoreApplication.translate("EffectExplorer", u"Add", None))
    # retranslateUi

