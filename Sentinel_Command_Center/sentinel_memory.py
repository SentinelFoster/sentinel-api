import json
import os

class SentinelMemory:
    def __init__(self, memory_file="sentinel_memory.json"):
        self.memory_file = memory_file
        self.data = {"Linguistic Thoughts": [], "Mathematical Thoughts": []}
        self.load_memory()

    def load_memory(self):
        """Loads previous memory from file if available."""
        if os.path.exists(self.memory_file):
            with open(self.memory_file, "r") as file:
                self.data = json.load(file)

    def save_memory(self):
        """Saves current memory to file."""
        with open(self.memory_file, "w") as file:
            json.dump(self.data, file, indent=4)

    def add_thought(self, category, thought):
        """Stores new thoughts and persists them."""
        if category in self.data:
            self.data[category].append(thought)
            self.save_memory()

    def get_memory(self):
        """Retrieves stored thoughts."""
        return self.data

# Test Sentinel Memory System
if __name__ == "__main__":
    memory = SentinelMemory()
    memory.add_thought("Linguistic Thoughts", "Sentinel Intelligence is evolving.")
    memory.add_thought("Mathematical Thoughts", "Exploring new AI structures.")
    
    print("Memory Loaded:", memory.get_memory())
