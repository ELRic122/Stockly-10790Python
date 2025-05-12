from fpdf import FPDF
import mysql.connector

def conectarBD():
    conn = None
    try:
        conn = mysql.connector.connect(user='root', host='localhost', database='stockly', autocommit=True)
        return conn
    except mysql.connector.Error as error:
        print(f"Erro ao conectar a base da dados. [{error}]")
        return None

def PDF(self):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Lista de Clientes", ln=True, align="C")
    pdf.ln(10)

    # Conectar à Base de Dados Cliente
    conn = conectarBD()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT ID_Cliente, Nome, Contacto, Data_Nascimento, Morada FROM cliente")
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
    pdf.output("clientes.pdf")