import sqlite3
from flask_bcrypt import generate_password_hash

# Conexão com o banco de dados SQLite local
conn = sqlite3.connect('local_database.db')

cur = conn.cursor()

# Criando a tabela 'usuarios' para SQLite
cur.execute('DROP TABLE IF EXISTS usuarios;')

cur.execute('CREATE TABLE usuarios (nome varchar(20) NOT NULL,'
            'nickname varchar (8) NOT NULL,'
            'senha varchar (100) NOT NULL,'
            'PRIMARY KEY (nickname)'
            ');'
            )

# Inserindo dados na tabela
usuario_sql = 'INSERT INTO usuarios (nome, nickname, senha) VALUES (?, ?, ?)'
usuarios = [
    ("ronald", "ralds", generate_password_hash("123").decode('utf-8')),
    ("joão carlos", "jc", generate_password_hash("123").decode('utf-8')),
    ("joão luiz", "jl", generate_password_hash("123").decode('utf-8'))
]
cur.executemany(usuario_sql, usuarios)

cur.execute('SELECT * FROM usuarios;')
for user in cur.fetchall():
    print(user)

conn.commit()
cur.close()
conn.close()
