import sqlite3
from datetime import datetime

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
age INTEGER,
created_at TEXT NOT NULL)
''')
conn.commit()

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
cursor.execute('''INSERT INTO users (id, name, age, created_at) VALUES
(1, 'Alice', 25, ?),
(2, 'Bob', 30, ?),
(3, 'Charlie', 35, ?)
''', (now, now, now))
conn.commit()

cursor.execute('''SELECT * FROM users''')

for row in cursor.fetchall():
    print(row)

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
cursor.execute('''INSERT INTO users (id, name, age, created_at) VALUES
(1, 'Alice', 25, ?)
''', (now,))
conn.commit()

conn.close()