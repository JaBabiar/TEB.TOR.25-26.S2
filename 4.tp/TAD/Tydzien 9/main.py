from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, 
                             QPushButton, QWidget, QVBoxLayout, 
                             QHBoxLayout, QMessageBox)
from PyQt6.QtCore import Qt
from logic import Postac
from gui import Okno
import sys


# =============================================================================
# BLOK 3: START
# =============================================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    okno = Okno()
    okno.show()
    sys.exit(app.exec())