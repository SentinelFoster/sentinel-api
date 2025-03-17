import sqlite3
import os
import shutil

# Set up database path
script_dir = os.path.dirname(os.path.abspath(__file__))
memory_hub_db = os.path.join(script_dir, "memory_hub_memory.db")
backup_dir = os.path.join(script_dir, "backups")

def connect_db():
    """Establish a connection to the Memory Hub database."""
    return sqlite3.connect(memory_hub_db)

def initialize_memory():
    """Ensures required tables exist in the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS hub_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            information TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ""
    )
    conn.commit()
    conn.close()
    print("✅ Memory Hub Initialized Successfully.")

def store_hub_information(category, information):
    """Stores structured memory insights into the Memory Hub database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO hub_data (category, information, timestamp) VALUES (?, ?, datetime('now'))", 
                   (category, information))
    conn.commit()
    conn.close()
    print(f"✅ Memory Hub Information Stored: {category}")

def recall_hub_information_by_category(category):
    """Fetches stored memory insights for a given category."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT information FROM hub_data WHERE category = ? ORDER BY timestamp DESC LIMIT 1", (category,))
    insights = cursor.fetchone()
    conn.close()
    return insights[0] if insights else "No stored memory insights found for this category."

def recall_last_hub_interaction():
    """Retrieve the most recent stored memory interaction."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT category, information FROM hub_data ORDER BY timestamp DESC LIMIT 1;")
    last_interaction = cursor.fetchone()
    conn.close()
    return last_interaction if last_interaction else ("No prior memory interactions recorded.", "N/A")

def backup_memory():
    """Backs up the memory hub database to a specified directory."""
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    backup_path = os.path.join(backup_dir, "memory_hub_memory_backup.db")
    try:
        shutil.copy(memory_hub_db, backup_path)
        print(f"✅ Memory Hub Data backed up to: {backup_path}")
    except Exception as e:
        print(f"❌ Backup failed: {e}")

def validate_memory():
    """Checks how many memory insights are stored in the Memory Hub database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM hub_data")
    count = cursor.fetchone()[0]
    conn.close()
    print(f"📦 Total Memory Hub Entries Stored: {count}")

def main_test():
    """Runs a full test sequence to verify Memory Hub functionality."""
    initialize_memory()
    store_hub_information("AI Models", "Transformers are widely used in natural language processing.")
    recall_hub_information_by_category("AI Models")
    backup_memory()
    validate_memory()
    last_interaction = recall_last_hub_interaction()
    print(f"✅ Last Memory Hub Interaction Recalled: {last_interaction}")

if __name__ == "__main__":
    main_test()