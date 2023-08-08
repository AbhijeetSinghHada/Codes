import sqlite3


class DatabaseConnection:
    def __enter__(self):
        self.connection = sqlite3.connect(
            "C:\\Users\\ahada\\OneDrive - WatchGuard Technologies Inc\\Codes\\Python\\Flask_Web_Development\\data.db")
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
