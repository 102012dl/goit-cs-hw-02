import sqlite3
def create_tables():
    conn = sqlite3.connect('websites.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS websites (
        id INTEGER PRIMARY KEY,
        url TEXT NOT NULL UNIQUE
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS status_checks (
        id INTEGER PRIMARY KEY,
        website_id INTEGER,
        status TEXT,
        check_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (website_id) REFERENCES websites (id)
    )
    ''')
    conn.commit()
    conn.close()
    print("Таблиці створено успішно.")
if __name__ == "__main__":
    create_tables()
