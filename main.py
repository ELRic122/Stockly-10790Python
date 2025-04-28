import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt

# QMainWindow -  Janela Principal
# QWidget - "Blocos" dentro da janela ex.: botoes, caixas de texto, labels...
# setGeometry(x, y, largura, altura) - define a posição e tamanho da janela
# setStyleSheet - Serve para dar cor e estilo
# connect - Liga um botao a uma funcao

class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Stockly - Gestão de Inventário') 
        self.setGeometry(70, 50, 1800, 1000)

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        # Layout principal horizontal
        mainLayout = QHBoxLayout(self.centralWidget)
        mainLayout.setAlignment(Qt.AlignCenter)

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
        self.button2.clicked.connect(lambda: self.mostrarMensagem("VISUALIZAR REGISTOS"))
        self.button3.clicked.connect(lambda: self.mostrarMensagem("APAGAR REGISTOS"))
        self.button4.clicked.connect(lambda: self.mostrarMensagem("ALTERAR REGISTOS"))

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
        self.inserirMenu = InserirMenu()
        self.inserirMenu.show()
        self.hide()

class InserirMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainMenu = MainMenu  # Guardar referência ao menu principal
        self.setWindowTitle('Stockly - Gestão de Inventário') 
        self.setGeometry(70, 50, 1800, 1000)

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        # Layout principal horizontal
        mainLayout = QHBoxLayout(self.centralWidget)
        mainLayout.setAlignment(Qt.AlignCenter)

        # Layouts verticais para os botões
        leftLayout = QVBoxLayout()
        rightLayout = QVBoxLayout()

        leftLayout.setAlignment(Qt.AlignVCenter)
        rightLayout.setAlignment(Qt.AlignVCenter)

        # Botões
        self.button1 = QPushButton('CLIENTES')
        self.button2 = QPushButton('FORNECEDORES')
        self.button3 = QPushButton('STOCK')
        self.button4 = QPushButton('VENDAS')
        self.buttonBack = QPushButton('VOLTAR')

        # Conectar os botões às funções
        self.button1.clicked.connect(lambda: self.mostrarMensagem("CLIENTES"))
        self.button2.clicked.connect(lambda: self.mostrarMensagem("FORNECEDORES"))
        self.button3.clicked.connect(lambda: self.mostrarMensagem("STOCK"))
        self.button4.clicked.connect(lambda: self.mostrarMensagem("VENDAS"))
        self.buttonBack.clicked.connect(self.voltarAoMenu)

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

        backStyle = """
            QPushButton {
                font-size: 22px;
                font-weight: bold;
                padding: 20px;
                background-color: #A93226;
                color: white;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #C0392B;
            }
        """

        for btn in [self.button1, self.button2, self.button3, self.button4]:
            btn.setStyleSheet(style)
        self.buttonBack.setStyleSheet(backStyle)

    
        # Adicionar botões aos layouts
        leftLayout.addWidget(self.button1)
        leftLayout.addSpacing(120)  # Espaço entre botões
        leftLayout.addWidget(self.button2)

        rightLayout.addWidget(self.button3)
        rightLayout.addSpacing(120)
        rightLayout.addWidget(self.button4)

        # Adicionar o botão "VOLTAR" abaixo dos outros botões
        mainLayout.addSpacing(50)  # Espaço entre os botões e o botão voltar
        mainLayout.addWidget(self.buttonBack, alignment=Qt.AlignCenter)

        # Adicionar os layouts ao layout principal
        mainLayout.addLayout(leftLayout)
        mainLayout.addSpacing(450)  # Espaço entre as colunas
        mainLayout.addLayout(rightLayout)

        self.centralWidget.setLayout(mainLayout)

    def voltarAoMenu(self):
        self.mainMenu.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainMenu()
    mainWin.show()
    sys.exit(app.exec_())
