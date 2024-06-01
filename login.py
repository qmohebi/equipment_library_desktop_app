import sys

from PySide6.QtWidgets import QApplication, QDialog, QLineEdit
from PySide6.QtGui import QIcon
from PySide6.QtCore import Signal, Qt

from ui_login import Ui_Dialog

from authentication import LDAPAuthentication


class LoginWindow(QDialog):
    login_successfull = Signal(list)

    def __init__(
        self, mpce_staff: dict, ldap_server: str, search_base: str, parent=None
    ) -> None:
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.mpce_member = mpce_staff
        self.ldap_server = ldap_server
        self.search_base = search_base

        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle("Login")

        self.ui.txt_password.setEchoMode(QLineEdit.Password)
        self.ui.txt_password.setPlaceholderText("Enter your password")
        self.ui.txt_username.setPlaceholderText("Enter username")
        self.ui.txt_username.setClearButtonEnabled(True)
        self.ui.txt_password.setClearButtonEnabled(True)

        self.ui.frame_error.hide()
        self.ui.txt_password.setEchoMode(QLineEdit.Password)
        self.ui.txt_username.setFocus()

        # self.ui.btn_login.clicked.connect(lambda: self.ui.frame_error.show())
        self.ui.btn_close_error.clicked.connect(lambda: self.ui.frame_error.hide())

        self.ui.btn_guest.clicked.connect(self.reset_form)
        self.ui.btn_login.clicked.connect(self.on_login_btn_clicked)

        # self.password_txtbox_icon()
        self.ui.txt_password.textChanged.connect(self.password_txtbox_icon)
        self.ui.txt_username.setFocus()

    def password_txtbox_icon(self):
        """update password icon to show or reveal
        the characters typed in the password text box"""
        echo_mode = self.ui.txt_password.echoMode()
        for action in self.ui.txt_password.actions():
            self.ui.txt_password.removeAction(action)

        if echo_mode == QLineEdit.Password:
            self.ui.txt_password.setClearButtonEnabled(False)
            reveal_password = self.ui.txt_password.addAction(
                QIcon(":/eye_show.png"), QLineEdit.TrailingPosition
            )
            reveal_password.triggered.connect(self.password_reveal_hide)
        else:
            self.ui.txt_password.setClearButtonEnabled(False)
            reveal_password = self.ui.txt_password.addAction(
                QIcon(":/eye_hide.png"), QLineEdit.TrailingPosition
            )
            reveal_password.triggered.connect(self.password_reveal_hide)

    def password_reveal_hide(self):
        if self.ui.txt_password.echoMode() == QLineEdit.EchoMode.Password:
            self.ui.txt_password.setEchoMode(QLineEdit.EchoMode.Normal)

        else:
            self.ui.txt_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.password_txtbox_icon()

    def reset_form(self):
        """When user presses on continue as guest,
        clear the form and set to original"""
        self.ui.txt_password.clear()
        self.ui.txt_username.clear()
        self.ui.txt_username.setFocus()
        self.ui.frame_error.hide()
        self.ui.txt_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.close()

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
                self.mpce_member[username_enetered][0],
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
            ldap_server=self.ldap_server, serach_base=self.search_base
        )
        authentiate = ldap_autho.authenticate(username=username, password=password)
        if authentiate is True:
            return True

        else:
            return False

    def mpce_staff(self, username: str) -> bool:
        """check if user is MPCE member"""
        if username in self.mpce_member:
            return True
        else:
            return False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
