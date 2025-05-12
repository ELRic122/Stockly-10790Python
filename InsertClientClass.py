from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QMessageBox
)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
import mysql.connector
from datetime import datetime

def conectarBD():
    try:
        return mysql.connector.connect(user='root', host='localhost', database='stockly', autocommit=True)
    except mysql.connector.Error as error:
        print(f"Erro ao conectar à base de dados. [{error}]")
        return None


class InserirCliente(QMainWindow):
    def __init__(self, inserirMenu_ref):
        super().__init__()
        self.inserirMenu = inserirMenu_ref

        self.setWindowTitle("Stockly - Gestão de Inventário")
        self.setGeometry(70, 50, 1800, 1000)
        self.setWindowIcon(QIcon('img/icon.png'))

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        layout = QVBoxLayout()

        # Layout do botão voltar no canto superior direito
        topBarLayout = QHBoxLayout()
        topBarLayout.addStretch()
        topBarLayout.setAlignment(Qt.AlignTop)

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
        self.buttonBack.clicked.connect(self.voltar)
        topBarLayout.addWidget(self.buttonBack)
        layout.addLayout(topBarLayout)

        # Campos de input
        self.input_nome = self.criarCampo(layout, "NOME:", "Inserir nome")
        self.input_contacto = self.criarCampo(layout, "CONTACTO:", "Inserir contacto")
        self.input_contacto.textChanged.connect(self.verificarPrefixoContacto)
        self.input_data = self.criarCampo(layout, "DATA NASCIMENTO:", "AAAA/MM/DD")
        self.input_morada = self.criarCampo(layout, "MORADA:", "Inserir morada")

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
        self.botao_inserir.clicked.connect(self.inserirCliente)
        layout.addSpacing(40)
        layout.addWidget(self.botao_inserir, alignment=Qt.AlignCenter)

        self.centralWidget.setLayout(layout)

    def criarCampo(self, parent_layout, label_texto, placeholder):
        linha_layout = QHBoxLayout()
        linha_layout.setSpacing(1)

        label = QLabel(label_texto)
        label.setFixedWidth(250)
        label.setFont(QFont("Inter", 18, QFont.Bold))
        label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

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

        linha_layout.addWidget(label)
        linha_layout.addWidget(input_field)
        parent_layout.addLayout(linha_layout)
        parent_layout.addSpacing(35)
        return input_field

    def verificarPrefixoContacto(self):
        texto = self.input_contacto.text().strip()
        if texto and not texto.startswith('+'):
            numeros = ''.join(filter(str.isdigit, texto))
            if len(numeros) >= 9:
                formatado = f'+351 {numeros[-9:-6]} {numeros[-6:-3]} {numeros[-3:]}'
                self.input_contacto.blockSignals(True)
                self.input_contacto.setText(formatado)
                self.input_contacto.blockSignals(False)

    def inserirCliente(self):
        nome = self.input_nome.text().strip().title()
        contacto = self.input_contacto.text().strip()
        data_nascimento = self.input_data.text().strip()
        morada = self.input_morada.text().strip()

        if not nome or not contacto or not data_nascimento or not morada:
            QMessageBox.warning(self, "Campos incompletos", "Por favor, preencha todos os campos.")
            return
        
        # Validar formato da data
        try:
            datetime.strptime(data_nascimento, "%Y-%m-%d")
        except ValueError:
            QMessageBox.warning(self, "Data inválida", "A data de nascimento deve estar no formato AAAA-MM-DD.")
            return

        conn = conectarBD()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("""
                    INSERT INTO cliente (Nome, Contacto, Data_Nascimento, Morada)
                    VALUES (%s, %s, %s, %s)
                """, (nome, contacto, data_nascimento, morada))
                conn.commit()
                QMessageBox.information(self, "Sucesso", "Cliente inserido com sucesso!")
                self.input_nome.clear()
                self.input_contacto.clear()
                self.input_data.clear()
                self.input_morada.clear()
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao inserir cliente: {e}")
                conn.rollback()
            finally:
                conn.close()

    def voltar(self):
        self.inserirMenu.show()
        self.close()
