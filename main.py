import sys
import re
from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QCompleter,
    QMessageBox,
    QDialog,
    QWidget,
)
from PySide6.QtGui import QPixmap, Qt

from ui.ui_mainwindow import Ui_MainWindow
from ui.ui_dialogue import Ui_Dialog

from database import Database


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
        self.asset = {
            "equipment_no": "",
            "category": "",
            "library_status_id": "",
            "equipment_id": "",
            "location_id": "",
            "loan_location": "",
            "loan_status_id": "",
        }

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

        completer = QCompleter(self.location_name, self)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.ui.txt_location.setCompleter(completer)

    def get_location(self):
        """get the location from database and create a list and dictionary
        lis to be used for autocompleting the location text box and
        dictionary for get the location_id"""
        location = self.db.get_location()
        self.location = location
        self.location_name = list(location.keys())

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
                self.asset["equipment_id"] = row[0]
                self.asset["category"] = row[1]
                self.asset["library_status_id"] = row[2]
                self.asset["loan_status_id"] = row[3]
                self.asset["loan_location"] = row[4]
            if self.asset["library_status_id"] == "WWW1":
                QMessageBox.warning(
                    self,
                    "Equipment",
                    f"Equipment No: {self.ui.txt_asset.text()}\n"
                    "Is not a library item ",
                )
                self.ui.lbl_eq_validate.setPixmap(self.error_pixmap)
            elif self.asset["library_status_id"] == "WWW3":
                dlg = LoanReturn(self)
                dlg.ui.label_2.setText(f"This Equpment is on loan to {self.asset['loan_location']} select from options below")
                dlg.exec()
            else:

                self.ui.lbl_eq_validate.setPixmap(self.confirm_pixmap)
                self.ui.lbl_category.setText(self.asset["category"])
                self.ui.lbl_arrow.setPixmap(self.arrow_pixmap)
                self.ui.btn_validate_loc.setDisabled(False)
                self.ui.txt_location.setDisabled(False)
                self.ui.txt_location.setFocus()
        else:
            QMessageBox.warning(
                self, "Equipment search", "Unable to find an Asset!"
            )
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
            self.asset["location_id"] = self.location[loc_inputted]
            self.ui.lbl_loc_validate.setPixmap(self.confirm_pixmap)
            self.ui.lbl_location.setText(loc_inputted)
            self.ui.btn_confirm.setDisabled(False)
            self.ui.btn_clear.setDisabled(False)
            self.ui.lbl_confirm_info.setVisible(True)
            self.ui.lbl_3.setVisible(True)
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
                equipment_id=self.asset["equipment_id"],
                location_id=self.asset["location_id"],
            )
            self.ui.lbl_confirm_icon.setPixmap(self.confirm_pixmap)
            QMessageBox.information(self, "Equipemnt Loan", "Succsefully issued loan!")
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


class LoanReturn(QDialog):
    """Loan return dialog"""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.check)
        

    def check(self):
        print("Clear clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
