from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QMessageBox, QTableWidgetItem, QTableWidget, QHeaderView, QLineEdit, QFrame
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
import mysql.connector

def conectarBD():
    conn = None
    try:
        conn = mysql.connector.connect(user='root', host='localhost', database='stockly', autocommit=True)
        return conn
    except mysql.connector.Error as error:
        print(f"Erro ao conectar a base da dados. [{error}]")
        return None
    
class VisualizarStock(QMainWindow):
    def __init__(self, ViewMenu_ref):
        super().__init__()
        self.ViewMenu = ViewMenu_ref
        self.setWindowTitle('Stockly - Visualizar Stock')
        self.setGeometry(70, 50, 1800, 1000)
        self.setWindowIcon(QIcon('img/icon.png'))

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        layout = QVBoxLayout()
        
        # Layout da barra de pesquisa
        barra_layout = QHBoxLayout()
        barra_layout.setAlignment(Qt.AlignCenter)

        frame_pesquisa = QFrame()
        frame_pesquisa.setFixedSize(420, 40)
        frame_pesquisa.setStyleSheet("background-color: transparent;")

        self.pesquisa = QLineEdit(frame_pesquisa)
        self.pesquisa.setPlaceholderText("Pesquisar...")
        self.pesquisa.setGeometry(0, 0, 420, 40)
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

        lupa = QPushButton(frame_pesquisa)
        lupa.setIcon(QIcon("img/lupa.png"))
        lupa.setGeometry(380, 5, 30, 30)
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

        barra_layout.addWidget(frame_pesquisa)
        layout.addSpacing(30) 
        layout.addLayout(barra_layout)
        layout.addSpacing(10)

        # Tabela configurada
        self.configurarTabela()
        self.tabela.setColumnCount(5)
        self.tabela.setHorizontalHeaderLabels(["ID STOCK","NOME PRODUTO", "PREÇO DO PRODUTO", "QUANTIDADE", "ID FORNECEDOR"])
        layout.addWidget(self.tabela)

        self.centralWidget.setLayout(layout)  
        self.carregarDados()

        self.pesquisa.textChanged.connect(self.filtrarTabela) # Pesquisa

    # Funcao de filtrar a tabela para pesquisa
    def filtrarTabela(self, texto):
        texto = texto.lower()
        for i in range(self.tabela.rowCount()):
            linhaVisivel = False
            for j in range(self.tabela.columnCount()):
                item = self.tabela.item(i, j)
                if item and texto in item.text().lower():
                    linhaVisivel = True
                    break
            self.tabela.setRowHidden(i, not linhaVisivel)

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
            cursor.execute("SELECT ID_Stock, Nome_Produto, Preco_Produto, Quantidade_Produto, ID_Fornecedor FROM Stock")
            resultados = cursor.fetchall()
            self.tabela.setRowCount(len(resultados))

            for i, linha in enumerate(resultados):
                for j, valor in enumerate(linha):
                    item = QTableWidgetItem(str(valor))
                    item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                    self.tabela.setItem(i, j, item)

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao carregar dados: {e}")
        finally:
            cursor.close()
            conn.close()
    
    def voltarAoMenu(self):
        self.ViewMenu.show()
        self.close()