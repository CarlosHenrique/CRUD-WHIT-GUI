import sqlite3

conn = sqlite3.connect('alunos.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    Cpf TEXT NOT NULL,
    Name TEXT NOT NULL);
""")

print('Conectado ao Banco de dados')
