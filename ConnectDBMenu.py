import mysql.connector
import beaupy
import os
import json
import pandas as pd

# funcao para conectar a base de dados
def conectarBD():
    conn = None
    try:
        conn = mysql.connector.connect(user='root', host='localhost', database='stockly', autocommit=True)
        return conn
    except mysql.connector.Error as error:
        print(f"Erro ao conectar a base da dados. [{error}]")
        return None

# inserir registos
def inserirRegistos(tabela):
    conn = conectarBD()
    if conn:
        cursor = conn.cursor()
        if tabela == 'cliente':
            NomeCliente = input("Nome do Cliente: ")
            ContactoCliente = input("Contacto do Cliente: ")
            DataNascimento = input("Data de Nascimento do Cliente: ")
            MoradaCliente = input("Morada do Cliente: ")
            cursor.execute("INSERT INTO cliente (Nome, Contacto, Data_Nascimento, Morada) VALUES (%s, %s, %s, %s)", (NomeCliente, ContactoCliente, DataNascimento, MoradaCliente))
        elif tabela == 'fornecedores':
            NomeFornecedor = input("Nome do Fornecedor: ")
            ContactoFornecedor = input("Contacto do Fornecedor: ")
            moradaFornecedor = input("Morada do Fornecedor: ")
            NIFFornecedor = input("NIF do Fornecedor: ")
            cursor.execute("INSERT INTO fornecedores (Nome, Contacto, Morada, NIF) VALUES (%s,%s,%s,%s)", (NomeFornecedor, ContactoFornecedor, moradaFornecedor, NIFFornecedor))
        elif tabela == 'stock':
            NomeProduto = input("Nome do Produto: ")
            PrecoProduto = input("Preço do Produto: ")
            QuantidadeProduto = input("Quantidade do Produto: ")
            idFornecedor = input("ID do Fornecedor: ")
            cursor.execute("INSERT INTO stock (Nome_Produto, Preco_Produto, Quantidade_Produto) VALUES (%s,%s)", (NomeProduto, PrecoProduto, Quantidade, idFornecedor))
        elif tabela == 'vendas':
            NomeProdutoVenda = input("Nome do Produto: ")
            PrecoVenda = input("Preço da venda: ")
            QuantidadeVenda = input("Quantidade de Produto para venda: ")
            idstock = input("ID do Stock: ")
            idcliente = input("ID do Cliente: ")
            cursor.execute("INSERT INTO stock (Nome_Produto, Preco_Produto, Quantidade_Produto, ID_Fornecedor) VALUES (%s, %s, %s, %s)", (NomeProduto, PrecoProduto, QuantidadeProduto, idFornecedor))
        conn.commit()
        print(f'Registo inserido na tabela {tabela} com sucesso.')
        conn.close()

# modificar registos
def modificarRegistos(tabela, id, coluna, novo_valor):
    conn = conectarBD()
    if conn:
        cursor = conn.cursor()
        primary_key = ""

        if tabela == "cliente":
            primary_key = "ID_Cliente"
        elif tabela == "fornecedores":
            primary_key = "ID_Fornecedor"
        elif tabela == "stock":
            primary_key = "ID_Stock"
        elif tabela == "vendas":
            primary_key = "ID_Venda"

        # Query de atualização simplificada
        query = f"UPDATE {tabela} SET {coluna} = %s WHERE {primary_key} = %s"
        cursor.execute(query, (novo_valor, id))
        conn.commit()
        print(f'Registo da tabela {tabela} atualizado com sucesso.')
        conn.close()


# remover registos
def removerRegistos(tabela, id):
    conn = conectarBD()
    if conn:
        cursor = conn.cursor()
        primary_key = ""
        
        if tabela == "cliente":
            primary_key = "ID_Cliente"
        elif tabela == "fornecedores":
            primary_key = "ID_Fornecedor"
        elif tabela == "stock":
            primary_key = "ID_Stock"
        elif tabela == "vendas":
            primary_key = "ID_Venda"

        cursor.execute(f"DELETE FROM {tabela} WHERE {primary_key} = %s", (id,))
        conn.commit()
        print(f'Registo removido da tabela {tabela} com sucesso.')
        conn.close()

