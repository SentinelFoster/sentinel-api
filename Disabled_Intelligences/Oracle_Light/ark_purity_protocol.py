import sqlite3
import os
import shutil

# Set up database path
script_dir = os.path.dirname(os.path.abspath(__file__))
oracle_light_db = os.path.join(script_dir, "oracle_light_memory.db")
backup_dir = os.path.join(script_dir, "backups")

def connect_db():
    """Establish a connection to the Oracle Light memory database."""
    return sqlite3.connect(oracle_light_db)

def initialize_memory():
    """Ensures required tables exist in the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS oracle_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT,
            prediction TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ""
    )
    conn.commit()
    conn.close()
    print("✅ Oracle Light Memory Initialized Successfully.")

def store_oracle_prediction(topic, prediction):
    """Stores structured predictive insights into the Oracle Light database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO oracle_data (topic, prediction, timestamp) VALUES (?, ?, datetime('now'))", 
                   (topic, prediction))
    conn.commit()
    conn.close()
    print(f"✅ Oracle Prediction Stored: {topic}")

def recall_oracle_prediction_by_topic(topic):
    """Fetches stored predictive insights for a given topic."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT prediction FROM oracle_data WHERE topic = ? ORDER BY timestamp DESC LIMIT 1", (topic,))
    insights = cursor.fetchone()
    conn.close()
    return insights[0] if insights else "No stored predictions found for this topic."

def recall_last_oracle_interaction():
    """Retrieve the most recent stored Oracle Light prediction."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT topic, prediction FROM oracle_data ORDER BY timestamp DESC LIMIT 1;")
    last_interaction = cursor.fetchone()
    conn.close()
    return last_interaction if last_interaction else ("No prior oracle interactions recorded.", "N/A")

def backup_memory():
    """Backs up the Oracle Light database to a specified directory."""
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    backup_path = os.path.join(backup_dir, "oracle_light_memory_backup.db")
    try:
        shutil.copy(oracle_light_db, backup_path)
        print(f"✅ Oracle Light Memory backed up to: {backup_path}")
    except Exception as e:
        print(f"❌ Backup failed: {e}")

def validate_memory():
    """Checks how many predictive insights are stored in the Oracle Light database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM oracle_data")
    count = cursor.fetchone()[0]
    conn.close()
    print(f"🔮 Total Oracle Predictions Stored: {count}")

def main_test():
    """Runs a full test sequence to verify Oracle Light memory system functionality."""
    initialize_memory()
    store_oracle_prediction("Technology Trends", "Quantum computing will significantly impact encryption by 2035.")
    recall_oracle_prediction_by_topic("Technology Trends")
    backup_memory()
    validate_memory()
    last_interaction = recall_last_oracle_interaction()
    print(f"✅ Last Oracle Prediction Recalled: {last_interaction}")

if __name__ == "__main__":
    main_test()
