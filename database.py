import sqlite3

# Initialize the database
def init_db():
    conn = sqlite3.connect("weather_notifier.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            location TEXT NOT NULL,
            frequency TEXT NOT NULL,
            preferred_time TEXT NOT NULL,
            language TEXT DEFAULT 'English'
        )
    """)
    conn.commit()
    conn.close()

# Add user details to the database
def add_user(username, email, location, frequency, preferred_time, language):
    conn = sqlite3.connect("weather_notifier.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO users (username, email, location, frequency, preferred_time, language) 
        VALUES (?, ?, ?, ?, ?, ?)
    """, (username, email, location, frequency, preferred_time, language))
    conn.commit()
    conn.close()

# Check if an email-location pair exists
def check_email_location(email, location):
    conn = sqlite3.connect("weather_notifier.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM users WHERE email = ? AND location = ?
    """, (email, location))
    result = cursor.fetchone()
    conn.close()
    return result

# Fetch all user data
def get_users():
    """
    Fetch all user data from the database.
    Returns:
        List of tuples, where each tuple represents a user:
        (id, username, email, location, frequency, preferred_time, language).
    """
    conn = sqlite3.connect("weather_notifier.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, username, email, location, frequency, preferred_time, language 
        FROM users
    """)
    users = cursor.fetchall()
    conn.close()
    return users

