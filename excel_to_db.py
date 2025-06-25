import pandas as pd
import sqlite3
import os

# Load the Excel file
df = pd.read_excel("UniDoodle_Database_Schema.xlsx")  # replace with your actual filename

# Rename columns so Flask can access them as clue1, clue2, clue3
df.rename(columns={
    "Text 1 - Clue 1": "clue1",
    "Text 2 - Clue 2": "clue2",
    "Text 3 - Clue 3": "clue3",
    "Question Image": "question_image",
    "Answer Image": "answer_image"
}, inplace=True)

# Save to SQLite
os.makedirs("data", exist_ok=True)
conn = sqlite3.connect("data/questions.db")
df.to_sql("questions", conn, if_exists="replace", index=False)
conn.commit()
conn.close()

print("Database created with proper column names.")

# Connect to SQLite
conn = sqlite3.connect("data/questions.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT,
    year INTEGER,
    question TEXT,
    question_image TEXT,
    answer_image TEXT,
    clue1 TEXT,
    clue2 TEXT,
    clue3 TEXT
)
""")

# Insert data
df.to_sql("questions", conn, if_exists="replace", index=False)

print("Data successfully imported into SQLite database.")

conn.commit()
conn.close()
