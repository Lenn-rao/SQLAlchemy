# Code Challenge Project

## Overview
A Python application to manage authors, articles, and magazines using a SQLite database and raw SQL queries within model classes.

## Setup
1. Install Python 3.x and pytest (`pip install pytest`).
2. Run `python scripts/setup_db.py` to create and seed the database.
3. Run `pytest` to verify implementation.
4. Use `python lib/debug.py` for interactive debugging.

## Structure
- `lib/models/`: Model classes (Author, Article, Magazine) with SQL queries.
- `lib/db/`: Database connection, schema, and seed data.
- `tests/`: Unit tests for models.
- `scripts/`: Scripts for setup and queries.

## Requirements
- SQLite for database.
- Raw SQL queries in models.
- Transaction handling and error management.
- Test coverage with pytest.

## Features
- **Author**: Save, find by ID/name, articles, magazines, add article, topic areas.
- **Magazine**: Save, find by ID/name/category, articles, contributors, article titles, contributing authors (>2 articles).
- **Article**: Save, find by ID/title/author/magazine, most prolific author.
- **Complex Queries**: Magazines with multiple authors, article counts, top publisher.
- **Transactions**: Context managers for safe database operations.
- **Indexes**: Added for query performance.

## Testing
- Run `pytest` from the root directory to verify all SQL operations and relationships.
- Debug with `python lib/debug.py` for interactive queries.