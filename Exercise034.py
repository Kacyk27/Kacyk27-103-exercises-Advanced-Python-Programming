import sqlite3


# Create connection
conn = sqlite3.connect('app.db')
cur = conn.cursor()

# Create table
sql = '''CREATE TABLE IF NOT EXISTS customer (
    customer_id INTEGER PRIMARY KEY,
    first_name  TEXT,
    last_name   TEXT,
    email       TEXT
)'''
cur.execute(sql)