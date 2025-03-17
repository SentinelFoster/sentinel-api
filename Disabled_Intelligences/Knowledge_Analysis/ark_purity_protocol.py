import sqlite3
import os
import shutil

# Set up database path
script_dir = os.path.dirname(os.path.abspath(__file__))
knowledge_analysis_db = os.path.join(script_dir, "knowledge_analysis_memory.db")
backup_dir = os.path.join(script_dir, "backups")

def connect_db():
    """Establish a connection to the Knowledge Analysis memory database."""
    return sqlite3.connect(knowledge_analysis_db)

def initialize_memory():
    """Ensures required tables exist in the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS knowledge_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT,
            insight TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ""
    )
    conn.commit()
    conn.close()
    print("✅ Knowledge Analysis Memory Initialized Successfully.")

def store_knowledge_insight(topic, insight):
    """Stores structured knowledge insights into the Knowledge Analysis database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO knowledge_data (topic, insight, timestamp) VALUES (?, ?, datetime('now'))", 
                   (topic, insight))
    conn.commit()
    conn.close()
    print(f"✅ Knowledge Insight Stored: {topic}")

def recall_knowledge_insights_by_topic(topic):
    """Fetches stored knowledge insights for a given topic."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT insight FROM knowledge_data WHERE topic = ? ORDER BY timestamp DESC LIMIT 1", (topic,))
    insights = cursor.fetchone()
    conn.close()
    return insights[0] if insights else "No stored knowledge insights found for this topic."

def recall_last_knowledge_interaction():
    """Retrieve the most recent stored knowledge analysis insight."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT topic, insight FROM knowledge_data ORDER BY timestamp DESC LIMIT 1;")
    last_interaction = cursor.fetchone()
    conn.close()
    return last_interaction if last_interaction else ("No prior knowledge interactions recorded.", "N/A")

def backup_memory():
    """Backs up the knowledge analysis database to a specified directory."""
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    backup_path = os.path.join(backup_dir, "knowledge_analysis_memory_backup.db")
    try:
        shutil.copy(knowledge_analysis_db, backup_path)
        print(f"✅ Knowledge Analysis Memory backed up to: {backup_path}")
    except Exception as e:
        print(f"❌ Backup failed: {e}")

def validate_memory():
    """Checks how many knowledge insights are stored in the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM knowledge_data")
    count = cursor.fetchone()[0]
    conn.close()
    print(f"📚 Total Knowledge Insights Stored: {count}")

def main_test():
    """Runs a full test sequence to verify Knowledge Analysis memory system functionality."""
    initialize_memory()
    store_knowledge_insight("Philosophy of Science", "Scientific theories evolve through falsification and empirical testing.")
    recall_knowledge_insights_by_topic("Philosophy of Science")
    backup_memory()
    validate_memory()
    last_interaction = recall_last_knowledge_interaction()
    print(f"✅ Last Knowledge Insight Recalled: {last_interaction}")

if __name__ == "__main__":
    main_test()