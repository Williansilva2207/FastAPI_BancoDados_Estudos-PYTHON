import sqlite3
from pathlib import Path
ROOT_PATH = Path(__file__).parent
conexao = sqlite3.connect(ROOT_PATH / 'banco.sqlite')
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

try:
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", ("Maria", "maria@email.com"))
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", (2,"João", "joao@email.com"))
    conexao.commit()
except Exception:
    print("Ocorreu um erro, realizando rollback")
    conexao.rollback()
    
