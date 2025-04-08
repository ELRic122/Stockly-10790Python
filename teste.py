from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout, QVBoxLayout
from PyQt5.QtGui import QPixmap, QFont, QPalette, QBrush
from PyQt5.QtCore import Qt
import sys

class MenuWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Principal")
        self.setFixedSize(700, 500)
        self.setup_ui()

    def setup_ui(self):
        # Fundo
        fundo_pixmap = QPixmap("C:/Users/jeanc/Desktop/fundo.jpg").scaled(self.size(), Qt.KeepAspectRatioByExpanding)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(fundo_pixmap))
        self.setPalette(palette)

        layout = QGridLayout()
        layout.setContentsMargins(100, 150, 100, 150)
        layout.setSpacing(20)

        btn_style = """
            QPushButton {
                background-color: #0066cc;
                color: white;
                border: none;
                padding: 10px 20px;
                font: bold 14px Verdana;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #004080;
            }
        """

        botoes = [
            ("Inserir Registos", self.abrir_submenu),
            ("Apagar Registos", self.abrir_submenu),
            ("Visualizar Registos", self.abrir_submenu),
            ("Editar Registos", self.abrir_submenu),
        ]

        for i, (texto, funcao) in enumerate(botoes):
            btn = QPushButton(texto)
            btn.setStyleSheet(btn_style)
            btn.clicked.connect(funcao)
            layout.addWidget(btn, i // 2, i % 2)

        self.setLayout(layout)

    def abrir_submenu(self):
        self.submenu = SubMenuWindow(self)
        self.submenu.show()
        self.hide()

class SubMenuWindow(QWidget):
    def __init__(self, menu_anterior):
        super().__init__()
        self.setWindowTitle("Submenu")
        self.setFixedSize(700, 500)
        self.menu_anterior = menu_anterior
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        btn_voltar = QPushButton("← Voltar")
        btn_voltar.setFont(QFont("Verdana", 12))
        btn_voltar.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #0066cc;
                border: none;
                font-weight: bold;
            }
            QPushButton:hover {
                color: #004080;
            }
        """)
        btn_voltar.clicked.connect(self.voltar_menu)

        titulo = QLabel("Página de Submenu")
        titulo.setFont(QFont("Verdana", 16, QFont.Bold))
        titulo.setStyleSheet("color: #333;")
        titulo.setAlignment(Qt.AlignCenter)

        layout.addWidget(btn_voltar, alignment=Qt.AlignLeft)
        layout.addWidget(titulo)
        layout.addStretch()
        self.setLayout(layout)

    def voltar_menu(self):
        self.menu_anterior.show()
        self.close()

# Iniciar app
app = QApplication(sys.argv)
window = MenuWindow()
window.show()
sys.exit(app.exec_())
