# Biblioetecas
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QMessageBox
)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
import sqlite3

# Função para conectar à base de dados
def conectarBD():
    conn = None
    try:
        conn = sqlite3.connect('stockly.db')
        return conn
    except sqlite3.Error as error:
        print(f"Erro ao conectar a base da dados. [{error}]")
        return None

# Classe para inserir vendas
class InserirVendas(QMainWindow):
    def __init__(self, inserirMenu_ref): # Construtor da classe
        super().__init__() # Inicializa a classe pai
        self.inserirMenu = inserirMenu_ref # Referência ao menu de inserir registos

        self.setWindowTitle("Stockly - Gestão de Inventário") # Definir título da janela
        self.setGeometry(70, 50, 1800, 1000) # Definir tamanho da janela
        self.setWindowIcon(QIcon('img/icon.png')) # Definir ícone da janela

        self.centralWidget = QWidget() # Cria um widget central
        self.setCentralWidget(self.centralWidget) # Define o widget central da janela
        layout = QVBoxLayout() # Layout principal vertical
        self.centralWidget.setStyleSheet("background-color: #C2C2C2;")  # Cor de fundo

        # Layout do botão voltar no canto superior direito
        topBarLayout = QHBoxLayout()
        topBarLayout.addStretch()
        topBarLayout.setAlignment(Qt.AlignTop)

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
        # Conectar o botão voltar à função
        self.buttonBack.clicked.connect(self.voltar)
        topBarLayout.addWidget(self.buttonBack)
        layout.addLayout(topBarLayout)

        # Campos de input
        self.input_nome = self.criarCampo(layout, "NOME PRODUTO:", "Inserir nome do Produto") # Campo para inserir o nome do produto
        self.input_preco = self.criarCampo(layout, "PREÇO DA VENDA:", "Inserir preço da Venda") # Campo para inserir o preço da venda
        self.input_quantidade = self.criarCampo(layout, "QUANTIDADE:", "Inserir Quantidade da Venda") # Campo para inserir a quantidade da venda
        self.input_IDstock = self.criarCampo(layout, "ID STOCK:", "Inserir ID do Stock") # Campo para inserir o ID do stock
        self.input_IDcliente = self.criarCampo(layout, "ID CLIENTE:", "Inserir ID do Cliente") # Campo para inserir o ID do cliente

        # Botão Inserir
        self.botao_inserir = QPushButton("INSERIR") 
        self.botao_inserir.setFixedSize(300, 100)
        self.botao_inserir.setFont(QFont("Inter", 16, QFont.Bold))
        # Estilo do botão
        self.botao_inserir.setStyleSheet("""
            QPushButton {
                background-color: #1E2A38;
                color: white;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #2F3E50;
            }
        """)
        # Conectar o botão Inserir à função de inserção
        self.botao_inserir.clicked.connect(self.inserirVendas)
        layout.addSpacing(40)
        layout.addWidget(self.botao_inserir, alignment=Qt.AlignCenter) # Adiciona o botão Inserir ao layout centralizado

        # Adiciona o layout principal ao widget central
        self.centralWidget.setLayout(layout)

    # Função para criar campos de input
    def criarCampo(self, parent_layout, label_texto, placeholder):
        linha_layout = QHBoxLayout()
        linha_layout.setSpacing(1)

        # Cria um label para o campo
        label = QLabel(label_texto)
        label.setFixedWidth(250)
        label.setFont(QFont("Inter", 18, QFont.Bold))
        label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        # Cria um campo de input
        input_field = QLineEdit()
        input_field.setPlaceholderText(placeholder)
        input_field.setFixedSize(1000, 50)
        # Estilo do campo de input
        input_field.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border-radius: 10px;
                padding: 10px;
                font-size: 16px;
            }
        """)

        # Adiciona o label e o campo de input ao layout
        linha_layout.addWidget(label)
        linha_layout.addWidget(input_field)
        parent_layout.addLayout(linha_layout)
        parent_layout.addSpacing(35)
        return input_field

    # Função para inserir vendas
    def inserirVendas(self):
        # Obter os valores dos campos de input
        Nome_Produto = self.input_nome.text().strip().title()
        Preco_Venda = self.input_preco.text().strip()
        Quantidade_Venda = self.input_quantidade.text().strip()
        ID_Stock = self.input_IDstock.text().strip()
        ID_Cliente = self.input_IDcliente.text().strip()

        # Verificar se os campos estão preenchidos
        if not Nome_Produto or not Preco_Venda or not Quantidade_Venda or not ID_Stock or not ID_Cliente:
            QMessageBox.warning(self, "Campos incompletos", "Por favor, preencha todos os campos.")
            return

        # Conectar à base de dados e inserir os dados
        conn = conectarBD()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("""
                    INSERT INTO vendas (Nome_Produto, Preco_Venda, Quantidade_Venda, ID_STOCK, ID_CLIENTE)
                    VALUES (?, ?, ?, ?, ?)
                """, (Nome_Produto, Preco_Venda, Quantidade_Venda, ID_Stock, ID_Cliente)) # Inserir os dados na tabela vendas
                conn.commit()
                QMessageBox.information(self, "Sucesso", "Produto inserido com sucesso!")
                # Limpar os campos de input após a inserção
                self.input_nome.clear() 
                self.input_preco.clear()
                self.input_quantidade.clear()
                self.input_IDstock.clear()
                self.input_IDcliente.clear()
            except Exception as e: # Exceção para erro de inserção
                QMessageBox.critical(self, "Erro", f"Erro ao inserir Produto: {e}")
                conn.rollback()
            finally:
                conn.close()

    # Função para voltar ao menu anterior
    def voltar(self):
        self.inserirMenu.show()
        self.close()
