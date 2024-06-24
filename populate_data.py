import sqlite3
def populate_data():
    conn = sqlite3.connect('websites.db')
    cursor = conn.cursor()
    websites = [
        ('https://google.com',),
        ('https://facebook.com',),
        ('https://twitter.com',)
    ]
    cursor.executemany('INSERT OR IGNORE INTO websites (url) VALUES (?)', websites)
    conn.commit()
    conn.close()
    print("Дані додано до таблиці websites.")
if __name__ == "__main__":
    populate_data()
