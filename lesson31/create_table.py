import sqlite3 as sql

con = sql.connect('database.db')

with con:
    cur = con.cursor()

    cur.execute(''' CREATE TABLE IF NOT EXISTS 'sales' (
                    id INTEGER PRIMARY KEY,
                    tardes TEXT NOT NULL,
                    transactions INT NOT NULL )
                ''')

    cur.execute('''CREATE TABLE IF NOT EXISTS 'salesmans' (
                    id INTEGER PRIMARY KEY,
                    nicknam TEXT NOT NULL,
                    tardes TEXT NOT NULL,
                    transactions INT NOT NULL)
                ''')

    cur.execute('''CREATE TABLE IF NOT EXISTS 'constumers' (
                    id INTEGER PRIMARY KEY,
                    nickname TEXT NOT NULL,
                    transactions INT NOT NULL)
                ''')
    con.commit()
print(con)
    
