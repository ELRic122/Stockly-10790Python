# Bibliotecas 
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

# class AlterarMenu
class AlterarMenu(QMainWindow): 
    def __init__(self, mainMenu_ref): # Construtor da classe
        super().__init__() # Inicializa a classe pai
        self.mainMenu = mainMenu_ref # Referência ao menu principal

        self.setWindowIcon(QIcon('img/icon.png')) # Definir ícone da janela
        self.setWindowTitle('Stockly - Gestão de Inventário') # Definir título da janela
        self.setGeometry(70, 50, 1800, 1000) # Definir tamanho da janela

        self.centralWidget = QWidget(self) # Cria um widget central
        self.setCentralWidget(self.centralWidget) # Define o widget central da janela

        # Layout principal vertical
        fullLayout = QVBoxLayout(self.centralWidget)

        # Layout horizontal no topo (botão voltar à direita)
        topBarLayout = QHBoxLayout()
        topBarLayout.addStretch()

        # Botão voltar
        self.buttonBack = QPushButton('←')
        self.buttonBack.setFixedSize(60, 60)
        self.buttonBack.setStyleSheet("""
            QPushButton {
                font-size: 30px;
                font-weight: bold;
                background-color: transparent;
                color: black;
                border: none;
            }
            QPushButton:hover {
                color: #CCCCCC;
            }
        """)
        # Conectar o botão voltar à função
        self.buttonBack.clicked.connect(self.voltarAoMenu)
        topBarLayout.addWidget(self.buttonBack)

        # Layout horizontal central (botões principais)
        mainLayout = QHBoxLayout()
        mainLayout.setAlignment(Qt.AlignCenter)

        # Layouts para os botões
        leftLayout = QVBoxLayout()
        rightLayout = QVBoxLayout()
        leftLayout.setAlignment(Qt.AlignVCenter)
        rightLayout.setAlignment(Qt.AlignVCenter)

        # Botões principais
        self.button1 = QPushButton('CLIENTES')
        self.button2 = QPushButton('FORNECEDORES')
        self.button3 = QPushButton('STOCK')
        self.button4 = QPushButton('VENDAS')

        # Conectar os botões às funções
        self.button1.clicked.connect(lambda: self.mostrarMensagem("CLIENTES"))  
        self.button2.clicked.connect(lambda: self.mostrarMensagem("FORNECEDORES"))
        self.button3.clicked.connect(lambda: self.mostrarMensagem("STOCK"))
        self.button4.clicked.connect(lambda: self.mostrarMensagem("VENDAS"))
        
        # Estilo dos botões
        buttonStyle = """
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

        # Conectar os botões às funções
        for btn in [self.button1, self.button2, self.button3, self.button4]:
            btn.setStyleSheet(buttonStyle)

        # Adicionar botões aos layouts
        leftLayout.addWidget(self.button1)
        leftLayout.addSpacing(120)
        leftLayout.addWidget(self.button2)

        # Adicionar botões ao layout da direita
        rightLayout.addWidget(self.button3)
        rightLayout.addSpacing(120)
        rightLayout.addWidget(self.button4)

        # Adicionar os layouts ao layout principal
        mainLayout.addLayout(leftLayout)
        mainLayout.addSpacing(450)
        mainLayout.addLayout(rightLayout)

        # Adicionar layouts ao principal
        fullLayout.addLayout(topBarLayout)
        fullLayout.addStretch()
        fullLayout.addLayout(mainLayout)
        fullLayout.addStretch()

        self.centralWidget.setLayout(fullLayout) # Adiciona o layout principal ao widget central

    # Função para voltar ao menu principal
    def voltarAoMenu(self):
        self.mainMenu.show()
        self.close()

    def mostrarMensagem(self, texto):
        print(f"Botão '{texto}' clicado!")
