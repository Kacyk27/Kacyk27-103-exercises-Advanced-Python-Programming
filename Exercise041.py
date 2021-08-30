import csv
import sqlite3


product_constraints = [
    'INTEGER PRIMARY KEY',
    'TEXT NOT NULL',
    'INTEGER NOT NULL',
    'INTEGER NOT NULL',
    'TEXT NOT NULL',
    'REAL NOT NULL',
    'INTEGER NOT NULL',
    'INTEGER NOT NULL',
    'INTEGER NOT NULL',
    'INTEGER NOT NULL'
]


def generate_sql(table_name, col_names, constraints):
    cols = [" ".join((col, constraint)).strip()
            for col, constraint in zip(col_names, constraints)]
    return f'CREATE TABLE {table_name} (' + ', '.join(cols) + ')'


# Enter your solution here
with open("Product.csv","r",encoding="utf-8") as file:
    data = csv.reader(file, delimiter=",")
    columns = next(data)
    rows = tuple(data)

sql_create = generate_sql("Product",columns,product_constraints)

conn = sqlite3.connect("store.db")
cur = conn.cursor()

cur.execute(sql_create)
cur.executemany("""INSERT INTO Product VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",rows)
conn.commit()

cur.execute("""SELECT COUNT(*) FROM Product""")
rows_amount = cur.fetchall()[0][0]
print(rows_amount)

conn.close()

# I had to use answer from course because i wasn't able to end this one.