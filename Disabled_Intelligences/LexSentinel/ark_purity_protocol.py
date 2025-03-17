import sqlite3
import os
import shutil

# Set up database path
script_dir = os.path.dirname(os.path.abspath(__file__))
lexsentinel_db = os.path.join(script_dir, "lexsentinel_memory.db")
backup_dir = os.path.join(script_dir, "backups")

def connect_db():
    """Establish a connection to the LexSentinel memory database."""
    return sqlite3.connect(lexsentinel_db)

def initialize_memory():
    """Ensures required tables exist in the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS legal_insights (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT,
            data TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ""
    )
    conn.commit()
    conn.close()
    print("✅ LexSentinel Memory Initialized Successfully.")

def store_legal_insight(topic, data):
    """Stores structured legal insights into the LexSentinel database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO legal_insights (topic, data, timestamp) VALUES (?, ?, datetime('now'))", 
                   (topic, data))
    conn.commit()
    conn.close()
    print(f"✅ Legal Insight Stored: {topic}")

def recall_legal_insights_by_topic(topic):
    """Fetches stored legal insights for a given topic."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT data FROM legal_insights WHERE topic = ? ORDER BY timestamp DESC LIMIT 1", (topic,))
    insights = cursor.fetchone()
    conn.close()
    return insights[0] if insights else "No stored legal insights found for this topic."

def recall_last_legal_interaction():
    """Retrieve the most recent stored legal discussion."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT topic, data FROM legal_insights ORDER BY timestamp DESC LIMIT 1;")
    last_interaction = cursor.fetchone()
    conn.close()
    return last_interaction if last_interaction else ("No prior legal discussions recorded.", "N/A")

def backup_memory():
    """Backs up the legal insights database to a specified directory."""
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    backup_path = os.path.join(backup_dir, "lexsentinel_memory_backup.db")
    try:
        shutil.copy(lexsentinel_db, backup_path)
        print(f"✅ LexSentinel Memory backed up to: {backup_path}")
    except Exception as e:
        print(f"❌ Backup failed: {e}")

def validate_memory():
    """Checks how many legal insights are stored in the LexSentinel memory."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM legal_insights")
    count = cursor.fetchone()[0]
    conn.close()
    print(f"⚖️ Total LexSentinel Legal Insights Stored: {count}")

def main_test():
    """Runs a full test sequence to verify LexSentinel memory system functionality."""
    initialize_memory()
    store_legal_insight("Contract Law", "A valid contract requires offer, acceptance, and consideration.")
    recall_legal_insights_by_topic("Contract Law")
    backup_memory()
    validate_memory()
    last_interaction = recall_last_legal_interaction()
    print(f"✅ Last Legal Insight Recalled: {last_interaction}")

if __name__ == "__main__":
    main_test()