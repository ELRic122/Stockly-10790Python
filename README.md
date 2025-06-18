**PORTUGUÊS**

# Stockly - Gestão de Inventário

**Stockly** é uma aplicação de gestão de inventário local, desenvolvida em Python, com interface gráfica em PyQt5 e base de dados SQLite3.

⚠️ **Nota importante:**  
É necessário executar o programa em modo administrador ou instalá-lo numa pasta fora de `C:\Program Files\` para garantir permissões corretas de escrita na base de dados.

⚠️ **Atenção:** Alguns antivírus podem identificar esta aplicação como ameaça por engano (falso positivo). O software é seguro.

---

## Instalação

### 1️⃣ Instalar o programa

1. Abrir o ficheiro de instalação `Stockly_1.0.0_SETUP`.
2. Seguir o assistente de instalação.

### 2️⃣ Permissões de administrador

- Se instalar fora de `C:\Program Files\`, pode abrir normalmente.
- Se instalar dentro de `C:\Program Files\`:
  - Clicar com o botão direito no `Stockly - Gestão de Inventário.exe`.
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

- Executar o ficheiro `Stockly - Gestão de Inventário.exe` em modo administrador.
- Garantir que o ficheiro `stockly.db` e as pastas `img/` e `documentos/` estão no mesmo diretório.

### Opção 2 - Executar o código-fonte

1. Instalar Python 3.13.11
2. Instalar as dependências:
```bash
pip install PyQt5 fpdf
```

---
**ENGLISH**

# Stockly - Inventory Management

**Stockly** is a local inventory management application developed in Python, with a graphical interface using PyQt5 and a SQLite3 database.

⚠️ **Important note:**  
You must run the program as Administrator or install it in a folder other than `C:\Program Files\` to ensure proper write permissions on the database.

⚠️ **Warning:** Some antivirus programs may mistakenly flag this application as a threat (false positive). The software is safe.

---

## Installation

### 1️⃣ Install the program

1. Open the setup file `Stockly_1.0.0_SETUP`.  
2. Follow the installation wizard.

### 2️⃣ Administrator permissions

- If installed outside `C:\Program Files\`, you can open it normally.  
- If installed inside `C:\Program Files\`:  
  - Right-click on `Stockly - Inventory Management.exe`.  
  - Go to **Properties > Compatibility > Run this program as administrator**.  
  - Click **Apply** and close the window.

---

## Technical Requirements

- Python 3.13.11 (only if running the source code)  
- PyQt5  
- FPDF  
- SQLite3 (already included in Python)  

---

## How to Run

### Option 1 - Executable (recommended for users)

- Run the `Stockly - Inventory Management.exe` file as Administrator.  
- Make sure the `stockly.db` file and folders `img/` and `documents/` are in the same directory.

### Option 2 - Run from source code

1. Install Python 3.13.11  
2. Install dependencies:  
   ```bash
   pip install PyQt5 fpdf
