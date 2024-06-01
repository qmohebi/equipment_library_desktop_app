import sys

from PySide6.QtWidgets import QCompleter, QDialog, QMessageBox
from PySide6.QtCore import Signal, Qt

from ui_assign_tech_window import Ui_Dialog

from database import Database


class AssignTech(QDialog):
    # technician = Signal(str)
    # job_number = Signal(str)
    job_created = Signal(list)

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

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui.txt_technician.setPlaceholderText("Start typing technician's name")
        self.ui.txt_reported_fault.setPlaceholderText("Enter reported fault")

        auto_completer = QCompleter(list(technicians.keys()))
        auto_completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.ui.txt_technician.setCompleter(auto_completer)
        self.ui.txt_technician.setClearButtonEnabled(True)
        self.ui.btn_confirm.clicked.connect(self.on_confirm_clicked)
        self.ui.btn_cancel.clicked.connect(self.on_cancel_clicked)

    def on_confirm_clicked(self) -> str:
        """Create a repair or ppm job"""
        # assigned_tech_id = self.technician[self.ui.txt_technician.text()]
        self.reported_fault = self.ui.txt_reported_fault.toPlainText()
        self.technician_id = self.technicians[self.ui.txt_technician.text()][0]
        
        self.db.return_loan(equipment_id=self.equipment_id)

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
            return_value = [job, self.ui.txt_technician.text()]
            print(return_value)
            self.job_created.emit(return_value)
            # self.technician.emit(self.ui.txt_technician.text())
            # self.job_number.emit(str(job))
            QMessageBox.information(
                self,
                "Loan Return",
                f"Loan returned and a Function Job created, job no: {job}",
            )

            self.hide()
        else:
            QMessageBox.warning(self, "Loan Return", "Unable to create job")

    def on_cancel_clicked(self):
        self.ui.txt_reported_fault.clear()
        self.ui.txt_reported_fault.clear()
        self.hide()
