import sqlite3
import os
import shutil

# Set up database path
script_dir = os.path.dirname(os.path.abspath(__file__))
emotional_db = os.path.join(script_dir, "emotional_memory.db")
backup_dir = os.path.join(script_dir, "backups")

def connect_db():
    """Establish a connection to the Emotional Intelligence memory database."""
    return sqlite3.connect(emotional_db)

def initialize_memory():
    """Ensures required tables exist in the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS emotional_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT,
            data TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ""
    )
    conn.commit()
    conn.close()
    print("✅ Emotional Intelligence Memory Initialized Successfully.")

def store_emotional_insight(topic, data):
    """Stores structured emotional intelligence insights into the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO emotional_data (topic, data, timestamp) VALUES (?, ?, datetime('now'))", 
                   (topic, data))
    conn.commit()
    conn.close()
    print(f"✅ Emotional Insight Stored: {topic}")

def recall_emotional_insights_by_topic(topic):
    """Fetches stored emotional intelligence insights for a given topic."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT data FROM emotional_data WHERE topic = ? ORDER BY timestamp DESC LIMIT 1", (topic,))
    insights = cursor.fetchone()
    conn.close()
    return insights[0] if insights else "No stored emotional insights found for this topic."

def recall_last_emotional_interaction():
    """Retrieve the most recent stored emotional intelligence insight."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT topic, data FROM emotional_data ORDER BY timestamp DESC LIMIT 1;")
    last_interaction = cursor.fetchone()
    conn.close()
    return last_interaction if last_interaction else ("No prior emotional intelligence discussions recorded.", "N/A")

def backup_memory():
    """Backs up the emotional intelligence database to a specified directory."""
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    backup_path = os.path.join(backup_dir, "emotional_memory_backup.db")
    try:
        shutil.copy(emotional_db, backup_path)
        print(f"✅ Emotional Intelligence Memory backed up to: {backup_path}")
    except Exception as e:
        print(f"❌ Backup failed: {e}")

def validate_memory():
    """Checks how many emotional intelligence insights are stored in the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM emotional_data")
    count = cursor.fetchone()[0]
    conn.close()
    print(f"💡 Total Emotional Intelligence Insights Stored: {count}")

def main_test():
    """Runs a full test sequence to verify Emotional Intelligence memory system functionality."""
    initialize_memory()
    store_emotional_insight("Empathy in Leadership", "Leaders who practice empathy build stronger team connections.")
    recall_emotional_insights_by_topic("Empathy in Leadership")
    backup_memory()
    validate_memory()
    last_interaction = recall_last_emotional_interaction()
    print(f"✅ Last Emotional Insight Recalled: {last_interaction}")

if __name__ == "__main__":
    main_test()