import sqlite3

def view_data():
    conn = sqlite3.connect("weather_notifier.db")  # Replace with your database name
    cursor = conn.cursor()
    
    # Fetch all data from the users table
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    
    # Print data in a readable format
    if rows:
        print("ID | Username | Email | Location | Frequency")
        print("-" * 50)
        for row in rows:
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")
    else:
        print("No data found in the database.")
    
    conn.close()

import sqlite3

def delete_rows_by_email(email):
    conn = sqlite3.connect("weather_notifier.db")  # Replace with your database name
    cursor = conn.cursor()
    
    # Delete rows with the specified email
    cursor.execute("DELETE FROM users WHERE email = ?", (email,))
    conn.commit()
    
    # Get the number of deleted rows
    deleted_rows = cursor.rowcount
    if deleted_rows > 0:
        print(f"Deleted {deleted_rows} rows with email: {email}")
    else:
        print(f"No rows found with email: {email}")
    
    conn.close()

# Call the function
# delete_rows_by_email("thanikachalamrmgm@gmail.com")


# # Call the function
# view_data()
