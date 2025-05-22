from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QMessageBox, QPushButton
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
import sqlite3

# Função para conectar á base de dados
def conectarBD():
    conn = None
    try:
        conn = sqlite3.connect('stockly.db')
        return conn
    except sqlite3.Error as error:
        print(f"Erro ao conectar a base da dados. [{error}]")
        return None
    
# Classe para visualizar stock mais movimentado    
class ProdutosMaisMovimentados(QMainWindow):
    def __init__(self, ViewStock_ref):# Construtor da classe
        super().__init__() # Inicializa a classe pai
        self.ViewStock = ViewStock_ref # Referência ao menu de visualizar registos
        self.setWindowTitle('Stockly - Produtos mais movimentados') # Definir título da janela
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
        # Estilo do botão voltar
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
        self.buttonBack.clicked.connect(self.voltarAoMenu)
        topBarLayout.addWidget(self.buttonBack)

        layout.addLayout(topBarLayout) # Adiciona o layout do botão voltar


        # Tabela configurada
        self.configurarTabela()
        self.tabela.setColumnCount(5)
        self.tabela.setHorizontalHeaderLabels(["ID STOCK","NOME PRODUTO", "PREÇO DO PRODUTO", "QUANTIDADE", "ID FORNECEDOR"])
        layout.addWidget(self.tabela)

        self.centralWidget.setLayout(layout)  
        self.carregarDados()


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

    # Função para carregar dados na tabela
    def carregarDados(self):
        conn = conectarBD() # Conectar à base de dados
        if conn is None: # Verifica se a conexão foi bem-sucedida
            QMessageBox.critical(self, "Erro", "Não foi possível ligar à base de dados.")
            return

        cursor = conn.cursor()
        try:
            # Exemplo de query que assume uma tabela de movimentos e produtos
            cursor.execute("""
                SELECT 
                    p.ID_Stock, 
                    p.Nome_Produto,
                    p.Preco_Produto, 
                    SUM(m.Quantidade_Produto) as TotalMovimentado,
                    p.ID_Fornecedor
                FROM 
                    Stock m
                JOIN 
                    Stock p ON m.ID_Stock = p.ID_Stock
                GROUP BY 
                    p.ID_Stock, p.Nome_Produto, p.Preco_Produto
                ORDER BY 
                    TotalMovimentado DESC
                LIMIT 20
            """)
            resultados = cursor.fetchall()
            self.tabela.setRowCount(len(resultados))

            # Preenche a tabela com os dados 
            for i, linha in enumerate(resultados):
                for j, valor in enumerate(linha):
                    item = QTableWidgetItem(str(valor))
                    item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                    self.tabela.setItem(i, j, item)

            self.tabela.resizeRowsToContents()

         # Verifica se a tabela está vazia
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao carregar dados: {e}")
        finally:
            cursor.close()
            conn.close()

    # Função para voltar ao menu
    def voltarAoMenu(self):
        self.ViewStock.show()
        self.close()
