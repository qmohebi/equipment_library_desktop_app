# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(514, 822)
        Dialog.setStyleSheet(u" QDialog{\n"
"background-color:#f5f6fa;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border-radius: 20px;\n"
"	border: 1px solid white;\n"
"	padding: 10px;\n"
"	font: 14pt;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 0px solid white;\n"
"    padding: 10px;\n"
"    border: 2px solid #fbc531;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color:#009639 ;\n"
"	border: none;\n"
"	color: white;\n"
"	border-radius: 20px;\n"
"	padding: 20px;\n"
"	font: bold 14pt;\n"
"}\n"
"\n"
"\n"
"QPushButton#btn_guest{\n"
"	background-color: transparent;\n"
"	color: black;\n"
"	border: 2px solid #0097e6;\n"
"	padding: 5px 20px;\n"
"	font: bold 14pt;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:#78BE20 ;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:#006747 ;\n"
"}\n"
"\n"
"\n"
"QPushButton#btn_guest:hover{\n"
"	background-color: #15afff;\n"
"	border: 0px;\n"
"	color: white;\n"
"	padding: 5px;\n"
"	font: bold 14pt;\n"
"}\n"
"\n"
"QPushButton#btn_guest:pressed{\n"
"	background-color:  #003087;\n"
""
                        "}\n"
"\n"
"QLabel{\n"
"	font: 14pt bold;\n"
"	padding: 10px 0px;\n"
"}\n"
"\n"
"QFrame#frame_error{\n"
"background-color: pink;\n"
"border-radius: 30px;\n"
"padding: 2px;\n"
"}\n"
"\n"
"QLabel#lbl_error{\n"
"font: bold 12pt;\n"
"}\n"
"\n"
"\n"
"QLabel#lbl_error_icon{\n"
" text-align: centre;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton#btn_close_error, hover, pressed{\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.gridLayout_3 = QGridLayout(Dialog)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_4 = QFrame(Dialog)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setLayoutDirection(Qt.RightToLeft)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_login = QPushButton(self.frame_4)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setMinimumSize(QSize(15, 49))
        self.btn_login.setMaximumSize(QSize(250, 16777215))
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_login, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 80, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_4, 2, 0, 1, 1)

        self.frame_guest = QFrame(Dialog)
        self.frame_guest.setObjectName(u"frame_guest")
        self.frame_guest.setLayoutDirection(Qt.RightToLeft)
        self.frame_guest.setFrameShape(QFrame.StyledPanel)
        self.frame_guest.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_guest)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btn_guest = QPushButton(self.frame_guest)
        self.btn_guest.setObjectName(u"btn_guest")
        self.btn_guest.setMinimumSize(QSize(0, 50))
        self.btn_guest.setMaximumSize(QSize(166666, 16777215))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.btn_guest.setFont(font)
        self.btn_guest.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_guest)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout_3.addWidget(self.frame_guest, 3, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 45, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 4, 0, 1, 1)

        self.frame_5 = QFrame(Dialog)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.frame_5)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(200, 120))
        self.label.setPixmap(QPixmap(u":/user_bw.png"))
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.frame_error = QFrame(self.frame_2)
        self.frame_error.setObjectName(u"frame_error")
        self.frame_error.setFrameShape(QFrame.StyledPanel)
        self.frame_error.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_error)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_error_icon = QLabel(self.frame_error)
        self.lbl_error_icon.setObjectName(u"lbl_error_icon")
        self.lbl_error_icon.setMaximumSize(QSize(40, 16777215))
        self.lbl_error_icon.setLayoutDirection(Qt.LeftToRight)
        self.lbl_error_icon.setPixmap(QPixmap(u":/error-30.png"))

        self.horizontalLayout_2.addWidget(self.lbl_error_icon)

        self.lbl_error = QLabel(self.frame_error)
        self.lbl_error.setObjectName(u"lbl_error")
        self.lbl_error.setScaledContents(False)
        self.lbl_error.setAlignment(Qt.AlignCenter)
        self.lbl_error.setWordWrap(True)
        self.lbl_error.setMargin(2)

        self.horizontalLayout_2.addWidget(self.lbl_error)

        self.btn_close_error = QPushButton(self.frame_error)
        self.btn_close_error.setObjectName(u"btn_close_error")
        self.btn_close_error.setMaximumSize(QSize(30, 30))
        self.btn_close_error.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/close-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close_error.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.btn_close_error)


        self.verticalLayout_2.addWidget(self.frame_error)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.txt_username = QLineEdit(self.frame_2)
        self.txt_username.setObjectName(u"txt_username")

        self.verticalLayout_2.addWidget(self.txt_username)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame_5)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 9)
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.txt_password = QLineEdit(self.frame_3)
        self.txt_password.setObjectName(u"txt_password")

        self.verticalLayout.addWidget(self.txt_password)


        self.verticalLayout_3.addWidget(self.frame_3)


        self.gridLayout_3.addWidget(self.frame_5, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btn_login.setText(QCoreApplication.translate("Dialog", u"Login", None))
        self.btn_guest.setText(QCoreApplication.translate("Dialog", u"Continue as guest", None))
        self.label.setText("")
        self.lbl_error_icon.setText("")
        self.lbl_error.setText(QCoreApplication.translate("Dialog", u"Incorrect username or password!", None))
        self.btn_close_error.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Username:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Password:", None))
    # retranslateUi

