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
    QDialog,
    QLineEdit,
)


from PySide6.QtGui import QMouseEvent, QPixmap

from ui_mainwindow import Ui_MainWindow

# from ui.ui_dialogue import Ui_Dialog
from ui_login import Ui_Dialog
from logout_timer import LogoutTimer
from database import Database
from authentication import LDAPAuthentication

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

        self.login_window = LoginWindow(self)
        self.login_window.hide()
        self.setMouseTracking(True)

        # tracks mouse movement across the wigdget and resets the timer
        self.tracker = MouseTracker()
        self.tracker.mouse_moved.connect(self.reset_countdown)

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
        self.ui.lbl_confirm_info.setVisible(False)

        self.ui.txt_asset.setFocus()
        self.ui.txt_asset.setPlaceholderText("Enter Equipment No")
        self.ui.txt_location.setPlaceholderText("Start typing the location")
        self.ui.btn_validate_eq.clicked.connect(self.get_asset_info)
        self.ui.txt_asset.returnPressed.connect(self.get_asset_info)
        self.ui.btn_validate_loc.clicked.connect(self.validate_location)
        self.ui.txt_location.returnPressed.connect(self.validate_location)
        self.ui.btn_confirm.clicked.connect(self.confirm_loan)
        self.ui.btn_clear.clicked.connect(self.clear)

        self.number_1_pixmap = QPixmap(":/1.png")
        self.ui.lbl_no_1.setPixmap(self.number_1_pixmap)
        self.number_2_pixmap = QPixmap(":/2.png")
        self.ui.lbl_no_2.setPixmap(self.number_2_pixmap)
        self.number_3_pixmap = QPixmap(":/3.png")
        self.ui.lbl_3.setPixmap(self.number_3_pixmap)

        # grey pixmap
        self.number_1_grey = QPixmap(":/1_grey.png")
        self.number_2_grey = QPixmap(":/2_grey.png")
        self.number_3_grey = QPixmap(":/3_grey.png")
        self.get_mpce_personnel()
        self.ui.stackedWidget.setCurrentIndex(0)

        self.confirm_labels = (
            self.ui.lbl_3,
            self.ui.lbl_confirm_icon,
            self.ui.lbl_confirm_info,
        )
        for label in self.confirm_labels:
            label.setVisible(False)

        self.txt_boxes = (self.ui.txt_asset, self.ui.txt_location)
        self.btns = (
            self.ui.btn_validate_loc,
            self.ui.btn_confirm,
        )
        self.icon_labels = (
            self.ui.lbl_eq_validate,
            self.ui.lbl_eq_validate,
            self.ui.lbl_confirm_icon,
        )
        self.details_lables = (
            self.ui.lbl_category,
            self.ui.lbl_arrow,
            self.ui.lbl_loc_validate,
            self.ui.lbl_location,
        )
        self.get_location()
        self.disable_buttons()

        self.ui.btn_user_2.clicked.connect(self.on_user_btn_pressed)

        location_completer = QCompleter(self.location_name, self)
        location_completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.ui.txt_location.setCompleter(location_completer)

        # capture the value returned from the login windows
        self.login_window.login_successfull.connect(self.on_successful_login)
        # self.logout_timer_window.logout_user.connect(self.action_from_timer)

        self.home_btn = (self.ui.btn_home, self.ui.btn_home_2)
        self.return_loan_btn = (self.ui.btn_check_in, self.ui.btn_check_in_2)

        self.logged_user_btn = (
            self.ui.btn_check_in,
            self.ui.btn_check_in_2,
            self.ui.btn_setting,
            self.ui.btn_setting_2,
            self.ui.btn_dashboard,
            self.ui.btn_dashboard_2,
        )

        self.authenticated_user_btn = (
            self.ui.btn_change_user,
            self.ui.btn_change_user_3,
            self.ui.btn_logout_4,
            self.ui.btn_logout_8,
        )

        self.logout_buttons = (
            self.ui.btn_logout_4,
            self.ui.btn_logout_8,
            self.ui.btn_logout_2,
            self.ui.btn_logout,
        )

        self.switch_user_buttons = (self.ui.btn_change_user, self.ui.btn_change_user_3)

        self.ui.side_menu.hide()
        self.ui.btn_menu_2.hide()
        self.ui.btn_menu.hide()

        self.return_loan_chkbox = (
            self.ui.chkbx_visual_insp,
            self.ui.chkbx_function,
            self.ui.chkbx_batt_replace,
            # self.ui.chkbx_rtls_batt,
        )
        self.radio_btn = (self.ui.rb_job, self.ui.rb_ppm)

        for button in self.switch_user_buttons:
            button.clicked.connect(self.switch_user)

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
        self.ui.txt_technician.setCompleter(tech_auto_complete)
        self.ui.txt_technician.setClearButtonEnabled(True)
        self.ui.txt_asset.setClearButtonEnabled(True)
        self.ui.txt_location.setClearButtonEnabled(True)

        self.ui.btn_submit.clicked.connect(self.return_loan)
        self.ui.btn_clear_2.clicked.connect(self.clear_issue_loan)

    def on_user_btn_pressed(self) -> None:
        """Actions on what happens when user presses the login
        button, if a user is logged in, present them with switch user or logout
        if user not logged in, open the login window to allow user to login"""
        if self.mpce_staff_logged_in is False:
            self.login_window.setModal(True)
            self.login_window.raise_()
            self.login_window.exec()
        elif self.ui.btn_change_user.isVisible():
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
            # check if category of asset in those that can be supplied by libarary
            if (
                ASSET["category"] in SUPPLY_CATEGORY
                and self.mpce_staff_logged_in is True
            ):
                self.permenant_supplied_by_library = True
                self.valid_asset_searched()
                # if not a library item
            elif (
                ASSET["library_status_id"] == "WWW1"
                or ASSET["library_status_id"] is None
            ):
                self.ui.lbl_eq_validate.setPixmap(self.error_pixmap)
                QMessageBox.warning(
                    self,
                    "Equipment",
                    f"Equipment No: {search_value} is not a library item ",
                )
                # If on loan check that mpce staff is logged in
                # if mpce staff logged in, take to checkin page
            elif ASSET["library_status_id"] == "WWW3":
                if self.mpce_staff_logged_in is True:
                    self.ui.stackedWidget.setCurrentIndex(1)
                    self.clear_issue_loan()
                    try:
                        index = RTLS_BATTERY["rtls_equipment_no"].index(search_value)
                        battery_capacity = RTLS_BATTERY["battery_capacity"][index]
                        print(battery_capacity)
                    except Exception:
                        print("not on the rtls battery list")

                    self.ui.txt_loan_location.setText(ASSET["loan_location"])
                    self.ui.txt_asset_2.setText(search_value)
                    self.ui.txt_category.setText(ASSET["category"])
                    self.ui.btn_check_in_2.setChecked(True)
                else:
                    QMessageBox.warning(
                        self,
                        "Equipment loan",
                        "This equipment has not been checked-in by libarry staff.\n"
                        "Please leave to aside and pick another one",
                    )
            else:
                self.valid_asset_searched()
        else:
            self.ui.lbl_eq_validate.setPixmap(self.error_pixmap)
            self.ui.lbl_loc_validate.clear()
            QMessageBox.critical(self, "Equipment search", "Unable to find an Asset!")
            # self.ui.lbl_category.setText("")
            self.ui.btn_confirm.setDisabled(True)

    def valid_asset_searched(self) -> None:
        self.ui.lbl_eq_validate.setPixmap(self.confirm_pixmap)
        self.ui.lbl_category.setText(ASSET["category"])
        self.ui.lbl_arrow.setPixmap(self.arrow_pixmap)
        self.ui.btn_validate_loc.setDisabled(False)
        self.ui.txt_location.setDisabled(False)
        self.ui.txt_location.setFocus()
        self.ui.lbl_equipment.setStyleSheet("color:grey")
        self.ui.lbl_no_1.setPixmap(self.number_1_grey)
        self.ui.txt_asset.setStyleSheet("color:grey")

    def validate_location(self):
        """Checks to make sure the location entered is a correct one
        by comparing to location dictionary
        """
        loc_inputted = self.ui.txt_location.text().strip()
        try:
            ASSET["location_id"] = self.location[loc_inputted]
            self.ui.lbl_loc_validate.setPixmap(self.confirm_pixmap)
            self.ui.lbl_location.setText(loc_inputted)
            self.ui.btn_confirm.setDisabled(False)
            self.ui.btn_clear.setDisabled(False)
            self.ui.lbl_confirm_info.setVisible(True)
            self.ui.lbl_3.setVisible(True)
            self.ui.lbl_loan.setStyleSheet("color:grey")
            self.ui.lbl_no_2.setPixmap(self.number_2_grey)
            self.ui.txt_location.setStyleSheet("color:grey")
        except KeyError:
            self.ui.lbl_loc_validate.setPixmap(self.error_pixmap)
            # self.ui.lbl_location.setText("")
            self.ui.btn_confirm.setDisabled(True)
            for label in self.confirm_labels:
                label.setVisible(False)

    def confirm_loan(self):
        """issues loan by called the db function"""
        if self.permenant_supplied_by_library is True:
            supply_job = QMessageBox.question(
                self,
                "Issue permanent loan",
                "Do you want to change location of this asset"
                "and issue a supply job?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                defaultButton=QMessageBox.StandardButton.No,
            )
            if supply_job == QMessageBox.StandardButton.Yes:
                job = self.db.create_job(
                    update_location=True,
                    create_job=True,
                    equipment_id=ASSET["equipment_id"],
                    location_id=ASSET["location_id"],
                    job_status_id=JOB_STATUS["Completed"],
                    job_type_id=JOB_TYPE["Supply"],
                    tech_id=MPCE_PERSONNEL[self.logged_in_user["username"]][3],
                    taken_by_id=MPCE_PERSONNEL[self.logged_in_user["username"]][3],
                    user_id=self.logged_in_user["user_id"],
                    reported_fault=f"Wards requires supply of the{ASSET['category']}",
                    work_done=f"Supplied ward with {ASSET['category']}",
                )
                if job:
                    QMessageBox.information(
                        self,
                        "Successful Job Creation",
                        f"A Supply Job with Job number: [{job}] has been created!",
                    )
        else:
            try:
                self.db.issue_loan(
                    equipment_id=ASSET["equipment_id"],
                    location_id=ASSET["location_id"],
                )
                self.ui.lbl_confirm_icon.setPixmap(self.confirm_pixmap)
                QMessageBox.information(
                    self, "Equipment Loan", " Loan succesfully issued!"
                )
                self.clear()
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

    def clear(self):
        """clears the form and disables the button"""

        for item in self.icon_labels:
            item.clear()

        for item in self.details_lables:
            item.clear()

        for item in self.txt_boxes:
            item.setText("")
        self.disable_buttons()

        for label in self.confirm_labels:
            label.setVisible(False)
        self.ui.txt_asset.setFocus()

        self.ui.lbl_equipment.setStyleSheet("color:black")
        self.ui.lbl_loan.setStyleSheet("color:black")
        self.ui.lbl_no_1.setPixmap(self.number_1_pixmap)
        self.ui.lbl_no_2.setPixmap(self.number_2_pixmap)
        for text in self.txt_boxes:
            text.setStyleSheet("color:black")

    def on_successful_login(self, value_returned: list):
        """capture the first name and change the user button text
        caputre the username that is logged in
        enable buttons for a authenticated user
        and set stylesheet for user button"""

        self.logged_in_user["first_name"] = value_returned[0]
        self.logged_in_user["username"] = value_returned[1]
        self.logged_in_user["user_id"] = MPCE_PERSONNEL[value_returned[1]][2]

        self.ui.btn_user_2.setText(self.logged_in_user["first_name"])
        self.mpce_staff_logged_in = True
        for item in self.logged_user_btn:
            item.show()
            item.setEnabled(True)
        self.ui.btn_user_2.setChecked(True)
        self.ui.btn_user_2.setStyleSheet("background-color:#009639")
        self.ui.btn_user_2.setChecked(True)
        self.ui.txt_asset.setFocus()
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
        self.ui.btn_user_2.setText("Guest")
        self.ui.btn_user_2.setStyleSheet("color:white")
        self.mpce_staff_logged_in = False
        self.username_logged_in = ""
        for item in self.logged_user_btn:
            item.hide()

        for button in self.authenticated_user_btn:
            button.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.txt_asset.setFocus()
        self.clear()
        self.countdown_timer.stop()

    def switch_user(self):
        """Log the current user and
        open the login page when switch user is pressed."""

        self.ui.btn_user_2.setText("Guest")
        self.ui.btn_user_2.setStyleSheet("color:white")
        self.mpce_staff_logged_in = False
        self.username_logged_in = ""
        for item in self.logged_user_btn:
            item.hide()

        for button in self.authenticated_user_btn:
            button.hide()
        self.login_window.setModal(True)
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
        # self.statusBar().showMessage(f"Timeout in {minutes:02}:{seconds:02}")

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
        reported_fault = self.ui.txt_reported_fault.toPlainText()
        function_check = self.ui.chkbx_function
        batt_rep = self.ui.chkbx_batt_replace
        vis_inspec = self.ui.chkbx_visual_insp

        repair_job = self.ui.rb_job
        ppm_job = self.ui.rb_ppm
        assigned_tech = self.ui.txt_technician.text()
        logged_user_personnel_id = MPCE_PERSONNEL[self.logged_in_user["username"]][3]

        if self.ui.tabWidget.currentIndex() == 0:
            job_type_id = JOB_TYPE["Function Check"]
            job_status_id = JOB_STATUS["Completed"]
            if work_done and not (
                function_check.isChecked()
                or batt_rep.isChecked()
                or vis_inspec.isChecked()
            ):
                QMessageBox.information(
                    self, "Loan Return", "At least one check box needs to be checked!"
                )

            elif not work_done and (
                function_check.isChecked()
                or batt_rep.isChecked()
                or vis_inspec.isChecked()
            ):
                QMessageBox.information(
                    self, "Loan Return", "Work done field is emtpy!"
                )
            elif not work_done and not (
                function_check.isChecked()
                or batt_rep.isChecked()
                or vis_inspec.isChecked()
            ):
                QMessageBox.information(
                    self,
                    "Loan Return",
                    "Fill the workdone field and tick one of the check boxes!",
                )
            else:
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
                    create_job=True,
                )

                if job:  # if job created successfully display a pop up message
                    QMessageBox.information(
                        self,
                        "Loan Return",
                        f"Loan returned and a Function Job created, job no: {job}",
                    )
                    self.ui.btn_submit.setDisabled(True)
        else:
            try:
                job_status_id = JOB_STATUS["Not Started"]
                assigned_tech = ASSIGNED_TECHNICIAN[self.ui.txt_technician.text()][0]
                if repair_job.isChecked() and reported_fault and assigned_tech:
                    job = self.db.create_job(
                        job_type_id=JOB_TYPE["Repair/Correction"],
                        job_status_id=job_status_id,
                        equipment_id=ASSET["equipment_id"],
                        reported_fault=reported_fault,
                        tech_id=assigned_tech,
                        user_id=self.logged_in_user["user_id"],
                        taken_by_id=logged_user_personnel_id,
                        create_job=True,
                    )
                    if job:
                        self.ui.btn_submit.setDisabled(True)
                        self.job_sticker["job_number"] = job
                        self.job_sticker["assigned_tech"] = (
                            self.ui.txt_technician.text()
                        )
                        self.job_sticker["job_type"] = "Repair"
                        self.job_sticker["equipment_no"] = ASSET["equipment_no"]
                        QMessageBox.information(
                            self,
                            "Successful Job Creation",
                            f"A Repair Job with Job number: [{job}] has been created!",
                        )

                elif ppm_job.isChecked() and reported_fault and assigned_tech:
                    job_type_id = JOB_TYPE["PPM"]
                    job = self.db.create_job(
                        job_status_id=job_status_id,
                        job_type_id=job_type_id,
                        equipment_id=ASSET["equipment_id"],
                        reported_fault=reported_fault,
                        tech_id=assigned_tech,
                        taken_by_id=logged_user_personnel_id,
                        user_id=self.logged_in_user["user_id"],
                        create_job=True,
                    )
                    if job:
                        self.ui.btn_submit.setDisabled(True)
                        self.job_sticker["job_number"] = job
                        self.job_sticker["assigned_tech"] = assigned_tech
                        self.job_sticker["job_type"] = "PPM"
                        self.job_sticker["equipment_no"] = ASSET["equipment_no"]
                        QMessageBox.information(
                            self,
                            "Successful Job Creation",
                            f"A PPM Job with Job number: [{job}] has been created!",
                        )
                    else:
                        QMessageBox.information(
                            self,
                            "Create Job",
                            "Unable to create job, please check all information has been entered correctly",
                        )
                else:
                    QMessageBox.information(
                        self,
                        "Create Job",
                        "Select a job type and fill in the reported fault field!",
                    )
            except KeyError:
                QMessageBox.warning(
                    self, "Job Creation", "Assigned technician field empty"
                )

    def print_label(self):
        pass

    def clear_issue_loan(self):
        """Clear the form off all entries"""
        for checkbox in self.return_loan_chkbox:
            checkbox.setChecked(False)
        for radio_btn in self.radio_btn:
            radio_btn.setChecked(False)

        self.ui.txt_technician.setText("")
        self.ui.txt_reported_fault.clear()
        self.ui.txt_work_done.clear()


