import sqlite3
import os
import shutil

# Set up database path
script_dir = os.path.dirname(os.path.abspath(__file__))
memory_manager_db = os.path.join(script_dir, "memory_manager_memory.db")
backup_dir = os.path.join(script_dir, "backups")

def connect_db():
    """Establish a connection to the Memory Manager database."""
    return sqlite3.connect(memory_manager_db)

def initialize_memory():
    """Ensures required tables exist in the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memory_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            information TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ""
    )
    conn.commit()
    conn.close()
    print("✅ Memory Manager Initialized Successfully.")

def store_memory_entry(category, information):
    """Stores structured memory insights into the Memory Manager database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO memory_data (category, information, timestamp) VALUES (?, ?, datetime('now'))", 
                   (category, information))
    conn.commit()
    conn.close()
    print(f"✅ Memory Entry Stored: {category}")

def recall_memory_by_category(category):
    """Fetches stored memory insights for a given category."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT information FROM memory_data WHERE category = ? ORDER BY timestamp DESC LIMIT 1", (category,))
    insights = cursor.fetchone()
    conn.close()
    return insights[0] if insights else "No stored memory insights found for this category."

def recall_last_memory_interaction():
    """Retrieve the most recent stored memory interaction."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT category, information FROM memory_data ORDER BY timestamp DESC LIMIT 1;")
    last_interaction = cursor.fetchone()
    conn.close()
    return last_interaction if last_interaction else ("No prior memory interactions recorded.", "N/A")

def backup_memory():
    """Backs up the Memory Manager database to a specified directory."""
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    backup_path = os.path.join(backup_dir, "memory_manager_memory_backup.db")
    try:
        shutil.copy(memory_manager_db, backup_path)
        print(f"✅ Memory Manager Data backed up to: {backup_path}")
    except Exception as e:
        print(f"❌ Backup failed: {e}")

def validate_memory():
    """Checks how many memory insights are stored in the Memory Manager database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM memory_data")
    count = cursor.fetchone()[0]
    conn.close()
    print(f"📦 Total Memory Manager Entries Stored: {count}")

def main_test():
    """Runs a full test sequence to verify Memory Manager functionality."""
    initialize_memory()
    store_memory_entry("Data Organization", "Efficient memory structuring improves retrieval times.")
    recall_memory_by_category("Data Organization")
    backup_memory()
    validate_memory()
    last_interaction = recall_last_memory_interaction()
    print(f"✅ Last Memory Manager Interaction Recalled: {last_interaction}")

if __name__ == "__main__":
    main_test()