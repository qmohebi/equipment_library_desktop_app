# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logout_timer.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(489, 492)
        Dialog.setStyleSheet(u"QDialog{\n"
"background-color: black;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: white;\n"
"	border-radius: none;\n"
"	padding:5px;\n"
"	color: black;\n"
"	margin-right: 10px;\n"
"	text-align: left;\n"
"	font: 20pt;	\n"
"	padding-left:7px;\n"
"	border-radius: 20px;\n"
"	text-align: centre;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:#3561fb ;\n"
"}\n"
"\n"
"\n"
"QPushButton#btn_logout{\n"
"	text-align: centre;\n"
"	background-color: transparent;\n"
"	color: white;\n"
"	font: 25px;\n"
"	border: 1px solid #e5e5e5;\n"
"	padding: 10px 20px;\n"
"}\n"
"QPushButton#btn_logout:hover{\n"
"	background-color: #b2b2b2;\n"
"	color: white;\n"
"	border: 1px solid #b2b2b2;\n"
"	font: 25px;\n"
"	padding: 10px 20px;\n"
"}\n"
"QPushButton#btn_logout:pressed{\n"
"	background-color: #989898;\n"
"	border: 1px solid #989898;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #6082fb;\n"
"}\n"
"\n"
"QLabel#lbl_countdown{\n"
"font: bold 50pt;\n"
"color: red;\n"
"}\n"
"\n"
"QLabel{\n"
"color: white;\n"
"}\n"
""
                        "\n"
"\n"
"\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.lbl_countdown = QLabel(Dialog)
        self.lbl_countdown.setObjectName(u"lbl_countdown")
        font1 = QFont()
        font1.setPointSize(50)
        font1.setBold(True)
        font1.setItalic(False)
        self.lbl_countdown.setFont(font1)
        self.lbl_countdown.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_countdown)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_continue = QPushButton(self.frame)
        self.btn_continue.setObjectName(u"btn_continue")
        self.btn_continue.setMinimumSize(QSize(0, 80))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(False)
        font2.setItalic(False)
        self.btn_continue.setFont(font2)

        self.verticalLayout_2.addWidget(self.btn_continue)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.btn_logout = QPushButton(self.frame)
        self.btn_logout.setObjectName(u"btn_logout")
        self.btn_logout.setMinimumSize(QSize(0, 50))
        font3 = QFont()
        font3.setBold(False)
        font3.setItalic(False)
        self.btn_logout.setFont(font3)
        self.btn_logout.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.btn_logout)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Automatic logout in", None))
        self.lbl_countdown.setText(QCoreApplication.translate("Dialog", u"30 sec", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Would you like to continue using the application?", None))
        self.btn_continue.setText(QCoreApplication.translate("Dialog", u"Continue working", None))
        self.btn_logout.setText(QCoreApplication.translate("Dialog", u"Logout", None))
#if QT_CONFIG(shortcut)
        self.btn_logout.setShortcut(QCoreApplication.translate("Dialog", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

