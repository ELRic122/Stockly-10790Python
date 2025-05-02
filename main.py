import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QMessageBox, QTableWidgetItem, QTableWidget, QHeaderView, QLineEdit, QFrame
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt
import mysql.connector

# QMainWindow -  Janela Principal
# QWidget - "Blocos" dentro da janela ex.: botoes, caixas de texto, labels...
# setGeometry(x, y, largura, altura) - define a posição e tamanho da janela
# setStyleSheet - Serve para dar cor e estilo
# connect - Liga um botao a uma funcao

def conectarBD():
    conn = None
    try:
        conn = mysql.connector.connect(user='root', host='localhost', database='stockly', autocommit=True)
        return conn
    except mysql.connector.Error as error:
        print(f"Erro ao conectar a base da dados. [{error}]")
        return None

class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Stockly - Gestão de Inventário') 
        self.setWindowIcon(QIcon('icon.png'))  # Definir ícone da janela
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
        self.inserirMenu = InserirMenu()
        self.inserirMenu.show()
        self.hide()

    def gotoApagarMenu(self):
        self.inserirMenu = ApagarMenu()
        self.inserirMenu.show()
        self.hide()

    def gotoVisualizarMenu(self):
        self.inserirMenu = VisualizarMenu()
        self.inserirMenu.show()
        self.hide()

    def gotoAlterarMenu(self):
        self.inserirMenu = VisualizarMenu()
        self.inserirMenu.show()
        self.hide()
    
class InserirMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainMenu = MainMenu  # Agora é a instância verdadeira
        self.setWindowIcon(QIcon('icon.png'))  # Definir ícone da janela
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

        # Aplicando o estilo aos botões
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

    def mostrarMensagem(self, texto):
        print(f"Botão '{texto}' clicado!")  # Coloca aqui uma MessageBox se quiseres

class ApagarMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainMenu = MainMenu  # Guardar referência ao menu principal
        self.setWindowIcon(QIcon('icon.png'))  # Definir ícone da janela
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

class VisualizarMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainMenu = MainMenu  # Guardar referência ao menu principal
        self.setWindowIcon(QIcon('icon.png'))  # Definir ícone da janela
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
        self.button1.clicked.connect(lambda: self.gotoVisualizarClientes())
        self.button2.clicked.connect(lambda: self.gotoVisualizarFornecedores())
        self.button3.clicked.connect(lambda: self.gotoVisualizarStock())
        self.button4.clicked.connect(lambda: self.gotoVisualizarVendas())
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

    def gotoVisualizarClientes(self):
        self.VizualizarClientes = VisualizarClientes()
        self.VizualizarClientes.show()
        self.hide()

    def gotoVisualizarFornecedores(self):
        self.VizualizarFornecedores = VisualizarFornecedores()
        self.VizualizarFornecedores.show()
        self.hide()

    def gotoVisualizarStock(self):
        self.VizualizarStock = VisualizarStock()
        self.VizualizarStock.show()
        self.hide()
    
    def gotoVisualizarVendas(self):
        self.VizualizarVendas = Visualizarvendas()
        self.VizualizarVendas.show()
        self.hide()

