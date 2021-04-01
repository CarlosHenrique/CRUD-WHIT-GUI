import sqlite3

conn = sqlite3.connect('misera.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS misera (
    Id TEXT NOT NULL,
    Materia TEXT NOT NULL
);
""")

print('Conectado ao Banco de dados')
