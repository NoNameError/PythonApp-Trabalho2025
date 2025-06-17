import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
''')

# Dados fictícios
usuarios = [
    ('Alice Silva', 'alice@email.com'),
    ('Bruno Costa', 'bruno@email.com'),
    ('Carlos Mendes', 'carlos@email.com')
]

c.executemany('INSERT OR IGNORE INTO usuarios (nome, email) VALUES (?, ?)', usuarios)
conn.commit()
conn.close()
