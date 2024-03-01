import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtGui import QIcon, QPixmap


from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.txt_asset.setFocus()
        self.ui.txt_asset.setPlaceholderText("Enter Asset No")
        self.ui.txt_location.setPlaceholderText("Enter location")
        self.ui.btn_validate_eq.clicked.connect(self.validate_search_value)

    def validate_search_value(
            self,) -> bool:
        
        equipment_confirm_pixmap = QPixmap("./confirm-96.png")

        self.ui.lbl_icon_eq.setPixmap(equipment_confirm_pixmap)

    def issue_loan(self):
        pass

    def clear(self):
        pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

