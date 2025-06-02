import requests
import time
import sqlite3
from datetime import datetime

DB_NAME = "monitor.db"

# Garante que a tabela exista
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            status TEXT NOT NULL,
            response_time REAL,
            timestamp TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Salva verificação no banco
def save_log(entry):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        INSERT INTO logs (url, status, response_time, timestamp)
        VALUES (?, ?, ?, ?)
    ''', (entry["url"], entry["status"], entry["response_time"], entry["timestamp"]))
    conn.commit()
    conn.close()

# Faz a verificação de um site
def check_site(url):
    init_db()
    try:
        start = time.time()
        response = requests.get(url, timeout=5)
        duration = round(time.time() - start, 3)
        result = {"url": url, "status": str(response.status_code), "response_time": duration}
    except requests.RequestException:
        result = {"url": url, "status": "DOWN", "response_time": None}

    result["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_log(result)
    return result
