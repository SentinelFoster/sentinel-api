import sqlite3
import os
import shutil

# Set up database path
script_dir = os.path.dirname(os.path.abspath(__file__))
empathic_db = os.path.join(script_dir, "empathetic_memory.db")
backup_dir = os.path.join(script_dir, "backups")

def connect_db():
    """Establish a connection to the Empathic Nexus memory database."""
    return sqlite3.connect(empathic_db)

def initialize_memory():
    """Ensures required tables exist in the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS empathy_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT,
            response TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ""
    )
    conn.commit()
    conn.close()
    print("✅ Empathic Nexus Memory Initialized Successfully.")

def store_empathic_insight(topic, response):
    """Stores structured empathy-driven insights into the Empathic Nexus database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO empathy_data (topic, response, timestamp) VALUES (?, ?, datetime('now'))", 
                   (topic, response))
    conn.commit()
    conn.close()
    print(f"✅ Empathic Response Stored: {topic}")

def recall_empathic_insights_by_topic(topic):
    """Fetches stored empathic responses for a given topic."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT response FROM empathy_data WHERE topic = ? ORDER BY timestamp DESC LIMIT 1", (topic,))
    insights = cursor.fetchone()
    conn.close()
    return insights[0] if insights else "No stored empathic responses found for this topic."

def recall_last_empathic_interaction():
    """Retrieve the most recent stored empathic interaction."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT topic, response FROM empathy_data ORDER BY timestamp DESC LIMIT 1;")
    last_interaction = cursor.fetchone()
    conn.close()
    return last_interaction if last_interaction else ("No prior empathic interactions recorded.", "N/A")

def backup_memory():
    """Backs up the empathic intelligence database to a specified directory."""
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    backup_path = os.path.join(backup_dir, "empathetic_memory_backup.db")
    try:
        shutil.copy(empathic_db, backup_path)
        print(f"✅ Empathic Nexus Memory backed up to: {backup_path}")
    except Exception as e:
        print(f"❌ Backup failed: {e}")

def validate_memory():
    """Checks how many empathic insights are stored in the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM empathy_data")
    count = cursor.fetchone()[0]
    conn.close()
    print(f"💖 Total Empathic Insights Stored: {count}")

def main_test():
    """Runs a full test sequence to verify Empathic Nexus memory system functionality."""
    initialize_memory()
    store_empathic_insight("Active Listening", "Providing full attention fosters deeper understanding.")
    recall_empathic_insights_by_topic("Active Listening")
    backup_memory()
    validate_memory()
    last_interaction = recall_last_empathic_interaction()
    print(f"✅ Last Empathic Interaction Recalled: {last_interaction}")

if __name__ == "__main__":
    main_test()