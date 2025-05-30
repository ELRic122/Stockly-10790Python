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
    
# Classe da janela de alteração de cliente
class AlterarCliente(QMainWindow):
    def __init__(self, alterMenuClass_ref):
        super().__init__()
        self.alterMenuClass_ref = alterMenuClass_ref# Referência ao menu de Alterar registos

        self.setWindowTitle("Stockly - Gestão de Inventário") # Definir título da janela
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
        label_pesquisa = QLabel("Nome do cliente:")
        label_pesquisa.setFont(QFont("Inter", 16))
        self.input_pesquisa = QLineEdit()
        self.input_pesquisa.setPlaceholderText("Pesquisar cliente...")

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
        self.botao_pesquisar.clicked.connect(self.carregarCliente)

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

        # Criar campos para: Nome, Contacto, Data Nascimento, Morada
        for campo in ["Nome", "Contacto", "Data Nascimento", "Morada"]:
            container = QVBoxLayout()
            
            # Rótulo
            label = QLabel(campo + ":")
            label.setFont(QFont("Inter", 14))
            label.setStyleSheet("color: black; margin-bottom: 5px;")

            # Campo de entrada
            entrada = QLineEdit()
            entrada.setFixedHeight(40)
            entrada.setStyleSheet(estilo_entrada)

            # Adiciona o campo ao dicionário com chave normalizada (sem espaços e lowercase)
            self.campos[campo.lower().replace(" ", "_")] = entrada

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
        self.id_cliente = None # Guarda o ID do cliente carregado para alteração

    # Função para carregar os dados de um cliente com base no nome pesquisado
    def carregarCliente(self):
        nome = self.input_pesquisa.text().strip()
        if not nome:
            QMessageBox.warning(self, "Aviso", "Introduza um nome.")
            return
        conn = conectarBD()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT ID_Cliente, Nome, Contacto, Data_Nascimento, Morada FROM cliente WHERE Nome LIKE ? LIMIT 1", (f"%{nome}%",))
            resultado = cursor.fetchone()
            conn.close()

            if resultado:
                # Preencher os campos com os dados do cliente
                self.id_cliente = resultado[0]
                self.campos["nome"].setText(resultado[1])
                self.campos["contacto"].setText(str(resultado[2]))
                self.campos["data_nascimento"].setText(str(resultado[3]))
                self.campos["morada"].setText(resultado[4])
            else:
                QMessageBox.information(self, "Sem resultados", "Cliente não encontrado.")

    # Função para guardar as alterações feitas aos dados do cliente
    def guardarAlteracoes(self):
        if not self.id_cliente:
            QMessageBox.warning(self, "Erro", "Nenhum cliente carregado.")
            return
        conn = conectarBD()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("""
                    UPDATE cliente
                    SET Nome = ?, Contacto = ?, Data_Nascimento = ?, Morada =?
                    WHERE ID_Cliente = ?
                """, (
                    self.campos["nome"].text(),
                    self.campos["contacto"].text(),
                    self.campos["data_nascimento"].text(),
                    self.campos["morada"].text(),
                    self.id_cliente
                ))
                conn.commit()
                QMessageBox.information(self, "Sucesso", "Cliente atualizado com sucesso.")
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao atualizar: {e}")
                conn.rollback()
            finally:
                conn.close()

    # Função para voltar ao menu anterior
    def voltar(self):
        self.alterMenuClass_ref.show()
        self.close()
