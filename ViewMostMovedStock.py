from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QMessageBox, QPushButton
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
import sqlite3

def conectarBD():
    conn = None
    try:
        conn = sqlite3.connect('stockly.db')
        return conn
    except sqlite3.Error as error:
        print(f"Erro ao conectar a base da dados. [{error}]")
        return None
    
class ProdutosMaisMovimentados(QMainWindow):
    def __init__(self, ViewStock_ref):
        super().__init__()
        self.ViewStock = ViewStock_ref
        self.setWindowTitle('Stockly - Produtos mais movimentados')
        self.setGeometry(70, 50, 1800, 1000)
        self.setWindowIcon(QIcon('img/icon.png'))

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        layout = QVBoxLayout()
        self.centralWidget.setStyleSheet("background-color: #C2C2C2;")  # Cor de fundo

        # Layout do botão voltar no canto superior direito
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
        self.buttonBack.clicked.connect(self.voltarAoMenu)
        topBarLayout.addWidget(self.buttonBack)

        layout.addLayout(topBarLayout)


        # Tabela configurada
        self.configurarTabela()
        self.tabela.setColumnCount(5)
        self.tabela.setHorizontalHeaderLabels(["ID STOCK","NOME PRODUTO", "PREÇO DO PRODUTO", "QUANTIDADE", "ID FORNECEDOR"])
        layout.addWidget(self.tabela)

        self.centralWidget.setLayout(layout)  
        self.carregarDados()


    def configurarTabela(self):
        self.tabela = QTableWidget()
        self.tabela.setFont(QFont("Inter", 12))
        self.tabela.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tabela.verticalHeader().setVisible(False)
        self.tabela.verticalHeader().setDefaultSectionSize(50)

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

        self.tabela.horizontalHeader().setStretchLastSection(True)
        self.tabela.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def carregarDados(self):
        conn = conectarBD()
        if conn is None:
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

            for i, linha in enumerate(resultados):
                for j, valor in enumerate(linha):
                    item = QTableWidgetItem(str(valor))
                    item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                    self.tabela.setItem(i, j, item)

            self.tabela.resizeRowsToContents()

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao carregar dados: {e}")
        finally:
            cursor.close()
            conn.close()

    def voltarAoMenu(self):
        self.ViewStock.show()
        self.close()
