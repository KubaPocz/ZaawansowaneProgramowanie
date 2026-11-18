import sqlite3
from time import sleep

# isolation_level=None -> sami sterujemy transakcjami (BEGIN / COMMIT)
conn = sqlite3.connect("queue.db", timeout=30, isolation_level=None)

conn.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        status TEXT NOT NULL DEFAULT 'pending'
            CHECK (status IN ('pending', 'in_progress', 'done'))
    )
""")


def pobierz_prace():
    """Znajduje pierwszą pracę pending i od razu zmienia ją na in_progress."""
    conn.execute("BEGIN IMMEDIATE")  # blokuje zapis dla innych consumerów
    wiersz = conn.execute(
        "SELECT id FROM jobs WHERE status = 'pending' ORDER BY id LIMIT 1"
    ).fetchone()
    if wiersz is not None:
        conn.execute("UPDATE jobs SET status = 'in_progress' WHERE id = ?", (wiersz[0],))
    conn.execute("COMMIT")
    return wiersz[0] if wiersz else None


def zakoncz_prace(id_pracy):
    conn.execute("UPDATE jobs SET status = 'done' WHERE id = ?", (id_pracy,))


while True:
    id_pracy = pobierz_prace()

    if id_pracy is None:
        print("Brak pracy, czekam 5s...")
        sleep(5)
        continue

    print(f"Wykonuję pracę {id_pracy}")
    sleep(2)
    zakoncz_prace(id_pracy)
    print(f"Zakończono pracę {id_pracy}")