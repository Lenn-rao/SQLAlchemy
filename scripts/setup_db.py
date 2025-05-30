from lib.db.connection import get_connection
from lib.db.seed import seed_database

def setup_database():
    """Set up the test database by creating tables and seeding data."""
    conn = get_connection()
    try:
        with conn:
            cursor = conn.cursor()
            with open('lib/db/schema.sql', 'r') as f:
                schema = f.read()
            cursor.executescript(schema)
        print("Database schema created!")
        seed_database()
    except Exception as e:
        conn.rollback()
        print(f"Setup failed: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    setup_database()