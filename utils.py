import sqlite3
import random

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

    # Show a specific index if provided
    if rotate_index is not None:
        return dict(rows[rotate_index % len(rows)])

    # Default to first result (or could random.choice)
    return dict(random.choice(rows))

def get_tags_from_fact(tags_string):
    if not tags_string:
        return []
    
    # Split by commas and clean up
    tags = [tag.strip() for tag in tags_string.split(",") if tag.strip()]

    # Remove generic/bad words if they sneak in
    banned_words = {"The", "A", "An", "Of", "On", "In", "At", "And", "For", "To", "From"}
    cleaned_tags = [tag for tag in tags if tag not in banned_words and len(tag) > 2]

    return cleaned_tags

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