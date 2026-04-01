class Okno(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("⚔️ Menedżer Bohatera")
        self.resize(500, 400)
        
        self.bohater = Postac("Geralt", 100)
        
        self.centralWidget = QWidget()
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setSpacing(20)
        self.mainLayout.setContentsMargins(40, 40, 40, 40)
        
        self.etkieta_statusu = QLabel(self.bohater.get_status())
        self.etkieta_statusu.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.etkieta_statusu.setFixedHeight(50)
        
        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setSpacing(15)
        
        self.btn_obrazenia = QPushButton("⚔️ Obrażenia")
        self.btn_leczenie = QPushButton("🧪 Ulecz")
        self.btn_zloto = QPushButton("💰 Złoto")
        
        self.buttonsLayout.addWidget(self.btn_obrazenia)
        self.buttonsLayout.addWidget(self.btn_leczenie)
        self.buttonsLayout.addWidget(self.btn_zloto)
        
        self.mainLayout.addWidget(self.etkieta_statusu)
        self.mainLayout.addLayout(self.buttonsLayout)
        
        self.centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.centralWidget)
        
        self.btn_obrazenia.clicked.connect(self.akcja_obrazenia)
        self.btn_leczenie.clicked.connect(self.akcja_leczenie)
        self.btn_zloto.clicked.connect(self.akcja_zloto)
        
        self.zastosuj_style()
    
    def zastosuj_style(self):
        self.etkieta_statusu.setStyleSheet("""
            QLabel {
                background-color: #f0f0f0;
                border-radius: 10px;
                padding: 10px;
                font-size: 18px;
                font-weight: bold;
                color: #333333;
                border: 2px solid #dddddd;
            }
        """)
        
        btn_style = """
            QPushButton {{
                background-color: {color};
                border: none;
                border-radius: 15px;
                padding: 20px;
                font-size: 16px;
                font-weight: bold;
                color: white;
                min-width: 120px;
            }}
            QPushButton:hover {{
                background-color: {hover_color};
            }}
            QPushButton:pressed {{
                background-color: {pressed_color};
            }}
            QPushButton:disabled {{
                background-color: #cccccc;
                color: #666666;
            }}
        """
        
        self.btn_obrazenia.setStyleSheet(btn_style.format(
            color="#e74c3c", hover_color="#c0392b", pressed_color="#922b21"
        ))
        self.btn_leczenie.setStyleSheet(btn_style.format(
            color="#27ae60", hover_color="#1e8449", pressed_color="#145a32"
        ))
        self.btn_zloto.setStyleSheet(btn_style.format(
            color="#f39c12", hover_color="#d68910", pressed_color="#9a7d0a"
        ))
        
        self.centralWidget.setStyleSheet("QWidget { background-color: #ffffff; }")
    
    def akcja_obrazenia(self):
        wynik = self.bohater.otrzymaj_obrazenia(10)
        self.aktualizuj_wyswietlanie()
        if wynik == 0:
            QMessageBox.critical(self, "Koniec Gry", "Twój bohater zginął!")
            self.zablokuj_przyciski()
    
    def akcja_leczenie(self):
        self.bohater.ulecz(20)
        self.aktualizuj_wyswietlanie()
    
    def akcja_zloto(self):
        self.bohater.zbierz_zloto(50)
        self.aktualizuj_wyswietlanie()
    
    def aktualizuj_wyswietlanie(self):
        self.etkieta_statusu.setText(self.bohater.get_status())
    
    def zablokuj_przyciski(self):
        self.btn_obrazenia.setEnabled(False)
        self.btn_leczenie.setEnabled(False)
        self.btn_zloto.setEnabled(False)
