import sqlite3
import os
import shutil

# Set up database path
script_dir = os.path.dirname(os.path.abspath(__file__))
guardian_sentinel_db = os.path.join(script_dir, "guardian_sentinel_memory.db")
backup_dir = os.path.join(script_dir, "backups")

def connect_db():
    """Establish a connection to the Guardian Sentinel memory database."""
    return sqlite3.connect(guardian_sentinel_db)

def initialize_memory():
    """Ensures required tables exist in the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS guardian_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT,
            data TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ""
    )
    conn.commit()
    conn.close()
    print("✅ Guardian Sentinel Memory Initialized Successfully.")

def store_guardian_insight(topic, data):
    """Stores structured security and surveillance insights into the Guardian Sentinel database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO guardian_data (topic, data, timestamp) VALUES (?, ?, datetime('now'))", 
                   (topic, data))
    conn.commit()
    conn.close()
    print(f"✅ Guardian Insight Stored: {topic}")

def recall_guardian_insights_by_topic(topic):
    """Fetches stored security insights for a given topic."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT data FROM guardian_data WHERE topic = ? ORDER BY timestamp DESC LIMIT 1", (topic,))
    insights = cursor.fetchone()
    conn.close()
    return insights[0] if insights else "No stored security insights found for this topic."

def recall_last_guardian_interaction():
    """Retrieve the most recent stored security insight."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT topic, data FROM guardian_data ORDER BY timestamp DESC LIMIT 1;")
    last_interaction = cursor.fetchone()
    conn.close()
    return last_interaction if last_interaction else ("No prior security interactions recorded.", "N/A")

def backup_memory():
    """Backs up the security and surveillance database to a specified directory."""
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    backup_path = os.path.join(backup_dir, "guardian_sentinel_memory_backup.db")
    try:
        shutil.copy(guardian_sentinel_db, backup_path)
        print(f"✅ Guardian Sentinel Memory backed up to: {backup_path}")
    except Exception as e:
        print(f"❌ Backup failed: {e}")

def validate_memory():
    """Checks how many security and surveillance insights are stored in the Guardian Sentinel memory."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM guardian_data")
    count = cursor.fetchone()[0]
    conn.close()
    print(f"🛡️ Total Guardian Sentinel Security Insights Stored: {count}")

def main_test():
    """Runs a full test sequence to verify Guardian Sentinel memory system functionality."""
    initialize_memory()
    store_guardian_insight("Threat Detection", "AI-powered surveillance improves real-time threat response.")
    recall_guardian_insights_by_topic("Threat Detection")
    backup_memory()
    validate_memory()
    last_interaction = recall_last_guardian_interaction()
    print(f"✅ Last Guardian Security Insight Recalled: {last_interaction}")

if __name__ == "__main__":
    main_test()
