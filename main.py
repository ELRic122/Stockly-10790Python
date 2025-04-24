import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit, QWidget, QVBoxLayout
from  PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

# QMainWindow -  Janela Principal
# QWidget - "Blocos" dentro da janela ex.: botoes, caixas de texto, labels...
# setGeometry(x, y, largura, altura) - define a posição e tamanho da janela
# setStyleSheet - Serve para dar cor e estilo
# connect - Liga um botao a uma funcao

class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__() # serve para inicializar a janela
        self.setWindowTitle('Stockly - Gestao de Inventario') 
        self.setGeometry(70, 50, 1800, 1000) # tamanho da janela

        self.centralWidget = QWidget(self) # cria um widget central
        self.setCentralWidget(self.centralWidget)

        layout = QVBoxLayout(self.centralWidget) # cria um layout vertical dentro do widget central

        # Botoes
        self.button1 = QPushButton('Inserir Registos', self)
        self.button2 = QPushButton('Apagar Registos', self)
        self.button3 = QPushButton('Visualizar Registos', self)
        self.button4 = QPushButton('Alterar Registos', self)

        # Funcoes dos botoes
        self.button1.clicked.connect(lambda: self.label.setText('Inserir Registos'))
        self.button2.clicked.connect(lambda: self.label.setText('Apagar Registos'))
        self.button3.clicked.connect(lambda: self.label.setText('Visualizar Registos'))
        self.button4.clicked.connect(lambda: self.label.setText('Alterar Registos'))

        for btn in [self.button1, self.button2, self.button3, self.button4]:
            btn.setStyleSheet('font-size: 16px; padding: 10px;') # define o estilo dos botoes
            layout.addWidget(btn)

        # Layout no widget central
        self.centralWidget.setLayout(layout)


        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainMenu()
    mainWin.show()
    sys.exit(app.exec_())