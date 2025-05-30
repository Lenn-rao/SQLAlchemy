from lib.models.article import Article
from lib.models.author import Author
from lib.models.magazine import Magazine

def test_article_save():
    """Test saving an article."""
    author = Author(name="Test Author")
    author.save()
    magazine = Magazine(name="Test Mag", category="Test")
    magazine.save()
    article = Article(title="Test Article", author_id=author.id, magazine_id=magazine.id)
    article.save()
    retrieved = Article.find_by_title("Test Article")
    assert retrieved is not None
    assert retrieved.title == "Test Article"

def test_article_find_by_author():
    """Test finding articles by author."""
    articles = Article.find_by_author(1)
    assert len(articles) >= 2
    assert all(a.author_id == 1 for a in articles)

def test_article_find_by_magazine():
    """Test finding articles by magazine."""
    articles = Article.find_by_magazine(1)
    assert len(articles) >= 2
    assert all(a.magazine_id == 1 for a in articles)

def test_most_prolific_author():
    """Test finding the most prolific author."""
    author = Article.most_prolific_author()
    assert author is not None
    assert isinstance(author, Author)