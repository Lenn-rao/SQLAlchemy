from lib.db.connection import get_connection
from lib.models.article import Article
from lib.models.author import Author

class Magazine:
    def __init__(self, name, category, id=None):
        self.id = id
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Magazine name must be a non-empty string")
        self._name = value.strip()

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Category must be a non-empty string")
        self._category = value.strip()

    def save(self):
        """Save or update the magazine in the database."""
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute(
                "INSERT INTO magazines (name, category) VALUES (?, ?)",
                (self.name, self.category)
            )
            self.id = cursor.lastrowid
        else:
            cursor.execute(
                "UPDATE magazines SET name = ?, category = ? WHERE id = ?",
                (self.name, self.category, self.id)
            )
        conn.commit()
        conn.close()

    @classmethod
    def find_by_id(cls, id):
        """Find a magazine by ID."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category FROM magazines WHERE id = ?", (id,))
        result = cursor.fetchone()
        conn.close()
        return cls(name=result['name'], category=result['category'], id=result['id']) if result else None

    @classmethod
    def find_by_name(cls, name):
        """Find a magazine by name."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category FROM magazines WHERE name = ?", (name,))
        result = cursor.fetchone()
        conn.close()
        return cls(name=result['name'], category=result['category'], id=result['id']) if result else None

    @classmethod
    def find_by_category(cls, category):
        """Find magazines by category."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category FROM magazines WHERE category = ?", (category,))
        results = cursor.fetchall()
        conn.close()
        return [cls(name=row['name'], category=row['category'], id=row['id']) for row in results]

    def articles(self):
        """Returns list of all articles published in this magazine."""
        return Article.find_by_magazine(self.id)

    def contributors(self):
        """Returns unique list of authors who have written for this magazine."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT a.* FROM authors a
            JOIN articles ar ON a.id = ar.author_id
            WHERE ar.magazine_id = ?
        """, (self.id,))
        results = cursor.fetchall()
        conn.close()
        return [Author(name=row['name'], id=row['id']) for row in results]

    def article_titles(self):
        """Returns list of titles of all articles in this magazine."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT title FROM articles WHERE magazine_id = ?", (self.id,))
        results = cursor.fetchall()
        conn.close()
        return [row['title'] for row in results]

    def contributing_authors(self):
        """Returns list of authors with more than 2 articles in this magazine."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT a.* FROM authors a
            JOIN articles ar ON a.id = ar.author_id
            WHERE ar.magazine_id = ?
            GROUP BY a.id, a.name
            HAVING COUNT(*) > 2
        """, (self.id,))
        results = cursor.fetchall()
        conn.close()
        return [Author(name=row['name'], id=row['id']) for row in results]