class VisualizarClientes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Stockly - Gestão de Inventário')
        self.setGeometry(70, 50, 1800, 1000)
        self.setWindowIcon(QIcon('icon.png'))
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        layout = QVBoxLayout()

        # Criar um layout horizontal para a barra de pesquisa
        barra_layout = QHBoxLayout()
        barra_layout.setAlignment(Qt.AlignCenter)

        frame_pesquisa = QFrame()
        frame_pesquisa.setFixedSize(420, 40)
        frame_pesquisa.setStyleSheet("background-color: transparent;")
        
        self.pesquisa = QLineEdit(frame_pesquisa)
        self.pesquisa.setPlaceholderText("Pesquisar...")
        self.pesquisa.setGeometry(0, 0, 420, 40)
        self.pesquisa.setStyleSheet("""
            QLineEdit {
                border: 2px solid #1e2c3a;
                border-radius: 10px;
                padding-left: 10px;
                padding-right: 35px;
                background-color: #112233;
                color: white;
                font-size: 16px;
            }
        """)

        lupa = QPushButton(frame_pesquisa)
        lupa.setIcon(QIcon("lupa.png"))
        lupa.setCursor(Qt.PointingHandCursor)
        lupa.setGeometry(380, 5, 30, 30)
        lupa.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
            }
        """)

        barra_layout.addWidget(frame_pesquisa)
        layout.addSpacing(50)  # Espaço acima da barra para melhor centralização
        layout.addLayout(barra_layout)
        layout.addSpacing(20)

        self.tabela = QTableWidget()
        self.tabela.setColumnCount(5)
        self.tabela.setHorizontalHeaderLabels(["ID Cliente","NOMES", "CONTACTOS", "DATA NASCIMENTO", "MORADA"])
        self.tabela.verticalHeader().setDefaultSectionSize(40)  # Altura fixa das linhas
        self.tabela.horizontalHeader().setStyleSheet("""
                QHeaderView::section {
                background-color: #3c3c3c;
                color: white;
                font-weight: bold;
                border: none;
                padding: 6px;
                font-size: 16px;    }
                """)
        
        self.tabela.setStyleSheet("""
            QTableWidget {
                background-color: #2b2b2b;
                color: white;
                gridline-color: #444;
                font-size: 14px;
            }
            QTableWidget::item:selected {
                background-color: #505050;
            }
        """)

        self.tabela.verticalHeader().setVisible(False)
        self.tabela.setFont(QFont("inter", 12))
        self.tabela.setEditTriggers(QTableWidget.NoEditTriggers)

        layout.addWidget(self.tabela, stretch=1)  # Permite expansão da tabela
        self.centralWidget.setLayout(layout)

        self.carregarDados()

    def carregarDados(self):
        conn = conectarBD()
        if conn is None:
            QMessageBox.critical(self, "Erro", "Não foi possível ligar à base de dados.")
            return

        cursor = conn.cursor()
        try:
            cursor.execute("SELECT ID_Cliente, Nome, Contacto, Data_Nascimento, Morada FROM cliente")
            resultados = cursor.fetchall()
            self.tabela.setRowCount(len(resultados))

            for i, linha in enumerate(resultados):
                for j, valor in enumerate(linha):
                    item = QTableWidgetItem(str(valor))
                    item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                    self.tabela.setItem(i, j, item)

            self.tabela.resizeRowsToContents()
            self.tabela.horizontalHeader().setStretchLastSection(True)
            self.tabela.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao carregar dados: {e}")
        finally:
            cursor.close()
            conn.close()

class VisualizarFornecedores(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Stockly - Gestão de Inventário')
        self.setGeometry(70, 50, 1800, 1000)
        self.setWindowIcon(QIcon('icon.png'))
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        layout = QVBoxLayout()

        # Criar um layout horizontal para a barra de pesquisa
        barra_layout = QHBoxLayout()
        barra_layout.setAlignment(Qt.AlignCenter)

        frame_pesquisa = QFrame()
        frame_pesquisa.setFixedSize(420, 40)
        frame_pesquisa.setStyleSheet("background-color: transparent;")
        
        self.pesquisa = QLineEdit(frame_pesquisa)
        self.pesquisa.setPlaceholderText("Pesquisar...")
        self.pesquisa.setGeometry(0, 0, 420, 40)
        self.pesquisa.setStyleSheet("""
            QLineEdit {
                border: 2px solid #1e2c3a;
                border-radius: 10px;
                padding-left: 10px;
                padding-right: 35px;
                background-color: #112233;
                color: white;
                font-size: 16px;
            }
        """)

        lupa = QPushButton(frame_pesquisa)
        lupa.setIcon(QIcon("lupa.png"))
        lupa.setCursor(Qt.PointingHandCursor)
        lupa.setGeometry(380, 5, 30, 30)
        lupa.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
            }
        """)

        barra_layout.addWidget(frame_pesquisa)
        layout.addSpacing(50)  # Espaço acima da barra para melhor centralização
        layout.addLayout(barra_layout)
        layout.addSpacing(20)

        self.tabela = QTableWidget()
        self.tabela.setColumnCount(5)
        self.tabela.setHorizontalHeaderLabels(["ID Fornecedor","NOME", "CONTACTO", "MORADA", "NIF"])
        self.tabela.horizontalHeader().setStyleSheet("""
                QHeaderView::section {
                background-color: #3c3c3c;
                color: white;
                font-weight: bold;
                border: none;
                padding: 6px;
                font-size: 16px;    }
                """)
        
        self.tabela.setStyleSheet("""
            QTableWidget {
                background-color: #2b2b2b;
                color: white;
                gridline-color: #444;
                font-size: 14px;
            }
            QTableWidget::item:selected {
                background-color: #505050;
            }
        """)

        self.tabela.verticalHeader().setVisible(False)
        self.tabela.setFont(QFont("inter", 12))
        self.tabela.setEditTriggers(QTableWidget.NoEditTriggers)

        layout.addWidget(self.tabela, stretch=1)  # Permite expansão da tabela
        self.centralWidget.setLayout(layout)

        self.carregarDados()

    def carregarDados(self):
        conn = conectarBD()
        if conn is None:
            QMessageBox.critical(self, "Erro", "Não foi possível ligar à base de dados.")
            return

        cursor = conn.cursor()
        try:
            cursor.execute("SELECT ID_Fornecedor, Nome, Contacto, Morada, NIF FROM Fornecedores")
            resultados = cursor.fetchall()
            self.tabela.setRowCount(len(resultados))

            for i, linha in enumerate(resultados):
                for j, valor in enumerate(linha):
                    item = QTableWidgetItem(str(valor))
                    item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                    self.tabela.setItem(i, j, item)

            self.tabela.resizeRowsToContents()
            self.tabela.horizontalHeader().setStretchLastSection(True)
            self.tabela.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao carregar dados: {e}")
        finally:
            cursor.close()
            conn.close()

