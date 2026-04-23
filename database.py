import sqlite3
def get_connection():
    return sqlite3.connect('users.db')

def create_table():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    username TEXT NULL
                    email TEXT NOT NULL,)''')

    connection.commit()
    connection.close()
