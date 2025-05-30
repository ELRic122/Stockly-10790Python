import sys
import sqlite3
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QMessageBox, QTableWidgetItem, QTableWidget, QHeaderView, QLabel, QPushButton, QDialog, QApplication
from PyQt5.QtGui import QIcon, QFont, QColor
from PyQt5.QtCore import Qt

def procurar_produtos_stock():
    """Procura os dados da base de dados."""
    conn = sqlite3.connect('stockly.db')
    cursor = conn.cursor()
    cursor.execute("SELECT ID_Stock, Nome_Produto, Quantidade_Produto FROM stock")
    produtos = cursor.fetchall()
    conn.close()
    return produtos

class TabelaStockPopup(QMainWindow):
    def __init__(self, viewstockClass_ref):
        super().__init__()
        self.ViewStock = viewstockClass_ref # Referência ao menu de visualizar registos
        self.setWindowTitle('Stockly - Status do Stock')
        self.setGeometry(70, 50, 1800, 1000) # Definir tamanho da janela
        self.setWindowIcon(QIcon('img/icon.png')) # Definir ícone da janela
        central_widget = QWidget()
        central_widget.setStyleSheet("background-color: #C2C2C2;")
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)  # Cor de fundo

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
        layout.addLayout(topBarLayout)

        self.label_titulo = QLabel("Gestão de Stock")
        self.label_titulo.setFont(QFont("Segoe UI", 16, QFont.Bold))
        self.label_titulo.setAlignment(Qt.AlignCenter)
        self.label_titulo.setStyleSheet("color: #333333; margin-bottom: 15px;")
        layout.addWidget(self.label_titulo)

        self.tabela = QTableWidget()
        layout.addWidget(self.tabela)

        self.carregar_dados()
        self.aplicar_estilo()

    def criar_item(self, texto, alinhamento=Qt.AlignLeft):
        item = QTableWidgetItem(texto)
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        item.setTextAlignment(alinhamento)
        item.setFont(QFont("Inter", 11))
        return item

    def carregar_dados(self):
        produtos = procurar_produtos_stock()
        self.tabela.setRowCount(len(produtos))
        self.tabela.setColumnCount(4)
        self.tabela.setHorizontalHeaderLabels(["ID", "Produto", "Quantidade", "Status"])

        for linha, produto in enumerate(produtos):
            id_stock, nome_produto, quantidade_produto = produto
            quantidade_produto = int(quantidade_produto)

            #status e cor
            if quantidade_produto == 0:
                status_texto = "❌ Sem Stock"
                cor_fundo = QColor(255, 102, 102)
                cor_texto = QColor(255, 255, 255)
            elif quantidade_produto <= 10:
                status_texto = "⚠️ Stock Crítico"
                cor_fundo = QColor(255, 204, 102)
                cor_texto = QColor(60, 30, 0)
            else:
                status_texto = "✅ Com Stock"
                cor_fundo = QColor(153, 255, 153)
                cor_texto = QColor(0, 80, 0)

            item_id = self.criar_item(str(id_stock), Qt.AlignCenter)
            item_nome = self.criar_item(nome_produto)
            item_quantidade = self.criar_item(str(quantidade_produto), Qt.AlignCenter)
            item_status = self.criar_item(status_texto, Qt.AlignCenter)

            for item in [item_id, item_nome, item_quantidade, item_status]:
                item.setBackground(cor_fundo)
                item.setForeground(cor_texto)

            self.tabela.setItem(linha, 0, item_id)
            self.tabela.setItem(linha, 1, item_nome)
            self.tabela.setItem(linha, 2, item_quantidade)
            self.tabela.setItem(linha, 3, item_status)

        self.tabela.resizeColumnsToContents()
        self.tabela.setAlternatingRowColors(True)
        self.tabela.horizontalHeader().setStretchLastSection(True)

    def aplicar_estilo(self):
        # Estilo geral da tabela
        self.tabela.setStyleSheet("""
            QTableWidget {
                background-color: #2b2b2b;
                border: 1px solid #d0d7de;
                border-radius: 6px;
                gridline-color: #d0d7de;
                font-family: "Inter";
                font-size: 12pt;
            }
            QHeaderView::section {
                background-color: #3c3c3c;
                color: white;
                padding: 8px;
                font-weight: 600;
                border: none;
                font-size: 13pt;
                font-family: "Inter";
            }
            QTableWidget::item {
                padding: 8px;
            }
            QTableWidget::item:selected {
                background-color: #b3d4fc;
                color: #023e8a;
            }
        """)

    # Função para voltar tabela do Stock
    def voltarAoMenu(self):
        self.ViewStock.show()
        self.close()

class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestão de Stock")
        self.resize(400, 200)
        self.setStyleSheet("background-color: #f8f9fa;")

        layout = QVBoxLayout()
        self.botao_abrir = QPushButton("Mostrar Stock")
        self.botao_abrir.setFont(QFont("Inter", 14))
        self.botao_abrir.setStyleSheet("""
            QPushButton {
                background-color: #4a90e2;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 12px 20px;
            }
            QPushButton:hover {
                background-color: #357ABD;
            }
        """)
        self.botao_abrir.clicked.connect(self.abrir_popup)

        layout.addStretch()
        layout.addWidget(self.botao_abrir, alignment=Qt.AlignCenter)
        layout.addStretch()
        self.setLayout(layout)

    def abrir_popup(self):
        self.popup = TabelaStockPopup(self)
        self.popup.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = JanelaPrincipal()
    janela.show()
    sys.exit(app.exec_())

    
