import sqlite3

connection=sqlite3.connect("app.db")
cur=connection.cursor()

sql = '''CREATE TABLE IF NOT EXISTS customer (
    customer_id INTEGER PRIMARY KEY,
    first_name  TEXT,
    last_name   TEXT,
    email       TEXT
)'''
cur.execute(sql)

cur.execute("""INSERT INTO customer (first_name, last_name, email)
VALUES ('John','Smith','john.smith@esmartdata.org')""")

connection.commit()

connection.close()