import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()



cursor.execute("CREATE TABLE Books(name text primary key, author text, read text)")
connection.commit()
connection.close()