import sqlite3
import os
import shutil

# Set up database path
script_dir = os.path.dirname(os.path.abspath(__file__))
ironroot_sentinel_db = os.path.join(script_dir, "ironroot_sentinel_memory.db")
backup_dir = os.path.join(script_dir, "backups")

def connect_db():
    """Establish a connection to the IronRoot Sentinel memory database."""
    return sqlite3.connect(ironroot_sentinel_db)

def initialize_memory():
    """Ensures required tables exist in the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS root_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT,
            data TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ""
    )
    conn.commit()
    conn.close()
    print("✅ IronRoot Sentinel Memory Initialized Successfully.")

def store_root_insight(topic, data):
    """Stores structured insights related to security and infrastructure into the IronRoot Sentinel database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO root_data (topic, data, timestamp) VALUES (?, ?, datetime('now'))", 
                   (topic, data))
    conn.commit()
    conn.close()
    print(f"✅ Root Insight Stored: {topic}")

def recall_root_insights_by_topic(topic):
    """Fetches stored root security and infrastructure insights for a given topic."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT data FROM root_data WHERE topic = ? ORDER BY timestamp DESC LIMIT 1", (topic,))
    insights = cursor.fetchone()
    conn.close()
    return insights[0] if insights else "No stored insights found for this topic."

def recall_last_root_interaction():
    """Retrieve the most recent stored security or infrastructure insight."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT topic, data FROM root_data ORDER BY timestamp DESC LIMIT 1;")
    last_interaction = cursor.fetchone()
    conn.close()
    return last_interaction if last_interaction else ("No prior root interactions recorded.", "N/A")

def backup_memory():
    """Backs up the root security and infrastructure database to a specified directory."""
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    backup_path = os.path.join(backup_dir, "ironroot_sentinel_memory_backup.db")
    try:
        shutil.copy(ironroot_sentinel_db, backup_path)
        print(f"✅ IronRoot Sentinel Memory backed up to: {backup_path}")
    except Exception as e:
        print(f"❌ Backup failed: {e}")

def validate_memory():
    """Checks how many security and infrastructure insights are stored in the IronRoot Sentinel memory."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM root_data")
    count = cursor.fetchone()[0]
    conn.close()
    print(f"🛡️ Total IronRoot Sentinel Security Entries Stored: {count}")

def main_test():
    """Runs a full test sequence to verify IronRoot Sentinel memory system functionality."""
    initialize_memory()
    store_root_insight("Network Security", "Multi-factor authentication increases security layers.")
    recall_root_insights_by_topic("Network Security")
    backup_memory()
    validate_memory()
    last_interaction = recall_last_root_interaction()
    print(f"✅ Last Root Security Insight Recalled: {last_interaction}")

if __name__ == "__main__":
    main_test()
