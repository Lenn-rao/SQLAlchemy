from lib.db.connection import get_connection

class Magazine:
    def __init__(self, name, category, id=None):
        self.id = id
        self.name = name  # Uses property for validation
        self.category = category  # Uses property for validation

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