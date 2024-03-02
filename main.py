import sys
import re

from PySide6.QtWidgets import QApplication, QMainWindow, QCompleter
from PySide6.QtGui import QIcon, QPixmap, Qt


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
            "location_id": ""
        }

        self.confirm_pixmap = QPixmap("./ui/confirm-96.png")
        self.error_pixmap = QPixmap("./ui/cancel-96.png")

        self.ui.txt_asset.setFocus()
        self.ui.txt_asset.setPlaceholderText("Enter Asset No")
        self.ui.txt_location.setPlaceholderText("Start typing the location")
        self.ui.btn_validate_eq.clicked.connect(self.get_asset_info)
        self.ui.btn_validate_loc.clicked.connect(self.validate_location)
        self.ui.bt_confirm.clicked.connect(self.confirm_loan)

        self.get_location()

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

        else:
            self.ui.lbl_icon_eq.setPixmap(self.error_pixmap)

    def validate_location(self):
        loc_inputted = self.ui.txt_location.text()
        try:
            self.asset["location_id"] = self.location[loc_inputted]
            self.ui.lbl_icon_loc.setPixmap(self.confirm_pixmap)
            print(self.location[loc_inputted])

            label_text = f"""
            Taking: {self.asset['category']} to: {loc_inputted}"""
            self.ui.lbl_details.setText(label_text)
        except KeyError:
            print("Incorrect location")
            self.ui.lbl_icon_loc.setPixmap(self.error_pixmap)

    def confirm_loan(self):
        try:
            self.db.issue_loan(
                equipment_id=self.asset["equipment_id"],
                location_id=self.asset["location_id"])
        except Exception:
            self.ui.lbl_icon_confirm.setPixmap(self.error_pixmap)

    def clear(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
