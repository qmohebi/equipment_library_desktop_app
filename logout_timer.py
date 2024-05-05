import sys
from PySide6.QtCore import Qt, Signal, QTimer
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
)


from ui_logout_timer import Ui_Dialog


class LogoutTimer(QDialog):
    continue_using_app = Signal()
    logout_user = Signal()

    def __init__(self, parent=None) -> None:
        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.countdown_timer = QTimer()
        self.seconds_remaining = 15*1000
        self.ui.lbl_countdown.setText("0:15")
        self.ui.btn_continue.clicked.connect(self.on_continue_btn_clicked)
        self.ui.btn_logout.clicked.connect(self.on_logout_btn_clicked)

    def start_countdown(self):
        self.reset_timer()
        print(self.seconds_remaining)
        self.countdown_timer.timeout.connect(self.update_countdown)
        self.countdown_timer.start(1000)

    def update_countdown(self):
        self.seconds_remaining -= 1000
        print(f"on start: {self.seconds_remaining//1000}")
        if self.seconds_remaining <= 0:
            # self.countdown_label.setText("Time's up!")
            self.countdown_timer.stop()

            self.logout_user.emit()
            self.close()
        else:
            self.ui.lbl_countdown.setText(f"0:{self.seconds_remaining//1000}")

    def on_continue_btn_clicked(self):
        self.reset_timer()
        self.continue_using_app.emit()
        print(f"On continue: {self.seconds_remaining//1000}")
        self.close()

    def on_logout_btn_clicked(self):
        self.logout_user.emit()
        # self.countdown_timer.stop()
        self.close()

    def closeEvent(self, event):
        self.countdown_timer.stop()
        super().closeEvent(event)

    def reset_timer(self):
        self.countdown_timer.stop()
        self.seconds_remaining = 15 * 1000
        self.countdown_timer.start(1000)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LogoutTimer()
    window.show()
    sys.exit(app.exec())
