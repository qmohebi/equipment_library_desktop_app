import sys
import re
import time

from PySide6.QtWidgets import QApplication, QMainWindow, QCompleter, QMessageBox
from PySide6.QtGui import QPixmap, Qt

from ui.ui_mainwindow import Ui_MainWindow

from database import Database


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.db = Database()

        self.location_name = []  # used for location auto complete
        self.location = {}  # use for getting location id
        self.location_id = ""
        self.asset = {
            "equipment_no": "",
            "category": "",
            "library_status": "",
            "equipment_id": "",
            "location_id": "",
        }

        self.confirm_pixmap = QPixmap("./ui/confirm_96.png")
        self.error_pixmap = QPixmap("./ui/cancel-96.png")
        self.arrow_pixmap = QPixmap("./ui/arrow.png")
        self.setWindowTitle("Library Loan")

        self.ui.txt_asset.setFocus()
        self.ui.txt_asset.setPlaceholderText("Enter Equipment No")
        self.ui.txt_location.setPlaceholderText("Start typing the location")
        self.ui.btn_validate_eq.clicked.connect(self.get_asset_info)
        self.ui.txt_asset.returnPressed.connect(self.get_asset_info)
        self.ui.btn_validate_loc.clicked.connect(self.validate_location)
        self.ui.txt_location.returnPressed.connect(self.validate_location)
        self.ui.btn_confirm.clicked.connect(self.confirm_loan)
        self.ui.btn_clear.clicked.connect(self.clear)

        self.txt_boxes = (self.ui.txt_asset, self.ui.txt_location)
        self.btns = (
            self.ui.btn_validate_loc,
            self.ui.btn_confirm,
        )
        self.icon_labels = (
            self.ui.lbl_icon_eq,
            self.ui.lbl_icon_loc,
            self.ui.lbl_icon_confirm,
        )
        self.details_lables = (
            self.ui.lbl_category,
            self.ui.lbl_arrow,
            self.ui.lbl_location,
        )
        self.get_location()
        self.disable_buttons()

        completer = QCompleter(self.location_name, self)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.ui.txt_location.setCompleter(completer)

    def get_location(self):
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
                self.asset["library_status"] = row[2]

            self.ui.lbl_icon_eq.setPixmap(self.confirm_pixmap)
            self.ui.lbl_category.setText(self.asset["category"])
            self.ui.lbl_arrow.setPixmap(self.arrow_pixmap)
            self.ui.btn_validate_loc.setDisabled(False)
            self.ui.txt_location.setDisabled(False)
        else:
            self.ui.lbl_icon_eq.setPixmap(self.error_pixmap)
            self.ui.lbl_category.setText("")

    def validate_location(self):
        """Checks to make sure the"""
        loc_inputted = self.ui.txt_location.text().strip()
        try:
            self.asset["location_id"] = self.location[loc_inputted]
            self.ui.lbl_icon_loc.setPixmap(self.confirm_pixmap)
            self.ui.lbl_location.setText(loc_inputted)
            self.ui.btn_confirm.setDisabled(False)
            self.ui.btn_clear.setDisabled(False)
        except KeyError:
            self.ui.lbl_icon_loc.setPixmap(self.error_pixmap)
            self.ui.lbl_location.setText("")

    def confirm_loan(self):
        """issues loan by called the db function"""
        try:
            self.db.issue_loan(
                equipment_id=self.asset["equipment_id"],
                location_id=self.asset["location_id"],
            )
            self.ui.lbl_icon_confirm.setPixmap(self.confirm_pixmap)
            QMessageBox.information(self, "Equipemnt Loan", "Succsefully issued loan!")
        except Exception:
            self.ui.lbl_icon_confirm.setPixmap(self.error_pixmap)

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
