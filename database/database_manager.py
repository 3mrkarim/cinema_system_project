import sqlite3 



class DatabaseManager:

    def __init__(self, db_path="cinebook.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute("PRAGMA foreign_keys = ON")

        with open("database/schema.sql", "r", encoding="utf-8") as f:
            self.conn.executescript(f.read())

    def add_movie(self, title, genre, duration, description):
        cursor = self.conn.execute(
            "INSERT INTO Movies (title, genre, duration, description) VALUES (?, ?, ?, ?)",
            (title, genre, duration, description),
        )
        self.conn.commit()
        return cursor.lastrowid