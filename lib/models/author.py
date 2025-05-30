from lib.db.connection import get_connection

class Author:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name  # Uses property for validation

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