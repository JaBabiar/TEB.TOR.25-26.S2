from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout
import sys 
from gra import Postac
class Okno(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gra RPG")

        self.enemy = Postac("żerard", 150)
        self.label = QLabel(self.enemy.status())
        self.btn = QPushButton("ATK")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.btn)

        
        self.centerBox = QWidget()
        self.centerBox.setLayout(self.layout)
        self.setCentralWidget(self.centerBox)

        ## Style
        self.centerBox.setStyleSheet("background: #ff3512; font-size:24px")
        self.btn.setStyleSheet("padding: 8px 12px; background: #ff1111")

        ## Sygnały 
        self.btn.clicked.connect(self.zadaj_dmg)

    def zadaj_dmg(self):
        nowe_hp = self.enemy.otrzymaj_obrazenia(6.7)
        self.label.setText(self.enemy.status())
        if nowe_hp == 0:
            self.label.setText("Przegrales")
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    okno = Okno()
    okno.show()
    sys.exit(app.exec())