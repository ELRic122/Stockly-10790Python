# bibliotecas utilizadas
import sqlite3
import mysql.connector

# caminho base de dados
path = '../stockly.db'

def connectDB():
    conn = None
    try:
        conn = mysql.connector.connect(user='root', host='localhost', database='stockly', autocommit=True)
        print('Conectado a base de dados com sucesso!')
        return conn
    except mysql.connector.Error as error:
        print(f'Erro ao conectar a base de dados. [{error}]')
        return None
    
def viewRecords(table):
    conn = connectDB()
    if conn:
        cursos = conn.cursor()

        if table == 'cliente':
            cursos.execute(f'SELECT * FROM {table}')
            records = cursos.fetchall()
            for record in records:
                print(f'ID cliente: {record[0]} | Nome cliente: {record[1]} | Contacto cliente: {record[2]} | Data Nascimento: {record[3]} | Morada: {record[4]}')
        elif table == 'fornecedores':
            cursos.execute(f'SELECT * FROM {table}')
            records = cursos.fetchall()
            for record in records:
                print(f'ID fornecedor: {record[0]} | Nome fornecedor: {record[1]} | Contacto fornecedor: {record[2]} | Morada: {record[3]} | NIF: {record[4]}')
        elif table == 'stock':
            cursos.execute(f'SELECT * FROM {table}')
            records = cursos.fetchall()
            for record in records:
                print(f'ID produto: {record[0]} | Nome produto: {record[1]} | Preço produto: {record[2]} | Quantidade produto: {record[3]} | ID fornecedor: {record[4]}')
        elif table == 'vendas':
            cursos.execute(f'SELECT * FROM {table}')
            records = cursos.fetchall()
            for record in records:
                print(f'ID venda: {record[0]} | Nome produto: {record[1]} | Preco venda: {record[2]} | Quantidade venda: {record[3]} | ID stock: {record[4]} | ID cliente: {record[5]}')
        conn.close()

connectDB()
table = 'cliente'  # Define the table name here, e.g., 'cliente', 'fornecedores', 'stock', or 'vendas'
viewRecords(table)