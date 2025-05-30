import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from insertMenuClass import InserirMenu
from deleteMenuClass import ApagarMenu
from viewMenuClass import VisualizarMenu
from alterMenuClass import AlterarMenu

class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Stockly - Gestão de Inventário') 
        
        self.setWindowIcon(QIcon('img/icon.png'))  # Definir ícone da janela
        self.setGeometry(70, 50, 1800, 1000)

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        # Layout principal horizontal
        mainLayout = QHBoxLayout(self.centralWidget)
        mainLayout.setAlignment(Qt.AlignCenter)
        self.centralWidget.setStyleSheet("background-color: #C2C2C2;")  # Cor de fundo

        # Layouts verticais para os botões
        leftLayout = QVBoxLayout()
        rightLayout = QVBoxLayout()

        leftLayout.setAlignment(Qt.AlignVCenter)
        rightLayout.setAlignment(Qt.AlignVCenter)

        # Botões
        self.button1 = QPushButton('INSERIR REGISTOS')
        self.button2 = QPushButton('VISUALIZAR REGISTOS')
        self.button3 = QPushButton('APAGAR REGISTOS')
        self.button4 = QPushButton('ALTERAR REGISTOS')

        # Conectar os botões às funções
        self.button1.clicked.connect(lambda: self.gotoInserirMenu())
        self.button2.clicked.connect(lambda: self.gotoVisualizarMenu())
        self.button3.clicked.connect(lambda: self.gotoApagarMenu())
        self.button4.clicked.connect(lambda: self.gotoAlterarMenu())

        # Estilo dos botões
        style = """
            QPushButton {
                font-size: 26px;
                font-weight: bold;
                padding: 40px;
                background-color: #1E2A38;
                color: white;
                border-radius: 15px;
                min-width: 300px;
                min-height: 50px; 
            }
            QPushButton:hover {
                background-color: #2F3E50;
            }
        """

        for btn in [self.button1, self.button2, self.button3, self.button4]:
            btn.setStyleSheet(style)
        
        
        # Adicionar botões aos layouts
        leftLayout.addWidget(self.button1)
        leftLayout.addSpacing(120)  # Espaço entre botões
        leftLayout.addWidget(self.button2)

        rightLayout.addWidget(self.button3)
        rightLayout.addSpacing(120)
        rightLayout.addWidget(self.button4)

        # Adicionar os layouts ao layout principal
        mainLayout.addLayout(leftLayout)
        mainLayout.addSpacing(450)  # Espaço entre as colunas
        mainLayout.addLayout(rightLayout)

        self.centralWidget.setLayout(mainLayout)

    def gotoInserirMenu(self):
        self.inserirMenu = InserirMenu(self)
        self.inserirMenu.show()
        self.hide()

    def gotoApagarMenu(self):
        self.ApagarMenu = ApagarMenu(self)
        self.ApagarMenu.show()
        self.hide()

    def gotoVisualizarMenu(self):
        self.VisualizarMenu = VisualizarMenu(self)
        self.VisualizarMenu.show()
        self.hide()

    def gotoAlterarMenu(self):
        self.AlterarMenu = AlterarMenu(self)
        self.AlterarMenu.show()
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainMenu()
    mainWin.show()
    sys.exit(app.exec_())

    