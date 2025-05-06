# ---------------------------------------
# utils.py
# Utility functions for facts, tags, categories, and quotes
# ---------------------------------------

import sqlite3
import random

# ---------------------------------------
# Function: get_fact_by_date(mm_dd, rotate_index=None)
# ---------------------------------------
# Retrieves a fact from the database based on month and day (MM-DD format)
# If no fact found, returns a fallback object
def get_fact_by_date(mm_dd, rotate_index=None):
    conn = sqlite3.connect("facts.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM facts WHERE date = ?", (mm_dd,))
    rows = cur.fetchall()
    conn.close()

    if not rows:
        return {
            "date": mm_dd,
            "title": "No Fact Found",
            "description": "There is no fact available for this day.",
            "category": "N/A",
            "tags": ""
        }

    # Show a specific index if provided (e.g., for rotation)
    if rotate_index is not None:
        return dict(rows[rotate_index % len(rows)])

    # Default to return a random fact if multiple available
    return dict(random.choice(rows))


# ---------------------------------------
# Function: get_tags_from_fact(tags_string)
# ---------------------------------------
# Splits a comma-separated string of tags into a clean list
# Filters out generic/banned words like "The", "Of", etc.
def get_tags_from_fact(tags_string):
    if not tags_string:
        return []
    
    tags = [tag.strip() for tag in tags_string.split(",") if tag.strip()]

    banned_words = {"The", "A", "An", "Of", "On", "In", "At", "And", "For", "To", "From"}
    cleaned_tags = [tag for tag in tags if tag not in banned_words and len(tag) > 2]

    return cleaned_tags


# ---------------------------------------
# Function: get_all_categories_and_tags()
# ---------------------------------------
# Fetches all categories and associated tags from the database
# Returns a dictionary {category: [sorted list of tags]}
def get_all_categories_and_tags():
    conn = sqlite3.connect("facts.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT category, tags FROM facts")
    rows = cur.fetchall()
    conn.close()

    categories = {}

    for row in rows:
        category = row["category"].strip() if row["category"] else "Other"
        tags = [tag.strip() for tag in row["tags"].split(",")] if row["tags"] else []

        if category not in categories:
            categories[category] = set()

        categories[category].update(tags)

    # Convert sets to sorted lists
    for cat in categories:
        categories[cat] = sorted(categories[cat])

    return dict(sorted(categories.items()))


# ---------------------------------------
# Function: get_all_quotes()
# ---------------------------------------
# Retrieves all quotes from the quotes table
# Each quote includes month, quote text, and author
def get_all_quotes():
    conn = sqlite3.connect('facts.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    c.execute('SELECT month, quote, author FROM quotes')
    rows = c.fetchall()

    quotes = []
    for row in rows:
        quotes.append({
            "month": row["month"],
            "quote": row["quote"],
            "author": row["author"]
        })

    conn.close()
    return quotes
