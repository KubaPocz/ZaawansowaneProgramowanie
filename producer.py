import sqlite3

conn = sqlite3.connect("queue.db")

conn.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        status TEXT NOT NULL DEFAULT 'pending'
            CHECK (status IN ('pending', 'in_progress', 'done'))
    )
""")

cursor = conn.execute("INSERT INTO jobs (status) VALUES ('pending')")
conn.commit()
conn.close()

print(f"Dodano pracę {cursor.lastrowid}")