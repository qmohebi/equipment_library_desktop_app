import sys
import re
import json
from datetime import datetime

from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QCompleter,
    QMessageBox,
    QDialog,
    QWidget,
    QStatusBar,
)
from PySide6.QtGui import QPixmap, Qt

from ui.ui_mainwindow import Ui_MainWindow
from ui.ui_dialogue import Ui_Dialog

from database import Database

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

JOB_STATUS = {
    "Not Started": "STG2005071800000",
    "Completed": "69914FCE64344265A0E72EC66528D9FA",
}


with open("config.json", encoding="utf-8") as config:
    data = json.load(config)
    REPORTED_FAULT = data["reported_fault"]
    DB_NAME = data["database"]


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.db = Database()

        # self.dialogue.setupUi(self)

        self.location_name = []  # used for location auto complete
        self.location = {}  # use for getting location id
        self.location_id = ""

        # WWW1 - not a library item
        # WWW2 - available
        # WWW3 - on loan
        # STG2005061300002 - Loan in progress

        self.confirm_pixmap = QPixmap("./ui/tick.png")
        self.error_pixmap = QPixmap("./ui/cancel.png")
        self.arrow_pixmap = QPixmap("./ui/arrow.png")
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

        self.number_1_pixmap = QPixmap("./ui/1.png")
        self.ui.lbl_no_1.setPixmap(self.number_1_pixmap)
        self.number_2_pixmap = QPixmap("./ui/2.png")
        self.ui.lbl_no_2.setPixmap(self.number_2_pixmap)
        self.number_3_pixmap = QPixmap("./ui/3.png")
        self.ui.lbl_3.setPixmap(self.number_3_pixmap)

        # grey pixmap
        self.number_1_grey = QPixmap("./ui/1_grey.png")
        self.number_2_grey = QPixmap("./ui/2_grey.png")
        self.number_3_grey = QPixmap("./ui/3_grey.png")
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

        self.status_bar = QStatusBar()
        self.status_bar.showMessage(DB_NAME)

        location_completer = QCompleter(self.location_name, self)
        location_completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.ui.txt_location.setCompleter(location_completer)

        self.return_loan = LoanReturn(self)

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
            PERSONNEL_RETURNING_LOAN[username] = [name, user_id, personnel_id, username]
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
                    f"Equipment No:{search_value}is not a library item ",
                )

            elif ASSET["library_status_id"] == "WWW3":
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
            QMessageBox.warning(self, "Equipment search", "Unable to find an Asset!")
            self.ui.lbl_eq_validate.setPixmap(self.error_pixmap)
            # self.ui.lbl_category.setText("")
            self.ui.btn_confirm.setDisabled(True)

    def asset_library_status(self) -> str:
        """By looking at the EquipmentLibrarySatusId it will check
        1 - checks whether an asset is library loan able,
        If so, return library_item
        2 - check if the asset is already on loan
        if so return is on loan
        """
        pass

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
            QMessageBox.information(self, "Equipemnt Loan", " Loan succesfully issued!")
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

    def loan_tab(self):
        self.ui.tabWidget.setEnabled(True)
        if self.ui.rb_create_job.isChecked():
            self.ui.tabWidget.setCurrentIndex(1)
        else:
            self.ui.tabWidget.setCurrentIndex(0)

    def return_loan_create_job(self):
        """makes some checks on the check box, radio buttons for job creation
        and ensures the workdone and reported fault fields are not blank.
        Makes a call to the return loan function of the DB class to return the loan
        and create function if the checkbox has been ticked and work done has been completed.
        if no tick box and nothing in the workdone, asks users if they want to just return the loan
        without creating a job
        """

        work_done = self.ui.txt_work_done.toPlainText()
        reported_fault = self.ui.txt_reported_fault.toPlainText()
        func_chk = self.ui.chkbx_function
        batt_rep = self.ui.chkbx_batt_replace
        vis_inspec = self.ui.chkbx_visual_insp

        repair_job = self.ui.rb_job
        ppm_job = self.ui.rb_ppm
        assigned_tech = self.ui.txt_technician.text()

        if self.ui.tabWidget.currentIndex() == 0:
            job_type_id = JOB_TYPE["Function Check"]
            job_status_id = JOB_STATUS["Completed"]
            if (
                func_chk.isChecked() or batt_rep.isChecked() or vis_inspec.isChecked()
            ) and work_done:
                # if any of the check boxes have been ticket and text in work done,
                # return the device to library and create a functional check job
                # by taking the value from the username field to get the personnel details
                # to be used for the creation of the job
                job = self.db.create_job(
                    job_type_id=job_type_id,
                    job_status_id=job_status_id,
                    equipemnt_id=ASSET["equipment_id"],
                    reported_fault=REPORTED_FAULT,
                    work_end_date=self.today,
                    tech_id=PERSONNEL_RETURNING_LOAN[self.ui.txt_username.text()][2],
                    work_done=work_done,
                    user_id=self.user_id,
                    visual_inspection=vis_inspec.isChecked(),
                    function_check=func_chk.isChecked(),
                    battery_replaced=batt_rep.isChecked(),
                    create_job=True,
                )
                if job:
                    print(f"create job: {job}")

            elif work_done and not (
                func_chk.isChecked() or batt_rep.isChecked() or vis_inspec.isChecked()
            ):
                QMessageBox.information(
                    self, "Loan Return", "At least one check box needs to be checked!"
                )

            elif not work_done and (
                func_chk.isChecked() or batt_rep.isChecked() or vis_inspec.isChecked()
            ):
                QMessageBox.information(
                    self, "Loan Return", "Work done field is emtpy!"
                )
            else:
                msg_box = QMessageBox.question(
                    self,
                    "Loan Return",
                    "Do you want to return loan without creating a Function Check Job?",
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                )
                if msg_box == QMessageBox.StandardButton.Yes:
                    # if user doesn't
                    self.db.create_job(
                        equipemnt_id=ASSET["equipment_id"],
                    )
                    QMessageBox.information(
                        self,
                        "Loan Return",
                        f"Successfully returned equipment: {ASSET['equipment_no']} to the library",
                    )
        else:
            job_status_id = JOB_STATUS["Not Started"]
            assigned_tech = TECHNICIANS[self.ui.txt_technician.text()][0]
            if repair_job.isChecked() and reported_fault and assigned_tech:
                job = self.db.create_job(
                    job_type_id=JOB_TYPE["Repair/Correction"],
                    job_status_id=job_status_id,
                    equipment_id=ASSET["equipment_id"],
                    reported_fault=reported_fault,
                    tech_id=assigned_tech,
                    user_id=self.user_id,
                    create_job=True,
                )
                if job:
                    self.job_sticker["job_number"] = job
                    self.job_sticker["assigned_tech"] = self.ui.txt_technician.text()
                    self.job_sticker["job_type"] = "Repair"
                    self.job_sticker["equipment_no"] = ASSET["equipment_no"]
                    QMessageBox.information(
                        self,
                        "Successful Job Creation",
                        f"A 'Repair Job' with Job number: [{job}] has been created!",
                    )
            elif ppm_job.isChecked() and reported_fault and assigned_tech:
                job_type_id = JOB_TYPE["PPM"]
                job = self.db.create_job(
                    job_status_id=job_status_id,
                    job_type_id=job_type_id,
                    equipment_id=ASSET["equipment_id"],
                    reported_fault=reported_fault,
                    tech_id=assigned_tech,
                    user_id=self.user_id,
                    create_job=True,
                )
                if job:
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
                    "Select a job type, technician and fill in the reported fault box!",
                )

    def print_label(self):
        print(self.job_sticker)

    # create print label by taking the info from the self.job_sticker dictionary


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
