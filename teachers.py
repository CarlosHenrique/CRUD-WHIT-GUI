import sqlite3

conn = sqlite3.connect('professores.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS professores (
    Cpf TEXT NOT NULL,
    Name TEXT NOT NULL,
    Departamento TEXT NOT NULL
);
""")

print('Conectado ao Banco de dados')
