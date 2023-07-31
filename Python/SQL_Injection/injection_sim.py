import sqlite3

def simulate():
    connection = sqlite3.connect("./data.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS books(name text,bookno int,author text)")
    cursor.execute("INSERT INTO books VALUES(?,?,?)",('Clean', '1', 'Robert'))
    cursor.execute("INSERT INTO books VALUES(?,?,?)",('Gulf', '2', 'Russle'))
    inp = input("Enter book name you want to fetch : ")
    cursor.execute(f"SELECT * FROM books WHERE name='{inp}'")
    output = cursor.fetchall()
    print(output)
 
if __name__=="__main__":    
    simulate()