# visualizacao registos
def visualizarRegistos(tabela):
    conn = conectarBD()
    if conn:
        cursor = conn.cursor()
        
        if tabela == "cliente":
            cursor.execute(f"SELECT * FROM {tabela}")
            registos = cursor.fetchall()
            for registo in registos:
                print(f'ID do Cliente: {registo[0]} | Nome do Cliente: {registo[1]} | Contacto do Cliente: {registo[2]} | Data de Nascimento do Cliente: {registo[3]} | Morada do Cliente: {registo[4]}\n')
        elif tabela == "fornecedores":
            cursor.execute(f"SELECT * FROM {tabela}")
            registos = cursor.fetchall()
            for registo in registos:
                print(f'ID do Fornecedor: {registo[0]} | Nome do Fornecedor: {registo[1]} | Contacto do fornecedor: {registo[2]} | Morada do Fornecedor: {registo[3]} | NIF do Fornecedor: {registo[4]}\n')
        elif tabela == "stock":
            cursor.execute(f"SELECT * FROM {tabela}")
            registos = cursor.fetchall()
            for registo in registos:
                print(f'ID do Stock: {registo[0]} | Nome do Produto: {registo[1]} | Preço Produto: {registo[2]}€ | Quantidade de Produto: {registo[3]} | ID do Fornecedor: {registo[4]}\n')
        elif tabela == "vendas":
            cursor.execute(f"SELECT * FROM {tabela}")
            registos = cursor.fetchall()
            for registo in registos:
                print(f'ID da Venda: {registo[0]} | Nome do Produto: {registo[1]} | Preço da Venda: {registo[2]}€ | Quantidade: {registo[3]} | ID Stock: {registo[4]} | ID Cliente: {registo[5]}\n')
        conn.close()

# funcao para limpar dados, como eliminar espacos em branco a mais, meter o formado +351 no telemovel, verificar que os digitos ficam como digitos e nao com caracteres.
def limparDados():
    print("Iniciando processo de limpeza de dados...")
    conn = conectarBD()
    if conn:
        cursor = conn.cursor()
        print("Conexão com o banco de dados estabelecida.")

        try:
            # Limpeza de dados para cliente
            print("Limpando dados de cliente...")
            cursor.execute("SELECT * FROM cliente")
            cliente = cursor.fetchall()
            df_clientes = pd.DataFrame(cliente, columns=['ID_Cliente', 'Nome', 'Contacto', 'Data_Nascimento', 'Morada'])
            
            df_clientes['Nome'] = df_clientes['Nome'].str.strip().str.title()
            df_clientes['Contacto'] = df_clientes['Contacto'].apply(lambda x: ''.join(filter(str.isdigit, x)))
            df_clientes['Contacto'] = df_clientes['Contacto'].apply(lambda x: f"+351 {x[-9:-6]} {x[-6:-3]} {x[-3:]}" if len(x) >= 9 else x)

            print("Atualizando dados de cliente no banco de dados...")
            for index, row in df_clientes.iterrows():
                cursor.execute("UPDATE cliente SET Nome = %s, Contacto = %s, Data_Nascimento = %s, Morada = %s WHERE ID_Cliente = %s",
                               (row['Nome'], row['Contacto'], row['Data_Nascimento'], row['Morada'], row['ID_Cliente']))

            # Limpeza de dados para fornecedores
            print("Limpando dados de fornecedores...")
            cursor.execute("SELECT * FROM fornecedores")
            fornecedores = cursor.fetchall()
            df_fornecedores = pd.DataFrame(fornecedores, columns=['ID_Fornecedor', 'Nome', 'Contacto', 'Morada', 'NIF'])
            
            df_fornecedores['Nome'] = df_fornecedores['Nome'].str.strip().str.title()
            df_fornecedores['Contacto'] = df_fornecedores['Contacto'].apply(lambda x: ''.join(filter(str.isdigit, x)))
            df_fornecedores['Contacto'] = df_fornecedores['Contacto'].apply(lambda x: f"+351 {x[-9:-6]} {x[-6:-3]} {x[-3:]}" if len(x) >= 9 else x)
            
            print("Atualizando dados de fornecedores no banco de dados...")
            for index, row in df_fornecedores.iterrows():
                cursor.execute("UPDATE fornecedores SET Nome = %s, Contacto = %s, Morada = %s, NIF = %s WHERE ID_Fornecedor = %s",
                               (row['Nome'], row['Contacto'], row['Morada'], row['NIF'], row['ID_Fornecedor']))

            # Limpeza de dados para stock
            print("Limpando dados de stock...")
            cursor.execute("SELECT * FROM stock")
            stock = cursor.fetchall()
            df_stock = pd.DataFrame(stock, columns=['ID_Stock', 'Nome_Produto', 'Preco_Produto', 'Quantidade_Produto', 'ID_Fornecedor'])
            
            df_stock['Nome_Produto'] = df_stock['Nome_Produto'].str.strip().str.title()
            df_stock['Preco_Produto'] = pd.to_numeric(df_stock['Preco_Produto'], errors='coerce').fillna(0).round(2)
            df_stock['Quantidade_Produto'] = pd.to_numeric(df_stock['Quantidade_Produto'], errors='coerce').fillna(0).astype(int)

            print("Atualizando dados de stock no banco de dados...")
            for index, row in df_stock.iterrows():
                cursor.execute("UPDATE stock SET Nome_Produto = %s, Preco_Produto = %s, Quantidade_Produto = %s WHERE ID_Stock = %s",
                               (row['Nome_Produto'], row['Preco_Produto'], row['Quantidade_Produto'], row['ID_Stock']))

            # Limpeza de dados para vendas
            print("Limpando dados de vendas...")
            cursor.execute("SELECT * FROM vendas")
            vendas = cursor.fetchall()
            df_vendas = pd.DataFrame(vendas, columns=['ID_Venda', 'Nome_Produto', 'Preco_Venda', 'Quantidade_Venda', 'ID_Stock', 'ID_Cliente'])
            
            df_vendas['Nome_Produto'] = df_vendas['Nome_Produto'].str.strip().str.title()
            df_vendas['Preco_Venda'] = pd.to_numeric(df_vendas['Preco_Venda'], errors='coerce').fillna(0).round(2)
            df_vendas['Quantidade_Venda'] = pd.to_numeric(df_vendas['Quantidade_Venda'], errors='coerce').fillna(0).astype(int)

            print("Atualizando dados de vendas no banco de dados...")
            for index, row in df_vendas.iterrows():
                cursor.execute("UPDATE vendas SET Nome_Produto = %s, Preco_Venda = %s, Quantidade_Venda = %s WHERE ID_Venda = %s",
                               (row['Nome_Produto'], row['Preco_Venda'], row['Quantidade_Venda'], row['ID_Venda']))

            conn.commit()
            print("Limpeza de dados concluída com sucesso para todas as tabelas.")
        except Exception as e:
            print(f"Ocorreu um erro durante a limpeza de dados: {e}")
            conn.rollback()
        finally:
            conn.close()
            print("Conexão com o banco de dados fechada.")
    else:
        print("Não foi possível conectar ao banco de dados para realizar a limpeza.")

    input("Pressione Enter para continuar...")

