import sys

from PySide6.QtWidgets import QApplication, QDialog, QToolButton, QLineEdit
from PySide6.QtGui import QIcon

from ui_login import Ui_Dialog


class LoginWindow(QDialog):

    def __init__(self, parent=None) -> None:
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.txt_password.setEchoMode(QLineEdit.Password)
        self.ui.txt_password.setPlaceholderText("Enter your password")
        self.ui.txt_username.setClearButtonEnabled(True)
        self.ui.txt_password.setClearButtonEnabled(True)

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
                QIcon(":/eye_hide.png"), QLineEdit.TrailingPosition
            )
            reveal_password.triggered.connect(self.password_reveal_hide)
        else:
            self.ui.txt_password.setClearButtonEnabled(False)
            reveal_password = self.ui.txt_password.addAction(
                QIcon(":/eye_show.png"), QLineEdit.TrailingPosition
            )
            reveal_password.triggered.connect(self.password_reveal_hide)

    def password_reveal_hide(self):
        if self.ui.txt_password.echoMode() == QLineEdit.EchoMode.Password:
            self.ui.txt_password.setEchoMode(QLineEdit.EchoMode.Normal)

        else:
            self.ui.txt_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_txtbox_icon()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
