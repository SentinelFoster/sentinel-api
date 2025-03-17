import sqlite3
import os
import shutil

# Set up database path
script_dir = os.path.dirname(os.path.abspath(__file__))
lunar_sentinel_db = os.path.join(script_dir, "lunar_sentinel_memory.db")
backup_dir = os.path.join(script_dir, "backups")

def connect_db():
    """Establish a connection to the Lunar Sentinel Core memory database."""
    return sqlite3.connect(lunar_sentinel_db)

def initialize_memory():
    """Ensures required tables exist in the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS lunar_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT,
            data TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ""
    )
    conn.commit()
    conn.close()
    print("✅ Lunar Sentinel Core Memory Initialized Successfully.")

def store_lunar_insight(topic, data):
    """Stores structured lunar research insights into the Lunar Sentinel database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO lunar_data (topic, data, timestamp) VALUES (?, ?, datetime('now'))", 
                   (topic, data))
    conn.commit()
    conn.close()
    print(f"✅ Lunar Research Insight Stored: {topic}")

def recall_lunar_insights_by_topic(topic):
    """Fetches stored lunar research insights for a given topic."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT data FROM lunar_data WHERE topic = ? ORDER BY timestamp DESC LIMIT 1", (topic,))
    insights = cursor.fetchone()
    conn.close()
    return insights[0] if insights else "No stored lunar insights found for this topic."

def recall_last_lunar_interaction():
    """Retrieve the most recent stored lunar research insight."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT topic, data FROM lunar_data ORDER BY timestamp DESC LIMIT 1;")
    last_interaction = cursor.fetchone()
    conn.close()
    return last_interaction if last_interaction else ("No prior lunar research recorded.", "N/A")

def backup_memory():
    """Backs up the lunar research database to a specified directory."""
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    backup_path = os.path.join(backup_dir, "lunar_sentinel_memory_backup.db")
    try:
        shutil.copy(lunar_sentinel_db, backup_path)
        print(f"✅ Lunar Sentinel Core Memory backed up to: {backup_path}")
    except Exception as e:
        print(f"❌ Backup failed: {e}")

def validate_memory():
    """Checks how many research entries are stored in the Lunar Sentinel Core memory."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM lunar_data")
    count = cursor.fetchone()[0]
    conn.close()
    print(f"🌕 Total Lunar Research Entries Stored: {count}")

def main_test():
    """Runs a full test sequence to verify Lunar Sentinel Core memory system functionality."""
    initialize_memory()
    store_lunar_insight("Moon Terrain Analysis", "Recent scans indicate large ice deposits in lunar craters.")
    recall_lunar_insights_by_topic("Moon Terrain Analysis")
    backup_memory()
    validate_memory()
    last_interaction = recall_last_lunar_interaction()
    print(f"✅ Last Lunar Research Recalled: {last_interaction}")

if __name__ == "__main__":
    main_test()