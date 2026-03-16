import sqlite3

# conecta ou cria o banco
def conectar():
    conn = sqlite3.connect("estoque.db")
    return conn

# Irá definir a tabela.
def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS insumos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        tipo TEXT NOT NULL,
        quantidade REAL NOT NULL,
        unidade TEXT NOT NULL,
        data TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

# inserir o tipo de insumo.
def inserir_insumo(nome, tipo, quantidade, unidade, data):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO insumos (nome, tipo, quantidade, unidade, data)
    VALUES (?, ?, ?, ?, ?)
    """, (nome, tipo, quantidade, unidade, data))

    conn.commit()
    conn.close()

# aqui você vai listar o insumo
def listar_insumos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM insumos")

    insumos = cursor.fetchall()

    conn.close()

    return insumos