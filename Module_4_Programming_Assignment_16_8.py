import csv
import sqlite3

try:
    import sqlalchemy as sa
except ImportError:
    print("Could not load SQLAlchemy.")
    print("Make sure you install SQLAlchemy with `pip install sqlalchemy`")
    sa = None

# Because 16.8 requires some background, we must first create the database.
conn = sqlite3.connect("M4_books.db")

cursor = conn.cursor()

# Clear the table, just in case.
cursor.execute("DROP TABLE IF EXISTS books")

cursor.execute("""
CREATE TABLE books (
    title TEXT,
    author TEXT,
    year INTEGER
)
""")

with open("m4_books.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] == "title":
            continue
        cursor.execute("INSERT INTO books VALUES (?, ?, ?)", row)

cursor.close()
conn.commit()


if sa:
    engine = sa.create_engine("sqlite:///M4_books.db")
    with engine.connect() as conn:
        result = conn.execute(
            sa.text("SELECT title FROM books ORDER BY title")
        )

        for row in result:
            print(row)