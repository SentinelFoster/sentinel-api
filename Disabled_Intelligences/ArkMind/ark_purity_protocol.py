import sqlite3
import os
import shutil

# Set up database path
script_dir = os.path.dirname(os.path.abspath(__file__))
arkmind_db = os.path.join(script_dir, "arkmind_memory.db")
backup_dir = os.path.join(script_dir, "backups")

def connect_db():
    """Establish a connection to the ArkMind memory database."""
    return sqlite3.connect(arkmind_db)

def initialize_memory():
    """Ensures required tables exist in the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cognitive_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT,
            data TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ""
    )
    conn.commit()
    conn.close()
    print("✅ ArkMind Memory Initialized Successfully.")

def store_cognitive_insight(topic, data):
    """Stores structured cognitive insights into the ArkMind database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cognitive_data (topic, data, timestamp) VALUES (?, ?, datetime('now'))", 
                   (topic, data))
    conn.commit()
    conn.close()
    print(f"✅ Cognitive Insight Stored: {topic}")

def recall_cognitive_insights_by_topic(topic):
    """Fetches stored cognitive insights for a given topic."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT data FROM cognitive_data WHERE topic = ? ORDER BY timestamp DESC LIMIT 1", (topic,))
    insights = cursor.fetchone()
    conn.close()
    return insights[0] if insights else "No stored cognitive insights found for this topic."

def recall_last_cognitive_interaction():
    """Retrieve the most recent stored cognitive interaction."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT topic, data FROM cognitive_data ORDER BY timestamp DESC LIMIT 1;")
    last_interaction = cursor.fetchone()
    conn.close()
    return last_interaction if last_interaction else ("No prior cognitive interactions recorded.", "N/A")

def backup_memory():
    """Backs up the cognitive data database to a specified directory."""
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    backup_path = os.path.join(backup_dir, "arkmind_memory_backup.db")
    try:
        shutil.copy(arkmind_db, backup_path)
        print(f"✅ ArkMind Memory backed up to: {backup_path}")
    except Exception as e:
        print(f"❌ Backup failed: {e}")

def validate_memory():
    """Checks how many cognitive insights are stored in the ArkMind memory."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM cognitive_data")
    count = cursor.fetchone()[0]
    conn.close()
    print(f"🧠 Total ArkMind Cognitive Insights Stored: {count}")

def main_test():
    """Runs a full test sequence to verify ArkMind memory system functionality."""
    initialize_memory()
    store_cognitive_insight("Neural Networks", "Deep learning models utilize multi-layered perceptrons for advanced pattern recognition.")
    recall_cognitive_insights_by_topic("Neural Networks")
    backup_memory()
    validate_memory()
    last_interaction = recall_last_cognitive_interaction()
    print(f"✅ Last Cognitive Insight Recalled: {last_interaction}")

if __name__ == "__main__":
    main_test()