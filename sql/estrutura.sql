--
-- File generated with SQLiteStudio v3.4.4 on qui abr 17 12:48:27 2025
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: Cliente
CREATE TABLE IF NOT EXISTS Cliente (
    ID_Cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Contacto TEXT NOT NULL,
    Data_Nascimento DATE NOT NULL,
    Morada TEXT NOT NULL
);

-- Table: Fornecedores
CREATE TABLE IF NOT EXISTS Fornecedores (
    ID_Fornecedor INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Contacto TEXT NOT NULL,
    Morada TEXT NOT NULL,
    NIF TEXT NOT NULL
);

-- Table: Stock
CREATE TABLE IF NOT EXISTS Stock (
    ID_Stock INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome_Produto TEXT NOT NULL,
    Pre�o_Produto TEXT NOT NULL,
    Quantidade_Produto TEXT NOT NULL,
    ID_Fornecedor INTEGER NOT NULL REFERENCES Fornecedores(ID_Fornecedor)
);

-- Table: Vendas
CREATE TABLE IF NOT EXISTS Vendas (
    ID_Venda INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome_Produto TEXT NOT NULL,
    Pre�o_Venda TEXT NOT NULL,
    Quantidade_Venda TEXT NOT NULL,
    ID_Stock INTEGER NOT NULL REFERENCES Stock(ID_Stock),
    ID_Cliente INTEGER NOT NULL REFERENCES Cliente(ID_Cliente)
);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
