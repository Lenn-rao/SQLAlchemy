-- Create Authors table
CREATE TABLE IF NOT EXISTS authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_authors_name ON authors(name);

-- Create Magazines table
CREATE TABLE IF NOT EXISTS magazines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_magazines_name ON magazines(name);
CREATE INDEX IF NOT EXISTS idx_magazines_category ON magazines(category);

-- Create Articles table with relationships
CREATE TABLE IF NOT EXISTS articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(255) NOT NULL,
    author_id INTEGER,
    magazine_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors(id) ON DELETE CASCADE,
    FOREIGN KEY (magazine_id) REFERENCES magazines(id) ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS idx_articles_author_id ON articles(author_id);
CREATE INDEX IF NOT EXISTS idx_articles_magazine_id ON articles(magazine_id);
CREATE INDEX IF NOT EXISTS idx_articles_title ON articles(title);