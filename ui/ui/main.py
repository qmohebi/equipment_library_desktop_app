import sys
import re
import json
from datetime import datetime
import csv
import os

from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QCompleter,
    QMessageBox,
    QDialog,
    QWidget,
    QStatusBar,
)
from PySide6.QtGui import QPixmap, Qt

from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
