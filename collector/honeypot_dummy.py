import random
import sqlite3
from datetime import datetime

DB_PATH = "data/attacks.db"

ATTACK_TYPES = ["Brute Force SSH", "SQL Injection", "XSS", "Port Scan", "Malware Upload"]
IP_LIST = ["192.168.0.10", "45.33.32.156", "201.33.45.90", "8.8.8.8"]

def log_attack():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS attacks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip TEXT,
        attack_type TEXT,
        timestamp TEXT
    )""")
    
    ip = random.choice(IP_LIST)
    attack_type = random.choice(ATTACK_TYPES)
    timestamp = datetime.now().isoformat()
    
    c.execute("INSERT INTO attacks (ip, attack_type, timestamp) VALUES (?, ?, ?)",
              (ip, attack_type, timestamp))
    conn.commit()
    conn.close()
    print(f"[LOG] Ataque registrado: {attack_type} de {ip}")

if __name__ == "__main__":
    for _ in range(5):  # gera 5 ataques falsos
        log_attack()
