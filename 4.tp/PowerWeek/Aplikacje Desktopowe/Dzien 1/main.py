import sys
from PyQt6 import uic, QtWidgets

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("untitled.ui", self)

        ## Definicja Akcji
        self.count = 0
        self.btn_test.clicked.connect(self.zmiana_tekstu)
        self.atack_btn.clicked.connect(self.atack_action)

    def zmiana_tekstu(self):
        self.btn_test.setText(f"Mango {self.count}")
        self.count += 1
    def atack_action(self):
        print("atack")
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    app.exec()