class VisualizarStock(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Stockly - Gestão de Inventário')
        self.setGeometry(70, 50, 1800, 1000)
        self.setWindowIcon(QIcon('icon.png'))
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        layout = QVBoxLayout()

        # Criar um layout horizontal para a barra de pesquisa
        barra_layout = QHBoxLayout()
        barra_layout.setAlignment(Qt.AlignCenter)

        frame_pesquisa = QFrame()
        frame_pesquisa.setFixedSize(420, 40)
        frame_pesquisa.setStyleSheet("background-color: transparent;")
        
        self.pesquisa = QLineEdit(frame_pesquisa)
        self.pesquisa.setPlaceholderText("Pesquisar...")
        self.pesquisa.setGeometry(0, 0, 420, 40)
        self.pesquisa.setStyleSheet("""
            QLineEdit {
                border: 2px solid #1e2c3a;
                border-radius: 10px;
                padding-left: 10px;
                padding-right: 35px;
                background-color: #112233;
                color: white;
                font-size: 16px;
            }
        """)

        lupa = QPushButton(frame_pesquisa)
        lupa.setIcon(QIcon("lupa.png"))
        lupa.setCursor(Qt.PointingHandCursor)
        lupa.setGeometry(380, 5, 30, 30)
        lupa.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
            }
        """)

        barra_layout.addWidget(frame_pesquisa)
        layout.addSpacing(50)  # Espaço acima da barra para melhor centralização
        layout.addLayout(barra_layout)
        layout.addSpacing(20)

        self.tabela = QTableWidget()
        self.tabela.setColumnCount(5)
        self.tabela.setHorizontalHeaderLabels(["ID STOCK","NOME PRODUTO", "PREÇO DO PRODUTO", "QUANTIDADE", "ID FORNECEDOR"])
        self.tabela.verticalHeader().setDefaultSectionSize(40)  # Altura fixa das linhas
        self.tabela.horizontalHeader().setStyleSheet("""
                QHeaderView::section {
                background-color: #3c3c3c;
                color: white;
                font-weight: bold;
                border: none;
                padding: 6px;
                font-size: 16px;    }
                """)
        
        self.tabela.setStyleSheet("""
            QTableWidget {
                background-color: #2b2b2b;
                color: white;
                gridline-color: #444;
                font-size: 14px;
            }
            QTableWidget::item:selected {
                background-color: #505050;
            }
        """)

        self.tabela.verticalHeader().setVisible(False)
        self.tabela.setFont(QFont("inter", 12))
        self.tabela.setEditTriggers(QTableWidget.NoEditTriggers)

        layout.addWidget(self.tabela, stretch=1)  # Permite expansão da tabela
        self.centralWidget.setLayout(layout)

        self.carregarDados()

    def carregarDados(self):
        conn = conectarBD()
        if conn is None:
            QMessageBox.critical(self, "Erro", "Não foi possível ligar à base de dados.")
            return

        cursor = conn.cursor()
        try:
            cursor.execute("SELECT ID_Stock, Nome_Produto, Preco_Produto, Quantidade_Produto, ID_Fornecedor FROM Stock")
            resultados = cursor.fetchall()
            self.tabela.setRowCount(len(resultados))

            for i, linha in enumerate(resultados):
                for j, valor in enumerate(linha):
                    item = QTableWidgetItem(str(valor))
                    item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                    self.tabela.setItem(i, j, item)

            self.tabela.resizeRowsToContents()
            self.tabela.horizontalHeader().setStretchLastSection(True)
            self.tabela.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao carregar dados: {e}")
        finally:
            cursor.close()
            conn.close()

class Visualizarvendas(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Stockly - Gestão de Inventário')
        self.setGeometry(70, 50, 1800, 1000)
        self.setWindowIcon(QIcon('icon.png'))
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        layout = QVBoxLayout()

        # Criar um layout horizontal para a barra de pesquisa
        barra_layout = QHBoxLayout()
        barra_layout.setAlignment(Qt.AlignCenter)

        frame_pesquisa = QFrame()
        frame_pesquisa.setFixedSize(420, 40)
        frame_pesquisa.setStyleSheet("background-color: transparent;")
        
        self.pesquisa = QLineEdit(frame_pesquisa)
        self.pesquisa.setPlaceholderText("Pesquisar...")
        self.pesquisa.setGeometry(0, 0, 420, 40)
        self.pesquisa.setStyleSheet("""
            QLineEdit {
                border: 2px solid #1e2c3a;
                border-radius: 10px;
                padding-left: 10px;
                padding-right: 35px;
                background-color: #112233;
                color: white;
                font-size: 16px;
            }
        """)

        lupa = QPushButton(frame_pesquisa)
        lupa.setIcon(QIcon("lupa.png"))
        lupa.setCursor(Qt.PointingHandCursor)
        lupa.setGeometry(380, 5, 30, 30)
        lupa.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
            }
        """)

        barra_layout.addWidget(frame_pesquisa)
        layout.addSpacing(50)  # Espaço acima da barra para melhor centralização
        layout.addLayout(barra_layout)
        layout.addSpacing(20)

        self.tabela = QTableWidget()
        self.tabela.setColumnCount(6)
        self.tabela.setHorizontalHeaderLabels(["ID VENDA","NOME PRODUTO", "PREÇO DA VENDA", "QUANTIDADE DA VENDA", "ID STOCK", "ID CLIENTE"])
        self.tabela.horizontalHeader().setStyleSheet("""
                QHeaderView::section {
                background-color: #3c3c3c;
                color: white;
                font-weight: bold;
                border: none;
                padding: 6px;
                font-size: 16px;    }
                """)
        
        self.tabela.setStyleSheet("""
            QTableWidget {
                background-color: #2b2b2b;
                color: white;
                gridline-color: #444;
                font-size: 14px;
            }
            QTableWidget::item:selected {
                background-color: #505050;
            }
        """)

        self.tabela.verticalHeader().setVisible(False)
        self.tabela.setFont(QFont("inter", 12))
        self.tabela.setEditTriggers(QTableWidget.NoEditTriggers)

        layout.addWidget(self.tabela, stretch=1)  # Permite expansão da tabela
        self.centralWidget.setLayout(layout)

        self.carregarDados()

    def carregarDados(self):
        conn = conectarBD()
        if conn is None:
            QMessageBox.critical(self, "Erro", "Não foi possível ligar à base de dados.")
            return

        cursor = conn.cursor()
        try:
            cursor.execute("SELECT ID_Venda, Nome_Produto, Preco_Venda, Quantidade_Venda, ID_Stock, ID_Cliente FROM Vendas")
            resultados = cursor.fetchall()
            self.tabela.setRowCount(len(resultados))

            for i, linha in enumerate(resultados):
                for j, valor in enumerate(linha):
                    item = QTableWidgetItem(str(valor))
                    item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                    self.tabela.setItem(i, j, item)

            self.tabela.resizeRowsToContents()
            self.tabela.horizontalHeader().setStretchLastSection(True)
            self.tabela.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao carregar dados: {e}")
        finally:
            cursor.close()
            conn.close()

class AlterarMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainMenu = MainMenu  # Guardar referência ao menu principal
        self.setWindowIcon(QIcon('icon.png'))  # Definir ícone da janela
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
