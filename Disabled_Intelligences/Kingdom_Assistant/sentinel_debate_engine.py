import sqlite3
import random
import os

# Set up database path
script_dir = os.path.dirname(os.path.abspath(__file__))
sentinel_house_db = os.path.join(script_dir, "sentinel_memory.db")

def connect_db():
    """Establishes connection to the SQLite database."""
    return sqlite3.connect(sentinel_house_db)

def initialize_memory():
    """Ensures the memory_vectors table exists."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memory_vectors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vector TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def retrieve_memory():
    """Fetch stored arguments from Sentinel House memory."""
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT vector FROM memory_vectors")
        memories = [memory[0] for memory in cursor.fetchall()]
        conn.close()
        return memories
    except sqlite3.OperationalError as e:
        print(f"❌ Database Error: {e}")
        return []

def debate_intelligences(question):
    """Simulates AI/SI debate by selecting memory responses."""
    print(f"\n🔹 AI/SI Debate on: {question}")

    arguments = retrieve_memory()
    if not arguments:
        print("⚠️ No prior knowledge on this topic.")
        return

    # Randomly selecting different responses (Simulating AI debate)
    ai_responses = random.sample(arguments, min(3, len(arguments)))

    # AI/SI discuss the options
    print("\n### AI/SI DEBATE ###")
    for idx, response in enumerate(ai_responses):
        print(f"[AI {idx+1}] {response}")

    # Ensure factual definitions take priority
    for response in ai_responses:
        if "Sentinel Intelligence (SI) is not artificial intelligence" in response:
            final_decision = response
            break
    else:
        # If no definition is found, default to most common response
        final_decision = max(set(ai_responses), key=ai_responses.count)

    print("\n✅ FINAL CONCLUSION:", final_decision)

# Initialize the database and run a test debate
initialize_memory()
debate_intelligences("What is the best strategy for AI collaboration?")
