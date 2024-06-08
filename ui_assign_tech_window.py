# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'assign_tech_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(901, 599)
        Dialog.setStyleSheet(u"QWidget{\n"
"background-color: #eff0f3;\n"
"}\n"
"\n"
"QLabel#lbl_title{\n"
"font: 25pt;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border-radius: 10px;\n"
"border: 1px solid black;\n"
"padding: 10px;\n"
"font:12pt;\n"
"}\n"
"\n"
"QPlainTextEdit{\n"
"border-radius: 10px;\n"
"border: 1px solid black;\n"
"padding: 5px;\n"
"font:12pt;\n"
"}\n"
"\n"
"\n"
"QGroupBox {\n"
"font: 12pt\n"
"}\n"
"\n"
"QPlainTextEdit:focus,QLineEdit:focus{\n"
"border: 2px solid  #0082ff;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: #16161a;\n"
"	border-radius: none;\n"
"	padding:5px;\n"
"	color: white;\n"
"	margin-right: 10px;\n"
"	text-align: left;\n"
"	font: 13pt;	\n"
"	padding:7px;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled {\n"
"	background-color: #5c5c5c;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color:#3561fb;\n"
"}\n"
"\n"
"QPushButton#btn_confirm,#btn_print,#btn_close, #btn_print{\n"
"text-align: centre;\n"
"font: 30px;\n"
"padding: 15px 50px;\n"
"}\n"
"\n"
"\n"
"QPushButton#btn_close{\n"
"	backgroun"
                        "d-color: #e5e5e5;\n"
"	color: black;\n"
"	border: 1px solid transparent;\n"
"	font: 30px;\n"
"}\n"
"\n"
"QPushButton#btn_close:hover{\n"
"	background-color: #b2b2b2;\n"
"	color: black;\n"
"	font: 30px;\n"
"}\n"
"QPushButton#btn_close:pressed{\n"
"	background-color: #989898;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #1a307c;\n"
"}\n"
"\n"
"QPushButton#btn_print{\n"
"background-color:#cc8400;\n"
"}\n"
"\n"
"QPushButton#btn_print:hover{\n"
"background-color:#f29c00;\n"
"}\n"
"\n"
"QPushButton#btn_print:pressed{\n"
"background-color:#b27300;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.gridLayout_4 = QGridLayout(Dialog)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_main = QFrame(Dialog)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setFrameShape(QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_main)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame_main)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_2 = QGroupBox(self.frame_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.txt_reported_fault = QPlainTextEdit(self.groupBox_2)
        self.txt_reported_fault.setObjectName(u"txt_reported_fault")

        self.verticalLayout_2.addWidget(self.txt_reported_fault)


        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frame = QFrame(self.frame_main)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_title = QLabel(self.frame_4)
        self.lbl_title.setObjectName(u"lbl_title")
        self.lbl_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lbl_title)


        self.gridLayout_2.addWidget(self.frame_4, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.txt_technician = QLineEdit(self.groupBox)
        self.txt_technician.setObjectName(u"txt_technician")

        self.verticalLayout.addWidget(self.txt_technician)


        self.gridLayout_2.addWidget(self.groupBox, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.frame_main)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_confirm = QPushButton(self.frame_3)
        self.btn_confirm.setObjectName(u"btn_confirm")
        self.btn_confirm.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_confirm)

        self.btn_print = QPushButton(self.frame_3)
        self.btn_print.setObjectName(u"btn_print")
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_print)

        self.btn_close = QPushButton(self.frame_3)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_close)


        self.gridLayout_3.addWidget(self.frame_3, 3, 0, 1, 1)

        self.frame_5 = QFrame(self.frame_main)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, -1, -1, 30)
        self.grp_job_number = QGroupBox(self.frame_5)
        self.grp_job_number.setObjectName(u"grp_job_number")
        self.gridLayout_5 = QGridLayout(self.grp_job_number)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label = QLabel(self.grp_job_number)
        self.label.setObjectName(u"label")

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)

        self.txt_job_number = QLineEdit(self.grp_job_number)
        self.txt_job_number.setObjectName(u"txt_job_number")
        self.txt_job_number.setEnabled(False)

        self.gridLayout_5.addWidget(self.txt_job_number, 0, 1, 1, 1)


        self.gridLayout_6.addWidget(self.grp_job_number, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_5, 2, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_main, 1, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Reported fault:", None))
        self.lbl_title.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Assign Technician:", None))
        self.btn_confirm.setText(QCoreApplication.translate("Dialog", u"Create Job", None))
        self.btn_print.setText(QCoreApplication.translate("Dialog", u"Print Sticker", None))
        self.btn_close.setText(QCoreApplication.translate("Dialog", u"Close", None))
        self.grp_job_number.setTitle(QCoreApplication.translate("Dialog", u"Job Details", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Job Number:", None))
    # retranslateUi

