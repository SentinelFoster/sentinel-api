import sqlite3
import os
import shutil

# Set up database path
script_dir = os.path.dirname(os.path.abspath(__file__))
quantum_sage_db = os.path.join(script_dir, "quantum_sage_memory.db")
backup_dir = os.path.join(script_dir, "backups")

def connect_db():
    """Establish a connection to the Quantum Sage memory database."""
    return sqlite3.connect(quantum_sage_db)

def initialize_memory():
    """Ensures required tables exist in the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sage_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT,
            insight TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ""
    )
    conn.commit()
    conn.close()
    print("✅ Quantum Sage Memory Initialized Successfully.")

def store_quantum_insight(topic, insight):
    """Stores structured quantum computing insights into the Quantum Sage database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sage_data (topic, insight, timestamp) VALUES (?, ?, datetime('now'))", 
                   (topic, insight))
    conn.commit()
    conn.close()
    print(f"✅ Quantum Sage Insight Stored: {topic}")

def recall_quantum_insight_by_topic(topic):
    """Fetches stored quantum computing insights for a given topic."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT insight FROM sage_data WHERE topic = ? ORDER BY timestamp DESC LIMIT 1", (topic,))
    insights = cursor.fetchone()
    conn.close()
    return insights[0] if insights else "No stored quantum insights found for this topic."

def recall_last_quantum_interaction():
    """Retrieve the most recent stored Quantum Sage insight."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT topic, insight FROM sage_data ORDER BY timestamp DESC LIMIT 1;")
    last_interaction = cursor.fetchone()
    conn.close()
    return last_interaction if last_interaction else ("No prior quantum interactions recorded.", "N/A")

def backup_memory():
    """Backs up the Quantum Sage database to a specified directory."""
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    backup_path = os.path.join(backup_dir, "quantum_sage_memory_backup.db")
    try:
        shutil.copy(quantum_sage_db, backup_path)
        print(f"✅ Quantum Sage Memory backed up to: {backup_path}")
    except Exception as e:
        print(f"❌ Backup failed: {e}")

def validate_memory():
    """Checks how many quantum computing insights are stored in the Quantum Sage database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM sage_data")
    count = cursor.fetchone()[0]
    conn.close()
    print(f"⚛️ Total Quantum Sage Insights Stored: {count}")

def main_test():
    """Runs a full test sequence to verify Quantum Sage memory system functionality."""
    initialize_memory()
    store_quantum_insight("Quantum Entanglement", "Quantum entanglement allows particles to be correlated over vast distances.")
    recall_quantum_insight_by_topic("Quantum Entanglement")
    backup_memory()
    validate_memory()
    last_interaction = recall_last_quantum_interaction()
    print(f"✅ Last Quantum Sage Insight Recalled: {last_interaction}")

if __name__ == "__main__":
    main_test()