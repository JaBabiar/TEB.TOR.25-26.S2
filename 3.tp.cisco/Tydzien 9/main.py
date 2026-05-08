import sys
from PyQt6 import uic, QtWidgets

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("./untitled.ui", self)
        print(self.ui.zglos_btn.clicked.connect(self.zgloszenie))

    def zgloszenie(self):
        dane = {
            "Zglaszajacy": self.ui.textEdit.toPlainText(),
            "Email": self.ui.textEdit_2.toPlainText(),
            "Zglaszany": self.ui.textEdit_3.toPlainText(),
            "Powod":self.ui.textEdit_4.toPlainText()
        }
        with open("./dane.json", "a") as file:
            print(str(dane))
            file.write(str(dane))
            file.write("\n")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("")
    window = MyApp()
    window.show()
    app.exec()