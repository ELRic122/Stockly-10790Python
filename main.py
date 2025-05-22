# Bibliotecas
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
# Importar classes de outros módulos
from insertMenuClass import InserirMenu
from deleteMenuClass import ApagarMenu
from viewMenuClass import VisualizarMenu
from alterMenuClass import AlterarMenu

# Classe do menu principal
class MainMenu(QMainWindow):
    # Construtor da classe
    def __init__(self):
        super().__init__() # Inicializa a classe pai
        self.setWindowTitle('Stockly - Gestão de Inventário')  # Definir título da janela
        self.setWindowIcon(QIcon('img/icon.png'))  # Definir ícone da janela
        self.setGeometry(70, 50, 1800, 1000) # Definir tamanho da janela

        self.centralWidget = QWidget(self) # Cria um widget central
        self.setCentralWidget(self.centralWidget) # Define o widget central da janela
        self.centralWidget.setStyleSheet("background-color: #C2C2C2;")  # Cor de fundo

        # Layout principal horizontal
        mainLayout = QHBoxLayout(self.centralWidget)
        mainLayout.setAlignment(Qt.AlignCenter)

        # Layouts verticais para os botões
        leftLayout = QVBoxLayout()
        rightLayout = QVBoxLayout()
        
        # Definir alinhamento dos layouts
        leftLayout.setAlignment(Qt.AlignVCenter)
        rightLayout.setAlignment(Qt.AlignVCenter)

        # Botões principais
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

        # Aplicar estilo aos botões
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

        # Adicionar layout principal ao widget central
        self.centralWidget.setLayout(mainLayout)

    # Função para ir para o menu de inserir
    def gotoInserirMenu(self):
        self.inserirMenu = InserirMenu(self)
        self.inserirMenu.show()
        self.hide()

    # Função para ir para o menu de apagar
    def gotoApagarMenu(self):
        self.ApagarMenu = ApagarMenu(self)
        self.ApagarMenu.show()
        self.hide()

    # Função para ir para o menu de visualizar
    def gotoVisualizarMenu(self):
        self.VisualizarMenu = VisualizarMenu(self)
        self.VisualizarMenu.show()
        self.hide()

    # Função para ir para o menu de alterar
    def gotoAlterarMenu(self):
        self.AlterarMenu = AlterarMenu(self)
        self.AlterarMenu.show()
        self.hide()

# Função principal para executar o aplicativo
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainMenu()
    mainWin.show()
    sys.exit(app.exec_())