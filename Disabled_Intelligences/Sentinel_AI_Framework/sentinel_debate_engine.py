import sqlite3
import random
import os

# Automatically set the path to match the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))
sentinel_house_db = os.path.join(script_dir, "sentinel_house_memory.db")

# AI/SI debate logic
def debate_intelligences(question):
    try:
        conn = sqlite3.connect(sentinel_house_db)
        cursor = conn.cursor()

        # Fetch stored answers from Sentinel House memory
        cursor.execute("SELECT memory_data FROM memory")
        memories = cursor.fetchall()

        # Simulating each AI/SI presenting an argument
        arguments = [memory[0] for memory in memories]
        if not arguments:
            print("No prior knowledge on this topic.")
            return

        # Randomly selecting different responses (Simulating AI debate)
        ai_responses = random.sample(arguments, min(3, len(arguments)))

        # AI/SI discuss the options
        print("\n### AI/SI DEBATE ###")
        for idx, response in enumerate(ai_responses):
            print(f"[AI {idx+1}] {response}")

        # Consensus: Most frequent or logical response wins
        final_decision = max(set(ai_responses), key=ai_responses.count)
        print("\nFINAL CONCLUSION:", final_decision)

        conn.close()
    except Exception as e:
        print(f"Error retrieving data: {e}")

# Example test question
debate_intelligences("What is the best strategy for AI collaboration?")
