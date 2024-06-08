import sys

from PySide6.QtWidgets import QCompleter, QDialog, QMessageBox
from PySide6.QtCore import Signal, Qt

from ui_assign_tech_window import Ui_Dialog

from database import Database


class AssignTech(QDialog):
    # technician = Signal(str)
    close_buton_clicked = Signal(bool)
    job_created = Signal(str)

    def __init__(
        self,
        technicians: dict,
        parent=None,
    ) -> None:
        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.db = Database()
        self.technicians = technicians
        self.equipment_id = ""
        self.job_type_id = ""
        self.job_status_id = ""
        self.taken_by_id = ""
        self.user_id = ""
        self.job_type = ""
        # capture if dialogue is opend by accident,
        #  use this signal to clear radio button in main window

        # self.job_created.emit(False)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui.txt_technician.setPlaceholderText("Start typing technician's name")
        self.ui.txt_reported_fault.setPlaceholderText("Enter reported fault")
        self.ui.lbl_title.setText(f"Create {self.job_type} Job")
        auto_completer = QCompleter(list(technicians.keys()))
        auto_completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.ui.txt_technician.setCompleter(auto_completer)
        self.ui.txt_technician.setClearButtonEnabled(True)
        self.ui.btn_confirm.clicked.connect(self.on_confirm_clicked)
        self.ui.btn_close.clicked.connect(self.on_close_clicked)

        self.ui.btn_print.clicked.connect(self.print_job_sticker)

        self.text_fields = (
            self.ui.txt_job_number,
            self.ui.txt_reported_fault,
            self.ui.txt_technician,
        )

    def on_confirm_clicked(self) -> list:
        """Create a repair or ppm job"""
        # assigned_tech_id = self.technician[self.ui.txt_technician.text()]
        try:
            self.reported_fault = self.ui.txt_reported_fault.toPlainText()
            self.technician_id = self.technicians[self.ui.txt_technician.text()][0]
        except KeyError:
            QMessageBox.warning(
                self,
                f"Creating {self.job_type} job",
                "Technician field is mandatory!",
            )
        if not self.reported_fault:
            self.reported_fault = "Unit due for PPM"
        # self.db.return_loan(equipment_id=self.equipment_id)
        if self.job_type == "repair":
            if not (self.reported_fault):
                QMessageBox.warning(
                    self,
                    f"Creating {self.job_type} job",
                    "Reported fault is mandatory!",
                )
        else:
            job = self.db.create_job(
                equipment_id=self.equipment_id,
                job_type_id=self.job_type_id,
                job_status_id=self.job_status_id,
                reported_fault=self.ui.txt_reported_fault.toPlainText(),
                tech_id=self.technician_id,
                user_id=self.user_id,
                taken_by_id=self.taken_by_id,
            )
            if job:
                # return_value = [job, self.ui.txt_technician.text()]
                # self.job_created.emit(return_value)
                # self.technician.emit(self.ui.txt_technician.text())
                # self.job_number.emit(str(job))
                QMessageBox.information(
                    self,
                    f"Creating {self.job_type} job",
                    f"Created a {self.job_type} job with job no: {job}",
                )
                self.ui.txt_job_number.setText(str(job))
                self.job_created.emit("yes")
            else:
                QMessageBox.warning(self, "Loan Return", "Unable to create job")

    def print_job_sticker(self) -> None:
        # TODO Create/desgin the ZPL code, send to Zebra printer
        # TODO collet the information needed to send to printer
        pass

    def on_close_clicked(self):
        """Clear the form and hide the dialogue"""
        for textbox in self.text_fields:
            textbox.clear()
        self.hide()
