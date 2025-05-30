# SQLAlchemy# Code Challenge Project

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