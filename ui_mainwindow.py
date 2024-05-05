# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTabWidget,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1515, 894)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet(u"QWidget{\n"
"background-color: white;\n"
"}\n"
"QLineEdit{\n"
"border-radius: 15px;\n"
"border: 1px solid black;\n"
"}\n"
"\n"
"QWidget#side_menu {\n"
"background-color: #16161a;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QWidget#side_menu_2 {\n"
"background-color: #16161a;\n"
"border-radius: 15px;\n"
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
"	padding-left:7px;\n"
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
"QPushButton:checked{\n"
"border-left: 5px solid #fc0d0d;\n"
"border-radius:0px;\n"
"font-weight:bold;\n"
"background-color:#2544af;\n"
"}\n"
"\n"
"\n"
"QPushButton#btn_user{\n"
"	color: white;\n"
"	font:15pt;\n"
"	font-weight: bold;\n"
"	padding: 10px 10px;\n"
"	border-radius: 20px;\n"
"	text-align: centre;\n"
"}\n"
"\n"
"QPushBu"
                        "tton#btn_user_2{\n"
"	color: white;\n"
"	font:14pt;\n"
"	font-weight: bold;\n"
"	padding: 10px 10px;\n"
"	border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton#btn_confirm{\n"
"	padding: 10px 70px;\n"
"	font: 30pt;\n"
"}\n"
"\n"
"QPushButton#btn_clear{\n"
"	background-color: #e5e5e5;\n"
"	color: black;\n"
"	border: 1px solid transparent;\n"
"	font: 30px;\n"
"	padding: 10px 50px;\n"
"}\n"
"\n"
"QPushButton#btn_clear:hover{\n"
"	background-color: #b2b2b2;\n"
"	color:black;\n"
"	font: 30px;\n"
"}\n"
"QPushButton#btn_clear:pressed{\n"
"	background-color: #989898;\n"
"}\n"
"\n"
"QLineEdit#txt_technician{\n"
"padding: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #1a307c;\n"
"}\n"
"\n"
"QPushButton#btn_validate_eq{\n"
"text-align: centre;\n"
"padding-left: 20px;\n"
"}\n"
"\n"
"QPushButton#btn_validate_loc{\n"
"text-align: centre;\n"
"padding-left: 20px;\n"
"}\n"
"\n"
"QPushButton#btn_validate_loc{\n"
"text-align: centre;\n"
"padding-left: 20px;\n"
"}\n"
"QPushButton#btn_submit{\n"
"text-align: centre;\n"
""
                        "font: 25px;\n"
"padding: 10px 30px;\n"
"}\n"
"\n"
"QPushButton#btn_print{\n"
"text-align: centre;\n"
"font: 25px;\n"
"padding: 10px 30px;\n"
"}\n"
"\n"
"QPushButton#btn_clear_2{\n"
"	text-align: centre;\n"
"	background-color: #e5e5e5;\n"
"	color: black;\n"
"	font: 25px;\n"
"	padding: 10px 20px;\n"
"}\n"
"QPushButton#btn_clear_2:hover{\n"
"	background-color: #b2b2b2;\n"
"	color: black;\n"
"	font: 25px;\n"
"	padding: 10px 20px;\n"
"}\n"
"QPushButton#btn_clear_2:pressed{\n"
"	background-color: #989898;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid  #0082ff;\n"
"}\n"
"\n"
"QPlainTextEdit:focus{\n"
"border: 2px solid  #0082ff;\n"
"}\n"
"\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 2px solid #C2C7CB;\n"
"}\n"
"\n"
"/*QTabBar::tab {\n"
"    background: blue;\n"
"    border: 2px solid black;\n"
"	color: white;\n"
"    border-bottom-color: #C2C7CB;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"}*/\n"
"\n"
"Q"
                        "TabBar::tab:selected{\n"