class LoginWindow(QDialog):
    """Opens login windows and returns true
    when the username and password matches the record on AD
    also returns true when the username is found on the MPCE DB
    else returns false and displays error messages."""

    login_successfull = Signal(list)

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        # self.user = user
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Login")

        self.ui.frame_error.hide()
        self.ui.txt_password.setEchoMode(QLineEdit.Password)
        self.ui.txt_username.setFocus()

        # self.ui.btn_login.clicked.connect(lambda: self.ui.frame_error.show())
        self.ui.btn_close_error.clicked.connect(lambda: self.ui.frame_error.hide())

        self.ui.btn_guest.clicked.connect(lambda: self.close())
        self.ui.btn_login.clicked.connect(self.on_login_btn_clicked)

    def on_login_btn_clicked(self):
        """take input for username and password and pass to the
        authentication funciton to check if correct username and password"""
        username_enetered = self.ui.txt_username.text()
        password_entered = self.ui.txt_password.text()
        authenticate = self.authenticate_user(
            username=username_enetered, password=password_entered
        )

        check_mpce_staff = self.mpce_staff(username=username_enetered)

        if authenticate is False:
            self.ui.frame_error.show()  # show error message

        elif authenticate is True and check_mpce_staff is False:
            self.ui.frame_error.show()
            self.ui.lbl_error.setText(
                "User not part of MPCE staff list, please contact system adminstrator!"
            )
        else:
            # return first name and username
            return_value = [
                MPCE_PERSONNEL[username_enetered][0],
                username_enetered,
            ]
            self.login_successfull.emit(return_value)
            self.ui.txt_password.clear()
            self.ui.txt_username.clear()
            self.ui.txt_username.setFocus()
            self.ui.frame_error.hide()
            self.close()

    def authenticate_user(self, username: str, password: str) -> bool:
        """takes the username and password typed and passes to LDAP class
        this carries a simple bind to the AD and if result is true
        then successful authentication"""

        ldap_autho = LDAPAuthentication(
            ldap_server=LDAP_SERVER, serach_base=SEARCH_BASE
        )
        authentiate = ldap_autho.authenticate(username=username, password=password)
        if authentiate is True:
            return True

        else:
            return False

    def mpce_staff(self, username: str) -> bool:
        """check if user is MPCE member"""
        if username in MPCE_PERSONNEL:
            return True
        else:
            return False


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
