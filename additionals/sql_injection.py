import sqlite3
path = 'additionals/main.db'

def init_db():
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS users (
                username TEXT,
                password TEXT
           )
        '''
    )

    cursor.execute(
        '''INSERT INTO users(username, password) VALUES ('admin', 'adminpass')'''
    )

def input_new_user(username, password):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users(username, password) VALUES (?, ?)", (username, password))

    conn.commit()
    conn.close()