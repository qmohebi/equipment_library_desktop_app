import sys
import re
import json
from datetime import datetime
import csv
import os

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QCompleter,
    QMessageBox,
    QDialog,
    QLineEdit,
    QStackedWidget,
    QWidget,
)

from PySide6.QtGui import QPixmap

from ui_mainwindow import Ui_MainWindow

# from ui.ui_dialogue import Ui_Dialog
from ui_login import Ui_Dialog

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

PERSONNEL_RETURNING_LOAN = {}
TECHNICIANS = {}
JOB_TYPE = {
    "Repair/Correction": "STG2005061300002",
    "PPM": "STG2005061300001",
    "Function Check": "591F356502204017989184484E650984",
}

RTLS_BATTERY = {"rtls_equipment_no": [], "battery_capacity": []}
JOB_STATUS = {
    "Not Started": "STG2005071800000",
    "Completed": "69914FCE64344265A0E72EC66528D9FA",
}

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

        self.db = Database()

        self.login_window = LoginWindow(self)
        self.login_window.hide()

        self.ui.btn_login.hide()
        self.ui.btn_login_2.hide()

        # self.dialogue.setupUi(self)

        self.location_name = []  # used for location auto complete
        self.location = {}  # use for getting location id
        self.location_id = ""

        # WWW1 - not a library item
        # WWW2 - available
        # WWW3 - on loan
        # STG2005061300002 - Loan in progress

        self.confirm_pixmap = QPixmap("./icon/tick.png")
        self.error_pixmap = QPixmap("./icon/cancel.png")
        self.arrow_pixmap = QPixmap("./icon/arrow.png")
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

        self.number_1_pixmap = QPixmap("./icon/1.png")
        self.ui.lbl_no_1.setPixmap(self.number_1_pixmap)
        self.number_2_pixmap = QPixmap("./icon/2.png")
        self.ui.lbl_no_2.setPixmap(self.number_2_pixmap)
        self.number_3_pixmap = QPixmap("./icon/3.png")
        self.ui.lbl_3.setPixmap(self.number_3_pixmap)

        # grey pixmap
        self.number_1_grey = QPixmap("./icon/1_grey.png")
        self.number_2_grey = QPixmap("./icon/2_grey.png")
        self.number_3_grey = QPixmap("./icon/3_grey.png")
        self.get_mpce_personnel()

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

        self.ui.btn_user_2.clicked.connect(self.login_page)

        location_completer = QCompleter(self.location_name, self)
        location_completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.ui.txt_location.setCompleter(location_completer)

        self.ui.btn_login_2.clicked.connect(self.login_page)

        self.login_window.login_successfull.connect(self.on_successful_login)
        # self.return_loan = LoanReturn(self)
        self.status_bar()

        self.home_btn = (self.ui.btn_home, self.ui.btn_home_2)
        self.return_loan_btn = (self.ui.btn_check_in, self.ui.btn_check_in_2)

        logged_user_btn = (
            self.return_loan_btn,
            self.ui.btn_setting,
            self.ui.btn_setting_2,
            self.ui.btn_dashboard,
            self.ui.btn_dashboard_2,
            self.ui.btn_logout,
            self.ui.btn_logout_2,
        )

        for button in self.return_loan_btn:
            button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))

        for button in self.home_btn:
            button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))

    def login_page(self):
        self.login_window.setModal(True)
        self.login_window.raise_()
        self.login_window.exec()

    def on_successful_login(self, first_name):
        self.ui.btn_user_2.setText(first_name)

    def toggle_login_icon(self):
        if self.ui.btn_login_2.isVisible():
            self.ui.btn_login_2.hide()
        else:
            self.ui.btn_login_2.show()

    def status_bar(self):
        self.statusBar().showMessage("Ready")

    def get_location(self):
        """get the location from database and create a list and dictionary
        lis to be used for autocompleting the location text box and
        dictionary for get the location_id"""
        location = self.db.get_location()
        self.location = location
        self.location_name = list(location.keys())

    def get_mpce_personnel(self):
        """populate the personnel dictionary with mpce personnel from the db"""
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

            PERSONNEL_RETURNING_LOAN[username] = [
                first_name,
                name,
                user_id,
                personnel_id,
                username,
                email,
            ]
            TECHNICIANS[name] = [personnel_id, user_id]

    def get_asset_info(self):
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
            if ASSET["library_status_id"] == "WWW1":
                self.ui.lbl_eq_validate.setPixmap(self.error_pixmap)
                QMessageBox.warning(
                    self,
                    "Equipment",
                    f"Equipment No: {search_value} is not a library item ",
                )

            elif ASSET["library_status_id"] == "WWW3":

                index = RTLS_BATTERY["rtls_equipment_no"].index(search_value)
                battery_capacity = RTLS_BATTERY["battery_capacity"][index]
                print(battery_capacity)

                # Open the dialogue windows and display the information
                dlg = LoanReturn()
                dlg.ui.txt_loan_location.setText(ASSET["loan_location"])
                dlg.ui.txt_asset.setText(search_value)
                dlg.ui.txt_category.setText(ASSET["category"])
                dlg.exec()
            else:

                self.ui.lbl_eq_validate.setPixmap(self.confirm_pixmap)
                self.ui.lbl_category.setText(ASSET["category"])
                self.ui.lbl_arrow.setPixmap(self.arrow_pixmap)
                self.ui.btn_validate_loc.setDisabled(False)
                self.ui.txt_location.setDisabled(False)
                self.ui.txt_location.setFocus()
                self.ui.lbl_equipment.setStyleSheet("color:grey")
                self.ui.lbl_no_1.setPixmap(self.number_1_grey)
                self.ui.txt_asset.setStyleSheet("color:grey")
        else:
            self.ui.lbl_eq_validate.setPixmap(self.error_pixmap)
            self.ui.lbl_loc_validate.clear()
            QMessageBox.critical(self, "Equipment search", "Unable to find an Asset!")
            # self.ui.lbl_category.setText("")
            self.ui.btn_confirm.setDisabled(True)

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
        try:
            self.db.issue_loan(
                equipment_id=ASSET["equipment_id"],
                location_id=ASSET["location_id"],
            )
            self.ui.lbl_confirm_icon.setPixmap(self.confirm_pixmap)
            QMessageBox.question(
                self,
                "Equipment Loan",
                " Loan succesfully issued!",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                defaultButton=QMessageBox.StandardButton.No,
            )
            self.clear()
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