# funcao para "limpar" o ecra ao "mudar" de janela
def clear():
    os.system('cls')

# menu
def menu():
    while True:
        clear()
        print('\n [Menu]')
        option = beaupy.select(["Ver registos", "Inserir Registos", "Modificar Registos", "Remover registos", "Limpar Dados", "Sair"], cursor='✏ ', cursor_style='purple')
        if option == "Ver registos":
            tabela = beaupy.select(["cliente", "fornecedores", "stock", "vendas", "voltar"], cursor=' ✏ ', cursor_style='purple')
            if tabela == "voltar":
                continue
            clear()
            visualizarRegistos(tabela)
            input(" 'Enter' para voltar ao menu principal...")
        elif option == "Inserir Registos":
            tabela = beaupy.select(["cliente", "fornecedores", "stock", "vendas", "voltar"], cursor='✏ ', cursor_style='purple')
            if tabela == "voltar":
                continue
            clear()
            visualizarRegistos(tabela)
            inserirRegistos(tabela)
            input(" 'Enter' para voltar ao menu principal...")
        elif option == "Modificar Registos":
            tabela = beaupy.select(["cliente", "fornecedores", "stock", "vendas", "voltar"], cursor='✏ ', cursor_style='purple')
            if tabela == "voltar":
                continue
            clear()
            visualizarRegistos(tabela)
            id = int(input("ID do registo a modificar: "))
            coluna = input("Nome da coluna a modificar: ")
            novo_valor = input("Novo valor: ")
            modificarRegistos(tabela, id, coluna, novo_valor)
            input(" 'Enter' para voltar ao menu principal...")
        elif option == "Remover registos":
            tabela = beaupy.select(["cliente", "fornecedores", "stock", "vendas", "voltar"], cursor='✏ ', cursor_style='purple')
            if tabela == "voltar":
                continue
            clear()
            visualizarRegistos(tabela)
            id = int(input("ID do registo: "))
            removerRegistos(tabela, id)
            input(" 'Enter' para voltar ao menu principal...")
        elif option == "Limpar Dados":
            limparDados()
            print("Processo de limpeza concluído.")
            input(" 'Enter' para voltar ao menu principal...")
        else:
            break

# --CHAMADA DE FUNCOES--
menu()
