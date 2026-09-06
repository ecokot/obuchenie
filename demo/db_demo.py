import sqlite3
from datetime import datetime

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute('PRAGMA foreign_keys = ON')
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    created_at TEXT NOT NULL
    )''')
conn.commit()

cursor.execute('DROP TABLE IF EXISTS posts')
cursor.execute('''CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE)''')
conn.commit()

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
data = [
    ('Alice', 25, now),
    ('Bob', 30, now),
    ('Charlie', 28, now),
    ('Alice', 26, now)
]
cursor.executemany('''INSERT INTO users (name, age, created_at) VALUES (?, ?, ?)''', data)
conn.commit()


print("--- INSERT POST")
try:
    cursor.executemany('''INSERT INTO posts (title, user_id) VALUES (?, ?)''', (('Post 1', 999),))
    conn.commit()
except sqlite3.IntegrityError as e:
    print("Ошибка:", e.args[0])

cursor.execute('''DELETE FROM users WHERE id = 1''')
conn.commit()
print("---")
data = [
    ('Post 2', 2),
    ('Post 3', 2),
    ('Post 4', 4)
]
cursor.executemany('''INSERT INTO posts (title, user_id) VALUES (?, ?)''', data)
conn.commit()
print("--- SELECT POSTS")
cursor.execute('''
    SELECT name
    FROM users
    WHERE id NOT IN (SELECT user_id FROM posts)
    ''')
for row in cursor.fetchall():
    print(row)


conn.close()