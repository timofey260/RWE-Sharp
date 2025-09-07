# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'camera.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_CameraView(object):
    def setupUi(self, CameraView):
        if not CameraView.objectName():
            CameraView.setObjectName(u"CameraView")
        CameraView.resize(310, 430)
        self.verticalLayout = QVBoxLayout(CameraView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(CameraView)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 294, 414))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ShowCameras = QCheckBox(self.scrollAreaWidgetContents)
        self.ShowCameras.setObjectName(u"ShowCameras")
        self.ShowCameras.setChecked(True)

        self.verticalLayout_2.addWidget(self.ShowCameras)

        self.ShowOuter = QCheckBox(self.scrollAreaWidgetContents)
        self.ShowOuter.setObjectName(u"ShowOuter")

        self.verticalLayout_2.addWidget(self.ShowOuter)

        self.ShowInner = QCheckBox(self.scrollAreaWidgetContents)
        self.ShowInner.setObjectName(u"ShowInner")

        self.verticalLayout_2.addWidget(self.ShowInner)

        self.Show43 = QCheckBox(self.scrollAreaWidgetContents)
        self.Show43.setObjectName(u"Show43")

        self.verticalLayout_2.addWidget(self.Show43)

        self.ShowEdgeCircles = QCheckBox(self.scrollAreaWidgetContents)
        self.ShowEdgeCircles.setObjectName(u"ShowEdgeCircles")

        self.verticalLayout_2.addWidget(self.ShowEdgeCircles)

        self.ShowCenter = QCheckBox(self.scrollAreaWidgetContents)
        self.ShowCenter.setObjectName(u"ShowCenter")

        self.verticalLayout_2.addWidget(self.ShowCenter)

        self.ShowCameraShape = QCheckBox(self.scrollAreaWidgetContents)
        self.ShowCameraShape.setObjectName(u"ShowCameraShape")

        self.verticalLayout_2.addWidget(self.ShowCameraShape)

        self.ShowIndex = QCheckBox(self.scrollAreaWidgetContents)
        self.ShowIndex.setObjectName(u"ShowIndex")

        self.verticalLayout_2.addWidget(self.ShowIndex)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(CameraView)
        self.ShowCameras.toggled.connect(self.ShowOuter.setEnabled)
        self.ShowCameras.toggled.connect(self.ShowInner.setEnabled)
        self.ShowCameras.toggled.connect(self.Show43.setEnabled)
        self.ShowCameras.toggled.connect(self.ShowEdgeCircles.setEnabled)
        self.ShowCameras.toggled.connect(self.ShowCenter.setEnabled)
        self.ShowCameras.toggled.connect(self.ShowCameraShape.setEnabled)
        self.ShowCameras.toggled.connect(self.ShowIndex.setEnabled)

        QMetaObject.connectSlotsByName(CameraView)
    # setupUi

    def retranslateUi(self, CameraView):
        CameraView.setWindowTitle(QCoreApplication.translate("CameraView", u"Cameras", None))
        self.ShowCameras.setText(QCoreApplication.translate("CameraView", u"Show Cameras", None))
        self.ShowOuter.setText(QCoreApplication.translate("CameraView", u"Show Outer Rectangle", None))
        self.ShowInner.setText(QCoreApplication.translate("CameraView", u"Show Inner Rectangle", None))
        self.Show43.setText(QCoreApplication.translate("CameraView", u"Show 4:3 Rectangle", None))
        self.ShowEdgeCircles.setText(QCoreApplication.translate("CameraView", u"Show Edge Circles", None))
        self.ShowCenter.setText(QCoreApplication.translate("CameraView", u"Show Center", None))
        self.ShowCameraShape.setText(QCoreApplication.translate("CameraView", u"Show Camera Shape", None))
        self.ShowIndex.setText(QCoreApplication.translate("CameraView", u"Show Index", None))
    # retranslateUi

