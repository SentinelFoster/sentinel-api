import sqlite3
import os
import shutil

# Set up database path
script_dir = os.path.dirname(os.path.abspath(__file__))
qlf_db = os.path.join(script_dir, "qlf_memory.db")
backup_dir = os.path.join(script_dir, "backups")

def connect_db():
    """Establish a connection to the Quantum Logic Framework memory database."""
    return sqlite3.connect(qlf_db)

def initialize_memory():
    """Ensures required tables exist in the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logical_vectors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT,
            data TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ""
    )
    conn.commit()
    conn.close()
    print("✅ Quantum Logic Framework Memory Initialized Successfully.")

def store_logical_insight(topic, data):
    """Stores structured logical insights into the QLF database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO logical_vectors (topic, data, timestamp) VALUES (?, ?, datetime('now'))", 
                   (topic, data))
    conn.commit()
    conn.close()
    print(f"✅ Logical Insight Stored: {topic}")

def recall_logical_insights_by_topic(topic):
    """Fetches stored logical insights for a given topic."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT data FROM logical_vectors WHERE topic = ? ORDER BY timestamp DESC LIMIT 1", (topic,))
    insights = cursor.fetchone()
    conn.close()
    return insights[0] if insights else "No stored insights found for this topic."

def recall_last_logical_interaction():
    """Retrieve the most recent stored logical interaction."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT topic, data FROM logical_vectors ORDER BY timestamp DESC LIMIT 1;")
    last_interaction = cursor.fetchone()
    conn.close()
    return last_interaction if last_interaction else ("No prior logical interactions recorded.", "N/A")

def backup_memory():
    """Backs up the logical insights database to a specified directory."""
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    backup_path = os.path.join(backup_dir, "qlf_memory_backup.db")
    try:
        shutil.copy(qlf_db, backup_path)
        print(f"✅ QLF Memory backed up to: {backup_path}")
    except Exception as e:
        print(f"❌ Backup failed: {e}")

def validate_memory():
    """Checks how many logical insights are stored in the Quantum Logic Framework memory."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM logical_vectors")
    count = cursor.fetchone()[0]
    conn.close()
    print(f"🧠 Total QLF Logical Insights Stored: {count}")

def main_test():
    """Runs a full test sequence to verify QLF memory system functionality."""
    initialize_memory()
    store_logical_insight("Quantum Computing", "Quantum bits (qubits) can exist in superposition states.")
    recall_logical_insights_by_topic("Quantum Computing")
    backup_memory()
    validate_memory()
    last_interaction = recall_last_logical_interaction()
    print(f"✅ Last Logical Interaction Recalled: {last_interaction}")

if __name__ == "__main__":
    main_test()