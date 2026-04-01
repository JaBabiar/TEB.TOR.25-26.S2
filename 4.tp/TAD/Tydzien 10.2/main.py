from PyQt6.QtWidgets import QApplication
import sys
import logic
from gui import Okno




if __name__ == "__main__":
    app = QApplication(sys.argv)
    okno = Okno()
    okno.show()
    app.setStyleSheet
    sys.exit(app.exec())