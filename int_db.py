import psycopg2
# https://www.digitalocean.com/community/tutorials/how-to-use-a-postgresql-database-in-a-flask-application
# https://towardsdatascience.com/sending-data-from-a-flask-app-to-postgresql-database-889304964bf2
conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user='ralds',
        password='admin')

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS books;')

cur.execute('CREATE TABLE books (id serial PRIMARY KEY,'
                                 'title varchar (150) NOT NULL,'
                                 'author varchar (50) NOT NULL,'
                                 'pages_num integer NOT NULL,'
                                 'review text,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

# Insert data into the table

cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('A Tale of Two Cities',
             'Charles Dickens',
             489,
             'A great classic!')
            )


cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('Anna Karenina',
             'Leo Tolstoy',
             864,
             'Another great classic!')
            )

cur.execute('SELECT title, author FROM books;')
for user in cur.fetchall():
    print(user)
conn.commit()
cur.close()
conn.close()