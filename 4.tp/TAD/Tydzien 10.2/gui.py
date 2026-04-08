from PyQt6.QtWidgets import QMainWindow, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout
from PyQt6.QtCore import Qt

class Okno(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FNAF TEB")

        ## Definicja Bloku 
        self.mainWidget = QWidget()
        self.titleScreen = QLabel("Five Night's At Teb")
        self.nameField = QLineEdit()
        
        self.gameWidget = QWidget()
        self.close_left_btn = QPushButton("Close Left Door")
        self.close_right_btn = QPushButton("Close Right Door")


        ## Definicja Układu 
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.titleScreen)
        self.titleScreen.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mainLayout.addWidget(self.nameField)
        self.setCentralWidget(self.mainWidget)
        self.mainWidget.setLayout(self.mainLayout)


        self.gameLayout = QHBoxLayout()
        self.gameWidget.setLayout(self.gameLayout)
        self.gameLayout.addWidget(self.close_left_btn)
        self.gameLayout.addWidget(self.close_right_btn)
        
        
        self.set_style()
        
       
        ### Podpisanie Akcji
        self.nameField.textEdited.connect(self.name_input)
        self.close_left_btn.clicked.connect(self.left_door)
        self.close_right_btn.clicked.connect(self.right_door)

    def set_style(self):
        self.mainWidget.setStyleSheet("""
        QWidget{
            background: #121212;
            color: #fefefe;
            padding:20px;
        }                              
        """)
        self.titleScreen.setStyleSheet("""
        QLabel{
            font-size: 32px;
            color: #fefefe;
        }
        """
        )
        self.nameField.setStyleSheet("""
        QLineEdit {
        background : #222;
        color: #fefefe;
        padding: 5px 10px }                      
        """)

    def name_input(self):
        if self.nameField.text() == "Gouomb":
            self.setCentralWidget(self.gameWidget)

    def left_door():
        pass

    def right_door():
        pass