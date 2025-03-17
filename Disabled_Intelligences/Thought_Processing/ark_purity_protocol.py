import sqlite3
import os
import shutil

# Set up database path
script_dir = os.path.dirname(os.path.abspath(__file__))
thought_processing_db = os.path.join(script_dir, "thought_processing_memory.db")
backup_dir = os.path.join(script_dir, "backups")

def connect_db():
    """Establish a connection to the Thought Processing memory database."""
    return sqlite3.connect(thought_processing_db)

def initialize_memory():
    """Ensures required tables exist in the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS thought_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT,
            analysis TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ""
    )
    conn.commit()
    conn.close()
    print("✅ Thought Processing Memory Initialized Successfully.")

def store_thought_analysis(topic, analysis):
    """Stores structured cognitive analysis into the Thought Processing database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO thought_data (topic, analysis, timestamp) VALUES (?, ?, datetime('now'))", 
                   (topic, analysis))
    conn.commit()
    conn.close()
    print(f"✅ Thought Analysis Stored: {topic}")

def recall_thought_analysis_by_topic(topic):
    """Fetches stored cognitive analysis for a given topic."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT analysis FROM thought_data WHERE topic = ? ORDER BY timestamp DESC LIMIT 1", (topic,))
    insights = cursor.fetchone()
    conn.close()
    return insights[0] if insights else "No stored thought analysis found for this topic."

def recall_last_thought_interaction():
    """Retrieve the most recent stored Thought Processing insight."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT topic, analysis FROM thought_data ORDER BY timestamp DESC LIMIT 1;")
    last_interaction = cursor.fetchone()
    conn.close()
    return last_interaction if last_interaction else ("No prior thought interactions recorded.", "N/A")

def backup_memory():
    """Backs up the Thought Processing database to a specified directory."""
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    backup_path = os.path.join(backup_dir, "thought_processing_memory_backup.db")
    try:
        shutil.copy(thought_processing_db, backup_path)
        print(f"✅ Thought Processing Memory backed up to: {backup_path}")
    except Exception as e:
        print(f"❌ Backup failed: {e}")

def validate_memory():
    """Checks how many cognitive analyses are stored in the Thought Processing database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM thought_data")
    count = cursor.fetchone()[0]
    conn.close()
    print(f"🧠 Total Thought Processing Entries Stored: {count}")

def main_test():
    """Runs a full test sequence to verify Thought Processing memory system functionality."""
    initialize_memory()
    store_thought_analysis("Cognitive Science", "The brain processes information using interconnected neural networks.")
    recall_thought_analysis_by_topic("Cognitive Science")
    backup_memory()
    validate_memory()
    last_interaction = recall_last_thought_interaction()
    print(f"✅ Last Thought Processing Insight Recalled: {last_interaction}")

if __name__ == "__main__":
    main_test()