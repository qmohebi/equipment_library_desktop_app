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
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1341, 831)
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
"QGroupBox {\n"
"font: 14pt\n"
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
"	"
                        "text-align: left;\n"
"}\n"
"\n"
"QPushButton#btn_user_2{\n"
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
"QPushButton#btn_validate_loc,#btn_validate_eq,#btn_badge {\n"
"text-align: centre;\n"
"padding-left: 20px;\n"
"border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton#btn_submit, #btn_print{\n"
"text-align: centre;\n"
"font: 25px;\n"
"padding: 10px 30px;\n"
"}\n"
"\n"
"QPushButton#btn_clear"
                        "_2{\n"
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
"border: 2px solid red;\n"
"background-color: #fe9f84;\n"
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
"\n"
"QTabBar::tab:selected{\n"
"    background: \n"
"}\n"
"QTabBar::tab::hover{\n"
"background: #3561fb;\n"
"}\n"
"QLineEdit #txt_asset_2, #txt_rtls_battery, #txt_loan_location, #txt_category {\n"
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
"QFrame#fram"
                        "e_user{\n"
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
"\n"
"\n"
"")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.side_menu_2 = QWidget(self.centralwidget)
        self.side_menu_2.setObjectName(u"side_menu_2")
        self.side_menu_2.setMinimumSize(QSize(200, 0))
        self.side_menu_2.setMaximumSize(QSize(210, 16777215))
        self.side_menu_2.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.side_menu_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_user = QPushButton(self.side_menu_2)
        self.btn_user.setObjectName(u"btn_user")
        self.btn_user.setEnabled(True)
        self.btn_user.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_user.setLayoutDirection(Qt.LeftToRight)
        self.btn_user.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons8-user-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_user.setIcon(icon)
        self.btn_user.setIconSize(QSize(50, 50))
        self.btn_user.setCheckable(False)

        self.verticalLayout.addWidget(self.btn_user)

        self.frame_user = QFrame(self.side_menu_2)
        self.frame_user.setObjectName(u"frame_user")
        self.frame_user.setMinimumSize(QSize(0, 100))
        self.frame_user.setFrameShape(QFrame.StyledPanel)
        self.frame_user.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_user)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.btn_switch_user = QPushButton(self.frame_user)
        self.btn_switch_user.setObjectName(u"btn_switch_user")
        self.btn_switch_user.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/change-user-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_switch_user.setIcon(icon1)
        self.btn_switch_user.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.btn_switch_user)

        self.btn_logout = QPushButton(self.frame_user)
        self.btn_logout.setObjectName(u"btn_logout")
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons8-log-out-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_logout.setIcon(icon2)
        self.btn_logout.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.btn_logout)

        self.verticalSpacer = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.frame_user)

        self.btn_home = QPushButton(self.side_menu_2)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(210, 0))
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons8-home-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon3)
        self.btn_home.setIconSize(QSize(40, 40))
        self.btn_home.setCheckable(True)
        self.btn_home.setChecked(True)
        self.btn_home.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_home)

        self.btn_check_in = QPushButton(self.side_menu_2)
        self.btn_check_in.setObjectName(u"btn_check_in")
        self.btn_check_in.setEnabled(True)
        self.btn_check_in.setMinimumSize(QSize(210, 0))
        self.btn_check_in.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons8-checkout-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_check_in.setIcon(icon4)
        self.btn_check_in.setIconSize(QSize(40, 40))
        self.btn_check_in.setCheckable(True)
        self.btn_check_in.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_check_in)

        self.btn_dashboard = QPushButton(self.side_menu_2)
        self.btn_dashboard.setObjectName(u"btn_dashboard")
        self.btn_dashboard.setEnabled(True)
        self.btn_dashboard.setMinimumSize(QSize(210, 0))
        self.btn_dashboard.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons8-dashboard-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_dashboard.setIcon(icon5)
        self.btn_dashboard.setIconSize(QSize(40, 40))
        self.btn_dashboard.setCheckable(True)
        self.btn_dashboard.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_dashboard)

        self.verticalSpacer_3 = QSpacerItem(20, 300, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.btn_setting = QPushButton(self.side_menu_2)
        self.btn_setting.setObjectName(u"btn_setting")
        self.btn_setting.setEnabled(True)
        self.btn_setting.setMinimumSize(QSize(210, 0))
        self.btn_setting.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons8-setting-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_setting.setIcon(icon6)
        self.btn_setting.setIconSize(QSize(40, 40))
        self.btn_setting.setCheckable(True)
        self.btn_setting.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_setting)

        self.btn_help = QPushButton(self.side_menu_2)
        self.btn_help.setObjectName(u"btn_help")
        self.btn_help.setMinimumSize(QSize(210, 0))
        self.btn_help.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons8-help-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_help.setIcon(icon7)
        self.btn_help.setIconSize(QSize(40, 40))
        self.btn_help.setCheckable(True)
        self.btn_help.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_help)

        self.btn_report = QPushButton(self.side_menu_2)
        self.btn_report.setObjectName(u"btn_report")
        self.btn_report.setMinimumSize(QSize(210, 0))
        self.btn_report.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons8-issue-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_report.setIcon(icon8)
        self.btn_report.setIconSize(QSize(40, 40))
        self.btn_report.setCheckable(True)
        self.btn_report.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_report)

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


        self.gridLayout_4.addWidget(self.side_menu_2, 0, 0, 1, 1)

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

        self.lbl_4 = QLabel(self.frame_5)
        self.lbl_4.setObjectName(u"lbl_4")

        self.horizontalLayout_4.addWidget(self.lbl_4)

        self.horizontalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.lbl_confirm_info = QLabel(self.frame_5)
        self.lbl_confirm_info.setObjectName(u"lbl_confirm_info")
        font = QFont()
        font.setPointSize(28)
        self.lbl_confirm_info.setFont(font)
        self.lbl_confirm_info.setLayoutDirection(Qt.LeftToRight)
        self.lbl_confirm_info.setScaledContents(False)
        self.lbl_confirm_info.setAlignment(Qt.AlignCenter)
        self.lbl_confirm_info.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.lbl_confirm_info)

        self.lbl_confirm_icon = QLabel(self.frame_5)
        self.lbl_confirm_icon.setObjectName(u"lbl_confirm_icon")

        self.horizontalLayout_4.addWidget(self.lbl_confirm_icon)

        self.horizontalSpacer_4 = QSpacerItem(100, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.gridLayout_7.addWidget(self.frame_5, 2, 0, 1, 2)

        self.groupBox = QGroupBox(self.page_home)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 300))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        self.groupBox.setFont(font1)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setSpacing(50)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 15, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.lbl_category = QLabel(self.groupBox)
        self.lbl_category.setObjectName(u"lbl_category")
        font2 = QFont()
        font2.setPointSize(25)
        self.lbl_category.setFont(font2)

        self.horizontalLayout_5.addWidget(self.lbl_category)

        self.lbl_arrow = QLabel(self.groupBox)
        self.lbl_arrow.setObjectName(u"lbl_arrow")

        self.horizontalLayout_5.addWidget(self.lbl_arrow)

        self.lbl_location = QLabel(self.groupBox)
        self.lbl_location.setObjectName(u"lbl_location")
        self.lbl_location.setFont(font2)

        self.horizontalLayout_5.addWidget(self.lbl_location)

        self.horizontalSpacer_2 = QSpacerItem(40, 15, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.gridLayout_7.addWidget(self.groupBox, 3, 0, 1, 2)

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
        font3 = QFont()
        font3.setPointSize(30)
        font3.setBold(False)
        font3.setItalic(False)
        self.btn_confirm.setFont(font3)
        self.btn_confirm.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_confirm.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_confirm)

        self.horizontalSpacer_8 = QSpacerItem(60, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_8)

        self.btn_clear = QPushButton(self.frame_3)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setMinimumSize(QSize(60, 100))
        font4 = QFont()
        font4.setBold(False)
        font4.setItalic(False)
        self.btn_clear.setFont(font4)
        self.btn_clear.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_clear.setLayoutDirection(Qt.LeftToRight)
        icon9 = QIcon()
        icon9.addFile(u":/clear-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_clear.setIcon(icon9)
        self.btn_clear.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.btn_clear)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)


        self.gridLayout_7.addWidget(self.frame_3, 4, 0, 1, 2)

        self.frame_15 = QFrame(self.page_home)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(30, 0))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_15)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_9 = QFrame(self.frame_15)
        self.frame_9.setObjectName(u"frame_9")
        font5 = QFont()
        font5.setPointSize(24)
        self.frame_9.setFont(font5)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_9)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(15)
        self.gridLayout_2.setContentsMargins(9, 0, -1, 6)
        self.lbl_eq_validate = QLabel(self.frame_9)
        self.lbl_eq_validate.setObjectName(u"lbl_eq_validate")
        self.lbl_eq_validate.setMinimumSize(QSize(60, 0))

        self.gridLayout_2.addWidget(self.lbl_eq_validate, 0, 0, 1, 1)

        self.btn_badge = QPushButton(self.frame_9)
        self.btn_badge.setObjectName(u"btn_badge")
        self.btn_badge.setEnabled(False)
        self.btn_badge.setMinimumSize(QSize(150, 70))
        font6 = QFont()
        font6.setPointSize(13)
        font6.setBold(False)
        font6.setItalic(False)
        self.btn_badge.setFont(font6)
        self.btn_badge.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_badge.setLayoutDirection(Qt.RightToLeft)
        icon10 = QIcon()
        icon10.addFile(u":/tick_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_badge.setIcon(icon10)
        self.btn_badge.setIconSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.btn_badge, 2, 1, 1, 1)

        self.lbl_badge_validate = QLabel(self.frame_9)
        self.lbl_badge_validate.setObjectName(u"lbl_badge_validate")

        self.gridLayout_2.addWidget(self.lbl_badge_validate, 2, 0, 1, 1)

        self.btn_validate_eq = QPushButton(self.frame_9)
        self.btn_validate_eq.setObjectName(u"btn_validate_eq")
        self.btn_validate_eq.setMinimumSize(QSize(30, 70))
        self.btn_validate_eq.setFont(font6)
        self.btn_validate_eq.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_validate_eq.setLayoutDirection(Qt.RightToLeft)
        self.btn_validate_eq.setIcon(icon10)
        self.btn_validate_eq.setIconSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.btn_validate_eq, 0, 1, 1, 1)

        self.btn_validate_loc = QPushButton(self.frame_9)
        self.btn_validate_loc.setObjectName(u"btn_validate_loc")
        self.btn_validate_loc.setEnabled(False)
        self.btn_validate_loc.setMinimumSize(QSize(150, 70))
        self.btn_validate_loc.setFont(font6)
        self.btn_validate_loc.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_validate_loc.setLayoutDirection(Qt.RightToLeft)
        self.btn_validate_loc.setIcon(icon10)
        self.btn_validate_loc.setIconSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.btn_validate_loc, 1, 1, 1, 1)

        self.lbl_loc_validate = QLabel(self.frame_9)
        self.lbl_loc_validate.setObjectName(u"lbl_loc_validate")

        self.gridLayout_2.addWidget(self.lbl_loc_validate, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_9, 2, 2, 1, 1)

        self.frame_8 = QFrame(self.frame_15)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_8)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setVerticalSpacing(10)
        self.gridLayout_6.setContentsMargins(0, 0, 10, 0)
        self.lbl_no_1 = QLabel(self.frame_8)
        self.lbl_no_1.setObjectName(u"lbl_no_1")

        self.gridLayout_6.addWidget(self.lbl_no_1, 0, 0, 1, 1)

        self.lbl_equipment = QLabel(self.frame_8)
        self.lbl_equipment.setObjectName(u"lbl_equipment")
        self.lbl_equipment.setMinimumSize(QSize(0, 50))
        font7 = QFont()
        font7.setPointSize(20)
        self.lbl_equipment.setFont(font7)

        self.gridLayout_6.addWidget(self.lbl_equipment, 0, 1, 1, 1)

        self.lbl_3 = QLabel(self.frame_8)
        self.lbl_3.setObjectName(u"lbl_3")

        self.gridLayout_6.addWidget(self.lbl_3, 2, 0, 1, 1)

        self.lbl_badge = QLabel(self.frame_8)
        self.lbl_badge.setObjectName(u"lbl_badge")
        self.lbl_badge.setMinimumSize(QSize(0, 50))
        self.lbl_badge.setFont(font7)

        self.gridLayout_6.addWidget(self.lbl_badge, 2, 1, 1, 1)

        self.lbl_loan = QLabel(self.frame_8)
        self.lbl_loan.setObjectName(u"lbl_loan")
        self.lbl_loan.setMinimumSize(QSize(0, 50))
        self.lbl_loan.setFont(font7)

        self.gridLayout_6.addWidget(self.lbl_loan, 1, 1, 1, 1)

        self.lbl_no_2 = QLabel(self.frame_8)
        self.lbl_no_2.setObjectName(u"lbl_no_2")

        self.gridLayout_6.addWidget(self.lbl_no_2, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_8, 2, 0, 1, 1)

        self.frame_2 = QFrame(self.frame_15)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 40))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font5)
        self.label_5.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_3.addWidget(self.label_5)


        self.gridLayout.addWidget(self.frame_2, 1, 1, 1, 1)

        self.frame = QFrame(self.frame_15)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, 9, 0)
        self.txt_asset = QLineEdit(self.frame)
        self.txt_asset.setObjectName(u"txt_asset")
        self.txt_asset.setMinimumSize(QSize(0, 50))
        self.txt_asset.setFont(font2)

        self.verticalLayout_2.addWidget(self.txt_asset)

        self.txt_location = QLineEdit(self.frame)
        self.txt_location.setObjectName(u"txt_location")
        self.txt_location.setMinimumSize(QSize(0, 50))
        self.txt_location.setFont(font2)

        self.verticalLayout_2.addWidget(self.txt_location)

        self.txt_badge = QLineEdit(self.frame)
        self.txt_badge.setObjectName(u"txt_badge")
        self.txt_badge.setMinimumSize(QSize(0, 50))
        self.txt_badge.setFont(font2)

        self.verticalLayout_2.addWidget(self.txt_badge)


        self.gridLayout.addWidget(self.frame, 2, 1, 1, 1)


        self.gridLayout_7.addWidget(self.frame_15, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_7.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_home)
        self.page_check_in = QWidget()
        self.page_check_in.setObjectName(u"page_check_in")
        self.gridLayout_8 = QGridLayout(self.page_check_in)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.frame_12 = QFrame(self.page_check_in)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 60))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.groupBox_4 = QGroupBox(self.frame_12)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setFont(font1)
        self.gridLayout_5 = QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")
        font8 = QFont()
        font8.setPointSize(14)
        self.label_4.setFont(font8)

        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 1)

        self.txt_asset_2 = QLineEdit(self.groupBox_4)
        self.txt_asset_2.setObjectName(u"txt_asset_2")
        self.txt_asset_2.setEnabled(False)
        self.txt_asset_2.setFont(font8)
        self.txt_asset_2.setLayoutDirection(Qt.LeftToRight)
        self.txt_asset_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.txt_asset_2.setReadOnly(False)

        self.gridLayout_5.addWidget(self.txt_asset_2, 0, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font8)

        self.gridLayout_5.addWidget(self.label_6, 1, 0, 1, 1)

        self.txt_category = QLineEdit(self.groupBox_4)
        self.txt_category.setObjectName(u"txt_category")
        self.txt_category.setEnabled(False)
        self.txt_category.setFont(font8)

        self.gridLayout_5.addWidget(self.txt_category, 1, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font8)

        self.gridLayout_5.addWidget(self.label_2, 2, 0, 1, 1)

        self.txt_loan_location = QLineEdit(self.groupBox_4)
        self.txt_loan_location.setObjectName(u"txt_loan_location")
        self.txt_loan_location.setEnabled(False)
        self.txt_loan_location.setFont(font8)

        self.gridLayout_5.addWidget(self.txt_loan_location, 2, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font8)

        self.gridLayout_5.addWidget(self.label_3, 3, 0, 1, 1)

        self.txt_rtls_battery = QLineEdit(self.groupBox_4)
        self.txt_rtls_battery.setObjectName(u"txt_rtls_battery")
        self.txt_rtls_battery.setEnabled(False)
        self.txt_rtls_battery.setFont(font8)

        self.gridLayout_5.addWidget(self.txt_rtls_battery, 3, 1, 1, 1)


        self.horizontalLayout_11.addWidget(self.groupBox_4)

        self.groupBox_11 = QGroupBox(self.frame_12)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setMinimumSize(QSize(0, 150))
        self.gridLayout_12 = QGridLayout(self.groupBox_11)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_13 = QLabel(self.groupBox_11)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_12.addWidget(self.label_13, 1, 0, 1, 1)

        self.txt_job_type = QLineEdit(self.groupBox_11)
        self.txt_job_type.setObjectName(u"txt_job_type")
        self.txt_job_type.setEnabled(False)
        self.txt_job_type.setFont(font8)

        self.gridLayout_12.addWidget(self.txt_job_type, 1, 3, 1, 1)

        self.txt_assinged_tech = QLineEdit(self.groupBox_11)
        self.txt_assinged_tech.setObjectName(u"txt_assinged_tech")
        self.txt_assinged_tech.setEnabled(False)
        self.txt_assinged_tech.setFont(font8)

        self.gridLayout_12.addWidget(self.txt_assinged_tech, 2, 3, 1, 1)

        self.label_12 = QLabel(self.groupBox_11)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_12.addWidget(self.label_12, 0, 0, 1, 1)

        self.label_14 = QLabel(self.groupBox_11)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_12.addWidget(self.label_14, 2, 0, 1, 1)

        self.txt_job_number = QLineEdit(self.groupBox_11)
        self.txt_job_number.setObjectName(u"txt_job_number")
        self.txt_job_number.setEnabled(False)
        self.txt_job_number.setFont(font8)
        self.txt_job_number.setLayoutDirection(Qt.LeftToRight)
        self.txt_job_number.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.txt_job_number.setReadOnly(False)

        self.gridLayout_12.addWidget(self.txt_job_number, 0, 3, 1, 1)


        self.horizontalLayout_11.addWidget(self.groupBox_11)


        self.gridLayout_8.addWidget(self.frame_12, 0, 0, 1, 1)

        self.frame_4 = QFrame(self.page_check_in)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 50))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.chkbx_visual_insp = QCheckBox(self.frame_4)
        self.chkbx_visual_insp.setObjectName(u"chkbx_visual_insp")
        self.chkbx_visual_insp.setFont(font8)
        self.chkbx_visual_insp.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.chkbx_visual_insp)

        self.chkbx_function = QCheckBox(self.frame_4)
        self.chkbx_function.setObjectName(u"chkbx_function")
        self.chkbx_function.setFont(font8)
        self.chkbx_function.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.chkbx_function)

        self.chkbx_batt_replace = QCheckBox(self.frame_4)
        self.chkbx_batt_replace.setObjectName(u"chkbx_batt_replace")
        self.chkbx_batt_replace.setFont(font8)
        self.chkbx_batt_replace.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.chkbx_batt_replace)

        self.chkbx_rtls_batt = QCheckBox(self.frame_4)
        self.chkbx_rtls_batt.setObjectName(u"chkbx_rtls_batt")
        self.chkbx_rtls_batt.setFont(font8)
        self.chkbx_rtls_batt.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.chkbx_rtls_batt)


        self.gridLayout_8.addWidget(self.frame_4, 1, 0, 1, 1)

        self.groupBox_12 = QGroupBox(self.page_check_in)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_12)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.radioButton = QRadioButton(self.groupBox_12)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout_4.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox_12)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout_4.addWidget(self.radioButton_2)


        self.gridLayout_8.addWidget(self.groupBox_12, 2, 0, 1, 1)

        self.groupBox_13 = QGroupBox(self.page_check_in)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_13)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.radioButton_3 = QRadioButton(self.groupBox_13)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout_6.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.groupBox_13)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.verticalLayout_6.addWidget(self.radioButton_4)


        self.gridLayout_8.addWidget(self.groupBox_13, 3, 0, 1, 1)

        self.frame_7 = QFrame(self.page_check_in)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 80))
        self.frame_7.setFont(font8)
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
        self.btn_print.setFont(font4)
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


        self.gridLayout_8.addWidget(self.frame_7, 5, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.page_check_in)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(1200, 16777215))
        self.groupBox_3.setFont(font1)
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.txt_work_done = QPlainTextEdit(self.groupBox_3)
        self.txt_work_done.setObjectName(u"txt_work_done")
        self.txt_work_done.setMinimumSize(QSize(0, 0))
        self.txt_work_done.setFont(font8)

        self.horizontalLayout_6.addWidget(self.txt_work_done)


        self.gridLayout_8.addWidget(self.groupBox_3, 4, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_check_in)
        self.page_dashboard = QWidget()
        self.page_dashboard.setObjectName(u"page_dashboard")
        self.groupBox_2 = QGroupBox(self.page_dashboard)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(30, 150, 741, 421))
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 50, 49, 16))
        self.frame_10 = QFrame(self.page_dashboard)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(20, 0, 1131, 80))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_10)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(80, 35, 381, 21))
        self.stackedWidget.addWidget(self.page_dashboard)
        self.page_setting = QWidget()
        self.page_setting.setObjectName(u"page_setting")
        self.frame_6 = QFrame(self.page_setting)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(0, 90, 1241, 791))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.groupBox_6 = QGroupBox(self.frame_6)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(40, 20, 371, 261))
        self.groupBox_10 = QGroupBox(self.frame_6)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setGeometry(QRect(40, 320, 371, 261))
        self.frame_11 = QFrame(self.page_setting)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(10, 0, 971, 80))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.label_8 = QLabel(self.frame_11)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(240, 30, 49, 16))
        self.stackedWidget.addWidget(self.page_setting)
        self.page_help = QWidget()
        self.page_help.setObjectName(u"page_help")
        self.label_9 = QLabel(self.page_help)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(280, 40, 201, 51))
        self.stackedWidget.addWidget(self.page_help)
        self.page_report_issue = QWidget()
        self.page_report_issue.setObjectName(u"page_report_issue")
        self.page_report_issue.setStyleSheet(u"QLabel{\n"
"font: 15pt;\n"
"}\n"
"\n"
"QGroupBox{\n"
"font: 15pt;\n"
"}\n"
"\n"
"QLineEdit{\n"
"font: 20pt;\n"
"padding: 10px 20px;\n"
"}\n"
"\n"
"QPushButton{\n"
"font: 25pt;\n"
"text-align: centre;\n"
"padding: 10px 20px\n"
"}")
        self.gridLayout_11 = QGridLayout(self.page_report_issue)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.frame_13 = QFrame(self.page_report_issue)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_13)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_14)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_11 = QLabel(self.frame_14)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_3.addWidget(self.label_11)

        self.plainTextEdit = QPlainTextEdit(self.frame_14)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout_3.addWidget(self.plainTextEdit)


        self.verticalLayout_7.addWidget(self.frame_14)

        self.frame_16 = QFrame(self.frame_13)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_13 = QSpacerItem(200, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_13)

        self.pushButton = QPushButton(self.frame_16)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_8.addWidget(self.pushButton)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_12)


        self.verticalLayout_7.addWidget(self.frame_16)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)


        self.gridLayout_11.addWidget(self.frame_13, 1, 0, 1, 1)

        self.frame_title = QFrame(self.page_report_issue)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_title)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_10 = QLabel(self.frame_title)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_7.addWidget(self.label_10)


        self.gridLayout_11.addWidget(self.frame_title, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_report_issue)

        self.gridLayout_4.addWidget(self.stackedWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_validate_eq, self.btn_validate_loc)
        QWidget.setTabOrder(self.btn_validate_loc, self.btn_confirm)
        QWidget.setTabOrder(self.btn_confirm, self.txt_work_done)
        QWidget.setTabOrder(self.txt_work_done, self.btn_submit)
        QWidget.setTabOrder(self.btn_submit, self.btn_print)
        QWidget.setTabOrder(self.btn_print, self.btn_clear_2)
        QWidget.setTabOrder(self.btn_clear_2, self.btn_user)
        QWidget.setTabOrder(self.btn_user, self.btn_home)
        QWidget.setTabOrder(self.btn_home, self.btn_check_in)
        QWidget.setTabOrder(self.btn_check_in, self.btn_dashboard)
        QWidget.setTabOrder(self.btn_dashboard, self.btn_setting)
        QWidget.setTabOrder(self.btn_setting, self.btn_help)
        QWidget.setTabOrder(self.btn_help, self.btn_report)
        QWidget.setTabOrder(self.btn_report, self.btn_logout_2)
        QWidget.setTabOrder(self.btn_logout_2, self.txt_category)
        QWidget.setTabOrder(self.txt_category, self.txt_loan_location)
        QWidget.setTabOrder(self.txt_loan_location, self.btn_clear)
        QWidget.setTabOrder(self.btn_clear, self.txt_asset_2)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_user.setText(QCoreApplication.translate("MainWindow", u"Guest", None))
        self.btn_switch_user.setText(QCoreApplication.translate("MainWindow", u"Switch User", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Issue Loan", None))
        self.btn_check_in.setText(QCoreApplication.translate("MainWindow", u"Return Loan", None))
        self.btn_dashboard.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.btn_setting.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.btn_help.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.btn_report.setText(QCoreApplication.translate("MainWindow", u"Report Issue", None))
        self.btn_logout_2.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.lbl_4.setText("")
        self.lbl_confirm_info.setText(QCoreApplication.translate("MainWindow", u"Press confirm to take out equipment", None))
        self.lbl_confirm_icon.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Loan Details", None))
        self.lbl_category.setText("")
        self.lbl_arrow.setText("")
        self.lbl_location.setText("")
        self.btn_confirm.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.lbl_eq_validate.setText("")
        self.btn_badge.setText("")
        self.lbl_badge_validate.setText("")
        self.btn_validate_eq.setText("")
        self.btn_validate_loc.setText("")
        self.lbl_loc_validate.setText("")
        self.lbl_no_1.setText("")
        self.lbl_equipment.setText(QCoreApplication.translate("MainWindow", u" Scan or Type Equipment No:", None))
        self.lbl_3.setText("")
        self.lbl_badge.setText(QCoreApplication.translate("MainWindow", u"Scan your badge:", None))
        self.lbl_loan.setText(QCoreApplication.translate("MainWindow", u"Type Location for Loan:", None))
        self.lbl_no_2.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"To borrow equipment:", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Equipment Details", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Equipment No:", None))
        self.txt_asset_2.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Category:", None))
        self.txt_category.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Current Loan Location:", None))
        self.txt_loan_location.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Mobileview battery status:", None))
        self.txt_rtls_battery.setText("")
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Job details:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Job Type:", None))
        self.txt_job_type.setText("")
        self.txt_assinged_tech.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Job Number:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Assigned Technician:", None))
        self.txt_job_number.setText("")
        self.chkbx_visual_insp.setText(QCoreApplication.translate("MainWindow", u"Visual Inspection", None))
        self.chkbx_function.setText(QCoreApplication.translate("MainWindow", u"Function Check", None))
        self.chkbx_batt_replace.setText(QCoreApplication.translate("MainWindow", u"Battery replaced", None))
        self.chkbx_rtls_batt.setText(QCoreApplication.translate("MainWindow", u"MobileView Battery Replaced", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"Functional check", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Pass", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Fail", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"PPM Required", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.btn_submit.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_clear_2.setText(QCoreApplication.translate("MainWindow", u"Clear All", None))
#if QT_CONFIG(shortcut)
        self.btn_clear_2.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Work Done", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Par Level", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Database server", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Database server", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Describe the issue you have experienced.", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Report an Issue", None))
    # retranslateUi

