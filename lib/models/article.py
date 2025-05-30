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
        """Save or update the article in the database."""
        conn = get_connection()
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
        conn.commit()
        conn.close()

    @classmethod
    def find_by_id(cls, id):
        """Find an article by ID."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, author_id, magazine_id FROM articles WHERE id = ?", (id,))
        result = cursor.fetchone()
        conn.close()
        return cls(title=result['title'], author_id=result['author_id'], magazine_id=result['magazine_id'], id=result['id']) if result else None

    @classmethod
    def find_by_title(cls, title):
        """Find an article by title."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, author_id, magazine_id FROM articles WHERE title = ?", (title,))
        result = cursor.fetchone()
        conn.close()
        return cls(title=result['title'], author_id=result['author_id'], magazine_id=result['magazine_id'], id=result['id']) if result else None

    @classmethod
    def find_by_author(cls, author_id):
        """Find articles by author ID."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, author_id, magazine_id FROM articles WHERE author_id = ?", (author_id,))
        results = cursor.fetchall()
        conn.close()
        return [cls(title=row['title'], author_id=row['author_id'], magazine_id=row['magazine_id'], id=row['id']) for row in results]

    @classmethod
    def find_by_magazine(cls, magazine_id):
        """Find articles by magazine ID."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, author_id, magazine_id FROM articles WHERE magazine_id = ?", (magazine_id,))
        results = cursor.fetchall()
        conn.close()
        return [cls(title=row['title'], author_id=row['author_id'], magazine_id=row['magazine_id'], id=row['id']) for row in results]