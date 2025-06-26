from fpdf import FPDF
import sqlite3
import os

def conectarBD():
    conn = None
    try:
        conn = sqlite3.connect('stockly.db')
        return conn
    except sqlite3.Error as error:
        print(f"Erro ao conectar a base da dados. [{error}]")
        return None

# B - Bold (negrito)
    #     # I - Italic (itálico)  
    #     # u - Underline (sublinhado)
    #     # C - Center (centralizado)
    #     # L - Left (esquerda)
    #     # R - Right (direita)

#Cria a pasta 'documentos' caso a mesma nao exista, para guardar os PDF's
os.makedirs('documentos', exist_ok=True)

def exportPDF_Clientes(self):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.set_auto_page_break(auto=True, margin=15)

    # Titulo
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Lista de Clientes", ln=True, align="C")
    pdf.ln(10)

    # Conectar à Base de Dados Cliente
    conn = conectarBD()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT ID_Cliente, Nome, Contacto, Data_Nascimento, Morada FROM Cliente")
        resultados = cursor.fetchall()
        
        pdf.set_font("Arial", size=11)
        for cliente in resultados:
            linha = f"ID: {cliente[0]} | Nome: {cliente[1]} | Contacto: {cliente[2]} | Data: {cliente[3]} | Morada: {cliente[4]}"
            pdf.multi_cell(0, 10, linha)
            pdf.ln(2)
        cursor.close()
        conn.close()
    else:
        pdf.cell(0, 10, "Erro a ligar à base de dados.", ln=True)
    # Guardar
    pdf.output("documentos/clientes.pdf")

def exportPDF_Fornecedores(self):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.set_auto_page_break(auto=True, margin=15)

    # Titulo
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Lista de Fornecedores", ln=True, align="C")
    pdf.ln(10)

    # Conectar à Base de Dados Cliente
    conn = conectarBD()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT ID_Fornecedor, Nome, Contacto, Morada, NIF FROM Fornecedores")
        resultados = cursor.fetchall()
        
        pdf.set_font("Arial", size=11)
        for forn in resultados:
            linha = f"ID: {forn[0]} | Nome: {forn[1]} | Contacto: {forn[2]} | Morada: {forn[3]} | NIF: {forn[4]}"
            pdf.multi_cell(0, 10, linha)
            pdf.ln(2)

        cursor.close()
        conn.close()
    else:
        pdf.cell(0, 10, "Erro a ligar à base de dados.", ln=True)
    # Guardar
    pdf.output("documentos/fornecedores.pdf")

def exportPDF_Stock(self):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.set_auto_page_break(auto=True, margin=15)

    # Titulo
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Lista de Stock", ln=True, align="C")
    pdf.ln(10)

    # Conectar à Base de Dados Cliente
    conn = conectarBD()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT ID_Stock, Nome_Produto, Preco_Produto, Quantidade_Produto, ID_Fornecedor FROM Stock")
        resultados = cursor.fetchall()
        
        pdf.set_font("Arial", size=11)
        for stock in resultados:
            linha = f"ID Stock: {stock[0]} | Nome: {stock[1]} | Preco: {str(stock[2]).replace('€', ' EUR')} | Quantidade: {stock[3]} | ID_Fornecedor: {stock[4]}"
            pdf.multi_cell(0, 10, linha)
            pdf.ln(2)

        cursor.close()
        conn.close()
    else:
        pdf.cell(0, 10, "Erro a ligar à base de dados.", ln=True)
    # Guardar
    pdf.output("documentos/stock.pdf")

def exportPDF_Vendas(self):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.set_auto_page_break(auto=True, margin=15)

    # Titulo
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Lista de Vendas", ln=True, align="C")
    pdf.ln(10)

    # Conectar à Base de Dados Cliente
    conn = conectarBD()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT ID_Venda, Nome_Produto, Preco_Venda, Quantidade_Venda, ID_Stock, ID_Cliente FROM Vendas")
        resultados = cursor.fetchall()
        
        pdf.set_font("Arial", size=11)
        for venda in resultados:
            linha = f"ID_Venda: {venda[0]} | Nome_Produto: {venda[1]} | Preco_Venda: {str(venda[2]).replace('€', ' EUR')}  | Quantidade_Venda: {venda[3]} | ID_Stock: {venda[4]} | ID_Cliente: {venda[5]}"
            pdf.multi_cell(0, 10, linha)
            pdf.ln(2)

        cursor.close()
        conn.close()
    else:
        pdf.cell(0, 10, "Erro a ligar à base de dados.", ln=True)
    # Guardar
    pdf.output("documentos/vendas.pdf")