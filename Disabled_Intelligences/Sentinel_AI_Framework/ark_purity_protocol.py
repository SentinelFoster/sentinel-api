import sqlite3
import os
import shutil

# Set up database path
script_dir = os.path.dirname(os.path.abspath(__file__))
sentinel_ai_db = os.path.join(script_dir, "sentinel_ai_memory.db")
backup_dir = os.path.join(script_dir, "backups")

def connect_db():
    """Establish a connection to the Sentinel AI memory database."""
    return sqlite3.connect(sentinel_ai_db)

def initialize_memory():
    """Ensures required tables exist in the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ai_knowledge (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT,
            data TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ""
    )
    conn.commit()
    conn.close()
    print("✅ Sentinel AI Memory Initialized Successfully.")

def store_ai_knowledge(topic, data):
    """Stores structured AI knowledge into the Sentinel AI database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ai_knowledge (topic, data, timestamp) VALUES (?, ?, datetime('now'))", 
                   (topic, data))
    conn.commit()
    conn.close()
    print(f"✅ AI Knowledge Stored: {topic}")

def recall_knowledge_by_topic(topic):
    """Fetches stored AI knowledge for a given topic."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT data FROM ai_knowledge WHERE topic = ? ORDER BY timestamp DESC LIMIT 1", (topic,))
    knowledge = cursor.fetchone()
    conn.close()
    return knowledge[0] if knowledge else "No stored knowledge found for this topic."

def recall_last_ai_interaction():
    """Retrieve the most recent stored AI knowledge interaction."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT topic, data FROM ai_knowledge ORDER BY timestamp DESC LIMIT 1;")
    last_interaction = cursor.fetchone()
    conn.close()
    return last_interaction if last_interaction else ("No prior AI interactions recorded.", "N/A")

def backup_memory():
    """Backs up the AI knowledge database to a specified directory."""
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    backup_path = os.path.join(backup_dir, "sentinel_ai_memory_backup.db")
    try:
        shutil.copy(sentinel_ai_db, backup_path)
        print(f"✅ Sentinel AI Memory backed up to: {backup_path}")
    except Exception as e:
        print(f"❌ Backup failed: {e}")

def validate_memory():
    """Checks how many knowledge entries are stored in the Sentinel AI memory."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM ai_knowledge")
    count = cursor.fetchone()[0]
    conn.close()
    print(f"🤖 Total Sentinel AI Knowledge Entries Stored: {count}")

def main_test():
    """Runs a full test sequence to verify AI memory system functionality."""
    initialize_memory()
    store_ai_knowledge("Machine Learning", "AI can learn from data using models like neural networks.")
    recall_knowledge_by_topic("Machine Learning")
    backup_memory()
    validate_memory()
    last_interaction = recall_last_ai_interaction()
    print(f"✅ Last AI Interaction Recalled: {last_interaction}")

if __name__ == "__main__":
    main_test()
