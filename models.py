import sqlite3

connection = sqlite3.connect('id_users.db')

cursor = connection.cursor()


with sqlite3.connect("id_users.db") as con:

    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_users TEXT UNIQUE)""")


def add_id_user(id_user):

    try:

        cursor.execute("INSERT INTO Users (id_users) VALUES (?)", (id_user,))

        connection.commit()

    except Exception:

        pass