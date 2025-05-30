from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from viewClientsClass import VisualizarClientes
from viewSuppliersClass import VisualizarFornecedores
from viewStockClass import VisualizarStock
from viewSalesClass import Visualizarvendas

class VisualizarMenu(QMainWindow):
    def __init__(self, mainMenu_ref):
        super().__init__()
        self.mainMenu = mainMenu_ref

        self.setWindowIcon(QIcon('img/icon.png'))
        self.setWindowTitle('Stockly - Menu de Vizualizar Registos') 
        self.setGeometry(70, 50, 1800, 1000)

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setStyleSheet("background-color: #C2C2C2;")  # Cor de fundo

        # Layout principal vertical
        fullLayout = QVBoxLayout(self.centralWidget)

        # Layout horizontal no topo (botão voltar à direita)
        topBarLayout = QHBoxLayout()
        topBarLayout.addStretch()

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
        self.buttonBack.clicked.connect(self.voltarAoMenu)
        topBarLayout.addWidget(self.buttonBack)

        # Layout horizontal central (botões principais)
        mainLayout = QHBoxLayout()
        mainLayout.setAlignment(Qt.AlignCenter)

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
        self.button1.clicked.connect(lambda: self.gotoVisualizarClientes())
        self.button2.clicked.connect(lambda: self.gotoVisualizarFornecedores())
        self.button3.clicked.connect(lambda: self.gotoVisualizarStock())
        self.button4.clicked.connect(lambda: self.gotoVisualizarVendas())
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
        for btn in [self.button1, self.button2, self.button3, self.button4]:
            btn.setStyleSheet(buttonStyle)

        # Adicionar botões aos layouts
        leftLayout.addWidget(self.button1)
        leftLayout.addSpacing(120)
        leftLayout.addWidget(self.button2)

        rightLayout.addWidget(self.button3)
        rightLayout.addSpacing(120)
        rightLayout.addWidget(self.button4)

        mainLayout.addLayout(leftLayout)
        mainLayout.addSpacing(450)
        mainLayout.addLayout(rightLayout)

        # Adicionar layouts ao principal
        fullLayout.addLayout(topBarLayout)
        fullLayout.addStretch()
        fullLayout.addLayout(mainLayout)
        fullLayout.addStretch()

        self.centralWidget.setLayout(fullLayout)

    def voltarAoMenu(self):
        self.mainMenu.show()
        self.close()

    def gotoVisualizarClientes(self):
        self.VizualizarClientes = VisualizarClientes(self)
        self.VizualizarClientes.show()
        self.hide()

    def gotoVisualizarFornecedores(self):
        self.VizualizarFornecedores = VisualizarFornecedores(self)
        self.VizualizarFornecedores.show()
        self.hide()

    def gotoVisualizarStock(self):
        self.VizualizarStock = VisualizarStock(self)
        self.VizualizarStock.show()
        self.hide()
    
    def gotoVisualizarVendas(self):
        self.VizualizarVendas = Visualizarvendas(self)
        self.VizualizarVendas.show()
        self.hide()