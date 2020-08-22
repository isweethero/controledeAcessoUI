# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastrofhpZqF.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_RegistroON(object):
    def setupUi(self, RegistroON):
        if not RegistroON.objectName():
            RegistroON.setObjectName(u"RegistroON")
        RegistroON.setWindowModality(Qt.NonModal)
        RegistroON.resize(512, 230)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RegistroON.sizePolicy().hasHeightForWidth())
        RegistroON.setSizePolicy(sizePolicy)
        RegistroON.setMinimumSize(QSize(512, 230))
        RegistroON.setMaximumSize(QSize(512, 230))
        icon = QIcon()
        icon.addFile(u"ico.png", QSize(), QIcon.Normal, QIcon.Off)
        RegistroON.setWindowIcon(icon)
        RegistroON.setWindowOpacity(1.000000000000000)
        self.verticalLayoutWidget = QWidget(RegistroON)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 10, 511, 41))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Ubuntu")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout.addWidget(self.label)

        self.verticalLayoutWidget_2 = QWidget(RegistroON)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(1, 59, 169, 72))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.RgL = QLabel(self.verticalLayoutWidget_2)
        self.RgL.setObjectName(u"RgL")
        self.RgL.setEnabled(True)
        sizePolicy.setHeightForWidth(self.RgL.sizePolicy().hasHeightForWidth())
        self.RgL.setSizePolicy(sizePolicy)
        self.RgL.setMinimumSize(QSize(25, 30))
        self.RgL.setMaximumSize(QSize(25, 30))
        self.RgL.setFont(font)
        self.RgL.setLayoutDirection(Qt.LeftToRight)
        self.RgL.setFrameShape(QFrame.NoFrame)
        self.RgL.setTextFormat(Qt.AutoText)
        self.RgL.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.RgL.setMargin(0)

        self.horizontalLayout.addWidget(self.RgL)

        self.RgNumeros = QLabel(self.verticalLayoutWidget_2)
        self.RgNumeros.setObjectName(u"RgNumeros")
        self.RgNumeros.setMinimumSize(QSize(120, 20))
        self.RgNumeros.setMaximumSize(QSize(120, 20))
        self.RgNumeros.setFont(font)
        self.RgNumeros.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.RgNumeros)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.Ra = QLabel(self.verticalLayoutWidget_2)
        self.Ra.setObjectName(u"Ra")
        self.Ra.setMinimumSize(QSize(25, 30))
        self.Ra.setMaximumSize(QSize(25, 30))
        self.Ra.setFont(font)
        self.Ra.setLayoutDirection(Qt.LeftToRight)
        self.Ra.setTextFormat(Qt.AutoText)
        self.Ra.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Ra.setMargin(0)

        self.horizontalLayout_2.addWidget(self.Ra)

        self.RaNumeros = QLabel(self.verticalLayoutWidget_2)
        self.RaNumeros.setObjectName(u"RaNumeros")
        self.RaNumeros.setMinimumSize(QSize(120, 20))
        self.RaNumeros.setMaximumSize(QSize(120, 20))
        self.RaNumeros.setFont(font)
        self.RaNumeros.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.RaNumeros)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayoutWidget_3 = QWidget(RegistroON)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(0, 160, 511, 61))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.confirmarb = QPushButton(self.horizontalLayoutWidget_3)
        self.confirmarb.setObjectName(u"confirmarb")
        self.confirmarb.setMinimumSize(QSize(100, 50))
        self.confirmarb.setMaximumSize(QSize(100, 50))
        self.confirmarb.setFont(font)

        self.horizontalLayout_3.addWidget(self.confirmarb)

        self.cancelarb = QPushButton(self.horizontalLayoutWidget_3)
        self.cancelarb.setObjectName(u"cancelarb")
        self.cancelarb.setMinimumSize(QSize(100, 50))
        self.cancelarb.setMaximumSize(QSize(100, 50))
        self.cancelarb.setFont(font)

        self.horizontalLayout_3.addWidget(self.cancelarb)


        self.retranslateUi(RegistroON)

        QMetaObject.connectSlotsByName(RegistroON)
    # setupUi

    def retranslateUi(self, RegistroON):
        RegistroON.setWindowTitle(QCoreApplication.translate("RegistroON", u"Registro", None))
        self.label.setText(QCoreApplication.translate("RegistroON", u"Confirme os dados abaixo:", None))
        self.RgL.setText(QCoreApplication.translate("RegistroON", u"RG:", None))
        self.RgNumeros.setText(QCoreApplication.translate("RegistroON", u"999999999", None))
        self.Ra.setText(QCoreApplication.translate("RegistroON", u"RA:", None))
        self.RaNumeros.setText(QCoreApplication.translate("RegistroON", u"1300000000000", None))
        self.confirmarb.setText(QCoreApplication.translate("RegistroON", u"Confirmar", None))
        self.cancelarb.setText(QCoreApplication.translate("RegistroON", u"Cancelar", None))
    # retranslateUi

