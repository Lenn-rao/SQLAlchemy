from lib.db.connection import get_connection
from lib.models.article import Article
from lib.models.magazine import Magazine

class Author:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Author name must be a non-empty string")
        self._name = value.strip()

    def save(self):
        """Save or update the author in the database."""
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute(
                "INSERT INTO authors (name) VALUES (?)",
                (self.name,)
            )
            self.id = cursor.lastrowid
        else:
            cursor.execute(
                "UPDATE authors SET name = ? WHERE id = ?",
                (self.name, self.id)
            )
        conn.commit()
        conn.close()

    @classmethod
    def find_by_id(cls, id):
        """Find an author by ID."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM authors WHERE id = ?", (id,))
        result = cursor.fetchone()
        conn.close()
        return cls(name=result['name'], id=result['id']) if result else None

    @classmethod
    def find_by_name(cls, name):
        """Find an author by name."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM authors WHERE name = ?", (name,))
        result = cursor.fetchone()
        conn.close()
        return cls(name=result['name'], id=result['id']) if result else None

    def articles(self):
        """Get all articles written by this author."""
        return Article.find_by_author(self.id)

    def magazines(self):
        """Find all magazines this author has contributed to."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT m.* FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        """, (self.id,))
        results = cursor.fetchall()
        conn.close()
        return [Magazine(name=row['name'], category=row['category'], id=row['id']) for row in results]

    def add_article(self, magazine, title):
        """Creates and inserts a new article for this author and magazine."""
        article = Article(title=title, author_id=self.id, magazine_id=magazine.id)
        article.save()
        return article

    def topic_areas(self):
        """Returns unique categories of magazines this author has contributed to."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT m.category FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        """, (self.id,))
        results = cursor.fetchall()
        conn.close()
        return [row['category'] for row in results]