class LoginWindow(QDialog):
    login_successfull =  Signal(str)
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        
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
            self.ui.frame_error.show()

        elif authenticate is True and check_mpce_staff is False:
            self.ui.frame_error.show()
            self.ui.lbl_error.setText(
                "User not part of MPCE staff list, please contact system adminstrator!"
            )
        else:
            self.login_successfull.emit(PERSONNEL_RETURNING_LOAN[username_enetered][0])
            self.close()

    def authenticate_user(self, username: str, password: str) -> bool:

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
        if username in PERSONNEL_RETURNING_LOAN:
            return True
        else:
            return False

        # if username in PERSONNEL_RETURNING_LOAN and user_authenticated is True:
        #     return PERSONNEL_RETURNING_LOAN[username][0]

        # else:
        #     return False


class LoanReturn(QDialog):
    """Loan return dialog"""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.db = Database()
        self.user_id = ""
        self.job_sticker = {
            "job_number": "",
            "assigned_tech": "",
            "job_type": "",
            "equipment_no": "",
        }
        self.loan_returned = False
        # date passed to MSSQL needs to be in ISO standard: YY-MM-DD
        self.today = datetime.today().strftime("%Y-%m-%d")
        self.ui.txt_username.setPlaceholderText(
            "Enter your username and press confirm to unlock the form"
        )
        self.setWindowTitle("Loan Return")

        # self.ui.btn_clear.clicked.connect(self.check)
        self.ui.btn_confirm.clicked.connect(self.validate_user)
        self.radio_btn = (self.ui.rb_return_loan, self.ui.rb_create_job)
        self.return_loan_options = (
            self.ui.chkbx_visual_insp,
            self.ui.chkbx_batt_replace,
            self.ui.chkbx_function,
            self.ui.txt_work_done,
        )

        self.ui.txt_username.setFocus()
        self.ui.txt_username.returnPressed.connect(self.validate_user)

        self.ui.txt_technician.setPlaceholderText("Start typing technician's name")

        self.txt_boxes = (
            self.ui.txt_technician,
            self.ui.txt_reported_fault,
            self.ui.txt_work_done,
        )

        self.loan_chkbox = (
            self.ui.chkbx_batt_replace,
            self.ui.chkbx_function,
            self.ui.chkbx_visual_insp,
        )
        for button in self.radio_btn:
            button.setDisabled(True)

        self.ui.tabWidget.setDisabled(True)

        self.loan_radio = (self.ui.rb_return_loan, self.ui.rb_create_job)
        for button in self.loan_radio:
            button.clicked.connect(self.loan_tab)

        self.job_radio = (self.ui.rb_job, self.ui.rb_ppm)

        # create auto completer for technicians in the job tab
        tech_auto_complete = QCompleter(list(TECHNICIANS.keys()), self)
        tech_auto_complete.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.ui.txt_technician.setCompleter(tech_auto_complete)
        self.ui.btn_submit.clicked.connect(self.return_loan_create_job)

        self.ui.btn_print.clicked.connect(self.print_label)
        self.ui.btn_clear.clicked.connect(self.clear_form)

    def validate_user(self):
        """check user entered to see if it a valid mpce user
        if so allow the user to use the rest of the form"""

        try:
            username_entered = self.ui.txt_username.text().lower()
            technician_name = PERSONNEL_RETURNING_LOAN[username_entered][0]

            # user id of the person returning the loan, creating the funcion check job
            # and creating repair/ppm jobs for the engineers
            self.user_id = PERSONNEL_RETURNING_LOAN[username_entered][1]
            self.ui.lbl_technician.setText(technician_name)
            for button in self.radio_btn:
                button.setDisabled(False)
            # self.ui.tabWidget.setDisabled(False)
        except KeyError:
            for button in self.radio_btn:
                button.setDisabled(True)
            self.ui.tabWidget.setDisabled(True)

            QMessageBox.warning(
                self,
                "Username",
                "Unable to find valid username, type your username name again!",
            )
            print(ASSET["equipment_no"])


