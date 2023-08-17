from . import databaseConnection
import traceback
import sys
# { 'Library' : [
#     {
#        'name' : sfffffff
#        'author' : wqkbf
#        'read' : ewfnf
#     }
# ]}
import json
import sqlite3


def update_database(datas):
    # Working with CSV
    # with open("data.csv","w") as db:
    #     for data in datas:
    #         temp = ','.join(i for i in data)
    #         db.writelines(temp+'\n')
    # Working With JSON
    # lib = {'Library' : []}
    # temp = [{'name' : itr[0],'author' : itr[1], 'read' : itr[2]} for itr in datas]
    # lib['Library']=temp
    # with open('dataLib.json','w') as db:
    #     json.dump(lib,db)
    # Working With Database
    with databaseConnection.DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS Books(name text,author text,read text)')
        cursor.execute("DELETE FROM Books")
        for data in datas:
            cursor.execute('INSERT INTO Books VALUES(?,?,?)',
                           (data[0], data[1], data[2]))


def fetch_data():
    # with open('dataLib.json','r') as db:
    #    data = json.load(db)
    # data = data['Library']
    # data = [[ist['name'],ist['author'],ist['read']] for ist in data]
    # return data
    # with open('data.csv','r') as instance:
    #     datas = instance.readlines()
    #     datas = [data.split(', ') for data in datas]
    #     datas = [data[0].strip().split(',') for data in datas]
    #     return datas
    with databaseConnection.DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Books')
        data = cursor.fetchall()
    data = [[i for i in sss] for sss in data]
    return data


def add_book(name, author):
    data = fetch_data()
    if name.strip() != '' or author.strip() != '':
        data.append([name, author, "0"])
        update_database(data)
        return True
    return False


def list_books():
    books = fetch_data()
    for index, book in enumerate(books, start=1):
        print()
        print(f"Book No. {index}")
        print(f"Name of Book {book[0]}")
        print(f"Author of Book {book[1]}")


def list_undread_books():
    books = fetch_data()
    for index, book in enumerate(books, start=1):
        if book[2] != "1":
            print(f"Book No. {index}")
            print(f"Name of Book {book[0]}")
            print(f"Author of Book {book[1]}")


def delete_book(name):
    books = fetch_data()
    for index, book in enumerate(books):
        if book[0] == name:
            books.pop(index)
            update_database(books)
            print(f"Book deleted successfully.\n")
            return
    print("Book not found.")


def mark_book_as_read(name):
    books = fetch_data()

    for book in books:
        if book[0] == name:
            book[2] = "1"
            update_database(books)
            print(f"Book marked as Read successfully.\n")
            return
    print("Book not found.")


def SearchBookByName(name):
    with databaseConnection.DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        try:
            cursor.executescript(
                f"SELECT * FROM books WHERE name='?'", (name,))
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))
        data = cursor.fetchall()
        for index, book in enumerate(data, start=1):
            print()
            print(f"Book No. {index}")
            print(f"Name of Book {book[0]}")
            print(f"Author of Book {book[1]}")


            # ' OR 1=1 --
            # ' ; DELETE FROM books;--
if __name__ == "__main__":
    with databaseConnection.DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS Books(name text,author text,read text)')
