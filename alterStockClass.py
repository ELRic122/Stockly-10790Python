from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
import sqlite3

# Função para conectar à base de dados
def conectarBD():
    conn = None
    try:
        conn = sqlite3.connect('stockly.db')# Nome do ficheiro da base de dados
        return conn
    except sqlite3.Error as error:
        print(f"Erro ao conectar a base da dados. [{error}]")
        return None
    
# Classe da janela de alteração de Stock
class AlterarStock(QMainWindow):
    def __init__(self, alterMenuClass_ref):
        super().__init__()
        self.alterMenuClass_ref = alterMenuClass_ref# Referência ao menu de Alterar registos

        self.setWindowTitle("Stockly - Alterar Produtos") # Definir título da janela
        self.setGeometry(70, 50, 1800, 1000) # Definir tamanho da janela
        self.setWindowIcon(QIcon('img/icon.png')) # Definir ícone da janela

        self.centralWidget = QWidget() # Cria um widget central
        self.setCentralWidget(self.centralWidget) # Define o widget central da janela
        layout = QVBoxLayout() # Layout principal vertical
        self.centralWidget.setStyleSheet("background-color: #C2C2C2;")  # Cor de fundo

        # Topo com botão voltar
        topBarLayout = QHBoxLayout()
        topBarLayout.addStretch()
        self.botao_Voltar = QPushButton("←")
        self.botao_Voltar.setFixedSize(60, 60)
        self.botao_Voltar.setStyleSheet("""
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
        self.botao_Voltar.clicked.connect(self.voltar)
        topBarLayout.addWidget(self.botao_Voltar)
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
        self.botao_pesquisar.setFixedSize(150, 50)
        # Estilo do botão pesquisar
        self.botao_pesquisar.setStyleSheet("""
            QPushButton {
                background-color: #1E2A38;
                color: white;
                border-radius: 10px;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: #2F3E50;
            }
        """)
        # Conectar o botão pesquisar à função de pesquisa
        self.botao_pesquisar.clicked.connect(self.carregarStock)

        # Adicionar widgets ao layout de pesquisa
        pesquisaLayout.addWidget(label_pesquisa)
        pesquisaLayout.addWidget(self.input_pesquisa)
        pesquisaLayout.addWidget(self.botao_pesquisar)
        pesquisaLayout.addStretch()  # empurra tudo para a esquerda

        layout.addLayout(pesquisaLayout)
        layout.addSpacing(20)

        # Campos de edição
        self.campos = {}
        formLayout = QHBoxLayout()
        # Campos de edição
        formLayout = QVBoxLayout()
        formLayout.setSpacing(20)

        estilo_entrada = """
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
        """

        campos_def = {
                "nome_do_produto": "Nome do Produto",
                "preco_do_produto": "Preço do Produto",
                "quantidade_de_produto": "Quantidade de Produto",
                "id_fornecedor": "ID Fornecedor"
}
        # Criar campos para: Nome do Produto, Preço do Produto, Quantidade de Produto, ID Fornecedor
        for chave, rotulo in campos_def.items():
            container = QVBoxLayout()
            
            # Rótulo
            label = QLabel(rotulo + ":")
            label.setFont(QFont("Inter", 14))
            label.setStyleSheet("color: black; margin-bottom: 5px;")

            # Campo de entrada
            entrada = QLineEdit()
            entrada.setFixedHeight(40)
            entrada.setStyleSheet(estilo_entrada)

            # Adiciona o campo ao dicionário com chave normalizada (sem espaços e lowercase)
            self.campos[chave] = entrada

            # Adiciona ao layout do campo
            container.addWidget(label)
            container.addWidget(entrada)

            formLayout.addLayout(container)

        layout.addLayout(formLayout)


        # Botão de guardar alterações
        self.botao_Guardar = QPushButton("GUARDAR ALTERAÇÕES")
        self.botao_Guardar.setFixedSize(450, 70)
        self.botao_Guardar.setStyleSheet("""
            QPushButton {
                background-color: #1E2A38;
                color: white;
                border-radius: 15px;
                font-size: 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2F3E50;
            }
        """)
        self.botao_Guardar.clicked.connect(self.guardarAlteracoes)
        layout.addWidget(self.botao_Guardar, alignment=Qt.AlignCenter)

        # Aplica o layout à janela
        self.centralWidget.setLayout(layout)
        self.id_Stock = None # Guarda o ID do Stock carregado para alteração

    # Função para carregar os dados de um Produto com base no nome pesquisado
    def carregarStock(self):
        nome = self.input_pesquisa.text().strip()
        if not nome:
            QMessageBox.warning(self, "Aviso", "Introduza um nome.")
            return
        conn = conectarBD()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT ID_Stock, Nome_Produto, Preco_Produto, Quantidade_Produto, ID_Fornecedor FROM Stock WHERE Nome_Produto LIKE ? LIMIT 1", (f"%{nome}%",))
            resultado = cursor.fetchone()
            conn.close()

            if resultado:
                # Preencher os campos com os dados do Stock
                self.id_Stock = resultado[0]
                self.campos["nome_do_produto"].setText(resultado[1])
                self.campos["preco_do_produto"].setText(str(resultado[2]))
                self.campos["quantidade_de_produto"].setText(str(resultado[3]))
                self.campos["id_fornecedor"].setText(str(resultado[4]))


            else:
                QMessageBox.information(self, "Sem resultados", "Produto não encontrado.")

    # Função para guardar as alterações feitas aos dados do Stock
    def guardarAlteracoes(self):
        if not self.id_Stock:
            QMessageBox.warning(self, "Erro", "Nenhum Produto carregado.")
            return
        conn = conectarBD()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("""
                    UPDATE Stock
                    SET Nome_Produto = ?, Preco_Produto = ?, Quantidade_Produto = ?, ID_Fornecedor = ?
                    WHERE ID_Stock = ?
                """, (
                    self.campos["nome_do_produto"].text(),
                    self.campos["preco_do_produto"].text(),
                    self.campos["quantidade_de_produto"].text(),
                    self.campos["id_fornecedor"].text(),
                    self.id_Stock
                    ))
                conn.commit()
                QMessageBox.information(self, "Sucesso", "Produto atualizado com sucesso.")
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao atualizar: {e}")
                conn.rollback()
            finally:
                conn.close()

    # Função para voltar ao menu anterior
    def voltar(self):
        self.alterMenuClass_ref.show()
        self.close()
