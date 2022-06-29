import psycopg2
from flask_bcrypt import generate_password_hash


conn = psycopg2.connect(
        host="localhost",
        database="eng",
        user='ralds',
        password='admin')

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS usuarios;')

cur.execute('CREATE TABLE usuarios (nome varchar(20) NOT NULL,'
                                 'nickname varchar (8) NOT NULL PRIMARY KEY,'
                                 'senha varchar (100) NOT NULL);'
                                 )

# Insert data into the table

usuario_sql = 'INSERT INTO usuarios (nome, nickname, senha) VALUES (%s, %s, %s)'
usuarios = [
    ("ronald", "ralds", generate_password_hash("123").decode('utf-8')),
    ("joão carlos", "jc", generate_password_hash("123").decode('utf-8')),
    ("joão luiz", "jl", generate_password_hash("123").decode('utf-8'))
]
cur.executemany(usuario_sql, usuarios)
#
cur.execute('SELECT * FROM usuarios;')
for user in cur.fetchall():
    print(user[1])
conn.commit()
cur.close()
conn.close()