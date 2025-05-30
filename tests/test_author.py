from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.db.connection import get_connection

def test_author_save():
    """Test saving an author."""
    author = Author(name="Test Author")
    author.save()
    retrieved = Author.find_by_name("Test Author")
    assert retrieved is not None
    assert retrieved.name == "Test Author"

def test_author_find_by_id():
    """Test finding an author by ID."""
    author = Author(name="Find Me")
    author.save()
    retrieved = Author.find_by_id(author.id)
    assert retrieved is not None
    assert retrieved.name == "Find Me"

def test_author_articles():
    """Test retrieving articles by author."""
    author = Author.find_by_name("John Doe")
    articles = author.articles()
    assert len(articles) >= 2
    assert all(a.author_id == author.id for a in articles)

def test_author_magazines():
    """Test retrieving magazines by author."""
    author = Author.find_by_name("John Doe")
    magazines = author.magazines()
    assert len(magazines) >= 2
    assert any(m.name == "Tech Weekly" for m in magazines)

def test_author_add_article():
    """Test adding an article for an author."""
    author = Author(name="New Author")
    author.save()
    magazine = Magazine(name="New Mag", category="Test")
    magazine.save()
    article = author.add_article(magazine, "New Article")
    assert article.title == "New Article"
    assert article.author_id == author.id
    assert article.magazine_id == magazine.id

def test_author_topic_areas():
    """Test retrieving topic areas for an author."""
    author = Author.find_by_name("John Doe")
    topics = author.topic_areas()
    assert len(topics) >= 2
    assert "Technology" in topics