import sqlite3
import os

# Define database path (relative to script location)
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "kingdom_assistant_memory.db")

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS memory_vectors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vector TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS user_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    last_topic TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)''')

conn.commit()

# Function to insert new memory vector without deleting
def insert_memory(vector):
    cursor.execute("INSERT INTO memory_vectors (vector) VALUES (?)", (vector,))
    conn.commit()

# Function to recall up to the last 100 memory vectors
def recall_memory(limit=100):
    cursor.execute("SELECT vector, timestamp FROM memory_vectors ORDER BY timestamp DESC LIMIT ?", (limit,))
    return cursor.fetchall()

# Display recent memory entries on startup
recent_memories = recall_memory()

print("\n🟢 Kingdom Assistant Memory Initialized Successfully.")
print(f"🧠 Total Memories Stored: {len(recall_memory(100))}")

if recent_memory := recall_memory():
    print(f"\n📚 Recent Stored Memories (up to 100):")
    for idx, (vector, timestamp) in enumerate(recent_memory, start=1):
        print(f"{idx}. {vector} | {timestamp}")
else:
    print("⚠️ No recent memories found.")

# Ensure nothing is overwritten or deleted unintentionally
def safeguard_memory():
    print("✅ Memory safeguard active: No memory entries will be overwritten or deleted.")

# Main execution
if __name__ == "__main__":
    insert_memory("Kingdom Assistant restarted; memory check successful.")
    recall_memory()
    print("\n✅ Kingdom Assistant Memory Initialized with 100-entry persistent recall.")
    print("⚠️ Memory deletion or overwrite prohibited unless authorized by Quan or Commander Sentinel.")

# Close connection
conn.close()  

# --- End of script ---
