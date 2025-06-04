# Bibliotecas
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QMessageBox
)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
from datetime import datetime
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

# Classe para inserir clientes
class InserirCliente(QMainWindow):
    def __init__(self, inserirMenu_ref): # Construtor da classe
        super().__init__() # Inicializa a classe pai
        self.inserirMenu = inserirMenu_ref # Referência ao menu de inserir registos

        self.setWindowTitle("Stockly - Inserir Clientes") # Definir título da janela
        self.setGeometry(70, 50, 1800, 1000) # Definir tamanho da janela
        self.setWindowIcon(QIcon('img/icon.png')) # Definir ícone da janela

        self.centralWidget = QWidget() # Cria um widget central
        self.setCentralWidget(self.centralWidget) # Define o widget central da janela
        layout = QVBoxLayout() # Layout principal vertical
        self.centralWidget.setStyleSheet("background-color: #C2C2C2;")  # Cor de fundo

        # Layout do botão voltar no canto superior direito
        topBarLayout = QHBoxLayout()
        topBarLayout.addStretch() # Adiciona espaço à esquerda
        topBarLayout.setAlignment(Qt.AlignTop) # Alinha o layout ao topo

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
        layout.addLayout(topBarLayout) # Adiciona o layout do botão voltar ao layout principal

        # Campos de input
        self.input_nome = self.criarCampo(layout, "NOME:", "Inserir nome") # Campo para inserir o nome
        self.input_contacto = self.criarCampo(layout, "CONTACTO:", "Inserir contacto") # Campo para inserir o contacto
        self.input_contacto.textChanged.connect(self.verificarPrefixoContacto) # Conectar a função de verificação ao campo de contacto
        self.input_data = self.criarCampo(layout, "DATA NASCIMENTO:", "AAAA-MM-DD") # Campo para inserir a data de nascimento
        self.input_morada = self.criarCampo(layout, "MORADA:", "Inserir morada") # Campo para inserir a morada

        
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
        # Conectar o botão Inserir à função de inserção
        self.botao_inserir.clicked.connect(self.inserirCliente)
        layout.addSpacing(40)
        layout.addWidget(self.botao_inserir, alignment=Qt.AlignCenter) # Adiciona o botão Inserir ao layout centralizado

        # Adiciona espaçamento entre os campos
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

        # Mascara para a data de nascimento
        if 'data' in label_texto.lower():
            input_field.setInputMask('00-00-0000') # Formato DD-MM-AAAA

        # Estilo do campo de input
        input_field.setStyleSheet("""
            QLineEdit {
                border: 2px solid silver;
                border-radius: 10px;
                padding: 10px;
                background-color: white;
                color: black;
                font-size: 16px;
            }
            QLineEdit:focus {
                border: 2px solid #1E2A38;
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
        if texto and not texto.startswith('+'): # Verifica se o texto não começa com '+' 
            numeros = ''.join(filter(str.isdigit, texto)) # Remove todos os caracteres não numéricos
            if len(numeros) >= 9:
                formatado = f'+351 {numeros[-9:-6]} {numeros[-6:-3]} {numeros[-3:]}' # Formato do contacto
                self.input_contacto.blockSignals(True) # Bloqueia sinais para evitar loops infinitos
                self.input_contacto.setText(formatado) # Define o texto formatado no campo
                self.input_contacto.blockSignals(False) # Desbloqueia sinais

    # Função para inserir cliente na base de dados
    def inserirCliente(self):
        nome = self.input_nome.text().strip().title() # Formata o nome
        contacto = self.input_contacto.text().strip() # Formata o contacto 
        data_nascimento = self.input_data.text().strip() # Formata a data de nascimento
        morada = self.input_morada.text().strip() # Formata a morada

        # Verifica se os campos estão preenchidos
        if not nome or not contacto or not data_nascimento or not morada:
            QMessageBox.warning(self, "Campos incompletos", "Por favor, preencha todos os campos.")
            return

        # Utilizador insere a data no formato DD-MM-AAAA mas converte para o formato AAAA-MM-DD para comunicar corretamente com a base de dados.
        try:
            converterData = datetime.strptime(data_nascimento, "%d-%m-%Y")
        except ValueError:
            QMessageBox.warning(self, "Data inválida", "A data de nascimento deve estar no formato DD-MM-AAAA.")
            return

        conn = conectarBD() # Conecta à base de dados

        # Verifica se a conexão foi bem-sucedida
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("""
                    INSERT INTO cliente (Nome, Contacto, Data_Nascimento, Morada)
                    VALUES (?, ?, ?, ?) 
                """, (nome, contacto, data_nascimento, morada))  # Insere os dados na tabela cliente

                id_cliente = cursor.lastrowid  # Obtém o ID do cliente inserido

                cursor.execute("""
                    INSERT INTO historico_cliente (id_cliente, campo_alterado, valor_antigo, valor_novo)
                    VALUES (?, 'INSERÇÃO', '', ?)
                """, (id_cliente, f"Nome: {nome}, Contacto: {contacto}, Nascimento: {data_nascimento}, Morada: {morada}"))

                conn.commit()
                QMessageBox.information(self, "Sucesso", "Cliente inserido com sucesso!")
                self.input_nome.clear() # Limpa o campo de nome
                self.input_contacto.clear() # Limpa o campo de contacto
                self.input_data.clear() # Limpa o campo de data
                self.input_morada.clear() # Limpa o campo de morada

            except Exception as e: # Captura exceções
                QMessageBox.critical(self, "Erro", f"Erro ao inserir cliente: {e}") 
                conn.rollback()
            finally:
                conn.close()

    # Função para voltar ao menu anterior
    def voltar(self):
        self.inserirMenu.show()
        self.close()
