from PyQt6.QtWidgets import QApplication
from gui import Okno
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    okno = Okno()
    okno.show()
    sys.exit(app.exec())