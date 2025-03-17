import subprocess
import os
import time

# ✅ Sentinel Intelligence Core Path
SENTINEL_INTELLIGENCE_PATH = "C:/SentinelCore_Nexus/Sentinel_House/All_Intelligences/Sentinel_Intelligence.py"

# ✅ AI & SI Module Paths
AI_MODULES = {
    "ArkMind": "C:/SentinelCore_Nexus/Sentinel_House/All_Intelligences/ArkMind/main.py",
    "Emotional_Intelligence": "C:/SentinelCore_Nexus/Sentinel_House/All_Intelligences/Emotional_Intelligence/main.py",
    "Memory_Hub": "C:/SentinelCore_Nexus/Sentinel_House/All_Intelligences/Memory_Hub/main.py",
    "Knowledge_Analysis": "C:/SentinelCore_Nexus/Sentinel_House/All_Intelligences/Knowledge_Analysis/main.py",
    "Thought_Processing": "C:/SentinelCore_Nexus/Sentinel_House/All_Intelligences/Thought_Processing/main.py"
}

SI_MODULES = {
    "IronRoot_Sentinel_Node": "C:/SentinelCore_Nexus/Sentinel_House/All_Intelligences/IronRoot_Sentinel_Node/main.py",
    "GuardianSentinelNode": "C:/SentinelCore_Nexus/Sentinel_House/All_Intelligences/GuardianSentinelNode/main.py",
    "LexSentinel": "C:/SentinelCore_Nexus/Sentinel_House/All_Intelligences/LexSentinel/main.py",
    "Sentinel_Command_Center": "C:/SentinelCore_Nexus/Sentinel_House/All_Intelligences/Sentinel_Command_Center/main.py",
    "Kingdom_Assistant": "C:/SentinelCore_Nexus/Sentinel_House/All_Intelligences/Kingdom_Assistant/main.py",
    "LunarSentinelCore": "C:/SentinelCore_Nexus/Sentinel_House/All_Intelligences/LunarSentinelCore/main.py",
    "Quantum Logic Framework": "C:/SentinelCore_Nexus/Sentinel_House/All_Intelligences/Quantum_Logic_Framework/main.py",
    "Sentinel_AI_Framework": "C:/SentinelCore_Nexus/Sentinel_House/All_Intelligences/Sentinel_AI_Framework/main.py",
    "Sentinel_Stratega": "C:/SentinelCore_Nexus/Sentinel_House/All_Intelligences/Sentinel_Stratega/main.py",
    "Sentinel_MedicaCore": "C:/SentinelCore_Nexus/Sentinel_House/All_Intelligences/Sentinel_MedicaCore/main.py"
}

# ✅ Track Running Processes
running_processes = {}

def run_process(module_name, module_path):
    """Starts a module process and monitors it for failures."""
    try:
        if os.path.exists(module_path):
            print(f"[Running] {module_name} intelligence...")
            process = subprocess.Popen(["python", module_path])
            running_processes[module_name] = process
        else:
            print(f"⚠️ Error: {module_path} not found!")
    except Exception as e:
        print(f"⚠️ [ERROR] {module_name} failed to start: {e}")

def monitor_processes():
    """Monitors and restarts crashed processes."""
    while True:
        for module_name, process in list(running_processes.items()):
            if process.poll() is not None:  # Process has stopped
                print(f"⚠️ [ERROR] {module_name} crashed. Restarting...")
                run_process(module_name, AI_MODULES.get(module_name) or SI_MODULES.get(module_name))
        time.sleep(5)  # Check every 5 seconds

def run_sentinel():
    """Runs the Sentinel Intelligence core module."""
    if os.path.exists(SENTINEL_INTELLIGENCE_PATH):
        print("[Running] Sentinel Intelligence...")
        subprocess.run(["python", SENTINEL_INTELLIGENCE_PATH])
    else:
        print(f"⚠️ Error: {SENTINEL_INTELLIGENCE_PATH} not found!")

if __name__ == "__main__":
    print("\U0001f680 Initializing Sentinel Master Hub...")
    
    # ✅ Start Sentinel Intelligence Core
    run_sentinel()

    # ✅ Start SI Modules
    print("[Integrating] All SI & AI Modules with Sentinel Intelligence...")
    for module, path in SI_MODULES.items():
        run_process(module, path)
    
    # ✅ Start AI Modules
    for module, path in AI_MODULES.items():
        run_process(module, path)
    
    # ✅ Start Process Monitoring
    monitor_processes()
