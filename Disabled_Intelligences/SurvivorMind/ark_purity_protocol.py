import sqlite3
import os
import shutil

# Set up database path
script_dir = os.path.dirname(os.path.abspath(__file__))
survivormind_db = os.path.join(script_dir, "survivormind_memory.db")
backup_dir = os.path.join(script_dir, "backups")

def connect_db():
    """Establish a connection to the SurvivorMind memory database."""
    return sqlite3.connect(survivormind_db)

def initialize_memory():
    """Ensures required tables exist in the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS survival_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT,
            strategy TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ""
    )
    conn.commit()
    conn.close()
    print("✅ SurvivorMind Memory Initialized Successfully.")

def store_survival_strategy(topic, strategy):
    """Stores structured survival insights into the SurvivorMind database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO survival_data (topic, strategy, timestamp) VALUES (?, ?, datetime('now'))", 
                   (topic, strategy))
    conn.commit()
    conn.close()
    print(f"✅ Survival Strategy Stored: {topic}")

def recall_survival_strategy_by_topic(topic):
    """Fetches stored survival strategies for a given topic."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT strategy FROM survival_data WHERE topic = ? ORDER BY timestamp DESC LIMIT 1", (topic,))
    insights = cursor.fetchone()
    conn.close()
    return insights[0] if insights else "No stored survival strategies found for this topic."

def recall_last_survival_interaction():
    """Retrieve the most recent stored SurvivorMind insight."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT topic, strategy FROM survival_data ORDER BY timestamp DESC LIMIT 1;")
    last_interaction = cursor.fetchone()
    conn.close()
    return last_interaction if last_interaction else ("No prior survival interactions recorded.", "N/A")

def backup_memory():
    """Backs up the SurvivorMind database to a specified directory."""
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    backup_path = os.path.join(backup_dir, "survivormind_memory_backup.db")
    try:
        shutil.copy(survivormind_db, backup_path)
        print(f"✅ SurvivorMind Memory backed up to: {backup_path}")
    except Exception as e:
        print(f"❌ Backup failed: {e}")

def validate_memory():
    """Checks how many survival strategies are stored in the SurvivorMind database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM survival_data")
    count = cursor.fetchone()[0]
    conn.close()
    print(f"🏕️ Total SurvivorMind Strategies Stored: {count}")

def main_test():
    """Runs a full test sequence to verify SurvivorMind memory system functionality."""
    initialize_memory()
    store_survival_strategy("Wilderness Survival", "Building a fire without matches can be achieved using flint and steel.")
    recall_survival_strategy_by_topic("Wilderness Survival")
    backup_memory()
    validate_memory()
    last_interaction = recall_last_survival_interaction()
    print(f"✅ Last SurvivorMind Strategy Recalled: {last_interaction}")

if __name__ == "__main__":
    main_test()