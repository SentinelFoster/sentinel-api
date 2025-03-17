import sqlite3

# Define the path to the Sentinel House database
db_path = "../sentinel_house_memory.db"  # Adjust path based on location

try:
    # Connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Execute a test query
    cursor.execute("SELECT * FROM memory;")
    results = cursor.fetchall()

    # Print results
    if results:
        print("Data retrieved successfully from sentinel_house_memory.db:")
        for row in results:
            print(row)
    else:
        print("No data found in sentinel_house_memory.db.")

    # Close connection
    conn.close()

except Exception as e:
    print("Error accessing sentinel_house_memory.db:", e)
