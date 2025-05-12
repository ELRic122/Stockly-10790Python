# Bibliotecas
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QMessageBox
)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
import mysql.connector

# Função para conectar à base de dados
def conectarBD():
    try:
        return mysql.connector.connect(user='root', host='localhost', database='stockly', autocommit=True)
    except mysql.connector.Error as error:
        print(f"Erro ao conectar à base de dados. [{error}]")
        return None

# Classe para inserir produtos no stock
class InserirFornecedores(QMainWindow):
    def __init__(self, inserirMenu_ref): # Construtor da classe
        super().__init__() # Inicializa a classe pai
        self.inserirMenu = inserirMenu_ref # Referência ao menu de inserir registos

        self.setWindowTitle("Stockly - Gestão de Inventário") # Definir título da janela
        self.setGeometry(70, 50, 1800, 1000) # Definir tamanho da janela
        self.setWindowIcon(QIcon('img/icon.png')) # Definir ícone da janela

        self.centralWidget = QWidget() # Cria um widget central
        self.setCentralWidget(self.centralWidget) # Define o widget central da janela
        layout = QVBoxLayout() # Layout principal vertical

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
        self.input_nome = self.criarCampo(layout, "NOME:", "Inserir nome") # Campo para inserir o nome
        self.input_contacto = self.criarCampo(layout, "CONTACTO:", "Inserir contacto") # Campo para inserir o contacto
        self.input_contacto.textChanged.connect(self.verificarPrefixoContacto) # Conectar a função de verificação ao campo de contacto
        self.input_morada = self.criarCampo(layout, "MORADA:", "Inserir morada") # Campo para inserir a morada
        self.input_NIF = self.criarCampo(layout, "NIF:", "Inserir NIF") # Campo para inserir o NIF

        # Botão Inserir
        self.botao_inserir = QPushButton("INSERIR")
        self.botao_inserir.setFixedSize(300, 100)
        self.botao_inserir.setFont(QFont("Inter", 16, QFont.Bold))
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
        # Conectar o botão Inserir à função
        self.botao_inserir.clicked.connect(self.inserirFornecedor)
        layout.addSpacing(40)
        layout.addWidget(self.botao_inserir, alignment=Qt.AlignCenter) # Adiciona o botão ao centro
 
        self.centralWidget.setLayout(layout) # Define o layout do widget central

    # Função para criar campos de input
    def criarCampo(self, parent_layout, label_texto, placeholder):
        linha_layout = QHBoxLayout()
        linha_layout.setSpacing(1)

        # Cria o layout para o campo de input
        label = QLabel(label_texto)
        label.setFixedWidth(300)
        label.setFont(QFont("Inter", 18, QFont.Bold))
        label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        # Cria o campo de input
        input_field = QLineEdit()
        input_field.setPlaceholderText(placeholder)
        input_field.setFixedSize(1000, 50)
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

    # Função para verificar o prefixo do contacto
    def verificarPrefixoContacto(self):
        texto = self.input_contacto.text().strip() # Remove espaços em branco
        if texto and not texto.startswith('+'): # Verifica se o texto não está vazio e não começa com '+'
            numeros = ''.join(filter(str.isdigit, texto)) # Remove caracteres não numéricos
            if len(numeros) >= 9:
                formatado = f'+351 {numeros[-9:-6]} {numeros[-6:-3]} {numeros[-3:]}'
                self.input_contacto.blockSignals(True) # Bloqueia os sinais para evitar loops infinitos
                self.input_contacto.setText(formatado) # Define o texto formatado no campo
                self.input_contacto.blockSignals(False) # Desbloqueia os sinais
 
    # Função para inserir o fornecedor na base de dados
    def inserirFornecedor(self):
        # Obter os valores dos campos de input
        nome = self.input_nome.text().strip().title()
        contacto = self.input_contacto.text().strip()
        morada = self.input_morada.text().strip()
        NIF = self.input_NIF.text().strip()

        # Verificar se os campos estão preenchidos
        if not nome or not contacto or not NIF or not morada:
            QMessageBox.warning(self, "Campos incompletos", "Por favor, preencha todos os campos.")
            return

        conn = conectarBD() # Conectar à base de dados
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("""
                    INSERT INTO fornecedores (Nome, Contacto, Morada, NIF)
                    VALUES (%s, %s, %s, %s)
                """, (nome, contacto, morada, NIF)) # Inserir os dados na tabela fornecedores
                conn.commit()
                QMessageBox.information(self, "Sucesso", "Fornecedor inserido com sucesso!")
                # Limpar os campos de input após a inserção
                self.input_nome.clear()
                self.input_contacto.clear()
                self.input_morada.clear()
                self.input_NIF.clear()

            except Exception as e: # Exceção para erro de inserção
                QMessageBox.critical(self, "Erro", f"Erro ao inserir Fornecedor: {e}")
                conn.rollback()
            finally:
                conn.close()

    # Função para voltar ao menu de inserir registos
    def voltar(self):
        self.inserirMenu.show()
        self.close()