#     def loan_tab(self):
#         self.ui.tabWidget.setEnabled(True)
#         if self.ui.rb_create_job.isChecked():
#             self.ui.tabWidget.setCurrentIndex(1)
#         else:
#             self.ui.tabWidget.setCurrentIndex(0)

#     def return_loan_create_job(self):
#         """makes some checks on the check box, radio buttons for job creation
#         and ensures the workdone and reported fault fields are not blank.
#         Makes a call to the return loan function of the DB class to return the loan
#         and create function if the checkbox has been ticked and work done has been completed.
#         if no tick box and nothing in the workdone, asks users if they want to just return the loan
#         without creating a job
#         """

#         work_done = self.ui.txt_work_done.toPlainText()
#         reported_fault = self.ui.txt_reported_fault.toPlainText()
#         func_chk = self.ui.chkbx_function
#         batt_rep = self.ui.chkbx_batt_replace
#         vis_inspec = self.ui.chkbx_visual_insp

#         repair_job = self.ui.rb_job
#         ppm_job = self.ui.rb_ppm
#         assigned_tech = self.ui.txt_technician.text()
#         tech_returning_loan = PERSONNEL_RETURNING_LOAN[self.ui.txt_username.text()][2]

#         if self.ui.tabWidget.currentIndex() == 0:
#             job_type_id = JOB_TYPE["Function Check"]
#             job_status_id = JOB_STATUS["Completed"]

#             if (
#                 func_chk.isChecked() or batt_rep.isChecked() or vis_inspec.isChecked()
#             ) and work_done:
#                 # if any of the check boxes have been ticket and text in work done,
#                 # return the device to library and create a functional check job
#                 # by taking the value from the username field to get the personnel details
#                 # to be used for the creation of the job
#                 job = self.db.create_job(
#                     job_type_id=job_type_id,
#                     job_status_id=job_status_id,
#                     equipment_id=ASSET["equipment_id"],
#                     reported_fault=REPORTED_FAULT,
#                     work_end_date=self.today,
#                     tech_id=tech_returning_loan,
#                     taken_by_id=tech_returning_loan,
#                     work_done=work_done,
#                     user_id=self.user_id,
#                     visual_inspection=vis_inspec.isChecked(),
#                     function_check=func_chk.isChecked(),
#                     battery_replaced=batt_rep.isChecked(),
#                     create_job=True,
#                 )

