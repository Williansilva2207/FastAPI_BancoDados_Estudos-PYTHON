import sqlite3
from pathlib import Path
ROOT_PATH = Path(__file__).parent
conexao = sqlite3.connect(ROOT_PATH / 'banco.sqlite')
cursor = conexao.cursor()
def criar_tabela(conexao,cursor, nome_tabela):
    cursor.execute("CREATE TABLE ? (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150));", (nome_tabela))
    conexao.commit()

def inserir_dados(conexao,cursor,  nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
    conexao.commit()

def atualizar_dados(conexao,cursor, nome, id):
    data = (nome, id)
    cursor.execute("UPDATE clientes SET nome = ? WHERE id = ?;", data)
    conexao.commit()

def excluir_data(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id = ?;", data)
    conexao.commit()

def insert_many(conexao, cursor, list):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES(?,?);", list)
    conexao.commit()

def printar_dados(cursor):
     cursor.execute("SELECT * FROM clientes;")
     resultado = cursor.fetchall()
     for linha in resultado:
         print(linha)
def printar_dados_row(cursor):
     cursor.row_factory = sqlite3.Row
     cursor.execute("SELECT * FROM clientes;")
     return cursor.fetchall()
     
row = printar_dados_row(cursor)
print(dict(row[0]))