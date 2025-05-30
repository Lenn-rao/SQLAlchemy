import sqlite3

def get_connection():
    """Establish and return a database connection."""
    conn = sqlite3.connect('code_challenge.db')
    conn.row_factory = sqlite3.Row  # Access columns by name
    return conn