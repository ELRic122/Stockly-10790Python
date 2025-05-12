# Bibliotecas
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QMessageBox, QTableWidgetItem, QTableWidget, QHeaderView, QLineEdit, QFrame
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
import mysql.connector

# Função para conectar à base de dados
def conectarBD():
    conn = None
    try:
        conn = mysql.connector.connect(user='root', host='localhost', database='stockly', autocommit=True)
        return conn
    except mysql.connector.Error as error:
        print(f"Erro ao conectar a base da dados. [{error}]")
        return None
    
# Classe para visualizar stock
class VisualizarStock(QMainWindow):
    def __init__(self, ViewMenu_ref): # Construtor da classe
        super().__init__() # Inicializa a classe pai
        self.ViewMenu = ViewMenu_ref # Referência ao menu de visualizar registos
        self.setWindowTitle('Stockly - Gestão de Inventário') # Definir título da janela
        self.setGeometry(70, 50, 1800, 1000) # Definir tamanho da janela
        self.setWindowIcon(QIcon('img/icon.png')) # Definir ícone da janela

        self.centralWidget = QWidget() # Cria um widget central
        self.setCentralWidget(self.centralWidget) # Define o widget central da janela
        layout = QVBoxLayout() # Layout principal vertical
        
        # Layout da barra de pesquisa
        barra_layout = QHBoxLayout()
        barra_layout.setAlignment(Qt.AlignCenter)

        # Frame para a barra de pesquisa
        frame_pesquisa = QFrame()
        frame_pesquisa.setFixedSize(420, 40)
        frame_pesquisa.setStyleSheet("background-color: transparent;")

        # Campo de pesquisa
        self.pesquisa = QLineEdit(frame_pesquisa)
        self.pesquisa.setPlaceholderText("Pesquisar...")
        self.pesquisa.setGeometry(0, 0, 420, 40)
        # Estilo do campo de pesquisa
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

        # Botão de pesquisa
        lupa = QPushButton(frame_pesquisa)
        lupa.setIcon(QIcon("img/lupa.png"))
        lupa.setCursor(Qt.PointingHandCursor)
        lupa.setGeometry(380, 5, 30, 30)
        # Estilo do botão de pesquisa
        lupa.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
            }
        """)
        # Layout principal
        layout = QVBoxLayout()

        # Layout do botão voltar no canto superior direito
        topBarLayout = QHBoxLayout()
        topBarLayout.addStretch()

        # Botão voltar
        self.buttonBack = QPushButton("←")
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
        # Estilo do botão voltar
        self.buttonBack.clicked.connect(self.voltarAoMenu)
        topBarLayout.addWidget(self.buttonBack)

        layout.addLayout(topBarLayout) # Adiciona o layout do botão voltar

        # Layout da barra de pesquisa
        barra_layout.addWidget(frame_pesquisa)
        layout.addSpacing(30) 
        layout.addLayout(barra_layout)
        layout.addSpacing(10)

        # Tabela configurada
        self.configurarTabela()
        self.tabela.setColumnCount(5) # Definir número de colunas da tabela
        self.tabela.setHorizontalHeaderLabels(["ID STOCK","NOME PRODUTO", "PREÇO DO PRODUTO", "QUANTIDADE", "ID FORNECEDOR"]) # Definir cabeçalho da tabela
        layout.addWidget(self.tabela)

        # Adiciona a tabela ao layout
        self.centralWidget.setLayout(layout)  
        self.carregarDados()

    # Função para configurar a tabela
    def configurarTabela(self):
        self.tabela = QTableWidget()
        self.tabela.setFont(QFont("Inter", 12))
        self.tabela.setEditTriggers(QTableWidget.NoEditTriggers) # Não permite edição
        self.tabela.verticalHeader().setVisible(False) # Oculta o cabeçalho vertical
        self.tabela.verticalHeader().setDefaultSectionSize(50) # Define a altura padrão das linhas

        # Estilo da tabela
        self.tabela.setStyleSheet("""
            QTableWidget {
                background-color: #2b2b2b;
                color: white;
                gridline-color: #444;
                font-size: 14px;
                border: none;
            }
            QHeaderView::section {
                background-color: #3c3c3c;
                color: white;
                font-weight: bold;
                border: none;
                padding: 8px;
                font-size: 16px;
            }
            QTableWidget::item {
                padding: 10px;
            }
            QTableWidget::item:selected {
                background-color: #505050;
            }
        """)

        # Configuração do cabeçalho
        self.tabela.horizontalHeader().setStretchLastSection(True)
        self.tabela.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    # Função para carregar dados na tabela
    def carregarDados(self):
        conn = conectarBD() # Conectar à base de dados
        if conn is None: # Verifica se a conexão foi bem-sucedida
            QMessageBox.critical(self, "Erro", "Não foi possível ligar à base de dados.")
            return

        cursor = conn.cursor()
        try:
            cursor.execute("SELECT ID_Stock, Nome_Produto, Preco_Produto, Quantidade_Produto, ID_Fornecedor FROM Stock") # Seleciona os dados da tabela Stock
            resultados = cursor.fetchall() # Obtém os resultados da consulta
            self.tabela.setRowCount(len(resultados)) # Define o número de linhas da tabela

            # Preenche a tabela com os dados    
            for i, linha in enumerate(resultados):
                for j, valor in enumerate(linha):
                    item = QTableWidgetItem(str(valor))
                    item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                    self.tabela.setItem(i, j, item)

        # Verifica se a tabela está vazia
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao carregar dados: {e}")
        finally:
            cursor.close()
            conn.close()
    
    # Função para voltar ao menu
    def voltarAoMenu(self):
        self.ViewMenu.show()
        self.close()