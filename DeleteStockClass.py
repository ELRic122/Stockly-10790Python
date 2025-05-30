#bibliotecas
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QMessageBox, QTableWidget, QTableWidgetItem
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

# Classe para apagar Stock
class ApagarStock(QMainWindow):
    def __init__(self, apagarmenu_ref): # Construtor da classe
        super().__init__() # Inicializa a classe pai
        self.apagarmenu = apagarmenu_ref # Referência ao menu de apagar registos

        self.setWindowTitle("Stockly - Gestão de Inventário") # Definir título da janela
        self.setGeometry(70, 50, 1800, 1000) # Definir tamanho da janela
        self.setWindowIcon(QIcon('img/icon.png')) # Definir ícone da janela

        self.centralWidget = QWidget() # Cria um widget central
        self.setCentralWidget(self.centralWidget) # Define o widget central da janela
        layout = QVBoxLayout() # Layout principal vertical
        self.centralWidget.setStyleSheet("background-color: #C2C2C2;")  # Cor de fundo

        # Botão voltar no topo direito
        topBarLayout = QHBoxLayout()
        topBarLayout.addStretch()
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

        # Campo de pesquisa
        pesquisaLayout = QHBoxLayout()
        label_pesquisa = QLabel("Nome do Produto:")
        label_pesquisa.setFont(QFont("Inter", 16))
        self.input_pesquisa = QLineEdit()
        self.input_pesquisa.setPlaceholderText("Pesquisar Produto...")

        # Estilo do campo de pesquisa
        self.input_pesquisa.setStyleSheet("""
                QLineEdit {
                border: silver;
                border-radius: 10px;
                padding-left: 10px;
                padding-right: 35px;
                background-color: silver;
                color: black;
                font-size: 16px;
            }
        """)

        # Definir tamanho do campo de pesquisa e botão
        self.input_pesquisa.setFixedSize(1000, 50)
        self.botao_pesquisar = QPushButton("PESQUISAR")
        self.botao_pesquisar.setFixedSize(150, 40)
        # Estilo do botão pesquisar
        self.botao_pesquisar.setStyleSheet("""
            QPushButton {
                background-color: #1E2A38;
                color: white;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #2F3E50;
            }
        """)
        # Conectar o botão pesquisar à função de pesquisa
        self.botao_pesquisar.clicked.connect(self.pesquisarStock)

        # Adicionar widgets ao layout de pesquisa
        pesquisaLayout.addWidget(label_pesquisa)
        pesquisaLayout.addWidget(self.input_pesquisa)
        pesquisaLayout.addWidget(self.botao_pesquisar)
        pesquisaLayout.addStretch()  # empurra tudo para a esquerda

        layout.addLayout(pesquisaLayout)
        layout.addSpacing(20)

        # Tabela de Stock
        self.tabela_Stock = QTableWidget()
        self.tabela_Stock.setColumnCount(5)
        self.tabela_Stock.setHorizontalHeaderLabels(["ID STOCK", "NOME DO PRODUTO", "PREÇO DO PRODUTO", "QUANTIDADE DE PRODUTO", "ID FORNECEDOR"])

        # Define as larguras das colunas
        self.tabela_Stock.setColumnWidth(0, 250)
        self.tabela_Stock.setColumnWidth(1, 350)
        self.tabela_Stock.setColumnWidth(2, 350)
        self.tabela_Stock.setColumnWidth(3, 500)
        self.tabela_Stock.setColumnWidth(4, 350)
        self.tabela_Stock.horizontalHeader().setStretchLastSection(False)
        self.tabela_Stock.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)

        self.tabela_Stock.setFixedSize(1800, 700) # Tamanho fixo da tabela

        # Ocultar os números das linhas (cabeçalho vertical)
        self.tabela_Stock.verticalHeader().setVisible(False)

        # Estilo da tabela
        self.tabela_Stock.setStyleSheet("""
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
                width: 1700px;
            }
            QTableWidget::item {
                padding: 10px;
            }
            QTableWidget::item:selected {
                background-color: #505050;
            }
        """)

        self.tabela_Stock.setSelectionBehavior(self.tabela_Stock.SelectRows)
        self.tabela_Stock.setEditTriggers(self.tabela_Stock.NoEditTriggers)
        layout.addWidget(self.tabela_Stock)

        # Botão apagar
        self.botao_apagar = QPushButton("APAGAR PRODUTO SELECIONADO")
        self.botao_apagar.setFixedSize(450, 70)
        self.botao_apagar.setFont(QFont("Inter", 14, QFont.Bold))
        # Estilo do botão apagar
        self.botao_apagar.setStyleSheet("""
            QPushButton {
                background-color: #1E2A38;
                color: white;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #2F3E50;
            }
        """)
        # Conectar o botão apagar à função de apagar Stock
        self.botao_apagar.clicked.connect(self.apagarStockSelecionado)
        layout.addWidget(self.botao_apagar, alignment=Qt.AlignCenter)

        self.centralWidget.setLayout(layout) # Adiciona o layout principal ao widget central

    # Função para carregar dados na tabela de Stock
    def pesquisarStock(self):
        nome = self.input_pesquisa.text().strip()
        if not nome:
            QMessageBox.warning(self, "Atenção", "Introduza um nome para pesquisa.")
            return

        conn = conectarBD() # Conecta á base de dados
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("""
                    SELECT ID_STOCK, Nome_Produto, Preco_Produto, Quantidade_Produto, ID_Fornecedor
                    FROM Stock
                    WHERE Nome_Produto LIKE ?
                """, (f"%{nome}%",)) # Pesquisa por nome parcial
                resultados = cursor.fetchall()

                self.tabela_Stock.setRowCount(0)  # Limpa a tabela antes de preencher
                for row_data in resultados:
                    row = self.tabela_Stock.rowCount()
                    self.tabela_Stock.insertRow(row)
                    for col, data in enumerate(row_data):
                        item = QTableWidgetItem(str(data))
                        item.setTextAlignment(Qt.AlignCenter)
                        self.tabela_Stock.setItem(row, col, item)

                if not resultados:
                    QMessageBox.information(self, "Sem resultados", "Nenhum Produto encontrado.")
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao pesquisar: {e}")
            finally:
                conn.close()

    # Função para apagar o fonnecedor selecionado na tabela
    def apagarStockSelecionado(self):
        row = self.tabela_Stock.currentRow()
        if row == -1:
            QMessageBox.warning(self, "Aviso", "Selecione uma linha da tabela.")
            return

        id_Stock = self.tabela_Stock.item(row, 0).text()
        nome = self.tabela_Stock.item(row, 1).text()

        confirmar = QMessageBox.question(
            self, "Confirmação",
            f"Tem a certeza que deseja apagar o Produto:\n\nID: {id_Stock}\nNome: {nome}?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirmar == QMessageBox.Yes:
            conn = conectarBD()
            if conn:
                cursor = conn.cursor()
                try:
                    cursor.execute("DELETE FROM Stock WHERE ID_Stock = ?", (id_Stock,))
                    conn.commit()
                    self.tabela_Stock.removeRow(row)
                    QMessageBox.information(self, "Sucesso", "Produto apagado com sucesso.")
                except Exception as e:
                    QMessageBox.critical(self, "Erro", f"Erro ao apagar Produto: {e}")
                    conn.rollback()
                finally:
                    conn.close()

    # Função para voltar ao menu anterior
    def voltar(self):
        self.apagarmenu.show()
        self.close()
