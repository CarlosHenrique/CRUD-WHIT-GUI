import sqlite3

conn = sqlite3.connect('turmas.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS turmas (

    Id TEXT NOT NULL,
    Materia TEXT NOT NULL,
    Periodo TEXT NOT NULL,
    Professor TEXT ,
    Aluno TEXT 

);
""")

print('Conectado ao Banco de dados')
