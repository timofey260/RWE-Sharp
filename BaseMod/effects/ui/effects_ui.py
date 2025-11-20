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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QToolButton, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

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
        self.label = QLabel(self.scrollAreaWidgetContents_3)
        self.label.setObjectName(u"label")

        self.verticalLayout_12.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.BrushShape = QComboBox(self.scrollAreaWidgetContents_3)
        self.BrushShape.setObjectName(u"BrushShape")

        self.horizontalLayout.addWidget(self.BrushShape)


        self.verticalLayout_12.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.BrushSizeDown = QPushButton(self.scrollAreaWidgetContents_3)
        self.BrushSizeDown.setObjectName(u"BrushSizeDown")

        self.horizontalLayout_2.addWidget(self.BrushSizeDown)

        self.BrushSizeUp = QPushButton(self.scrollAreaWidgetContents_3)
        self.BrushSizeUp.setObjectName(u"BrushSizeUp")

        self.horizontalLayout_2.addWidget(self.BrushSizeUp)


        self.verticalLayout_12.addLayout(self.horizontalLayout_2)

        self.label_6 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_12.addWidget(self.label_6)

        self.EffectsTree = QTreeWidget(self.scrollAreaWidgetContents_3)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"Index");
        self.EffectsTree.setHeaderItem(__qtreewidgetitem)
        self.EffectsTree.setObjectName(u"EffectsTree")
        self.EffectsTree.setHeaderHidden(True)

        self.verticalLayout_12.addWidget(self.EffectsTree)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.PasteEffect = QPushButton(self.scrollAreaWidgetContents_3)
        self.PasteEffect.setObjectName(u"PasteEffect")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PasteEffect.sizePolicy().hasHeightForWidth())
        self.PasteEffect.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.PasteEffect, 2, 2, 1, 1)

        self.Up = QToolButton(self.scrollAreaWidgetContents_3)
        self.Up.setObjectName(u"Up")
        self.Up.setArrowType(Qt.ArrowType.UpArrow)

        self.gridLayout_5.addWidget(self.Up, 1, 0, 1, 1)

        self.MoveUp = QPushButton(self.scrollAreaWidgetContents_3)
        self.MoveUp.setObjectName(u"MoveUp")
        sizePolicy.setHeightForWidth(self.MoveUp.sizePolicy().hasHeightForWidth())
        self.MoveUp.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.MoveUp, 1, 1, 1, 1)

        self.Down = QToolButton(self.scrollAreaWidgetContents_3)
        self.Down.setObjectName(u"Down")
        self.Down.setArrowType(Qt.ArrowType.DownArrow)

        self.gridLayout_5.addWidget(self.Down, 2, 0, 1, 1)

        self.MoveDown = QPushButton(self.scrollAreaWidgetContents_3)
        self.MoveDown.setObjectName(u"MoveDown")
        sizePolicy.setHeightForWidth(self.MoveDown.sizePolicy().hasHeightForWidth())
        self.MoveDown.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.MoveDown, 2, 1, 1, 1)

        self.CopyEffect = QPushButton(self.scrollAreaWidgetContents_3)
        self.CopyEffect.setObjectName(u"CopyEffect")
        sizePolicy.setHeightForWidth(self.CopyEffect.sizePolicy().hasHeightForWidth())
        self.CopyEffect.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.CopyEffect, 1, 2, 1, 1)

        self.DuplicateEffect = QPushButton(self.scrollAreaWidgetContents_3)
        self.DuplicateEffect.setObjectName(u"DuplicateEffect")
        sizePolicy.setHeightForWidth(self.DuplicateEffect.sizePolicy().hasHeightForWidth())
        self.DuplicateEffect.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.DuplicateEffect, 1, 3, 1, 1)

        self.DeleteEffect = QPushButton(self.scrollAreaWidgetContents_3)
        self.DeleteEffect.setObjectName(u"DeleteEffect")
        sizePolicy.setHeightForWidth(self.DeleteEffect.sizePolicy().hasHeightForWidth())
        self.DeleteEffect.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.DeleteEffect, 2, 3, 1, 1)


        self.verticalLayout_12.addLayout(self.gridLayout_5)

        self.Explorer = QPushButton(self.scrollAreaWidgetContents_3)
        self.Explorer.setObjectName(u"Explorer")

        self.verticalLayout_12.addWidget(self.Explorer)

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
        self.label.setText(QCoreApplication.translate("Effects", u"Brush:", None))
        self.label_2.setText(QCoreApplication.translate("Effects", u"Shape:", None))
        self.BrushSizeDown.setText(QCoreApplication.translate("Effects", u"Size-", None))
        self.BrushSizeUp.setText(QCoreApplication.translate("Effects", u"Size+", None))
        self.label_6.setText(QCoreApplication.translate("Effects", u"Effects:", None))
        ___qtreewidgetitem = self.EffectsTree.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Effects", u"Name", None));
        self.PasteEffect.setText(QCoreApplication.translate("Effects", u"Paste", None))
        self.Up.setText(QCoreApplication.translate("Effects", u"...", None))
        self.MoveUp.setText(QCoreApplication.translate("Effects", u"Move up", None))
        self.Down.setText(QCoreApplication.translate("Effects", u"...", None))
        self.MoveDown.setText(QCoreApplication.translate("Effects", u"Move down", None))
        self.CopyEffect.setText(QCoreApplication.translate("Effects", u"Copy", None))
        self.DuplicateEffect.setText(QCoreApplication.translate("Effects", u"Duplicate", None))
        self.DeleteEffect.setText(QCoreApplication.translate("Effects", u"Delete", None))
        self.Explorer.setText(QCoreApplication.translate("Effects", u"Open Explorer", None))
        self.label_7.setText(QCoreApplication.translate("Effects", u"Options:", None))
    # retranslateUi

