import sqlite3


conn = sqlite3.connect('app.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS category (
    category_id INTEGER,
    category_name  TEXT NOT NULL,
    PRIMARY KEY (category_id)
)''')

cur.executescript('''INSERT INTO category (category_name) VALUES ("technology");
INSERT INTO category (category_name) VALUES ("e-commerce");
INSERT INTO category (category_name) VALUES ("gaming")''')

categories=cur.execute('''SELECT * FROM category''').fetchall()
print(categories)
conn.commit()
conn.close()