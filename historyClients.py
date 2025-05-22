from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QMessageBox, QTableWidgetItem, QTableWidget, QHeaderView, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QFont
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

# Classe do histórico de Clientes
class HistoricoClientes(QMainWindow): 
    def __init__(self, viewClientsClass_ref): # Construtor da classe
        super().__init__() # Inicializa a classe pai
        self.ViewClients = viewClientsClass_ref # Referência ao menu de visualizar registos
        self.setWindowTitle('Stockly - Histórico de Alterações dos Clientes')
        self.setGeometry(70, 50, 1800, 1000) # Definir tamanho da janela
        self.setWindowIcon(QIcon('img/icon.png')) # Definir ícone da janela

        self.centralWidget = QWidget() # Cria um widget central
        self.setCentralWidget(self.centralWidget) # Define o widget central da janela
        layout = QVBoxLayout() # Layout principal vertical
        self.centralWidget.setStyleSheet("background-color: #C2C2C2;")  # Cor de fundo

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

        titulo = QLabel("Últimas Alterações aos Clientes")
        titulo.setFont(QFont("Inter", 20))
        titulo.setStyleSheet("color: #112233; margin-bottom: 20px;")
        layout.addWidget(titulo)

        # Tabela configurada
        self.configurarTabela()
        self.tabela.setColumnCount(5)
        self.tabela.setHorizontalHeaderLabels(["ID CLIENTE","CAMPO ALTERADO", "VALOR ANTIGO", "VALOR NOVO", "DATA ALTERAÇÃO"])
        layout.addWidget(self.tabela)

        self.centralWidget.setLayout(layout)  
        self.carregarHistorico()


    # Função para configurar a tabela
    def configurarTabela(self):
        self.tabela = QTableWidget()
        self.tabela.setFont(QFont("Inter", 12))
        self.tabela.setEditTriggers(QTableWidget.NoEditTriggers) # Não permite edição
        self.tabela.verticalHeader().setVisible(False) # Oculta o cabeçalho vertical
        self.tabela.verticalHeader().setDefaultSectionSize(50) # Define a altura padrão das linhas

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

    def carregarHistorico(self):
        conn = conectarBD()
        if conn is None:
            QMessageBox.critical(self, "Erro", "Erro ao ligar à base de dados.")
            return

        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT id_cliente, campo_alterado, valor_antigo, valor_novo, data_alteracao
                FROM historico_cliente
                ORDER BY data_alteracao DESC
                LIMIT 100
            """)
            resultados = cursor.fetchall()
            self.tabela.setRowCount(len(resultados))

            for i, linha in enumerate(resultados):
                for j, valor in enumerate(linha):
                    item = QTableWidgetItem(str(valor) if valor else "-")
                    item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                    self.tabela.setItem(i, j, item)

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao carregar histórico: {e}")
        finally:
            cursor.close()
            conn.close()

    # Função para voltar tabela dos Clientes
    def voltarAoMenu(self):
        self.ViewClients.show()
        self.close()