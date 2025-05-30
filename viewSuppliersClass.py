from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QMessageBox, QTableWidgetItem, QTableWidget, QHeaderView, QLineEdit, QFrame, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
import sqlite3
from exportAsPDF import exportPDF_Fornecedores
from HistorySupplier import HistoricoFornecedores

# Função para conectar à base de dados
def conectarBD():
    conn = None
    try:
        conn = sqlite3.connect('stockly.db')
        return conn
    except sqlite3.Error as error:
        print(f"Erro ao conectar a base da dados. [{error}]")
        return None
    
# Classe para visualizar fornecedores
class VisualizarFornecedores(QMainWindow):
    def __init__(self,ViewMenu_ref): # Construtor da classe
        super().__init__() # Inicializa a classe pai
        self.ViewMenu = ViewMenu_ref # Referência ao menu de visualizar registos

        self.setWindowTitle('Stockly - Vizualizar Fornecedores') # Definir título da janela
        self.setGeometry(70, 50, 1800, 1000) # Definir tamanho da janela
        self.setWindowIcon(QIcon('img/icon.png')) # Definir ícone da janela

        self.centralWidget = QWidget() # Cria um widget central
        self.setCentralWidget(self.centralWidget) # Define o widget central da janela
        layout = QVBoxLayout() # Layout principal vertical
        self.centralWidget.setStyleSheet("background-color: #C2C2C2;")  # Cor de fundo

        
        # Total de Fornecedores
        self.totalFornecedores = QLabel('Total de Fornecedores: 0')
        self.totalFornecedores.setStyleSheet("color: #112233; font-size: 14px; font-weight: bold;")

        # Layout da barra de pesquisa
        barra_layout = QHBoxLayout()
        barra_layout.setAlignment(Qt.AlignCenter)

        # Frame para a barra de pesquisa
        frame_pesquisa = QFrame()
        frame_pesquisa.setFixedSize(420, 40)
        frame_pesquisa.setStyleSheet("background-color: transparent;")

        # Campo de pesquisa
        self.pesquisa = QLineEdit(frame_pesquisa)
        self.pesquisa.setPlaceholderText("Pesquisar...")
        self.pesquisa.setGeometry(0, 0, 420, 40)
        # Estilo do campo de pesquisa
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

        # Botão de pesquisa
        lupa = QPushButton(frame_pesquisa)
        lupa.setIcon(QIcon("img/lupa.png"))
        lupa.setGeometry(380, 5, 30, 30)
        # Estilo do botão de pesquisa
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

        layout.addLayout(topBarLayout) # Adiciona o botão voltar ao layout

        # Adiciona a barra de pesquisa ao layout
        barra_layout.addWidget(frame_pesquisa)
        layout.addSpacing(30) 
        layout.addLayout(barra_layout)
        layout.addSpacing(10)

        # Layout horizontal para Total de Fornecedores + Botão PDF
        linha_info_layout = QHBoxLayout()
        linha_info_layout.addWidget(self.totalFornecedores)

        # Botão de exportar para pdf
        self.buttonPDF = QPushButton("Download Lista Fornecedores")
        self.buttonPDF.setFixedSize(300, 50)
        self.buttonPDF.setStyleSheet("""
            QPushButton {
                font-size: 14px;
                font-weight: bold;
                background-color: #1e2c3a;
                color: white;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #2f3e50;
            }
        """)

        # Botão do Histórico de alterações
        self.botaoHistoricoFornecedores = QPushButton("Histórico de Alterações")
        self.botaoHistoricoFornecedores.setFixedSize(300, 50)
        self.botaoHistoricoFornecedores.setStyleSheet("""
            QPushButton {
                font-size: 14px;
                font-weight: bold;
                background-color: #1e2c3a;
                color: white;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #2f3e50;
            }
        """)

        # Adiciona o layout do botão do histórico de alterações
        self.botaoHistoricoFornecedores.clicked.connect(self.gotoHistoricoFornecedores)
        linha_info_layout.addWidget(self.botaoHistoricoFornecedores)

        # Adiciona o layout do botão para exportar para pdf
        self.buttonPDF.clicked.connect(exportPDF_Fornecedores)
        linha_info_layout.addWidget(self.buttonPDF)
        linha_info_layout.addStretch()

        layout.addLayout(linha_info_layout)     

        # Tabela configurada
        self.configurarTabela()
        self.tabela.setColumnCount(5) # Definir número de colunas
        self.tabela.setHorizontalHeaderLabels(["ID Fornecedor","NOME", "CONTACTO", "MORADA", "NIF"]) # Definir nomes das colunas
        layout.addWidget(self.tabela)

        # Adiciona a tabela ao layout
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

    # Funcão para criar a tabela
    def configurarTabela(self):
        self.tabela = QTableWidget()
        self.tabela.setFont(QFont("Inter", 12))
        self.tabela.setEditTriggers(QTableWidget.NoEditTriggers) # Não permite editar as células
        self.tabela.verticalHeader().setVisible(False) # Esconde o cabeçalho vertical
        self.tabela.verticalHeader().setDefaultSectionSize(50) # Define o tamanho padrão das linhas

        # Estilo da tabela
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


        # Função para carregar os dados na tabela
    def carregarDados(self):
        conn = conectarBD() # Conectar à base de dados
        if conn is None:
            QMessageBox.critical(self, "Erro", "Não foi possível ligar à base de dados.")
            return

        cursor = conn.cursor()
        try:
            cursor.execute("SELECT ID_Fornecedor, Nome, Contacto, Morada, NIF FROM Fornecedores") # Seleciona os dados da tabela Fornecedores
            resultados = cursor.fetchall() 
            self.tabela.setRowCount(len(resultados)) # Define o número de linhas da tabela

            # Preenche a tabela com os dados
            for i, linha in enumerate(resultados):
                for j, valor in enumerate(linha):
                    item = QTableWidgetItem(str(valor))
                    item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                    self.tabela.setItem(i, j, item)

        # Verifica se a tabela está vazia
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao carregar dados: {e}")
        finally:
            cursor.close()
            conn.close()

    # Função para voltar ao menu
    def voltarAoMenu(self):
        self.ViewMenu.show()
        self.close()

    # Função para ir para o histórico de alterações
    def gotoHistoricoFornecedores(self):
        self.HistoricoFornecedores = HistoricoFornecedores(self)
        self.HistoricoFornecedores.show()
        self.hide()