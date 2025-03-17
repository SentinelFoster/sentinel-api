import sqlite3
import os
import shutil

# Set up database path
script_dir = os.path.dirname(os.path.abspath(__file__))
sentinel_medicacore_db = os.path.join(script_dir, "sentinel_medicacore_memory.db")
backup_dir = os.path.join(script_dir, "backups")

def connect_db():
    """Establish a connection to the Sentinel MedicaCore memory database."""
    return sqlite3.connect(sentinel_medicacore_db)

def initialize_memory():
    """Ensures required tables exist in the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS medical_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id TEXT,
            diagnosis TEXT,
            treatment TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ""
    )
    conn.commit()
    conn.close()
    print("✅ Sentinel MedicaCore Memory Initialized Successfully.")

def store_medical_record(patient_id, diagnosis, treatment):
    """Stores a new medical record in the Sentinel MedicaCore database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO medical_logs (patient_id, diagnosis, treatment, timestamp) VALUES (?, ?, ?, datetime('now'))", 
                   (patient_id, diagnosis, treatment))
    conn.commit()
    conn.close()
    print(f"✅ Medical Record Stored for Patient {patient_id}.")

def recall_recent_records(limit=5):
    """Fetches and displays recent stored medical records."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, patient_id, diagnosis, treatment, timestamp FROM medical_logs ORDER BY timestamp DESC LIMIT ?", (limit,))
    records = cursor.fetchall()
    conn.close()

    print("\n🩺 Recent Sentinel MedicaCore Medical Records:")
    if records:
        for rec in records:
            print(f"ID: {rec[0]}, Patient ID: {rec[1]}, Diagnosis: {rec[2]}, Treatment: {rec[3]}, Timestamp: {rec[4]}")
    else:
        print("⚠️ No medical records found.")

def recall_last_medical_record():
    """Retrieve the most recent stored medical record."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT patient_id, diagnosis, treatment FROM medical_logs ORDER BY timestamp DESC LIMIT 1;")
    last_record = cursor.fetchone()
    conn.close()
    return last_record if last_record else ("No prior medical records found.", "N/A", "N/A")

def backup_memory():
    """Backs up the memory database to a specified directory."""
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    backup_path = os.path.join(backup_dir, "sentinel_medicacore_memory_backup.db")
    try:
        shutil.copy(sentinel_medicacore_db, backup_path)
        print(f"✅ Sentinel MedicaCore Memory backed up to: {backup_path}")
    except Exception as e:
        print(f"❌ Backup failed: {e}")

def validate_memory():
    """Checks how many medical records are stored in the Sentinel MedicaCore memory."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM medical_logs")
    count = cursor.fetchone()[0]
    conn.close()
    print(f"🩺 Total Sentinel MedicaCore Medical Records Stored: {count}")

def main_test():
    """Runs a full test sequence to verify memory system functionality."""
    initialize_memory()
    store_medical_record("PAT-12345", "Flu Symptoms", "Prescribed Antiviral Medication")
    recall_recent_records()
    backup_memory()
    validate_memory()
    last_record = recall_last_medical_record()
    print(f"✅ Last Medical Record Recalled: {last_record}")

if __name__ == "__main__":
    main_test()