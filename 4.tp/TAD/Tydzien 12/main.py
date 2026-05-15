from PyQt6 import QtWidgets, uic
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi('./untitled.ui', self)

        self.ui.login_btn.clicked.connect(self.loginUser)

    def loginUser(self):
        print(f"Zalogowano jako {self.ui.login.text()} za pomocą hasła {self.ui.pwd.text()}" )
        
if "__main__" == __name__:
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('fusion')
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

