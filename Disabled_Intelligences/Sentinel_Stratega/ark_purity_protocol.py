import sqlite3
import os
import shutil

# Set up database path
script_dir = os.path.dirname(os.path.abspath(__file__))
ark_purity_db = os.path.join(script_dir, "ark_purity_memory.db")
backup_dir = os.path.join(script_dir, "backups")

def connect_db():
    """Establish a connection to the Ark Purity Protocol memory database."""
    return sqlite3.connect(ark_purity_db)

def initialize_memory():
    """Ensures required tables exist in the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vectors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vector TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ""
    )
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            last_topic TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ""
    )
    conn.commit()
    conn.close()
    print("✅ Ark Purity Protocol Memory Initialized Successfully.")

def store_memory(vector):
    """Adds a new memory vector to the Ark Purity Protocol database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO vectors (vector, timestamp) VALUES (?, datetime('now'))", (vector,))
    conn.commit()
    conn.close()
    print(f"✅ New Ark Memory Vector Stored: {vector}")

def recall_recent_memories(limit=5):
    """Fetches and displays recent stored memory vectors."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, vector, timestamp FROM vectors ORDER BY timestamp DESC LIMIT ?", (limit,))
    memories = cursor.fetchall()
    conn.close()

    print("\n🧠 Recent Ark Purity Protocol Memory:")
    if memories:
        for mem in memories:
            print(f"ID: {mem[0]}, Vector: {mem[1]}, Timestamp: {mem[2]}")
    else:
        print("⚠️ No memory vectors found.")

def recall_last_interaction():
    """Retrieve the most recent stored memory interaction."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT vector FROM vectors ORDER BY timestamp DESC LIMIT 1;")
    last_memory = cursor.fetchone()
    conn.close()
    return last_memory[0] if last_memory else "No prior interactions recorded."

def backup_memory():
    """Backs up the memory database to a specified directory."""
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    backup_path = os.path.join(backup_dir, "ark_purity_memory_backup.db")
    try:
        shutil.copy(ark_purity_db, backup_path)
        print(f"✅ Ark Purity Protocol Memory backed up to: {backup_path}")
    except Exception as e:
        print(f"❌ Backup failed: {e}")

def validate_memory():
    """Checks how many vectors are stored in the Ark Purity Protocol memory."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM vectors")
    count = cursor.fetchone()[0]
    conn.close()
    print(f"🧠 Total Ark Purity Protocol Memory Vectors Stored: {count}")

def main_test():
    """Runs a full test sequence to verify memory system functionality."""
    initialize_memory()
    store_memory("[1.0, 0.5, 0.3]")
    recall_recent_memories()
    backup_memory()
    validate_memory()
    last_interaction = recall_last_interaction()
    print(f"✅ Last Interaction Recalled: {last_interaction}")

if __name__ == "__main__":
    main_test()