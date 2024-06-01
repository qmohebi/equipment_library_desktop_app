import sys
import re
import json
from datetime import datetime
import csv
import os

from PySide6.QtCore import Qt, Signal, QTimer, QEvent, QObject

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QCompleter,
    QMessageBox,
)

from PySide6.QtGui import QPixmap, QIntValidator

from ui_mainwindow import Ui_MainWindow

from logout_timer import LogoutTimer
from database import Database
from login import LoginWindow
from assing_technician import AssignTech

# pyside6-uic .\ui\loan_dialogue.ui -o .\ui\ui_dialogue.py

ASSET = {
    "equipment_no": "",
    "category": "",
    "library_status_id": "",
    "equipment_id": "",
    "location_id": "",
    "loan_location": "",
    "loan_status_id": "",
}

ASSIGNED_TECHNICIAN = {}

MPCE_PERSONNEL = {}

JOB_TYPE = {
    "Repair/Correction": "STG2005061300002",
    "PPM": "STG2005061300001",
    "Function Check": "591F356502204017989184484E650984",
    "Supply": "STG2009101500001",
}

RTLS_BATTERY = {"rtls_equipment_no": [], "battery_capacity": []}

JOB_STATUS = {
    "Not Started": "STG2005071800000",
    "Completed": "69914FCE64344265A0E72EC66528D9FA",
}

SUPPLY_CATEGORY = [
    "Suction Controller - High Vacuum",
    "Flowmeter/Regulator - O2 - Low flow",
    "Suction Controller - Thoracic - Indirect",
    "Flowmeter/Regulator - O2",
    "Suction Controller - Low Vacuum - Indirect",
    "Flowmeter/Regulator - Air",
    "Flowmeter/Regulator - O2 - Indirect",
    "Suction Controller - High Vacuum - Indirect",
    "Suction Controller - Thoracic",
    "Suction Controller - Low Vacuum",
    "Nebuliser",
]

INACTIVE_TIMEOUT = 10  # time in minutes before a user is logged out automatically

# location for the rtl battery report
src_folder = r"K:\main_python_work\equipment_library_desktop_app"

with open("config.json", encoding="utf-8") as config:
    data = json.load(config)
    REPORTED_FAULT = data["reported_fault"]
    DB_NAME = data["database"]
    LDAP_SERVER = data["ldap_server"]
    SEARCH_BASE = data["search_base"]
    BATTERY_REPORT = data["battery_report"]
    INVALID_ASSET_ERROR = data["error_message"]

