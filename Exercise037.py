import sqlite3

conn = sqlite3.connect('app.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE category (
    category_id   INTEGER,
    category_name TEXT    NOT NULL,
    PRIMARY KEY (category_id)
)''')

cur.execute('''INSERT INTO category (category_name) VALUES ('technology')''')
cur.execute('''INSERT INTO category (category_name) VALUES ('e-commerce')''')
cur.execute('''INSERT INTO category (category_name) VALUES ('gaming')''')
conn.commit()

# Enter your solution here
cur.execute('''UPDATE category SET category_name="online shop" WHERE category_id=2''')
conn.commit()
x=cur.execute('''SELECT * FROM category''').fetchall()
for i in x:
    print(i)

conn.close()