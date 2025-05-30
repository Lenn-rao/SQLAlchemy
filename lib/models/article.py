from lib.db.connection import get_connection
from lib.models.author import Author
from lib.models.magazine import Magazine

class Article:
    def __init__(self, title, author_id, magazine_id, id=None):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Article title must be a non-empty string")
        self._title = value.strip()

    def save(self):
        """Save or update the article in the database with transaction."""
        conn = get_connection()
        try:
            with conn:
                cursor = conn.cursor()
                if self.id is None:
                    cursor.execute(
                        "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                        (self.title, self.author_id, self.magazine_id)
                    )
                    self.id = cursor.lastrowid
                else:
                    cursor.execute(
                        "UPDATE articles SET title = ?, author_id = ?, magazine_id = ? WHERE id = ?",
                        (self.title, self.author_id, self.magazine_id, self.id)
                    )
        except Exception as e:
            conn.rollback()
            raise Exception(f"Failed to save article: {e}")
        finally:
            conn.close()

    @classmethod
    def find_by_id(cls, id):
        """Find an article by ID."""
        conn = get_connection()
        try:
            with conn:
                cursor = conn.cursor()
                cursor.execute("SELECT id, title, author_id, magazine_id FROM articles WHERE id = ?", (id,))
                result = cursor.fetchone()
                return cls(title=result['title'], author_id=result['author_id'], magazine_id=result['magazine_id'], id=result['id']) if result else None
        except Exception as e:
            raise Exception(f"Failed to find article: {e}")
        finally:
            conn.close()

    @classmethod
    def find_by_title(cls, title):
        """Find an article by title."""
        conn = get_connection()
        try:
            with conn:
                cursor = conn.cursor()
                cursor.execute("SELECT id, title, author_id, magazine_id FROM articles WHERE title = ?", (title,))
                result = cursor.fetchone()
                return cls(title=result['title'], author_id=result['author_id'], magazine_id=result['magazine_id'], id=result['id']) if result else None
        except Exception as e:
            raise Exception(f"Failed to find article: {e}")
        finally:
            conn.close()

    @classmethod
    def find_by_author(cls, author_id):
        """Find articles by author ID."""
        conn = get_connection()
        try:
            with conn:
                cursor = conn.cursor()
                cursor.execute("SELECT id, title, author_id, magazine_id FROM articles WHERE author_id = ?", (author_id,))
                results = cursor.fetchall()
                return [cls(title=row['title'], author_id=row['author_id'], magazine_id=row['magazine_id'], id=row['id']) for row in results]
        except Exception as e:
            raise Exception(f"Failed to find articles: {e}")
        finally:
            conn.close()

    @classmethod
    def find_by_magazine(cls, magazine_id):
        """Find articles by magazine ID."""
        conn = get_connection()
        try:
            with conn:
                cursor = conn.cursor()
                cursor.execute("SELECT id, title, author_id, magazine_id FROM articles WHERE magazine_id = ?", (magazine_id,))
                results = cursor.fetchall()
                return [cls(title=row['title'], author_id=row['author_id'], magazine_id=row['magazine_id'], id=row['id']) for row in results]
        except Exception as e:
            raise Exception(f"Failed to find articles: {e}")
        finally:
            conn.close()

    @classmethod
    def most_prolific_author(cls):
        """Find the author who has written the most articles."""
        conn = get_connection()
        try:
            with conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT a.* FROM authors a
                    JOIN articles ar ON a.id = ar.author_id
                    GROUP BY a.id, a.name
                    ORDER BY COUNT(*) DESC
                    LIMIT 1
                """)
                result = cursor.fetchone()
                return Author(name=result['name'], id=result['id']) if result else None
        except Exception as e:
            raise Exception(f"Failed to fetch most prolific author: {e}")
        finally:
            conn.close()