for filname in os.listdir(src_folder):
    if filname.endswith(".CSV"):
        file_path = os.path.join(src_folder, filname)

        with open(file_path, "r") as csv_file:
            data = csv.reader(csv_file)
            next(data)

            for row in data:
                RTLS_BATTERY["rtls_equipment_no"].append(row[0])
                RTLS_BATTERY["battery_capacity"].append(row[1])

            # remove the last items from the list as that is irrelevant.
            RTLS_BATTERY["rtls_equipment_no"].pop()
            RTLS_BATTERY["battery_capacity"].pop()


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.login_window = LoginWindow(
            parent=self,
            mpce_staff=MPCE_PERSONNEL,
            ldap_server=LDAP_SERVER,
            search_base=SEARCH_BASE,
        )

        self.login_window.hide()
        self.setMouseTracking(True)

        #   -------------------------------------
        # tracks mouse movement across the wigdget and resets the timer
        # self.tracker = MouseTracker()
        # self.tracker.mouse_moved.connect(self.reset_countdown)

        self.db = Database()

        # date passed to MSSQL needs to be in ISO standard: YY-MM-DD
        self.today = datetime.today().strftime("%Y-%m-%d")
        self.mpce_staff_logged_in = False
        self.username_logged_in = ""
        self.logged_in_user = {"username": "", "user_id": "", "first_name": ""}

        # used as flag on whether to create supply job and
        # permenantly change location of asset
        self.permenant_supplied_by_library = False

        self.location_name = []  # used for location auto complete
        self.location = {}  # used for getting location id
        self.location_id = ""
        self.job_sticker = {}  # dictionary to be used for printing job sticker

        # WWW1 - not a library item
        # WWW2 - available
        # WWW3 - on loan
        # STG2005061300002 - Loan in progress

        self.confirm_pixmap = QPixmap(":/tick.png")
        self.error_pixmap = QPixmap(":/cancel.png")
        self.arrow_pixmap = QPixmap(":/arrow.png")
        self.setWindowTitle("Library Loan")

        self.ui.txt_asset.setFocus()
        self.ui.txt_asset.setPlaceholderText("Enter Equipment No")
        self.ui.txt_location.setPlaceholderText("Start typing the location")
        self.ui.txt_badge.setPlaceholderText("Staff badge number")
        self.ui.btn_validate_eq.clicked.connect(self.get_asset_info)
        self.ui.txt_asset.returnPressed.connect(self.get_asset_info)
        self.ui.btn_validate_loc.clicked.connect(self.validate_location)
        self.ui.txt_location.returnPressed.connect(self.validate_location)
        self.ui.btn_confirm.clicked.connect(self.confirm_loan)
        self.ui.btn_clear.clicked.connect(lambda: self.clear(clear_all=True))

        self.number_1_pixmap = QPixmap(":/1.png")
        self.ui.lbl_no_1.setPixmap(self.number_1_pixmap)
        self.number_2_pixmap = QPixmap(":/2.png")
        self.ui.lbl_no_2.setPixmap(self.number_2_pixmap)
        self.number_3_pixmap = QPixmap(":/3.png")
        self.ui.lbl_3.setPixmap(self.number_3_pixmap)
        self.number_4_pixmap = QPixmap(":/4.png")
        self.ui.lbl_4.setPixmap(self.number_4_pixmap)

        self.mandatory_check_box = (
            self.ui.rb_function_fail,
            self.ui.rb_function_pass,
            self.ui.rb_ppm_no,
            self.ui.rb_ppm_yes,
            self.ui.chkbx_function,
            self.ui.chkbx_batt_replace,
        )

        # grey pixmap
        self.number_1_grey = QPixmap(":/1_grey.png")
        self.number_2_grey = QPixmap(":/2_grey.png")
        self.number_3_grey = QPixmap(":/3_grey.png")
        self.number_4_grey = QPixmap(":/4_grey.png")

        self.get_mpce_personnel()
        self.ui.stackedWidget.setCurrentIndex(0)

        self.assing_tech_window = AssignTech(technicians=ASSIGNED_TECHNICIAN)
        self.assing_tech_window.hide()

        self.ui.frame_user.show()
        self.confirm_labels = (
            self.ui.lbl_4,
            self.ui.lbl_confirm_icon,
            self.ui.lbl_confirm_info,
        )

        self.txt_boxes = (self.ui.txt_asset, self.ui.txt_location, self.ui.txt_badge)
        self.btns = (self.ui.btn_validate_loc, self.ui.btn_confirm, self.ui.btn_badge)
        self.icon_labels = (
            self.ui.lbl_eq_validate,
            self.ui.lbl_confirm_icon,
            self.ui.lbl_badge_validate,
        )
        self.details_lables = (
            self.ui.lbl_category,
            self.ui.lbl_arrow,
            self.ui.lbl_loc_validate,
            self.ui.lbl_location,
        )
        self.get_location()
        self.disable_buttons()

        self.ui.lbl_4.clear()

        self.ui.btn_user.clicked.connect(self.on_user_btn_pressed)

        location_completer = QCompleter(self.location_name, self)
        location_completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.ui.txt_location.setCompleter(location_completer)

        # capture the value returned from the login windows
        self.login_window.login_successfull.connect(self.on_successful_login)

        self.home_btn = (self.ui.btn_home, self.ui.btn_home)
        self.return_loan_btn = (self.ui.btn_check_in, self.ui.btn_check_in)

        self.logged_user_btn = (
            self.ui.btn_check_in,
            self.ui.btn_check_in,
            self.ui.btn_setting,
            self.ui.btn_setting,
            self.ui.btn_dashboard,
            self.ui.btn_dashboard,
        )

        self.authenticated_user_btn = (self.ui.btn_switch_user, self.ui.btn_logout)

        self.logout_buttons = (
            self.ui.btn_logout_2,
            self.ui.btn_logout,
        )

        self.return_loan_chkbox = (
            self.ui.chkbx_visual_insp,
            self.ui.chkbx_function,
            self.ui.chkbx_batt_replace,
            # self.ui.chkbx_rtls_batt,
        )

        # only_integer = QIntValidator()

        # self.ui.txt_badge.setValidator(only_integer)

        # self.ui.lbl_loan.setStyleSheet("color:white")

        self.ui.btn_switch_user.clicked.connect(self.switch_user)

        for button in self.authenticated_user_btn:
            button.hide()

        for item in self.logged_user_btn:
            item.hide()

        for button in self.return_loan_btn:
            button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))

        for button in self.home_btn:
            button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))

        for button in self.logout_buttons:
            button.clicked.connect(self.log_out)

        # create auto completer for MPCE_PERSONNEL in the job tab
        tech_auto_complete = QCompleter(list(ASSIGNED_TECHNICIAN.keys()), self)
        tech_auto_complete.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        # self.ui.txt_technician.setCompleter(tech_auto_complete)
        # self.ui.txt_technician.setClearButtonEnabled(True)
        self.ui.txt_asset.setClearButtonEnabled(True)
        self.ui.txt_location.setClearButtonEnabled(True)
        self.ui.txt_badge.setClearButtonEnabled(True)

        self.ui.btn_submit.clicked.connect(self.return_loan)
        self.ui.btn_clear_2.clicked.connect(self.clear_return_loan)
        self.ui.txt_asset.textChanged.connect(self.on_clear_txt_clicked)
        self.ui.txt_location.textChanged.connect(self.on_clear_txt_clicked)
        self.ui.txt_badge.textChanged.connect(self.on_clear_txt_clicked)
        self.ui.btn_badge.clicked.connect(self.validate_badge)
        self.ui.txt_badge.returnPressed.connect(self.validate_badge)

        self.ui.rb_function_fail.toggled.connect(self.on_failed_function_check)
        self.ui.rb_ppm_yes.toggled.connect(self.on_ppm_required)

        self.assing_tech_window.job_created.connect(self.on_job_by_dialog)

    def on_clear_txt_clicked(self) -> None:
        """When clear button in the asset or location is pressed
        reset"""
        if self.ui.txt_asset.text() == "":
            self.reset_issue_loan_form()
        elif self.ui.txt_location.text() == "":
            self.ui.lbl_loan.setStyleSheet("color: black")
            self.ui.lbl_no_2.setPixmap(self.number_2_pixmap)
            self.ui.lbl_loc_validate.clear()
            self.ui.btn_badge.setDisabled(True)
            self.ui.txt_badge.setDisabled(True)
        elif self.ui.txt_badge.text() == "":
            self.ui.lbl_badge_validate.clear()
            self.ui.lbl_4.clear()
            self.ui.lbl_confirm_info.clear()
            self.ui.btn_confirm.setDisabled(True)

    def on_user_btn_pressed(self) -> None:
        """Actions on what happens when user presses the login
        button, if a user is logged in, present them with switch user or logout
        if user not logged in, open the login window to allow user to login"""
        if self.mpce_staff_logged_in is False:
            self.login_window.setModal(True)
            self.login_window.ui.txt_username.clear()
            self.login_window.ui.txt_password.clear()
            self.login_window.raise_()
            self.login_window.exec()
        elif self.ui.btn_switch_user.isVisible():
            for button in self.authenticated_user_btn:
                button.hide()
        else:
            for button in self.authenticated_user_btn:
                button.show()

    def get_location(self) -> None:
        """get the location from database and create a list and dictionary
        lis to be used for autocompleting the location text box and
        dictionary for get the location_id"""
        location = self.db.get_location()
        self.location = location
        self.location_name = list(location.keys())

    def get_mpce_personnel(self) -> None:
        """populate the personnel dictionary with mpce personnel from the db
        this dictionary is used for getting the PersonnelID, the userID
        for creating the job"""
        result = self.db.get_mpce_personnel()

        # go through personnel json file, clean up spaces at the end of name and email and
        # store it in a PERSONNEL dict.
        for item in result:
            try:
                name = item["PersonnelShortName"].strip().title()

            except Exception:
                name = None
            try:
                username = item["DomainLogin"].strip().lower()
            except Exception:
                username = None
            try:
                user_id = item["UserId"]
            except Exception:
                user_id = None
            try:
                personnel_id = item["PersonnelId"]
            except Exception:
                personnel_id = None
            try:
                first_name = item["FirstName"]
            except Exception:
                first_name = None
            try:
                email = item["EMail"]
            except Exception:
                email = None

            MPCE_PERSONNEL[username] = [
                first_name,
                name,
                user_id,
                personnel_id,
                username,
                email,
            ]
            ASSIGNED_TECHNICIAN[name] = [personnel_id, user_id]

    def get_asset_info(self) -> None:
        """Run regex on the equipment number that is typed into the text field
        this is to remove the GS1 additional info that gets scanned
        if not GS1 code, use the equipment number and fetch info
        from the database and write to the ASSET dictionary"""

        search_value = self.ui.txt_asset.text().strip()
        self.ui.txt_location.clear()

        # validate the equipment number to distinguish gs1 or old asset no.
        pattern = r"\d{14}(\d{7})"
        match = re.search(pattern, search_value)
        if match:
            equipment_no = match.group(1)
            self.ui.txt_asset.setText(equipment_no)
        else:
            equipment_no = search_value

        result = self.db.get_asset(equipment_number=equipment_no)

        if result:
            for row in result:
                ASSET["equipment_id"] = row[0]
                ASSET["category"] = row[1]
                ASSET["library_status_id"] = row[2]
                ASSET["loan_status_id"] = row[3]
                ASSET["loan_location"] = row[4]
            # check if category of asset in those that can be supplied by library
            if (
                ASSET["category"] in SUPPLY_CATEGORY
                and self.mpce_staff_logged_in is True
                and ASSET["library_status_id"] != "WWW3"
            ):
                self.permenant_supplied_by_library = True
                self.on_valid_asset_searched()
                # if not a library item
            elif (
                ASSET["library_status_id"] == "WWW1"
                or ASSET["library_status_id"] is None
            ):
                self.ui.lbl_eq_validate.setPixmap(self.error_pixmap)
                self.invalid_asset()

                # If on loan check that mpce staff is logged in
                # if mpce staff logged in, take to checkin page
            elif ASSET["library_status_id"] == "WWW3":
                if self.mpce_staff_logged_in is True:
                    self.ui.btn_check_in.setDisabled(False)
                    self.ui.stackedWidget.setCurrentIndex(1)
                    self.clear_return_loan()
                    self.ui.btn_submit.setDisabled(False)
                    try:
                        index = RTLS_BATTERY["rtls_equipment_no"].index(search_value)
                        battery_capacity = RTLS_BATTERY["battery_capacity"][index]
                        print(battery_capacity)
                    except Exception:
                        print("not on the rtls battery list")

                    self.ui.txt_loan_location.setText(ASSET["loan_location"])
                    self.ui.txt_asset_2.setText(search_value)
                    self.ui.txt_category.setText(ASSET["category"])
                    self.ui.btn_check_in.setChecked(True)
                else:
                    self.invalid_asset()
            else:
                self.on_valid_asset_searched()
                self.permenant_supplied_by_library = False
        else:
            self.ui.lbl_eq_validate.setPixmap(self.error_pixmap)
            self.ui.lbl_loc_validate.clear()
            QMessageBox.critical(self, "Equipment search", "Unable to find an Asset!")
            # self.ui.lbl_category.setText("")
            self.ui.btn_confirm.setDisabled(True)

    def invalid_asset(self):
        """Set messaging for invalid asset"""

        self.ui.lbl_4.setVisible(True)
        self.ui.lbl_4.setPixmap(self.error_pixmap)
        self.ui.lbl_confirm_info.setVisible(True)
        self.ui.lbl_confirm_info.setWordWrap(True)
        self.ui.frame_confirm.setStyleSheet(
            "background-color: pink; border-radius: 10px;"
        )
        self.ui.lbl_confirm_info.setStyleSheet("font: 20pt")
        self.ui.lbl_confirm_info.setText(INVALID_ASSET_ERROR)

    def on_valid_asset_searched(self) -> None:
        """Sets up the form when a valid library asset has been searched"""
        # self.ui.btn_validate_eq.setStyleSheet("background-color:#4abc96")
        self.ui.lbl_eq_validate.setPixmap(self.confirm_pixmap)
        self.ui.lbl_category.setText(ASSET["category"])
        self.ui.lbl_arrow.setPixmap(self.arrow_pixmap)
        self.ui.btn_validate_loc.setDisabled(False)
        self.ui.txt_location.setDisabled(False)
        self.ui.txt_location.setFocus()
        self.ui.lbl_equipment.setStyleSheet("color:grey")
        self.ui.lbl_no_1.setPixmap(self.number_1_grey)
        self.ui.txt_asset.setStyleSheet("color:grey")
        self.reset_confirm_label()

    def validate_location(self):
        """Checks to make sure the location entered is a correct one
        by comparing to location dictionary"""

        loc_inputted = self.ui.txt_location.text().strip()
        try:
            ASSET["location_id"] = self.location[loc_inputted]
            self.ui.lbl_loc_validate.setPixmap(self.confirm_pixmap)
            self.ui.lbl_location.setText(loc_inputted)
            self.ui.lbl_loan.setStyleSheet("color:grey")
            # self.ui.btn_validate_loc.setStyleSheet("background-color:#4abc96")
            self.ui.lbl_no_2.setPixmap(self.number_2_grey)
            self.ui.txt_location.setStyleSheet("color:grey")
            self.ui.btn_badge.setDisabled(False)
            self.ui.txt_badge.setDisabled(False)
            self.ui.txt_badge.setFocus()

        except KeyError:
            self.ui.lbl_loc_validate.setPixmap(self.error_pixmap)
            # self.ui.lbl_location.setText("")
            self.ui.btn_confirm.setDisabled(True)
            for label in self.confirm_labels:
                label.setVisible(False)

    def reset_confirm_label(self):
        self.ui.frame_confirm.setStyleSheet("background-color: transparent")
        for label in self.confirm_labels:
            label.clear()

    def validate_badge(self):
        """Check the entered badge number is integer
        and above 10 digits long"""

        badget_number = self.ui.txt_badge.text()

        try:
            if int(badget_number) and len(badget_number) >= 10:

                self.ui.lbl_4.setVisible(True)
                self.ui.lbl_4.setPixmap(self.number_4_pixmap)
                self.ui.lbl_confirm_info.setVisible(True)
                self.ui.lbl_confirm_info.setWordWrap(False)
                self.ui.frame_confirm.setStyleSheet(
                    "border-color: green; border-radius: 10px;"
                )
                self.ui.lbl_confirm_info.setText("Press confirm to take out equipment.")
                self.ui.lbl_confirm_info.setStyleSheet("font:30pt")
                self.ui.btn_confirm.setDisabled(False)
                self.ui.lbl_badge_validate.setPixmap(self.confirm_pixmap)
            else:
                self.ui.lbl_badge_validate.setPixmap(self.error_pixmap)
                QMessageBox.warning(self, "Library Loan", "Incorrect badge number!")
                self.ui.txt_badge.setFocus()
        except Exception:
            self.ui.lbl_badge_validate.setPixmap(self.error_pixmap)
            QMessageBox.warning(self, "Library Loan", "Incorrect badge number")
            self.ui.txt_badge.setFocus()

        # validate staff badge and show info

    def confirm_loan(self):
        """issues loan by called the db function"""

        loan_note = (
            f"Badge ID: {self.ui.txt_badge.text()} - Created by library checkout"
        )
        if self.permenant_supplied_by_library is True:
            supply_job = QMessageBox.question(
                self,
                "Issue permanent loan",
                "Issue a supply job and change location of this asset!",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                defaultButton=QMessageBox.StandardButton.No,
            )
            if supply_job == QMessageBox.StandardButton.Yes:
                self.db.update_location(
                    equipment_id=ASSET["equipment_id"], location_id=ASSET["location_id"]
                )
                job = self.db.create_job(
                    work_end_date=self.today,
                    equipment_id=ASSET["equipment_id"],
                    job_status_id=JOB_STATUS["Completed"],
                    job_type_id=JOB_TYPE["Supply"],
                    tech_id=MPCE_PERSONNEL[self.logged_in_user["username"]][3],
                    taken_by_id=MPCE_PERSONNEL[self.logged_in_user["username"]][3],
                    user_id=self.logged_in_user["user_id"],
                    reported_fault=f"Wards requires supply of a {ASSET['category']}",
                    work_done=f"Supplied ward with {ASSET['category']}",
                )
                if job:
                    QMessageBox.information(
                        self,
                        "Successful Job Creation",
                        f"Permantly issued a {ASSET['category']} to {self.ui.txt_location.text().strip()}\n"
                        f"and a supply Job with Job number: [{job}] has been created!",
                    )
                    self.clear()
        else:
            try:
                self.db.issue_loan(
                    equipment_id=ASSET["equipment_id"],
                    location_id=ASSET["location_id"],
                    notes=loan_note,
                )
                self.ui.lbl_confirm_icon.setPixmap(self.confirm_pixmap)
                QMessageBox.information(
                    self, "Equipment Loan", " Loan succesfully issued!"
                )
                self.clear(clear_all=True)
                # for logged in user only where this button is enabled after loan is issued
                self.ui.btn_submit.setDisabled(False)
            except Exception:
                self.ui.lbl_confirm_icon.setPixmap(self.error_pixmap)

    def disable_buttons(self) -> None:
        """Set up windoes for first time by
        disabling buttons and location text field."""
        for button in self.btns:
            button.setDisabled(True)
        self.ui.txt_location.setDisabled(True)
        self.ui.txt_badge.setDisabled(True)

    def reset_issue_loan_form(self) -> None:
        """clears the issue loan form and disables the button"""
        for item in self.icon_labels:
            item.clear()

        for item in self.details_lables:
            item.clear()

        self.disable_buttons()

        # for label in self.confirm_labels:
        #     label.setVisible(False)
        self.ui.txt_asset.setFocus()

        self.ui.lbl_equipment.setStyleSheet("color:black")
        self.ui.lbl_loan.setStyleSheet("color:black")
        self.ui.lbl_badge.setStyleSheet("color:black")
        self.ui.frame_confirm.setStyleSheet("color:transparent")

        self.ui.lbl_no_1.setPixmap(self.number_1_pixmap)
        self.ui.lbl_no_2.setPixmap(self.number_2_pixmap)
        self.ui.lbl_3.setPixmap(self.number_3_pixmap)
        self.ui.lbl_4.setVisible(False)
        for text in self.txt_boxes:
            text.setStyleSheet("color:black")

    def clear(self, clear_all: bool = None):
        """clears the content of form based on whether it is all the form
        or through the QLineedit clear button"""

        if clear_all is True:
            for item in self.txt_boxes:
                item.setText("")

        self.reset_issue_loan_form()

    def on_successful_login(self, value_returned: list):
        """capture the first name and change the user button text
        caputre the username that is logged in
        enable buttons for a authenticated user
        and set stylesheet for user button"""

        self.logged_in_user["first_name"] = value_returned[0]
        self.logged_in_user["username"] = value_returned[1]
        self.logged_in_user["user_id"] = MPCE_PERSONNEL[value_returned[1]][2]

        self.ui.btn_user.setText(self.logged_in_user["first_name"])
        self.mpce_staff_logged_in = True
        for item in self.logged_user_btn:
            item.show()
            item.setEnabled(True)
        self.ui.btn_user.setChecked(True)
        self.ui.btn_user.setStyleSheet("background-color:#009639")
        self.ui.btn_user.setChecked(True)
        self.ui.txt_asset.setFocus()
        self.ui.btn_check_in.setDisabled(True)
        self.start_countdown_main_window()

    def log_out(self) -> None:
        if self.mpce_staff_logged_in is True:
            logout_option = QMessageBox.question(
                self,
                "Logging out",
                "Are you sure you want to log out",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                defaultButton=QMessageBox.StandardButton.No,
            )
            if logout_option == QMessageBox.StandardButton.Yes:
                self.reset_window_on_logout()

    def reset_window_on_logout(self):
        """Resets the windows fields for guest users"""
        self.ui.btn_user.setText("Guest")
        self.ui.btn_user.setStyleSheet("color:white")
        self.mpce_staff_logged_in = False
        self.username_logged_in = ""
        for item in self.logged_user_btn:
            item.hide()

        for button in self.authenticated_user_btn:
            button.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.txt_asset.setFocus()
        self.clear(clear_all=True)
        self.countdown_timer.stop()

    def switch_user(self):
        """Log the current user and
        open the login page when switch user is pressed."""

        self.ui.btn_user.setText("Guest")
        self.ui.btn_user.setStyleSheet("color:white")
        self.mpce_staff_logged_in = False
        self.username_logged_in = ""
        for item in self.logged_user_btn:
            item.hide()

        for button in self.authenticated_user_btn:
            button.hide()
        self.login_window.setModal(True)
        self.login_window.reset_form()
        self.login_window.raise_()
        self.login_window.exec()

    def open_logout_timer_window(self):
        """class the logout timer window
        which is a countdown window that allows user
        if they want to continue or logout"""

        if self.mpce_staff_logged_in is True:
            self.logout_timer_window = LogoutTimer(self)
            self.logout_timer_window.start_countdown()

            self.logout_timer_window.setModal(True)
            self.logout_timer_window.show()

        self.logout_timer_window.continue_using_app.connect(
            self.start_countdown_main_window
        )
        self.logout_timer_window.logout_user.connect(self.reset_window_on_logout)

    def start_countdown_main_window(self):
        """Start the logout countdown timer"""
        self.countdown_timer = QTimer(self)
        self.reset_countdown()
        self.countdown_timer.start(1000)
        self.countdown_timer.timeout.connect(self.update_countdown)

    def update_countdown(self):
        """update the countdown, and display in the status bar"""
        self.time_remaining -= 1000
        remaining_time = max(0, self.time_remaining)
        minutes = remaining_time // 60000
        seconds = (remaining_time % 60000) // 1000
        self.statusBar().showMessage(f"Timeout in {minutes:02}:{seconds:02}")

        if self.time_remaining <= 0:
            self.countdown_timer.stop()
            self.open_logout_timer_window()

    def reset_countdown(self):
        """reset the time remaining in minutes"""

        if self.mpce_staff_logged_in is True:
            self.time_remaining = INACTIVE_TIMEOUT * 60 * 1000

    def return_loan(self):
        """based on the tab the user is in
        return loan and created the correct job"""
        work_done = self.ui.txt_work_done.toPlainText()
        # reported_fault = self.ui.txt_reported_fault.toPlainText()
        function_check = self.ui.chkbx_function
        batt_rep = self.ui.chkbx_batt_replace
        vis_inspec = self.ui.chkbx_visual_insp

        logged_user_personnel_id = MPCE_PERSONNEL[self.logged_in_user["username"]][3]

        job_type_id = JOB_TYPE["Function Check"]
        job_status_id = JOB_STATUS["Completed"]

        if work_done and not (function_check.isChecked() or batt_rep.isChecked()):
            QMessageBox.information(
                self, "Loan Return", "Fill in the mandatory fields."
            )

        elif not work_done and (function_check.isChecked() or vis_inspec.isChecked()):
            QMessageBox.information(self, "Loan Return", "Work done field is emtpy!")
        elif not work_done and not (
            function_check.isChecked() or vis_inspec.isChecked()
        ):
            QMessageBox.information(
                self,
                "Loan Return",
                "Fill the workdone field and tick one of the check boxes!",
            )
        elif not (self.ui.rb_function_pass.isChecked()):
            QMessageBox.information(
                self,
                "Loan Return",
                "Select funcitonal check pass/fail and PPM required",
            )
        elif not (self.ui.rb_ppm_no.isChecked() or self.ui.rb_ppm_yes.isChecked()):
            QMessageBox.information(
                self,
                "Loan Return",
                "Select PPM required",
            )
        else:
            print("create job")
            self.db.return_loan(equipment_id=ASSET["equipment_id"])
            job = self.db.create_job(
                job_type_id=job_type_id,
                job_status_id=job_status_id,
                equipment_id=ASSET["equipment_id"],
                reported_fault=REPORTED_FAULT,
                work_end_date=self.today,
                tech_id=logged_user_personnel_id,
                taken_by_id=logged_user_personnel_id,
                work_done=work_done,
                user_id=self.logged_in_user["user_id"],
                visual_inspection=vis_inspec.isChecked(),
                function_check=function_check.isChecked(),
                battery_replaced=batt_rep.isChecked(),
            )
            if (
                job
            ):  # if job created successfully display a pop up message and update the job fields
                QMessageBox.information(
                    self,
                    "Loan Return",
                    f"Loan returned and a Function Job created, job no: {job}",
                )
                self.ui.btn_submit.setDisabled(True)
                self.ui.txt_job_number.setText(str(job))
                self.ui.txt_job_type.setText("Function Check")
                self.ui.txt_assinged_tech.setText(
                    MPCE_PERSONNEL[self.logged_in_user["username"]][1]
                )  # Get full name of MPCE personnel

    def print_label(self):
        pass

    def clear_return_loan(self):
        """Clear the return loan form off all entries"""
        for checkbox in self.return_loan_chkbox:
            checkbox.setChecked(False)

        # self.ui.txt_technician.setText("")
        # self.ui.txt_reported_fault.clear()
        self.ui.txt_work_done.clear()

    def on_failed_function_check(self) -> None:
        """Open the repair/ppm job dialogue"""

        self.assing_tech_window.equipment_id = ASSET["equipment_id"]
        self.assing_tech_window.job_type_id = JOB_TYPE["Repair/Correction"]
        self.assing_tech_window.job_status_id = JOB_STATUS["Not Started"]
        self.assing_tech_window.taken_by_id = MPCE_PERSONNEL[
            self.logged_in_user["username"]
        ][3]
        self.assing_tech_window.user_id = self.logged_in_user["user_id"]

        self.assing_tech_window.setModal(True)
        if self.ui.rb_function_fail.isChecked():
            self.assing_tech_window.show()
            self.ui.txt_job_type.setText("Repair/Correction")
            self.assing_tech_window.ui.txt_technician.setFocus()
            self.assing_tech_window.ui.groupBox_2.setVisible(True)
            self.assing_tech_window.ui.lbl_title.setText("Create Repair Job")

    def on_ppm_required(self) -> None:
        """Open the repair/ppm job dialogue"""

        self.assing_tech_window.equipment_id = ASSET["equipment_id"]
        self.assing_tech_window.job_type_id = JOB_TYPE["PPM"]
        self.assing_tech_window.job_status_id = JOB_STATUS["Not Started"]
        self.assing_tech_window.taken_by_id = MPCE_PERSONNEL[
            self.logged_in_user["username"]
        ][3]
        self.assing_tech_window.user_id = self.logged_in_user["user_id"]
        self.ui.txt_job_type.setText("PPM")
        self.assing_tech_window.setModal(True)

        if self.ui.rb_ppm_yes.isChecked():
            self.assing_tech_window.show()
            self.assing_tech_window.ui.txt_technician.setFocus()
            self.assing_tech_window.ui.groupBox_2.setVisible(False)
            self.assing_tech_window.ui.lbl_title.setText("Create PPM Job")

    def on_job_by_dialog(self, job_info: list) -> None:
        """Populate the created job fields"""

        print("triggered this")
        self.ui.txt_job_number.setText() = job_info[0]
        self.ui.txt_assinged_tech.setText() = job_info[1]

        print(job_info)


class MouseTracker(QObject):
    """Class used for emit signal that connects to the main window
    when a mose moves across the screen, the signal is used to reset
    the auto-logout timer."""

    mouse_moved = Signal()

    def __init__(self):
        super().__init__()
        self.app = app
        self.app.installEventFilter(self)

    def eventFilter(self, obj, event):
        """Event filter used to filter mouse move event and emit a signal
        both are returning false otherwise the change of mouse pointer
        from hand to arrow would not work"""

        if event.type() == QEvent.MouseMove:
            self.mouse_moved.emit()
            return False
        return False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setStyleSheet(
    #     """QMessageBox QPushButton{min-width: 100px;
    #     background-color:#89cff3;
    #                 }
    #     QPushButton:default{
    #     background-color:#00a9ff;
    #     }"""
    # )
    window = MainWindow()
    window.show()
    # tracker = MouseTracker(app)
    sys.exit(app.exec())
