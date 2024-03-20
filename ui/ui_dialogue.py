# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loan_dialogue.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(892, 794)
        Dialog.setStyleSheet(u"QWidget {\n"
"	background-color: white\n"
"}\n"
"QLabel{\n"
"	font-size: 14pt;\n"
"}\n"
"QLineEdit {\n"
"	border: 1px;\n"
"	border-radius: 5px;\n"
"	font-size: 14pt;\n"
"	border: 1px solid rgb(33, 44, 200)\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid #127eff\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color:  #89CFF3;\n"
"padding: 5px 10px;\n"
"border-radius: 5px;	\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #127eff\n"
"}\n"
"QPushButton#btn_clear{\n"
"background-color: rgb(255, 137, 116);\n"
"}\n"
"QPushButton:hover#btn_clear{\n"
"	background-color: rgb(255, 106, 92) ;\n"
"}")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 15)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.rb_return_loan = QRadioButton(self.groupBox)
        self.rb_return_loan.setObjectName(u"rb_return_loan")
        self.rb_return_loan.setFont(font)

        self.horizontalLayout.addWidget(self.rb_return_loan)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.rb_create_job = QRadioButton(self.groupBox)
        self.rb_create_job.setObjectName(u"rb_create_job")
        self.rb_create_job.setFont(font)

        self.horizontalLayout.addWidget(self.rb_create_job)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.gridLayout.addWidget(self.groupBox, 4, 0, 1, 1)

        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFont(font)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_7 = QHBoxLayout(self.tab)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_5 = QFrame(self.tab)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 9, -1)
        self.chkbx_visual_insp = QCheckBox(self.frame_5)
        self.chkbx_visual_insp.setObjectName(u"chkbx_visual_insp")
        self.chkbx_visual_insp.setFont(font)

        self.verticalLayout.addWidget(self.chkbx_visual_insp)

        self.chkbx_function = QCheckBox(self.frame_5)
        self.chkbx_function.setObjectName(u"chkbx_function")
        self.chkbx_function.setFont(font)

        self.verticalLayout.addWidget(self.chkbx_function)

        self.chkbx_batt_replace = QCheckBox(self.frame_5)
        self.chkbx_batt_replace.setObjectName(u"chkbx_batt_replace")
        self.chkbx_batt_replace.setFont(font)

        self.verticalLayout.addWidget(self.chkbx_batt_replace)


        self.horizontalLayout_7.addWidget(self.frame_5)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(500, 16777215))
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.txt_work_done = QPlainTextEdit(self.groupBox_2)
        self.txt_work_done.setObjectName(u"txt_work_done")

        self.horizontalLayout_6.addWidget(self.txt_work_done)


        self.horizontalLayout_7.addWidget(self.groupBox_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_5 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_4 = QFrame(self.tab_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.rb_ppm = QRadioButton(self.frame_3)
        self.rb_ppm.setObjectName(u"rb_ppm")
        self.rb_ppm.setGeometry(QRect(10, 10, 104, 32))
        font1 = QFont()
        font1.setPointSize(16)
        self.rb_ppm.setFont(font1)
        self.rb_job = QRadioButton(self.frame_3)
        self.rb_job.setObjectName(u"rb_job")
        self.rb_job.setGeometry(QRect(10, 48, 119, 32))
        self.rb_job.setFont(font1)

        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.frame_4)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.txt_reported_fault = QTextEdit(self.groupBox_3)
        self.txt_reported_fault.setObjectName(u"txt_reported_fault")

        self.verticalLayout_3.addWidget(self.txt_reported_fault)


        self.gridLayout_2.addWidget(self.groupBox_3, 0, 1, 2, 1)

        self.groupBox_5 = QGroupBox(self.frame_4)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setFont(font1)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.txt_technician = QLineEdit(self.groupBox_5)
        self.txt_technician.setObjectName(u"txt_technician")

        self.verticalLayout_2.addWidget(self.txt_technician)


        self.gridLayout_2.addWidget(self.groupBox_5, 1, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.frame_4)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 7, 0, 1, 1)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 9, -1, 9)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout_3.addWidget(self.label)

        self.txt_username = QLineEdit(self.frame_2)
        self.txt_username.setObjectName(u"txt_username")
        self.txt_username.setFont(font)

        self.horizontalLayout_3.addWidget(self.txt_username)

        self.btn_confirm = QPushButton(self.frame_2)
        self.btn_confirm.setObjectName(u"btn_confirm")
        self.btn_confirm.setFont(font)

        self.horizontalLayout_3.addWidget(self.btn_confirm)


        self.gridLayout.addWidget(self.frame_2, 2, 0, 1, 1)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_submit_job = QPushButton(self.frame)
        self.btn_submit_job.setObjectName(u"btn_submit_job")
        self.btn_submit_job.setFont(font)

        self.horizontalLayout_2.addWidget(self.btn_submit_job)

        self.btn_print = QPushButton(self.frame)
        self.btn_print.setObjectName(u"btn_print")
        self.btn_print.setFont(font)

        self.horizontalLayout_2.addWidget(self.btn_print)

        self.btn_clear = QPushButton(self.frame)
        self.btn_clear.setObjectName(u"btn_clear")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setItalic(True)
        self.btn_clear.setFont(font2)

        self.horizontalLayout_2.addWidget(self.btn_clear)


        self.gridLayout.addWidget(self.frame, 8, 0, 1, 1)

        self.frame_6 = QFrame(Dialog)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(100, 16777215))
        self.label_3.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_3)

        self.lbl_technician = QLabel(self.frame_6)
        self.lbl_technician.setObjectName(u"lbl_technician")
        self.lbl_technician.setFont(font)

        self.horizontalLayout_8.addWidget(self.lbl_technician)


        self.gridLayout.addWidget(self.frame_6, 3, 0, 1, 1)

        self.frame_7 = QFrame(Dialog)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(421, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.lbl_loan = QLabel(self.frame_7)
        self.lbl_loan.setObjectName(u"lbl_loan")
        self.lbl_loan.setFont(font)

        self.horizontalLayout_4.addWidget(self.lbl_loan)

        self.horizontalSpacer_2 = QSpacerItem(420, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.gridLayout.addWidget(self.frame_7, 0, 0, 1, 1)

        self.groupBox_4 = QGroupBox(Dialog)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setFont(font)
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(30)
        self.gridLayout_4.setVerticalSpacing(6)
        self.txt_loan_location = QLineEdit(self.groupBox_4)
        self.txt_loan_location.setObjectName(u"txt_loan_location")
        self.txt_loan_location.setEnabled(False)
        self.txt_loan_location.setFont(font)

        self.gridLayout_4.addWidget(self.txt_loan_location, 2, 1, 1, 1)

        self.txt_asset = QLineEdit(self.groupBox_4)
        self.txt_asset.setObjectName(u"txt_asset")
        self.txt_asset.setEnabled(False)
        self.txt_asset.setFont(font)

        self.gridLayout_4.addWidget(self.txt_asset, 0, 1, 1, 1)

        self.txt_category = QLineEdit(self.groupBox_4)
        self.txt_category.setObjectName(u"txt_category")
        self.txt_category.setEnabled(False)
        self.txt_category.setFont(font)

        self.gridLayout_4.addWidget(self.txt_category, 1, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout_4.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_4, 1, 0, 1, 1)

        QWidget.setTabOrder(self.txt_username, self.rb_return_loan)
        QWidget.setTabOrder(self.rb_return_loan, self.rb_create_job)
        QWidget.setTabOrder(self.rb_create_job, self.chkbx_visual_insp)
        QWidget.setTabOrder(self.chkbx_visual_insp, self.chkbx_function)
        QWidget.setTabOrder(self.chkbx_function, self.chkbx_batt_replace)
        QWidget.setTabOrder(self.chkbx_batt_replace, self.txt_work_done)
        QWidget.setTabOrder(self.txt_work_done, self.btn_clear)
        QWidget.setTabOrder(self.btn_clear, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.rb_ppm)
        QWidget.setTabOrder(self.rb_ppm, self.rb_job)
        QWidget.setTabOrder(self.rb_job, self.txt_reported_fault)
        QWidget.setTabOrder(self.txt_reported_fault, self.txt_category)
        QWidget.setTabOrder(self.txt_category, self.txt_asset)
        QWidget.setTabOrder(self.txt_asset, self.txt_loan_location)

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Options", None))
        self.rb_return_loan.setText(QCoreApplication.translate("Dialog", u"Return Loan", None))
        self.rb_create_job.setText(QCoreApplication.translate("Dialog", u"Create Job for Workshop", None))
        self.chkbx_visual_insp.setText(QCoreApplication.translate("Dialog", u"Visual Inspection", None))
        self.chkbx_function.setText(QCoreApplication.translate("Dialog", u"Function Check", None))
        self.chkbx_batt_replace.setText(QCoreApplication.translate("Dialog", u"Battery replaced", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Work Done", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"Return Loan", None))
        self.rb_ppm.setText(QCoreApplication.translate("Dialog", u"PPM Job", None))
        self.rb_job.setText(QCoreApplication.translate("Dialog", u"Repair Job", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Reported fault", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Dialog", u"Assign to technician", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"Create Job", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Enter your useranme to unlock the form:", None))
        self.btn_confirm.setText(QCoreApplication.translate("Dialog", u"Confirm", None))
        self.btn_submit_job.setText(QCoreApplication.translate("Dialog", u"Submit", None))
        self.btn_print.setText(QCoreApplication.translate("Dialog", u"Print", None))
        self.btn_clear.setText(QCoreApplication.translate("Dialog", u"Clear", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Technician:", None))
        self.lbl_technician.setText("")
        self.lbl_loan.setText(QCoreApplication.translate("Dialog", u"Loan Return", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog", u"Equipment Details", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Category:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Loan Location:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Equipment No:", None))
    # retranslateUi

