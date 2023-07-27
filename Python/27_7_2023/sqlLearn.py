from utils import databaseConnection
import sqlite3
connection = sqlite3.connect('data.db')
cursor = connection.cursor()


with databaseConnection.DatabaseConnection() as connection:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Books(name text primary key, author text, read text)")
    cursor.execute("INSERT INTO Books VALUES('Raam','Ved Vyas', 'True')")
    cursor.execute('SELECT * FROM Books')
    data = cursor.fetchall()

    print(data)
    connection.commit()
