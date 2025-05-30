from lib.db.connection import get_connection
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def seed_database():
    """Seed the database with test data using transactions."""
    conn = get_connection()
    try:
        with conn:
            cursor = conn.cursor()
            # Insert authors
            cursor.execute("INSERT OR IGNORE INTO authors (name) VALUES (?)", ("John Doe",))
            cursor.execute("INSERT OR IGNORE INTO authors (name) VALUES (?)", ("Jane Smith",))
            cursor.execute("INSERT OR IGNORE INTO authors (name) VALUES (?)", ("Bob Johnson",))
            
            # Insert magazines
            cursor.execute("INSERT OR IGNORE INTO magazines (name, category) VALUES (?, ?)", 
                          ("Tech Weekly", "Technology"))
            cursor.execute("INSERT OR IGNORE INTO magazines (name, category) VALUES (?, ?)", 
                          ("News Monthly", "News"))
            cursor.execute("INSERT OR IGNORE INTO magazines (name, category) VALUES (?, ?)", 
                          ("Science Today", "Science"))
            
            # Insert articles
            cursor.execute("INSERT OR IGNORE INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                          ("Tech Trends", 1, 1))
            cursor.execute("INSERT OR IGNORE INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                          ("World News", 2, 2))
            cursor.execute("INSERT OR IGNORE INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                          ("AI Advances", 1, 3))
            cursor.execute("INSERT OR IGNORE INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                          ("Tech Future", 1, 1))
            cursor.execute("INSERT OR IGNORE INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                          ("Science Breakthrough", 3, 3))
        print("Database seeded successfully!")
    except Exception as e:
        conn.rollback()
        print(f"Seed failed: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    seed_database()