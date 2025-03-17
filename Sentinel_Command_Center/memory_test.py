import sqlite3

# Connect to the database
conn = sqlite3.connect("vector_data.db")
cursor = conn.cursor()

# Fetch all stored vectors
cursor.execute("SELECT * FROM vectors")
rows = cursor.fetchall()

# Print stored vectors
print("Stored Memory Vectors:")
for row in rows:
    print(f"ID: {row[0]}, Vector: {row[1]}")

# Insert new memory (Optional)
new_vector = '[0.7, 0.8, 0.9]'
cursor.execute("INSERT INTO vectors (vector_data) VALUES (?)", (new_vector,))
conn.commit()

print("\nNew memory added!")

# Fetch again to verify
cursor.execute("SELECT * FROM vectors")
updated_rows = cursor.fetchall()
print("\nUpdated Memory Vectors:")
for row in updated_rows:
    print(f"ID: {row[0]}, Vector: {row[1]}")

# Close the connection
conn.close()
