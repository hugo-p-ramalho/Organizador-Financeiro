import sqlite3
import pandas as pd

DB_NAME = "financeiro.db"

def criar_conexao():
    return sqlite3.connect(DB_NAME)

def criar_tabela():
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS gastos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT,
            categoria TEXT,
            descricao TEXT,
            valor REAL
        )
    """)
    conn.commit()
    conn.close()

def salvar_dados(df):
    criar_tabela()
    conn = criar_conexao()
    df.to_sql('gastos', conn, if_exists='replace', index=False)
    conn.close()
    print(f"{len(df)} registros salvos no banco!")

def carregar_dados():
    criar_tabela()
    conn = criar_conexao()
    df = pd.read_sql("SELECT * FROM gastos", conn)
    conn.close()
    return df