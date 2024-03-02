# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_no_icon.ui'
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
        MainWindow.resize(1350, 877)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(20)
        self.frame_9 = QFrame(self.centralwidget)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_9)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_validate_eq = QPushButton(self.frame_9)
        self.btn_validate_eq.setObjectName(u"btn_validate_eq")
        self.btn_validate_eq.setMinimumSize(QSize(200, 70))
        font = QFont()
        font.setPointSize(20)
        self.btn_validate_eq.setFont(font)

        self.verticalLayout_3.addWidget(self.btn_validate_eq)

        self.btn_validate_loc = QPushButton(self.frame_9)
        self.btn_validate_loc.setObjectName(u"btn_validate_loc")
        self.btn_validate_loc.setMinimumSize(QSize(200, 70))
        self.btn_validate_loc.setFont(font)

        self.verticalLayout_3.addWidget(self.btn_validate_loc)


        self.gridLayout.addWidget(self.frame_9, 1, 2, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.txt_asset = QLineEdit(self.frame)
        self.txt_asset.setObjectName(u"txt_asset")
        self.txt_asset.setMinimumSize(QSize(0, 70))
        font1 = QFont()
        font1.setPointSize(30)
        self.txt_asset.setFont(font1)

        self.verticalLayout_2.addWidget(self.txt_asset)

        self.txt_location = QLineEdit(self.frame)
        self.txt_location.setObjectName(u"txt_location")
        self.txt_location.setMinimumSize(QSize(0, 70))
        self.txt_location.setFont(font1)

        self.verticalLayout_2.addWidget(self.txt_location)


        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(80)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(80, -1, 80, -1)
        self.bt_confirm = QPushButton(self.frame_3)
        self.bt_confirm.setObjectName(u"bt_confirm")
        self.bt_confirm.setMinimumSize(QSize(0, 100))
        font2 = QFont()
        font2.setPointSize(40)
        self.bt_confirm.setFont(font2)

        self.horizontalLayout.addWidget(self.bt_confirm)

        self.btn_clear = QPushButton(self.frame_3)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setMinimumSize(QSize(0, 100))
        self.btn_clear.setFont(font2)

        self.horizontalLayout.addWidget(self.btn_clear)


        self.gridLayout.addWidget(self.frame_3, 3, 0, 1, 3)

        self.frame_8 = QFrame(self.centralwidget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame_8)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 50))
        font3 = QFont()
        font3.setPointSize(25)
        self.label.setFont(font3)

        self.verticalLayout.addWidget(self.label)

        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 50))
        self.label_3.setFont(font3)

        self.verticalLayout.addWidget(self.label_3)


        self.gridLayout.addWidget(self.frame_8, 1, 0, 1, 1)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        font4 = QFont()
        font4.setFamilies([u"Franklin Gothic Book"])
        font4.setPointSize(25)
        self.label_4.setFont(font4)

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.lbl_icon_eq = QLabel(self.frame_4)
        self.lbl_icon_eq.setObjectName(u"lbl_icon_eq")
        self.lbl_icon_eq.setPixmap(QPixmap(u":/icon/confirm-96.png"))

        self.gridLayout_2.addWidget(self.lbl_icon_eq, 0, 1, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lbl_icon_loc = QLabel(self.frame_6)
        self.lbl_icon_loc.setObjectName(u"lbl_icon_loc")
        self.lbl_icon_loc.setPixmap(QPixmap(u":/icon/confirm-96.png"))

        self.gridLayout_3.addWidget(self.lbl_icon_loc, 0, 1, 1, 1)

        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font4)

        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_7)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font4)

        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)

        self.lbl_icon_confirm = QLabel(self.frame_7)
        self.lbl_icon_confirm.setObjectName(u"lbl_icon_confirm")
        self.lbl_icon_confirm.setPixmap(QPixmap(u":/icon/confirm-96.png"))

        self.gridLayout_4.addWidget(self.lbl_icon_confirm, 0, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.frame_7)


        self.gridLayout.addWidget(self.frame_5, 0, 0, 1, 3)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setSpacing(50)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.lbl_details = QLabel(self.groupBox)
        self.lbl_details.setObjectName(u"lbl_details")
        font5 = QFont()
        font5.setPointSize(26)
        self.lbl_details.setFont(font5)

        self.horizontalLayout_5.addWidget(self.lbl_details)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1350, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.txt_asset, self.btn_validate_eq)
        QWidget.setTabOrder(self.btn_validate_eq, self.txt_location)
        QWidget.setTabOrder(self.txt_location, self.btn_validate_loc)
        QWidget.setTabOrder(self.btn_validate_loc, self.bt_confirm)
        QWidget.setTabOrder(self.bt_confirm, self.btn_clear)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_validate_eq.setText(QCoreApplication.translate("MainWindow", u"Validate", None))
        self.btn_validate_loc.setText(QCoreApplication.translate("MainWindow", u"Validate", None))
        self.bt_confirm.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Equipment Number:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Location for loan:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"1. Scan equipment", None))
        self.lbl_icon_eq.setText("")
        self.lbl_icon_loc.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"2. Scan Location", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"3. Confirm", None))
        self.lbl_icon_confirm.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Loan Details", None))
        self.lbl_details.setText("")
    # retranslateUi

