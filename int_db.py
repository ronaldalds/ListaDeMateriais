import psycopg2
from flask_bcrypt import generate_password_hash


conn = psycopg2.connect(
        host="ec2-44-195-162-77.compute-1.amazonaws.com",
        database="dckbnake75kr9r",
        user='gtxmgfpnwqemej',
        password='0a3ade179595158f9d6c9440ed155a467b361e197146ac6af303b234085d1518')

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS usuarios;')
cur.execute('DROP TABLE IF EXISTS file;')

cur.execute('CREATE TABLE usuarios (nome varchar(20) NOT NULL,'
                                 'nickname varchar (8) NOT NULL,'
                                 'senha varchar (100) NOT NULL,'
                                'PRIMARY KEY (nickname)'
            ');'
                                 )

# Insert data into the table
usuario_sql = 'INSERT INTO usuarios (nome, nickname, senha) VALUES (%s, %s, %s)'
usuarios = [
    ("ronald", "ralds", generate_password_hash("123").decode('utf-8')),
    ("joão carlos", "jc", generate_password_hash("123").decode('utf-8')),
    ("joão luiz", "jl", generate_password_hash("123").decode('utf-8'))
]
cur.executemany(usuario_sql, usuarios)

cur.execute('SELECT * FROM usuarios;')
for user in cur.fetchall():
    print(user)

cur.execute('CREATE TABLE file (id SERIAL PRIMARY KEY,'
                                 'filename varchar (50) NOT NULL,'
                                 'data BYTEA);'
                                 )

conn.commit()
cur.close()
conn.close()