"    background: \n"
"}\n"
"QTabBar::tab::hover{\n"
"background: #3561fb;\n"
"}\n"
"QLineEdit#txt_asset_2, #txt_rtls_battery, #txt_loan_location, #txt_category{\n"
"padding: 0px 20px;\n"
"}\n"
"\n"
"QMessageBox#QPushButton{\n"
"min-width: 100px;\n"
" background-color: #d0d0d0;\n"
"    }\n"
"  QMessageBox#QPushButton:default{\n"
" background-color:#2544af;\n"
"   }\n"
"\n"
"QFrame#frame_user{\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QPushButton#btn_change_user, #btn_logout_4{\n"
"	padding: 5px 15px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#btn_user_2:checked{\n"
"background-color:#009639;\n"
"border: 0px;\n"
"}\n"
"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.side_menu_2 = QWidget(self.centralwidget)
        self.side_menu_2.setObjectName(u"side_menu_2")
        self.side_menu_2.setMinimumSize(QSize(200, 0))
        self.side_menu_2.setMaximumSize(QSize(210, 16777215))
        self.side_menu_2.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.side_menu_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_user_2 = QPushButton(self.side_menu_2)
        self.btn_user_2.setObjectName(u"btn_user_2")
        self.btn_user_2.setEnabled(True)
        self.btn_user_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_user_2.setLayoutDirection(Qt.LeftToRight)
        self.btn_user_2.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons8-user-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_user_2.setIcon(icon)
        self.btn_user_2.setIconSize(QSize(50, 50))
        self.btn_user_2.setCheckable(False)

        self.verticalLayout.addWidget(self.btn_user_2)

        self.frame_user = QFrame(self.side_menu_2)
        self.frame_user.setObjectName(u"frame_user")
        self.frame_user.setMinimumSize(QSize(0, 100))
        self.frame_user.setFrameShape(QFrame.StyledPanel)
        self.frame_user.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_user)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.btn_change_user = QPushButton(self.frame_user)
        self.btn_change_user.setObjectName(u"btn_change_user")
        self.btn_change_user.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/change-user-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_change_user.setIcon(icon1)
        self.btn_change_user.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.btn_change_user)

        self.btn_logout_4 = QPushButton(self.frame_user)
        self.btn_logout_4.setObjectName(u"btn_logout_4")
        self.btn_logout_4.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons8-log-out-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_logout_4.setIcon(icon2)
        self.btn_logout_4.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.btn_logout_4)


        self.verticalLayout.addWidget(self.frame_user)

        self.btn_menu_2 = QPushButton(self.side_menu_2)
        self.btn_menu_2.setObjectName(u"btn_menu_2")
        self.btn_menu_2.setEnabled(True)
        self.btn_menu_2.setMinimumSize(QSize(210, 0))
        self.btn_menu_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_2.setLayoutDirection(Qt.LeftToRight)
        icon3 = QIcon()
        icon3.addFile(u":/icons8-menu-vertical-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu_2.setIcon(icon3)
        self.btn_menu_2.setIconSize(QSize(30, 40))
        self.btn_menu_2.setCheckable(True)

        self.verticalLayout.addWidget(self.btn_menu_2)

        self.btn_home_2 = QPushButton(self.side_menu_2)
        self.btn_home_2.setObjectName(u"btn_home_2")
        self.btn_home_2.setMinimumSize(QSize(210, 0))
        self.btn_home_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons8-home-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home_2.setIcon(icon4)
        self.btn_home_2.setIconSize(QSize(40, 40))
        self.btn_home_2.setCheckable(True)
        self.btn_home_2.setChecked(True)
        self.btn_home_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_home_2)

        self.btn_check_in_2 = QPushButton(self.side_menu_2)
        self.btn_check_in_2.setObjectName(u"btn_check_in_2")
        self.btn_check_in_2.setEnabled(True)
        self.btn_check_in_2.setMinimumSize(QSize(210, 0))
        self.btn_check_in_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons8-checkout-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_check_in_2.setIcon(icon5)
        self.btn_check_in_2.setIconSize(QSize(40, 40))
        self.btn_check_in_2.setCheckable(True)
        self.btn_check_in_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_check_in_2)

        self.btn_dashboard_2 = QPushButton(self.side_menu_2)
        self.btn_dashboard_2.setObjectName(u"btn_dashboard_2")
        self.btn_dashboard_2.setEnabled(True)
        self.btn_dashboard_2.setMinimumSize(QSize(210, 0))
        self.btn_dashboard_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons8-dashboard-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_dashboard_2.setIcon(icon6)
        self.btn_dashboard_2.setIconSize(QSize(40, 40))
        self.btn_dashboard_2.setCheckable(True)
        self.btn_dashboard_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_dashboard_2)

        self.verticalSpacer_3 = QSpacerItem(20, 300, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.btn_setting_2 = QPushButton(self.side_menu_2)
        self.btn_setting_2.setObjectName(u"btn_setting_2")
        self.btn_setting_2.setEnabled(True)
        self.btn_setting_2.setMinimumSize(QSize(210, 0))
        self.btn_setting_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons8-setting-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_setting_2.setIcon(icon7)
        self.btn_setting_2.setIconSize(QSize(40, 40))
        self.btn_setting_2.setCheckable(True)
        self.btn_setting_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_setting_2)

        self.btn_help_2 = QPushButton(self.side_menu_2)
        self.btn_help_2.setObjectName(u"btn_help_2")
        self.btn_help_2.setMinimumSize(QSize(210, 0))
        self.btn_help_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons8-help-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_help_2.setIcon(icon8)
        self.btn_help_2.setIconSize(QSize(40, 40))
        self.btn_help_2.setCheckable(True)
        self.btn_help_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_help_2)

        self.btn_report_2 = QPushButton(self.side_menu_2)
        self.btn_report_2.setObjectName(u"btn_report_2")
        self.btn_report_2.setMinimumSize(QSize(210, 0))
        self.btn_report_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons8-issue-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_report_2.setIcon(icon9)
        self.btn_report_2.setIconSize(QSize(40, 40))
        self.btn_report_2.setCheckable(True)
        self.btn_report_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_report_2)

        self.line = QFrame(self.side_menu_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.btn_logout_2 = QPushButton(self.side_menu_2)
        self.btn_logout_2.setObjectName(u"btn_logout_2")
        self.btn_logout_2.setMinimumSize(QSize(210, 0))
        self.btn_logout_2.setStyleSheet(u"")
        self.btn_logout_2.setIcon(icon2)
        self.btn_logout_2.setIconSize(QSize(40, 40))
        self.btn_logout_2.setCheckable(False)

        self.verticalLayout.addWidget(self.btn_logout_2)


        self.gridLayout.addWidget(self.side_menu_2, 0, 1, 2, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.gridLayout_7 = QGridLayout(self.page_home)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.frame_5 = QFrame(self.page_home)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 100))
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
        font = QFont()
        font.setPointSize(28)
        self.lbl_confirm_info.setFont(font)

        self.horizontalLayout_4.addWidget(self.lbl_confirm_info)

        self.lbl_confirm_icon = QLabel(self.frame_5)
        self.lbl_confirm_icon.setObjectName(u"lbl_confirm_icon")

        self.horizontalLayout_4.addWidget(self.lbl_confirm_icon)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.gridLayout_7.addWidget(self.frame_5, 2, 0, 1, 2)

        self.frame_2 = QFrame(self.page_home)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 200))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_8)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lbl_no_1 = QLabel(self.frame_8)
        self.lbl_no_1.setObjectName(u"lbl_no_1")

        self.gridLayout_6.addWidget(self.lbl_no_1, 0, 0, 1, 1)

        self.lbl_equipment = QLabel(self.frame_8)
        self.lbl_equipment.setObjectName(u"lbl_equipment")
        self.lbl_equipment.setMinimumSize(QSize(0, 50))
        font1 = QFont()
        font1.setPointSize(20)
        self.lbl_equipment.setFont(font1)

        self.gridLayout_6.addWidget(self.lbl_equipment, 0, 1, 1, 1)

        self.lbl_no_2 = QLabel(self.frame_8)
        self.lbl_no_2.setObjectName(u"lbl_no_2")

        self.gridLayout_6.addWidget(self.lbl_no_2, 1, 0, 1, 1)

        self.lbl_loan = QLabel(self.frame_8)
        self.lbl_loan.setObjectName(u"lbl_loan")
        self.lbl_loan.setMinimumSize(QSize(0, 50))
        self.lbl_loan.setFont(font1)

        self.gridLayout_6.addWidget(self.lbl_loan, 1, 1, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_8)

        self.frame = QFrame(self.frame_2)
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


        self.horizontalLayout_3.addWidget(self.frame)

        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_9)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(30)
        self.gridLayout_2.setContentsMargins(9, -1, -1, -1)
        self.lbl_loc_validate = QLabel(self.frame_9)
        self.lbl_loc_validate.setObjectName(u"lbl_loc_validate")

        self.gridLayout_2.addWidget(self.lbl_loc_validate, 1, 0, 1, 1)

        self.lbl_eq_validate = QLabel(self.frame_9)
        self.lbl_eq_validate.setObjectName(u"lbl_eq_validate")
        self.lbl_eq_validate.setMinimumSize(QSize(60, 0))

        self.gridLayout_2.addWidget(self.lbl_eq_validate, 0, 0, 1, 1)

        self.btn_validate_eq = QPushButton(self.frame_9)
        self.btn_validate_eq.setObjectName(u"btn_validate_eq")
        self.btn_validate_eq.setMinimumSize(QSize(150, 70))
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(False)
        font3.setItalic(False)
        self.btn_validate_eq.setFont(font3)
        self.btn_validate_eq.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_validate_eq.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_2.addWidget(self.btn_validate_eq, 0, 1, 1, 1)

        self.btn_validate_loc = QPushButton(self.frame_9)
        self.btn_validate_loc.setObjectName(u"btn_validate_loc")
        self.btn_validate_loc.setEnabled(False)
        self.btn_validate_loc.setMinimumSize(QSize(150, 70))
        self.btn_validate_loc.setFont(font3)
        self.btn_validate_loc.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_validate_loc.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout_2.addWidget(self.btn_validate_loc, 1, 1, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_9)


        self.gridLayout_7.addWidget(self.frame_2, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.page_home)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox.setFont(font1)
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


        self.gridLayout_7.addWidget(self.groupBox, 4, 0, 1, 2)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_7.addItem(self.verticalSpacer_6, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_7.addItem(self.verticalSpacer_2, 6, 0, 1, 1)

        self.frame_3 = QFrame(self.page_home)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 150))
        self.frame_3.setLayoutDirection(Qt.LeftToRight)
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.btn_confirm = QPushButton(self.frame_3)
        self.btn_confirm.setObjectName(u"btn_confirm")
        self.btn_confirm.setEnabled(False)
        self.btn_confirm.setMinimumSize(QSize(60, 100))
        font5 = QFont()
        font5.setPointSize(30)
        font5.setBold(False)
        font5.setItalic(False)
        self.btn_confirm.setFont(font5)
        self.btn_confirm.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_confirm.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_confirm)

        self.horizontalSpacer_8 = QSpacerItem(60, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_8)

        self.btn_clear = QPushButton(self.frame_3)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setMinimumSize(QSize(60, 100))
        font6 = QFont()
        font6.setBold(False)
        font6.setItalic(False)
        self.btn_clear.setFont(font6)
        self.btn_clear.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_clear.setLayoutDirection(Qt.LeftToRight)
        icon10 = QIcon()
        icon10.addFile(u":/clear-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_clear.setIcon(icon10)
        self.btn_clear.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.btn_clear)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)


        self.gridLayout_7.addWidget(self.frame_3, 5, 0, 1, 2)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_7.addItem(self.verticalSpacer_7, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_home)
        self.page_check_in = QWidget()
        self.page_check_in.setObjectName(u"page_check_in")
        self.verticalLayout_10 = QVBoxLayout(self.page_check_in)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, -1, 100, 50)
        self.groupBox_4 = QGroupBox(self.page_check_in)
        self.groupBox_4.setObjectName(u"groupBox_4")
        font7 = QFont()
        font7.setPointSize(14)
        self.groupBox_4.setFont(font7)
        self.gridLayout_5 = QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(30)
        self.gridLayout_5.setVerticalSpacing(6)
        self.gridLayout_5.setContentsMargins(20, -1, -1, 20)
        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font7)

        self.gridLayout_5.addWidget(self.label_2, 2, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font7)

        self.gridLayout_5.addWidget(self.label_6, 1, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(200, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_10, 1, 3, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_11, 1, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font7)

        self.gridLayout_5.addWidget(self.label_3, 3, 1, 1, 1)

        self.txt_asset_2 = QLineEdit(self.groupBox_4)
        self.txt_asset_2.setObjectName(u"txt_asset_2")
        self.txt_asset_2.setEnabled(False)
        self.txt_asset_2.setFont(font7)
        self.txt_asset_2.setLayoutDirection(Qt.LeftToRight)
        self.txt_asset_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.txt_asset_2.setReadOnly(False)

        self.gridLayout_5.addWidget(self.txt_asset_2, 0, 2, 1, 1)

        self.txt_loan_location = QLineEdit(self.groupBox_4)
        self.txt_loan_location.setObjectName(u"txt_loan_location")
        self.txt_loan_location.setEnabled(False)
        self.txt_loan_location.setFont(font7)

        self.gridLayout_5.addWidget(self.txt_loan_location, 2, 2, 1, 1)

        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font7)

        self.gridLayout_5.addWidget(self.label_4, 0, 1, 1, 1)

        self.txt_category = QLineEdit(self.groupBox_4)
        self.txt_category.setObjectName(u"txt_category")
        self.txt_category.setEnabled(False)
        self.txt_category.setFont(font7)

        self.gridLayout_5.addWidget(self.txt_category, 1, 2, 1, 1)

        self.txt_rtls_battery = QLineEdit(self.groupBox_4)
        self.txt_rtls_battery.setObjectName(u"txt_rtls_battery")
        self.txt_rtls_battery.setEnabled(False)
        self.txt_rtls_battery.setFont(font7)

        self.gridLayout_5.addWidget(self.txt_rtls_battery, 3, 2, 1, 1)


        self.verticalLayout_10.addWidget(self.groupBox_4)

        self.tabWidget = QTabWidget(self.page_check_in)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(800, 0))
        self.tabWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tabWidget.setFont(font7)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_9 = QVBoxLayout(self.tab)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.groupBox_8 = QGroupBox(self.tab)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setMaximumSize(QSize(1200, 16777215))
        font8 = QFont()
        font8.setPointSize(16)
        self.groupBox_8.setFont(font8)
        self.groupBox_8.setCursor(QCursor(Qt.ArrowCursor))
        self.gridLayout_4 = QGridLayout(self.groupBox_8)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, -1, 400, -1)
        self.chkbx_visual_insp = QCheckBox(self.groupBox_8)
        self.chkbx_visual_insp.setObjectName(u"chkbx_visual_insp")
        self.chkbx_visual_insp.setFont(font7)
        self.chkbx_visual_insp.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.chkbx_visual_insp, 0, 0, 1, 1)

        self.chkbx_batt_replace = QCheckBox(self.groupBox_8)
        self.chkbx_batt_replace.setObjectName(u"chkbx_batt_replace")
        self.chkbx_batt_replace.setFont(font7)
        self.chkbx_batt_replace.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.chkbx_batt_replace, 0, 1, 2, 1)

        self.chkbx_function = QCheckBox(self.groupBox_8)
        self.chkbx_function.setObjectName(u"chkbx_function")
        self.chkbx_function.setFont(font7)
        self.chkbx_function.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.chkbx_function, 1, 0, 2, 1)

        self.chkbx_batt_replace_2 = QCheckBox(self.groupBox_8)
        self.chkbx_batt_replace_2.setObjectName(u"chkbx_batt_replace_2")
        self.chkbx_batt_replace_2.setFont(font7)
        self.chkbx_batt_replace_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.chkbx_batt_replace_2, 2, 1, 1, 1)


        self.verticalLayout_9.addWidget(self.groupBox_8)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(1200, 16777215))
        self.groupBox_3.setFont(font7)
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.txt_work_done = QPlainTextEdit(self.groupBox_3)
        self.txt_work_done.setObjectName(u"txt_work_done")
        self.txt_work_done.setMinimumSize(QSize(0, 0))
        self.txt_work_done.setFont(font7)

        self.horizontalLayout_6.addWidget(self.txt_work_done)


        self.verticalLayout_9.addWidget(self.groupBox_3)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_9 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_4 = QFrame(self.tab_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_4)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.groupBox_7 = QGroupBox(self.frame_4)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMaximumSize(QSize(1200, 16777215))
        self.groupBox_7.setFont(font7)
        self.gridLayout_3 = QGridLayout(self.groupBox_7)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.txt_reported_fault = QPlainTextEdit(self.groupBox_7)
        self.txt_reported_fault.setObjectName(u"txt_reported_fault")
        self.txt_reported_fault.setFont(font7)

        self.gridLayout_3.addWidget(self.txt_reported_fault, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_7, 2, 0, 1, 1)

        self.groupBox_9 = QGroupBox(self.frame_4)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setMaximumSize(QSize(1200, 16777215))
        self.groupBox_9.setFont(font8)
        self.gridLayout_8 = QGridLayout(self.groupBox_9)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.rb_job = QRadioButton(self.groupBox_9)
        self.rb_job.setObjectName(u"rb_job")
        self.rb_job.setFont(font7)
        self.rb_job.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_8.addWidget(self.rb_job, 1, 0, 1, 1)

        self.rb_ppm = QRadioButton(self.groupBox_9)
        self.rb_ppm.setObjectName(u"rb_ppm")
        self.rb_ppm.setFont(font7)
        self.rb_ppm.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_8.addWidget(self.rb_ppm, 0, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_7, 1, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_9, 0, 1, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_9, 0, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.frame_4)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMaximumSize(QSize(1200, 16777215))
        self.groupBox_5.setFont(font8)
        self.gridLayout_9 = QGridLayout(self.groupBox_5)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.txt_technician = QLineEdit(self.groupBox_5)
        self.txt_technician.setObjectName(u"txt_technician")
        font9 = QFont()
        font9.setPointSize(12)
        self.txt_technician.setFont(font9)

        self.gridLayout_9.addWidget(self.txt_technician, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_5, 1, 0, 1, 1)


        self.horizontalLayout_9.addWidget(self.frame_4)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_10.addWidget(self.tabWidget)

        self.frame_7 = QFrame(self.page_check_in)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 80))
        self.frame_7.setFont(font7)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_10.setSpacing(20)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.btn_submit = QPushButton(self.frame_7)
        self.btn_submit.setObjectName(u"btn_submit")
        self.btn_submit.setEnabled(True)
        self.btn_submit.setMinimumSize(QSize(0, 50))
        self.btn_submit.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.btn_submit)

        self.btn_print = QPushButton(self.frame_7)
        self.btn_print.setObjectName(u"btn_print")
        self.btn_print.setEnabled(True)
        self.btn_print.setMinimumSize(QSize(0, 50))
        self.btn_print.setFont(font6)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_10.addWidget(self.btn_print)

        self.btn_clear_2 = QPushButton(self.frame_7)
        self.btn_clear_2.setObjectName(u"btn_clear_2")
        self.btn_clear_2.setMinimumSize(QSize(0, 50))
        self.btn_clear_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/clear_30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_clear_2.setIcon(icon11)
        self.btn_clear_2.setIconSize(QSize(30, 30))

        self.horizontalLayout_10.addWidget(self.btn_clear_2)


        self.verticalLayout_10.addWidget(self.frame_7)

        self.stackedWidget.addWidget(self.page_check_in)

        self.gridLayout.addWidget(self.stackedWidget, 0, 2, 1, 1)

        self.side_menu = QWidget(self.centralwidget)
        self.side_menu.setObjectName(u"side_menu")
        self.side_menu.setMaximumSize(QSize(80, 16777215))
        self.side_menu.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.side_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, -1, -1, -1)
        self.btn_user = QPushButton(self.side_menu)
        self.btn_user.setObjectName(u"btn_user")
        self.btn_user.setMinimumSize(QSize(35, 40))
        self.btn_user.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_user.setStyleSheet(u"")
        self.btn_user.setIcon(icon)
        self.btn_user.setIconSize(QSize(50, 50))
        self.btn_user.setCheckable(False)

        self.verticalLayout_3.addWidget(self.btn_user)

        self.frame_user_2 = QFrame(self.side_menu)
        self.frame_user_2.setObjectName(u"frame_user_2")
        self.frame_user_2.setMinimumSize(QSize(0, 100))
        self.frame_user_2.setFrameShape(QFrame.StyledPanel)
        self.frame_user_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_user_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.btn_change_user_3 = QPushButton(self.frame_user_2)
        self.btn_change_user_3.setObjectName(u"btn_change_user_3")
        self.btn_change_user_3.setIcon(icon1)
        self.btn_change_user_3.setIconSize(QSize(30, 30))

        self.verticalLayout_8.addWidget(self.btn_change_user_3)

        self.btn_logout_8 = QPushButton(self.frame_user_2)
        self.btn_logout_8.setObjectName(u"btn_logout_8")
        self.btn_logout_8.setCheckable(False)

        self.verticalLayout_8.addWidget(self.btn_logout_8)


        self.verticalLayout_3.addWidget(self.frame_user_2)

        self.btn_menu = QPushButton(self.side_menu)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setMinimumSize(QSize(70, 0))
        self.btn_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu.setLayoutDirection(Qt.LeftToRight)
        self.btn_menu.setStyleSheet(u"")
        icon12 = QIcon()
        icon12.addFile(u":/icons8-menu-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon12)
        self.btn_menu.setIconSize(QSize(40, 40))
        self.btn_menu.setCheckable(True)
        self.btn_menu.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn_menu)

        self.btn_home = QPushButton(self.side_menu)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(70, 0))
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setIcon(icon4)
        self.btn_home.setIconSize(QSize(40, 40))
        self.btn_home.setCheckable(True)
        self.btn_home.setChecked(True)
        self.btn_home.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn_home)

        self.btn_check_in = QPushButton(self.side_menu)
        self.btn_check_in.setObjectName(u"btn_check_in")
        self.btn_check_in.setEnabled(True)
        self.btn_check_in.setMinimumSize(QSize(70, 0))
        self.btn_check_in.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_check_in.setIcon(icon5)
        self.btn_check_in.setIconSize(QSize(40, 40))
        self.btn_check_in.setCheckable(True)
        self.btn_check_in.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn_check_in)

        self.btn_dashboard = QPushButton(self.side_menu)
        self.btn_dashboard.setObjectName(u"btn_dashboard")
        self.btn_dashboard.setEnabled(True)
        self.btn_dashboard.setMinimumSize(QSize(70, 0))
        self.btn_dashboard.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_dashboard.setIcon(icon6)
        self.btn_dashboard.setIconSize(QSize(40, 40))
        self.btn_dashboard.setCheckable(True)
        self.btn_dashboard.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn_dashboard)

        self.verticalSpacer = QSpacerItem(20, 300, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.btn_setting = QPushButton(self.side_menu)
        self.btn_setting.setObjectName(u"btn_setting")
        self.btn_setting.setEnabled(True)
        self.btn_setting.setMinimumSize(QSize(70, 0))
        self.btn_setting.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_setting.setIcon(icon7)
        self.btn_setting.setIconSize(QSize(40, 40))
        self.btn_setting.setCheckable(True)
        self.btn_setting.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn_setting)

        self.btn_help = QPushButton(self.side_menu)
        self.btn_help.setObjectName(u"btn_help")
        self.btn_help.setMinimumSize(QSize(70, 0))
        self.btn_help.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_help.setIcon(icon8)
        self.btn_help.setIconSize(QSize(40, 40))
        self.btn_help.setCheckable(True)
        self.btn_help.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn_help)

        self.btn_report = QPushButton(self.side_menu)
        self.btn_report.setObjectName(u"btn_report")
        self.btn_report.setMinimumSize(QSize(70, 0))
        self.btn_report.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_report.setIcon(icon9)
        self.btn_report.setIconSize(QSize(40, 40))
        self.btn_report.setCheckable(True)
        self.btn_report.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn_report)

        self.line_2 = QFrame(self.side_menu)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.btn_logout = QPushButton(self.side_menu)
        self.btn_logout.setObjectName(u"btn_logout")
        self.btn_logout.setMinimumSize(QSize(70, 0))
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setStyleSheet(u"")
        self.btn_logout.setIcon(icon2)
        self.btn_logout.setIconSize(QSize(40, 40))
        self.btn_logout.setCheckable(False)

        self.verticalLayout_3.addWidget(self.btn_logout)


        self.gridLayout.addWidget(self.side_menu, 0, 0, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.txt_asset, self.btn_validate_eq)
        QWidget.setTabOrder(self.btn_validate_eq, self.txt_location)
        QWidget.setTabOrder(self.txt_location, self.btn_validate_loc)
        QWidget.setTabOrder(self.btn_validate_loc, self.btn_confirm)
        QWidget.setTabOrder(self.btn_confirm, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.chkbx_visual_insp)
        QWidget.setTabOrder(self.chkbx_visual_insp, self.chkbx_function)
        QWidget.setTabOrder(self.chkbx_function, self.chkbx_batt_replace)
        QWidget.setTabOrder(self.chkbx_batt_replace, self.chkbx_batt_replace_2)
        QWidget.setTabOrder(self.chkbx_batt_replace_2, self.txt_work_done)
        QWidget.setTabOrder(self.txt_work_done, self.btn_submit)
        QWidget.setTabOrder(self.btn_submit, self.btn_print)
        QWidget.setTabOrder(self.btn_print, self.btn_clear_2)
        QWidget.setTabOrder(self.btn_clear_2, self.rb_ppm)
        QWidget.setTabOrder(self.rb_ppm, self.rb_job)
        QWidget.setTabOrder(self.rb_job, self.txt_technician)
        QWidget.setTabOrder(self.txt_technician, self.txt_reported_fault)
        QWidget.setTabOrder(self.txt_reported_fault, self.btn_user_2)
        QWidget.setTabOrder(self.btn_user_2, self.btn_home_2)
        QWidget.setTabOrder(self.btn_home_2, self.btn_check_in_2)
        QWidget.setTabOrder(self.btn_check_in_2, self.btn_dashboard_2)
        QWidget.setTabOrder(self.btn_dashboard_2, self.btn_setting_2)
        QWidget.setTabOrder(self.btn_setting_2, self.btn_help_2)
        QWidget.setTabOrder(self.btn_help_2, self.btn_report_2)
        QWidget.setTabOrder(self.btn_report_2, self.btn_logout_2)
        QWidget.setTabOrder(self.btn_logout_2, self.txt_category)
        QWidget.setTabOrder(self.txt_category, self.txt_loan_location)
        QWidget.setTabOrder(self.txt_loan_location, self.btn_menu_2)
        QWidget.setTabOrder(self.btn_menu_2, self.btn_clear)
        QWidget.setTabOrder(self.btn_clear, self.txt_asset_2)
        QWidget.setTabOrder(self.txt_asset_2, self.txt_rtls_battery)
        QWidget.setTabOrder(self.txt_rtls_battery, self.btn_user)
        QWidget.setTabOrder(self.btn_user, self.btn_menu)
        QWidget.setTabOrder(self.btn_menu, self.btn_setting)
        QWidget.setTabOrder(self.btn_setting, self.btn_help)
        QWidget.setTabOrder(self.btn_help, self.btn_report)
        QWidget.setTabOrder(self.btn_report, self.btn_logout)
        QWidget.setTabOrder(self.btn_logout, self.btn_home)
        QWidget.setTabOrder(self.btn_home, self.btn_check_in)
        QWidget.setTabOrder(self.btn_check_in, self.btn_dashboard)

        self.retranslateUi(MainWindow)
        self.btn_menu_2.pressed.connect(self.side_menu_2.hide)
        self.btn_check_in_2.toggled.connect(self.btn_check_in.setChecked)
        self.btn_menu_2.pressed.connect(self.side_menu.show)
        self.btn_check_in.toggled.connect(self.btn_check_in_2.setChecked)
        self.btn_report.toggled.connect(self.btn_report_2.setChecked)
        self.btn_report_2.toggled.connect(self.btn_report.setChecked)
        self.btn_home.toggled.connect(self.btn_home_2.setChecked)
        self.btn_help.toggled.connect(self.btn_help_2.setChecked)
        self.btn_dashboard.toggled.connect(self.btn_dashboard_2.setChecked)
        self.btn_menu.pressed.connect(self.side_menu_2.show)
        self.btn_dashboard_2.toggled.connect(self.btn_dashboard.setChecked)
        self.btn_menu.pressed.connect(self.side_menu.hide)
        self.btn_setting_2.toggled.connect(self.btn_setting.setChecked)
        self.btn_home_2.toggled.connect(self.btn_home.setChecked)
        self.btn_setting.toggled.connect(self.btn_setting_2.setChecked)
        self.btn_help_2.toggled.connect(self.btn_help.setChecked)

        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_user_2.setText(QCoreApplication.translate("MainWindow", u"Guest", None))
        self.btn_change_user.setText(QCoreApplication.translate("MainWindow", u"Switch User", None))
        self.btn_logout_4.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.btn_menu_2.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home_2.setText(QCoreApplication.translate("MainWindow", u"Issue Loan", None))
        self.btn_check_in_2.setText(QCoreApplication.translate("MainWindow", u"Return Loan", None))
        self.btn_dashboard_2.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.btn_setting_2.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.btn_help_2.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.btn_report_2.setText(QCoreApplication.translate("MainWindow", u"Report Issue", None))
        self.btn_logout_2.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.lbl_3.setText("")
        self.lbl_confirm_info.setText(QCoreApplication.translate("MainWindow", u"Press confirm to take out equipment", None))
        self.lbl_confirm_icon.setText("")
        self.lbl_no_1.setText("")
        self.lbl_equipment.setText(QCoreApplication.translate("MainWindow", u" Scan or Type Equipment No:", None))
        self.lbl_no_2.setText("")
        self.lbl_loan.setText(QCoreApplication.translate("MainWindow", u"Type Location for Loan:", None))
        self.lbl_loc_validate.setText("")
        self.lbl_eq_validate.setText("")
        self.btn_validate_eq.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.btn_validate_loc.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Loan Details", None))
        self.lbl_category.setText("")
        self.lbl_arrow.setText("")
        self.lbl_location.setText("")
        self.btn_confirm.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Equipment Details", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Current Loan Location:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Category:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Mobileview battery status:", None))
        self.txt_asset_2.setText("")
        self.txt_loan_location.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Equipment No:", None))
        self.txt_category.setText("")
        self.txt_rtls_battery.setText("")
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Checks", None))
        self.chkbx_visual_insp.setText(QCoreApplication.translate("MainWindow", u"Visual Inspection", None))
        self.chkbx_batt_replace.setText(QCoreApplication.translate("MainWindow", u"Battery replaced", None))
        self.chkbx_function.setText(QCoreApplication.translate("MainWindow", u"Function Check", None))
        self.chkbx_batt_replace_2.setText(QCoreApplication.translate("MainWindow", u"Active RTLS tag battery replaced", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Work Done", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Return Loan", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Reported fault", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Job Type", None))
        self.rb_job.setText(QCoreApplication.translate("MainWindow", u"Repair Job", None))
        self.rb_ppm.setText(QCoreApplication.translate("MainWindow", u"PPM Job", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Assign to technician", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Create Job", None))
        self.btn_submit.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_clear_2.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
#if QT_CONFIG(shortcut)
        self.btn_clear_2.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.btn_user.setText("")
        self.btn_change_user_3.setText(QCoreApplication.translate("MainWindow", u"Change user", None))
        self.btn_logout_8.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.btn_menu.setText("")
        self.btn_home.setText("")
        self.btn_check_in.setText("")
        self.btn_dashboard.setText("")
        self.btn_setting.setText("")
        self.btn_help.setText("")
        self.btn_report.setText("")
        self.btn_logout.setText("")
    # retranslateUi

