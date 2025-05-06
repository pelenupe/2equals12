-- Create the main facts table
CREATE TABLE IF NOT EXISTS facts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,        -- Format: MM-DD
    fact TEXT NOT NULL,        -- The main fact text
    category TEXT NOT NULL,    -- E.g., Civil Rights, Arts, Politics
    tags TEXT                  -- Comma-separated tags
);

-- Create the quotes table (for monthly quotes)
CREATE TABLE IF NOT EXISTS quotes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    month TEXT NOT NULL,       -- E.g., January, February, etc.
    quote TEXT NOT NULL,       -- The quote text
    author TEXT NOT NULL       -- Who said the quote
);