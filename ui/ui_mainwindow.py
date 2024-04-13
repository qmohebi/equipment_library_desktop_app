# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1310, 853)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	background-color: white\n"
"}\n"
"QMessageBox#QPushButton{\n"
"border: 10px solid black; border-radius: 1px;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	border: none;\n"
"	border-bottom: none;\n"
"	text-align: left;\n"
"	padding: 5px 10px;\n"
"	background: rgb(110, 141, 255);\n"
"	font-size: 14px\n"
"}\n"
"\n"
"QPushButton{\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"	background-color: #89CFF3;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border: 3px;\n"
"	border-radius: 5px;\n"
"	border: 1px solid black\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid #127eff\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #00A9FF;\n"
"\n"
"}\n"
"\n"
"QPushButton#btn_clear {\n"
"	padding: 5px 10px;\n"
"	background-color: rgb(255, 137, 116);\n"
"}\n"
"\n"
"\n"
"QPushButton#btn_clear:hover {\n"
"	background-color:rgb(255, 106, 92) ;\n"
"}\n"
"\n"
"\n"
"QMessageBox{\n"
"	background-color: white;\n"
"}\n"
"\n"
"QMessageBox:QPushButton{\n"
"	background-color: #89CFF3;\n"
"}\n"
"\n"
"	")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(20)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 150))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(80)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(80, -1, 80, -1)
        self.btn_confirm = QPushButton(self.frame_3)
        self.btn_confirm.setObjectName(u"btn_confirm")
        self.btn_confirm.setMinimumSize(QSize(0, 100))
        font = QFont()
        font.setPointSize(40)
        self.btn_confirm.setFont(font)

        self.horizontalLayout.addWidget(self.btn_confirm)

        self.btn_clear = QPushButton(self.frame_3)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setMinimumSize(QSize(0, 100))
        font1 = QFont()
        font1.setPointSize(26)
        self.btn_clear.setFont(font1)

        self.horizontalLayout.addWidget(self.btn_clear)


        self.gridLayout.addWidget(self.frame_3, 6, 0, 1, 3)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(30)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 20, 9)
        self.txt_asset = QLineEdit(self.frame)
        self.txt_asset.setObjectName(u"txt_asset")
        self.txt_asset.setMinimumSize(QSize(0, 50))
        font2 = QFont()
        font2.setPointSize(30)
        self.txt_asset.setFont(font2)

        self.verticalLayout_2.addWidget(self.txt_asset)

        self.txt_location = QLineEdit(self.frame)
        self.txt_location.setObjectName(u"txt_location")
        self.txt_location.setMinimumSize(QSize(0, 50))
        self.txt_location.setFont(font2)

        self.verticalLayout_2.addWidget(self.txt_location)


        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)

        self.frame_8 = QFrame(self.centralwidget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_8)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(5)
        self.lbl_loan = QLabel(self.frame_8)
        self.lbl_loan.setObjectName(u"lbl_loan")
        self.lbl_loan.setMinimumSize(QSize(0, 50))
        font3 = QFont()
        font3.setPointSize(20)
        self.lbl_loan.setFont(font3)

        self.gridLayout_3.addWidget(self.lbl_loan, 1, 1, 1, 1)

        self.lbl_equipment = QLabel(self.frame_8)
        self.lbl_equipment.setObjectName(u"lbl_equipment")
        self.lbl_equipment.setMinimumSize(QSize(0, 50))
        self.lbl_equipment.setFont(font3)

        self.gridLayout_3.addWidget(self.lbl_equipment, 0, 1, 1, 1)

        self.lbl_no_2 = QLabel(self.frame_8)
        self.lbl_no_2.setObjectName(u"lbl_no_2")

        self.gridLayout_3.addWidget(self.lbl_no_2, 1, 0, 1, 1)

        self.lbl_no_1 = QLabel(self.frame_8)
        self.lbl_no_1.setObjectName(u"lbl_no_1")

        self.gridLayout_3.addWidget(self.lbl_no_1, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_8, 1, 0, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox.setFont(font3)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setSpacing(50)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 15, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.lbl_category = QLabel(self.groupBox)
        self.lbl_category.setObjectName(u"lbl_category")
        font4 = QFont()
        font4.setPointSize(25)
        self.lbl_category.setFont(font4)

        self.horizontalLayout_5.addWidget(self.lbl_category)

        self.lbl_arrow = QLabel(self.groupBox)
        self.lbl_arrow.setObjectName(u"lbl_arrow")

        self.horizontalLayout_5.addWidget(self.lbl_arrow)

        self.lbl_location = QLabel(self.groupBox)
        self.lbl_location.setObjectName(u"lbl_location")
        self.lbl_location.setFont(font4)

        self.horizontalLayout_5.addWidget(self.lbl_location)

        self.horizontalSpacer_2 = QSpacerItem(40, 15, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.gridLayout.addWidget(self.groupBox, 4, 0, 1, 3)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 40))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_2, 3, 0, 1, 2)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 150))
        self.frame_5.setMaximumSize(QSize(16777215, 100))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.lbl_3 = QLabel(self.frame_5)
        self.lbl_3.setObjectName(u"lbl_3")

        self.horizontalLayout_4.addWidget(self.lbl_3)

        self.lbl_confirm_info = QLabel(self.frame_5)
        self.lbl_confirm_info.setObjectName(u"lbl_confirm_info")
        font5 = QFont()
        font5.setPointSize(28)
        self.lbl_confirm_info.setFont(font5)

        self.horizontalLayout_4.addWidget(self.lbl_confirm_info)

        self.lbl_confirm_icon = QLabel(self.frame_5)
        self.lbl_confirm_icon.setObjectName(u"lbl_confirm_icon")

        self.horizontalLayout_4.addWidget(self.lbl_confirm_icon)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.gridLayout.addWidget(self.frame_5, 2, 0, 1, 3)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 30))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_4, 5, 0, 1, 2)

        self.frame_9 = QFrame(self.centralwidget)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_9)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(30)
        self.gridLayout_2.setContentsMargins(9, -1, -1, -1)
        self.lbl_eq_validate = QLabel(self.frame_9)
        self.lbl_eq_validate.setObjectName(u"lbl_eq_validate")
        self.lbl_eq_validate.setMinimumSize(QSize(60, 0))

        self.gridLayout_2.addWidget(self.lbl_eq_validate, 0, 0, 1, 1)

        self.btn_validate_eq = QPushButton(self.frame_9)
        self.btn_validate_eq.setObjectName(u"btn_validate_eq")
        self.btn_validate_eq.setMinimumSize(QSize(200, 70))
        self.btn_validate_eq.setFont(font3)

        self.gridLayout_2.addWidget(self.btn_validate_eq, 0, 1, 1, 1)

        self.lbl_loc_validate = QLabel(self.frame_9)
        self.lbl_loc_validate.setObjectName(u"lbl_loc_validate")

        self.gridLayout_2.addWidget(self.lbl_loc_validate, 1, 0, 1, 1)

        self.btn_validate_loc = QPushButton(self.frame_9)
        self.btn_validate_loc.setObjectName(u"btn_validate_loc")
        self.btn_validate_loc.setMinimumSize(QSize(200, 70))
        self.btn_validate_loc.setFont(font3)

        self.gridLayout_2.addWidget(self.btn_validate_loc, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_9, 1, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1310, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.txt_asset, self.txt_location)
        QWidget.setTabOrder(self.txt_location, self.btn_validate_loc)
        QWidget.setTabOrder(self.btn_validate_loc, self.btn_confirm)
        QWidget.setTabOrder(self.btn_confirm, self.btn_clear)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Library Loan", None))
        self.btn_confirm.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.lbl_loan.setText(QCoreApplication.translate("MainWindow", u"Type Location for Loan:", None))
        self.lbl_equipment.setText(QCoreApplication.translate("MainWindow", u" Scan or Type Equipment No:", None))
        self.lbl_no_2.setText("")
        self.lbl_no_1.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Loan Details", None))
        self.lbl_category.setText("")
        self.lbl_arrow.setText("")
        self.lbl_location.setText("")
        self.lbl_3.setText("")
        self.lbl_confirm_info.setText(QCoreApplication.translate("MainWindow", u"Press confirm to take out equipment", None))
        self.lbl_confirm_icon.setText("")
        self.lbl_eq_validate.setText("")
        self.btn_validate_eq.setText(QCoreApplication.translate("MainWindow", u"Validate", None))
        self.lbl_loc_validate.setText("")
        self.btn_validate_loc.setText(QCoreApplication.translate("MainWindow", u"Validate", None))
    # retranslateUi

