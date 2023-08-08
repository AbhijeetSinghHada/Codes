import sqlite3
from utils.databaseConnection import DatabaseConnection


class Database:
    CREATE_TABLE = "CREATE TABLE IF NOT EXISTS blog_data(id number, title text, content text)"
    FETCH_DATA = "SELECT * FROM blog_data"
    UPLOAD_DATA = "INSERT INTO blog_data values(?,?,?)"

    def __init__(self):
        with DatabaseConnection() as db:
            cursor = db.cursor()
            cursor.execute(self.CREATE_TABLE)

    @property
    def import_web_data(self):
        self.cursor.execute(self.FETCH_DATA)
        data = self.cursor.fetchall()
        data = {x[0]: {"id": x[0], 'title': x[1], 'content': x[2]}
                for x in data}
        return data

    def upload_data(self, data_id, title, content):
        self.cursor.execute(self.UPLOAD_DATA, (data_id, title, content))

    def __exit__(self):
        self.connection.commit()
        self.connection.close()
# posts = {
#     0: {
#         "id": 0,
#         'title': 'Hello, World',
#         'content': 'This is my first blog post'
#     }
# }


if __name__ == "__main__":
    a = Database()
    print(a.import_web_data)
