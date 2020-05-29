# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CalculatriceDeviseGUI.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(268, 386)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 2, 1, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_2.addWidget(self.lineEdit_2, 3, 0, 1, 2)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 1, 0, 1, 2)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_7 = QPushButton(Form)
        self.btn_7.setObjectName(u"btn_7")
        self.btn_7.setMinimumSize(QSize(64, 64))

        self.gridLayout.addWidget(self.btn_7, 0, 0, 1, 1)

        self.btn_8 = QPushButton(Form)
        self.btn_8.setObjectName(u"btn_8")
        self.btn_8.setMinimumSize(QSize(64, 64))

        self.gridLayout.addWidget(self.btn_8, 0, 1, 1, 1)

        self.btn_9 = QPushButton(Form)
        self.btn_9.setObjectName(u"btn_9")
        self.btn_9.setMinimumSize(QSize(64, 64))

        self.gridLayout.addWidget(self.btn_9, 0, 2, 1, 1)

        self.btn_4 = QPushButton(Form)
        self.btn_4.setObjectName(u"btn_4")
        self.btn_4.setMinimumSize(QSize(64, 64))

        self.gridLayout.addWidget(self.btn_4, 1, 0, 1, 1)

        self.btn_5 = QPushButton(Form)
        self.btn_5.setObjectName(u"btn_5")
        self.btn_5.setMinimumSize(QSize(64, 64))

        self.gridLayout.addWidget(self.btn_5, 1, 1, 1, 1)

        self.btn_6 = QPushButton(Form)
        self.btn_6.setObjectName(u"btn_6")
        self.btn_6.setMinimumSize(QSize(64, 64))

        self.gridLayout.addWidget(self.btn_6, 1, 2, 1, 1)

        self.btn_1 = QPushButton(Form)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setMinimumSize(QSize(64, 64))

        self.gridLayout.addWidget(self.btn_1, 2, 0, 1, 1)

        self.btn_2 = QPushButton(Form)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setMinimumSize(QSize(64, 64))

        self.gridLayout.addWidget(self.btn_2, 2, 1, 1, 1)

        self.btn_3 = QPushButton(Form)
        self.btn_3.setObjectName(u"btn_3")
        self.btn_3.setMinimumSize(QSize(64, 64))

        self.gridLayout.addWidget(self.btn_3, 2, 2, 1, 1)

        self.btn_point = QPushButton(Form)
        self.btn_point.setObjectName(u"btn_point")
        self.btn_point.setMinimumSize(QSize(64, 64))

        self.gridLayout.addWidget(self.btn_point, 3, 0, 1, 1)

        self.btn_0 = QPushButton(Form)
        self.btn_0.setObjectName(u"btn_0")
        self.btn_0.setMinimumSize(QSize(64, 64))

        self.gridLayout.addWidget(self.btn_0, 3, 1, 1, 1)

        self.btn_clear = QPushButton(Form)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setMinimumSize(QSize(64, 64))

        self.gridLayout.addWidget(self.btn_clear, 3, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.btn_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.btn_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.btn_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.btn_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.btn_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.btn_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.btn_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.btn_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.btn_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.btn_point.setText(QCoreApplication.translate("Form", u".", None))
        self.btn_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.btn_clear.setText(QCoreApplication.translate("Form", u"C", None))
    # retranslateUi

