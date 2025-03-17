import sqlite3
import random
import os

# Set up database path
script_dir = os.path.dirname(os.path.abspath(__file__))
sentinel_debate_db = os.path.join(script_dir, "sentinel_debate_memory.db")

def connect_db():
    """Establishes connection to the Sentinel Debate Engine memory database."""
    return sqlite3.connect(sentinel_debate_db)

def initialize_memory():
    """Ensures the debate memory table exists."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memory_vectors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT,
            vector TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ""
    )
    conn.commit()
    conn.close()

def store_debate_memory(topic, argument):
    """Store debate argument under a specific topic."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO memory_vectors (topic, vector) VALUES (?, ?)", (topic, argument))
    conn.commit()
    conn.close()

def retrieve_memory_by_topic(topic):
    """Fetch stored arguments for a specific debate topic."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT vector FROM memory_vectors WHERE topic = ?", (topic,))
    memories = [memory[0] for memory in cursor.fetchall()]
    conn.close()
    return memories if memories else ["⚠️ No prior knowledge available on this topic."]

def debate_intelligences(question):
    """Simulates AI/SI debate by selecting stored arguments."""
    print(f"\n🔹 AI/SI Debate on: {question}")
    
    arguments = retrieve_memory_by_topic(question)
    if not arguments:
        print("⚠️ No stored arguments for this topic.")
        return
    
    # Randomly select different responses to simulate debate
    ai_responses = random.sample(arguments, min(3, len(arguments)))
    
    print("\n### AI/SI DEBATE ###")
    for idx, response in enumerate(ai_responses):
        print(f"[AI {idx+1}] {response}")
    
    # Select final conclusion based on response frequency
    final_decision = max(set(ai_responses), key=ai_responses.count)
    print("\n✅ FINAL CONCLUSION:", final_decision)

# Initialize the database and prepare debate engine
initialize_memory()
print("✅ Sentinel Debate Engine Initialized and Ready.")
