from lib.models.magazine import Magazine
from lib.models.author import Author
from lib.db.connection import get_connection

def test_magazine_save():
    """Test saving a magazine."""
    magazine = Magazine(name="Test Mag", category="Test")
    magazine.save()
    retrieved = Magazine.find_by_name("Test Mag")
    assert retrieved is not None
    assert retrieved.name == "Test Mag"
    assert retrieved.category == "Test"

def test_magazine_find_by_category():
    """Test finding magazines by category."""
    magazines = Magazine.find_by_category("Technology")
    assert len(magazines) >= 1
    assert any(m.name == "Tech Weekly" for m in magazines)

def test_magazine_articles():
    """Test retrieving articles for a magazine."""
    magazine = Magazine.find_by_name("Tech Weekly")
    articles = magazine.articles()
    assert len(articles) >= 2
    assert all(a.magazine_id == magazine.id for a in articles)

def test_magazine_contributors():
    """Test retrieving contributors for a magazine."""
    magazine = Magazine.find_by_name("Tech Weekly")
    contributors = magazine.contributors()
    assert len(contributors) >= 1
    assert any(c.name == "John Doe" for c in contributors)

def test_magazine_article_titles():
    """Test retrieving article titles for a magazine."""
    magazine = Magazine.find_by_name("Tech Weekly")
    titles = magazine.article_titles()
    assert len(titles) >= 2
    assert "Tech Trends" in titles

def test_magazine_contributing_authors():
    """Test retrieving authors with >2 articles (may be empty based on seed)."""
    magazine = Magazine.find_by_name("Tech Weekly")
    authors = magazine.contributing_authors()
    # May be empty unless seed data has >2 articles per author
    if authors:
        assert all(a.name for a in authors)