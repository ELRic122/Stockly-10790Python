# Stockly - Gestão de Inventário

**Stockly** é uma aplicação de gestão de inventário local, desenvolvida em Python, com interface gráfica em PyQt5 e base de dados SQLite3.

⚠️ **Nota importante:**  
É necessário executar o programa em modo administrador ou instalá-lo numa pasta fora de `C:\Program Files\` para garantir permissões corretas de escrita na base de dados.

---

## Instalação

### 1️⃣ Instalar o programa

1. Abrir o ficheiro de instalação `setup.exe`.
2. Seguir o assistente de instalação.

### 2️⃣ Permissões de administrador

- Se instalar fora de `C:\Program Files\`, pode abrir normalmente.
- Se instalar dentro de `C:\Program Files\`:
  - Clicar com o botão direito no `Stockly.exe`.
  - Ir a **Propriedades > Compatibilidade > Executar este programa como administrador**.
  - Carregar em **Aplicar** e fechar.

---

## Requisitos Técnicos

- Python 3.13.11 (apenas se for executar o código-fonte)
- PyQt5
- FPDF
- SQLite3 (já incluído no Python)

---

## Como Executar

### Opção 1 - Executável (recomendado para utilizadores)

- Executar o ficheiro `Stockly.exe` em modo administrador.
- Garantir que o ficheiro `stockly.db` e as pastas `img/` e `documentos/` estão no mesmo diretório.

### Opção 2 - Executar o código-fonte

1. Instalar Python 3.13.11
2. Instalar as dependências:
```bash
pip install PyQt5 fpdf
