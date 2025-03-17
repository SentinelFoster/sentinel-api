print("[ArkMind] Intelligence module loaded successfully.") 
import os
import logging

# Extract module name dynamically from the folder structure
module_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

# Set up logging for debugging
log_filename = f"{module_name}.log"
logging.basicConfig(filename=log_filename, level=logging.INFO)

try:
    logging.info(f"[{module_name}] Module starting...")

    def run_module():
        print(f"[{module_name}] Intelligence module running.")
        
        # Example: Check if the database exists
        db_path = f"{module_name.lower()}_memory.db"
        if os.path.exists(db_path):
            print(f"Database found: {db_path}")
        else:
            print(f"Warning: {db_path} not found!")

    run_module()

    logging.info(f"[{module_name}] Module executed successfully.")

except Exception as e:
    logging.error(f"An error occurred in {module_name}: {e}")
    print(f"Error in {module_name}: {e}")
