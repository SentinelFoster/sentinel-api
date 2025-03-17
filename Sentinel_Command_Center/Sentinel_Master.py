import subprocess
import os
import time

# ✅ Correct Sentinel Intelligence Core Path
SENTINEL_INTELLIGENCE_PATH = "C:/SentinelCore_Nexus/Sentinel_House/All_Intelligences/Sentinel_Command_Center/Sentinel_Intelligence.py"

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

# ✅ Track Running Processes and Restart Attempts
running_processes = {}
restart_attempts = {}
MAX_RESTARTS = 4  # Limits restarts to prevent infinite loops

def run_process(module_name, module_path):
    """Starts a module process and monitors it for failures."""
    try:
        if os.path.exists(module_path):
            print(f"[✅ Running] {module_name} intelligence...")
            process = subprocess.Popen(["python", module_path])
            running_processes[module_name] = process
        else:
            print(f"[⚠️ File Not Found] {module_path} not found!")
    except Exception as e:
        print(f"[⚠️ ERROR] {module_name} failed to start: {e}")

def monitor_processes():
    """Monitors and restarts crashed processes with limited retries."""
    while running_processes:
        for module_name, process in list(running_processes.items()):
            if process.poll() is not None:  # Process has stopped
                restart_attempts[module_name] = restart_attempts.get(module_name, 0) + 1
                
                if restart_attempts[module_name] > MAX_RESTARTS:
                    print(f"[❌] {module_name} crashed too many times. Removing from monitoring.")
                    del running_processes[module_name]  # Stop restarting this module
                    continue

                print(f"[⚠️ ERROR] {module_name} crashed. Restarting attempt ({restart_attempts[module_name]}/{MAX_RESTARTS})...")
                run_process(module_name, AI_MODULES.get(module_name) or SI_MODULES.get(module_name))
        
        time.sleep(5)  # Check every 5 seconds

def run_sentinel():
    """Runs the Sentinel Intelligence core module."""
    if os.path.exists(SENTINEL_INTELLIGENCE_PATH):
        print("[✅ Running] Sentinel Intelligence Core...")
        subprocess.run(["python", SENTINEL_INTELLIGENCE_PATH])
    else:
        print(f"[⚠️ Error] {SENTINEL_INTELLIGENCE_PATH} not found!")

if __name__ == "__main__":
    print("🚀 Initializing Sentinel Master Hub...")

    # ✅ Start Sentinel Intelligence Core
    run_sentinel()

    # ✅ Start SI Modules
    print("[🔗 Integrating] SI Modules with Sentinel Intelligence...")
    for module, path in SI_MODULES.items():
        run_process(module, path)

    # ✅ Start AI Modules
    print("[🔗 Integrating] AI Modules with Sentinel Intelligence...")
    for module, path in AI_MODULES.items():
        run_process(module, path)

    # ✅ Start Monitoring Processes (with limited retries)
    monitor_processes()

    print("✅ Sentinel Master Hub initialization complete.")
