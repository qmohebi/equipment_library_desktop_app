import sys
import json
from PySide6.QtCore import Qt, Signal, QTimer
from PySide6.QtWidgets import QApplication, QDialog, QLineEdit


from ui_login import Ui_Dialog

from authentication import LDAPAuthentication

with open("config.json", encoding="utf-8") as config:
    data = json.load(config)
    REPORTED_FAULT = data["reported_fault"]
    DB_NAME = data["database"]
    LDAP_SERVER = data["ldap_server"]
    SEARCH_BASE = data["search_base"]
    BATTERY_REPORT = data["battery_report"]


class LoginWindow(QDialog):
    login_successfull = Signal(list)

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
            return_value = [
                PERSONNEL_RETURNING_LOAN[username_enetered][0],
                username_enetered,
            ]
            self.login_successfull.emit(return_value)
            self.ui.txt_password.clear()
            self.ui.txt_username.clear()
            self.ui.txt_username.setFocus()
            self.ui.frame_error.hide()
            self.close()

    def authenticate_user(self, username: str, password: str) -> bool:
        """takes username and password and authenticates to AD
        returns true if the given username and password pass, else return false"""
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
