import sqlite3
import requests
from datetime import datetime
def check_websites():
    conn = sqlite3.connect('websites.db')
    cursor = conn.cursor()
    # SQL запит для отримання всіх веб-сайтів
    cursor.execute('SELECT id, url FROM websites')
    websites = cursor.fetchall()
    log_file = "website_status.log"
    with open(log_file, 'w') as log:
        for website_id, url in websites:
            try:
                response = requests.get(url, timeout=5)
                status = 'UP' if response.status_code == 200 else 'DOWN'
            except requests.RequestException:
                status = 'DOWN'
            # SQL запит для вставки результату перевірки
            cursor.execute('''
            INSERT INTO status_checks (website_id, status, check_time)
            VALUES (?, ?, ?)
            ''', (website_id, status, datetime.now()))
            log_entry = f"{url} is {status}\n"
            log.write(log_entry)
            print(log_entry, end='')
    conn.commit()
    # SQL запит для отримання останніх результатів перевірок
    cursor.execute('''
    SELECT w.url, s.status, s.check_time
    FROM websites w
    JOIN status_checks s ON w.id = s.website_id
    WHERE s.check_time = (
        SELECT MAX(check_time)
        FROM status_checks
        WHERE website_id = w.id
    )
    ''')
    
    print("\nОстанні результати перевірок:")
    for row in cursor.fetchall():
        print(f"{row[0]}: {row[1]} (перевірено: {row[2]})")
    conn.close()
    print(f"\nРезультати перевірки записано у файл {log_file}")
if __name__ == "__main__":
    check_websites()