#                 if job:
#                     QMessageBox.information(
#                         self,
#                         "Loan Return",
#                         f"Loan returned and a Function Job created, job no: {job}",
#                     )
#                     self.ui.btn_confirm.setDisabled(True)

#             elif work_done and not (
#                 func_chk.isChecked() or batt_rep.isChecked() or vis_inspec.isChecked()
#             ):
#                 QMessageBox.information(
#                     self, "Loan Return", "At least one check box needs to be checked!"
#                 )

#             elif not work_done and (
#                 func_chk.isChecked() or batt_rep.isChecked() or vis_inspec.isChecked()
#             ):
#                 QMessageBox.information(
#                     self, "Loan Return", "Work done field is emtpy!"
#                 )
#             else:
#                 msg_box = QMessageBox.question(
#                     self,
#                     "Loan Return",
#                     "Do you want to return loan without creating a Function Check Job?",
#                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
#                     defaultButton=QMessageBox.StandardButton.No,
#                 )
#                 if msg_box == QMessageBox.StandardButton.Yes:
#                     # if user doesn't
#                     self.db.create_job(
#                         equipment_id=ASSET["equipment_id"],
#                     )
#                     QMessageBox.information(
#                         self,
#                         "Loan Return",
#                         f"Successfully returned equipment: {ASSET['equipment_no']} to the library",
#                     )
#                     self.ui.btn_confirm.setDisabled(True)
#         else:
#             job_status_id = JOB_STATUS["Not Started"]
#             assigned_tech = TECHNICIANS[self.ui.txt_technician.text()][0]
#             if repair_job.isChecked() and reported_fault and assigned_tech:
#                 job = self.db.create_job(
#                     job_type_id=JOB_TYPE["Repair/Correction"],
#                     job_status_id=job_status_id,
#                     equipment_id=ASSET["equipment_id"],
#                     reported_fault=reported_fault,
#                     tech_id=assigned_tech,
#                     user_id=self.user_id,
#                     taken_by_id=tech_returning_loan,
#                     create_job=True,
#                 )
#                 if job:
#                     self.job_sticker["job_number"] = job
#                     self.job_sticker["assigned_tech"] = self.ui.txt_technician.text()
#                     self.job_sticker["job_type"] = "Repair"
#                     self.job_sticker["equipment_no"] = ASSET["equipment_no"]
#                     QMessageBox.information(
#                         self,
#                         "Successful Job Creation",
#                         f"A 'Repair Job' with Job number: [{job}] has been created!",
#                     )
#                     self.ui.btn_confirm.setDisabled(True)
#             elif ppm_job.isChecked() and reported_fault and assigned_tech:
#                 job_type_id = JOB_TYPE["PPM"]
#                 job = self.db.create_job(
#                     job_status_id=job_status_id,
#                     job_type_id=job_type_id,
#                     equipment_id=ASSET["equipment_id"],
#                     reported_fault=reported_fault,
#                     tech_id=assigned_tech,
#                     taken_by_id=tech_returning_loan,
#                     user_id=self.user_id,
#                     create_job=True,
#                 )
#                 if job:
#                     self.job_sticker["job_number"] = job
#                     self.job_sticker["assigned_tech"] = assigned_tech
#                     self.job_sticker["job_type"] = "PPM"
#                     self.job_sticker["equipment_no"] = ASSET["equipment_no"]
#                     QMessageBox.information(
#                         self,
#                         "Successful Job Creation",
#                         f"A PPM Job with Job number: [{job}] has been created!",
#                     )
#                     self.ui.btn_confirm.setDisabled(True)
#                 else:
#                     QMessageBox.information(
#                         self,
#                         "Create Job",
#                         "Unable to create job, please check all information has been entered correctly",
#                     )
#             else:
#                 QMessageBox.information(
#                     self,
#                     "Create Job",
#                     "Select a job type, technician and fill in the reported fault box!",
#                 )

#     def print_label(self):
#         print(self.job_sticker)

#     def clear_form(self):
#         """Clear the form off all entries"""
#         for text in self.txt_boxes:
#             text.clear()
#         for checkbox in self.loan_chkbox:
#             checkbox.setChecked(False)


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
    sys.exit(app.exec())
