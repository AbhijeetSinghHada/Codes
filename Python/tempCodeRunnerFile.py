import sqlite3

class Database:
    CREATE_TABLE = "CREATE TABLE IF NOT EXISTS blog_data(id number, title text, content text)"
    FETCH_DATA = "SELECT * FROM blog_data"
    def __init__(self):
        connection = sqlite3.connect("data.db")
        self.cursor = connection.cursor()
        self.cursor.execute(self.CREATE_TABLE)
        connection.commit()
    
    def import_web_data(self):
        self.cursor.execute('SELECT * FROM blog_data')
        data = self.cursor.fetchall()
        print(data)
        data = [{"id" : x[0],'title' : x[1],'content':x[2]} for x in data]
        print(data)

       
a = Database()
a.import_web_data()