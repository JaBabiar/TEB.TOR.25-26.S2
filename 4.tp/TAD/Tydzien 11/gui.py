from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton

class Okno(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("totalnie prawdziwa gra")
        

        # main widget
        central_widget = QWidget()
        # Main Layout
        main_layout = QVBoxLayout()

        title = QLabel("Witaj w Aplikacji")

        self.btn_start = QPushButton("Start")
        self.btn_options = QPushButton("Opcje")
        self.btn_exit = QPushButton("Wyjdż")

        main_layout.addWidget(title)
        main_layout.addWidget(self.btn_start)
        main_layout.addWidget(self.btn_options) 
        main_layout.addWidget(self.btn_exit)      

        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.exit_menu = ExitMenu()

        # Podpisanie akcji do kliknięcia w przycisk exit
        self.btn_exit.clicked.connect(self.show_exit_dialog)

    def show_exit_dialog(self):
        self.exit_menu.show()

    

class ExitMenu(QWidget):

    def __init__(self):
        super().__init__()
        
        self.label = QLabel("Na pewno zamknac ?")
        self.btn_yes = QPushButton("tak")
        self.btn_no = QPushButton("no")

        main_layout = QVBoxLayout()
        controls_layout = QHBoxLayout()

        controls_layout.addWidget(self.btn_yes)
        controls_layout.addWidget(self.btn_no)

        main_layout.addWidget(self.label)
        main_layout.addLayout(controls_layout)
        self.setLayout(main_layout)
        self.btn_yes.clicked.connect(self.quit_app)
        self.btn_no.clicked.connect(self.close_dialog)

    def quit_app(self):
        QApplication.quit()
    def close_dialog(self):
        self.close()

    pass