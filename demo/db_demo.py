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

cursor.execute('''CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id))''')
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


print("---")
data = [
    ('Post 2', 1),
    ('Post 3', 1)
]
cursor.executemany('''INSERT INTO posts (title, user_id) VALUES (?, ?)''', data)
conn.commit()
cursor.execute('''SELECT * FROM posts''')

for row in cursor.fetchall():
    print(row)
# ==========================================
# ДЕМОНСТРАЦИЯ ТРАНЗАКЦИЙ
# ==========================================

print("\n=== ДЕМО ТРАНЗАКЦИЙ ===")

# 1. Создаём таблицу accounts
cursor.execute('''CREATE TABLE accounts (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    balance INTEGER NOT NULL
)''')
conn.commit()

# 2. Вставляем две строки с балансом 100
data = [
    (1, 'Alice', 100),
    (2, 'Bob', 100)
]
cursor.executemany('''INSERT INTO accounts (id, name, balance) VALUES (?, ?, ?)''', data)
conn.commit()

# 3. Показываем начальные балансы
print("\nДо перевода:")
cursor.execute('SELECT * FROM accounts')
for row in cursor.fetchall():
    print(row)

# 4. ПЕРЕВОД С ROLLBACK
# Списываем 50 у Alice
print("\n--- Перевод 50 от Alice к Bob (с ROLLBACK) ---")
cursor.execute('UPDATE accounts SET balance = balance - 50 WHERE id = 1')
# Зачисляем 50 Bob... НО НЕ COMMIT, а ROLLBACK
cursor.execute('UPDATE accounts SET balance = balance + 50 WHERE id = 2')

# Вместо conn.commit() делаем откат!
conn.rollback()

# 5. Проверяем — балансы остались 100
print("\nПосле ROLLBACK:")
cursor.execute('SELECT * FROM accounts')
for row in cursor.fetchall():
    print(row)

# 6. ПЕРЕВОД С COMMIT — успешный перевод
cursor.execute('UPDATE accounts SET balance = balance - 50 WHERE id = 1')
cursor.execute('UPDATE accounts SET balance = balance + 50 WHERE id = 2')
conn.commit()

print("\nПосле успешного COMMIT:")
cursor.execute('SELECT * FROM accounts')
for row in cursor.fetchall():
    print(row)


conn.close()