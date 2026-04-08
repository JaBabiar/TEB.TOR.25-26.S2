from PyQt6.QtWidgets import QApplication
from gui import Okno, ExitMenu
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Okno()
    window.show()

    sys.exit(app.exec())