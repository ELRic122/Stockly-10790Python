# Bibliotecas
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

# Classe para inserir produtos no stock
class InserirStock(QMainWindow):
    def __init__(self, inserirMenu_ref): # Construtor da classe
        super().__init__() # Inicializa a classe pai
        self.inserirMenu = inserirMenu_ref # Referência ao menu de inserir registos

        self.setWindowTitle("Stockly - Inserir Produtos") # Definir título da janela
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
        self.input_preco = self.criarCampo(layout, "PREÇO:", "Inserir preço do produto") # Campo para inserir o preço do produto
        self.input_quantidade = self.criarCampo(layout, "QUANTIDADE:", "Inserir Quantidade do Produto") # Campo para inserir a quantidade do produto
        self.input_IDfornecedor = self.criarCampo(layout, "ID FORNECEDOR:", "Inserir ID do Fornecedor") # Campo para inserir o ID do fornecedor

        # Botão Inserir
        self.botao_inserir = QPushButton("INSERIR")
        self.botao_inserir.setFixedSize(300, 100)
        self.botao_inserir.setFont(QFont("Inter", 16, QFont.Bold))
        # Estilo do botão Inserir
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
        # Conectar o botão Inserir à função de inserir
        self.botao_inserir.clicked.connect(self.inserirStock)
        layout.addSpacing(40)
        layout.addWidget(self.botao_inserir, alignment=Qt.AlignCenter) # Adiciona o botão Inserir ao layout centralizado

        self.centralWidget.setLayout(layout) # Adiciona o layout principal ao widget central

    # Função para criar campos de input
    def criarCampo(self, parent_layout, label_texto, placeholder):
        linha_layout = QHBoxLayout()
        linha_layout.setSpacing(1)
 
        # Criação do label
        label = QLabel(label_texto)
        label.setFixedWidth(250)
        label.setFont(QFont("Inter", 18, QFont.Bold))
        label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
 
        # Criação do campo de input
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

    # Função para inserir o produto no stock
    def inserirStock(self):
        # Obter os valores dos campos de input
        Nome_Produto = self.input_nome.text().strip().title()
        Preco_Produto = self.input_preco.text().strip()
        Quantidade_Produto = self.input_quantidade.text().strip()
        ID_Fornecedor = self.input_IDfornecedor.text().strip()

        # Verificar se os campos estão preenchidos
        if not Nome_Produto or not Preco_Produto or not Quantidade_Produto or not ID_Fornecedor:
            QMessageBox.warning(self, "Campos incompletos", "Por favor, preencha todos os campos.")
            return

        # Conectar à base de dados
        conn = conectarBD()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("""
                    INSERT INTO Stock (Nome_Produto, Preco_Produto, Quantidade_Produto, ID_Fornecedor)
                    VALUES (?, ?, ?, ?)
                """, (Nome_Produto, Preco_Produto, Quantidade_Produto, ID_Fornecedor)) # Inserir os dados na tabela Stock
                conn.commit()

                id_Stock = cursor.lastrowid  # Obtém o ID do Stock inserido

                cursor.execute("""
                    INSERT INTO historico_Stock (id_Stock, campo_alterado, valor_antigo, valor_novo)
                    VALUES (?, 'INSERÇÃO', '', ?)
                """, (id_Stock, f"Nome: {Nome_Produto}, Preco Produto: {Preco_Produto}, Quantidade Produto: {Quantidade_Produto}, ID Fornecedor: {ID_Fornecedor}"))

                conn.commit()
                QMessageBox.information(self, "Sucesso", "Produto inserido com sucesso!")
                # Limpar os campos de input após a inserção
                self.input_nome.clear()
                self.input_preco.clear()
                self.input_quantidade.clear()
                self.input_IDfornecedor.clear()
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao inserir Produto: {e}") # Exceção para erro de inserção
                conn.rollback()
            finally:
                conn.close()

    # Função para voltar ao menu de inserir registos
    def voltar(self):
        self.inserirMenu.show()
        self.close()
