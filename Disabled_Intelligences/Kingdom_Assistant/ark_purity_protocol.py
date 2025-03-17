import sqlite3
import os
import shutil

DB_NAME = "sentinel_memory.db"
BACKUP_DIR = "backups"

def connect_db():
    """Establish a connection to the SQLite database."""
    conn = sqlite3.connect(DB_NAME)
    return conn, conn.cursor()

def initialize_memory():
    """Ensures required tables exist in the database."""
    conn, cursor = connect_db()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vectors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vector TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            last_topic TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()
    print("✅ Ark Memory and User Data Initialized Successfully.")

def add_memory(vector):
    """Adds a new memory vector to the database."""
    conn, cursor = connect_db()
    cursor.execute("INSERT INTO vectors (vector, timestamp) VALUES (?, datetime('now'))", (vector,))
    conn.commit()
    conn.close()
    print(f"✅ New Ark Memory Vector Added: {vector}")

def recall_recent_memories(limit=5):
    """Fetches and displays recent memory vectors."""
    conn, cursor = connect_db()
    cursor.execute("SELECT id, vector, timestamp FROM vectors ORDER BY timestamp DESC LIMIT ?", (limit,))
    memories = cursor.fetchall()
    conn.close()

    print("\n🧠 Recent Ark Memory Vectors:")
    if memories:
        for mem in memories:
            print(f"ID: {mem[0]}, Vector: {mem[1]}, Timestamp: {mem[2]}")
    else:
        print("⚠️ No memory vectors found.")

def backup_memory():
    """Backs up the memory database to a specified directory."""
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    backup_path = os.path.join(BACKUP_DIR, DB_NAME)
    try:
        shutil.copy(DB_NAME, backup_path)
        print(f"✅ Ark Memory backed up to: {backup_path}")
    except Exception as e:
        print(f"❌ Backup failed: {e}")

def validate_memory():
    """Checks how many vectors are stored in the memory."""
    conn, cursor = connect_db()
    cursor.execute("SELECT COUNT(*) FROM vectors")
    count = cursor.fetchone()[0]
    conn.close()
    print(f"🧠 Total Ark Memory Vectors Stored: {count}")

def main_test():
    """Runs a full test sequence to verify memory system functionality."""
    initialize_memory()
    add_memory("[0.7, 0.8, 0.9]")
    recall_recent_memories()
    backup_memory()
    validate_memory()

if __name__ == "__main__":
    main_test()
