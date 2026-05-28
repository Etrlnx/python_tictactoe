# database.py
import sqlite3

DB_NAME = "scores.db"

def init_db():
    """Creates the high score table if it doesn't already exist."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS high_scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player_name TEXT NOT NULL,
                wins INTEGER DEFAULT 1,
                date_achieved TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()

def add_win(player_name):
    """Increments a user's wins, or creates a new row if they don't exist."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT wins FROM high_scores WHERE player_name = ?", (player_name,))
        row = cursor.fetchone()
        
        if row:
            cursor.execute("UPDATE high_scores SET wins = wins + 1 WHERE player_name = ?", (player_name,))
        else:
            cursor.execute("INSERT INTO high_scores (player_name, wins) VALUES (?, 1)", (player_name,))
        conn.commit()

def get_leaderboard():
    """Retrieves top 5 players sorted by most wins."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT player_name, wins FROM high_scores ORDER BY wins DESC LIMIT 5")
        rows = cursor.fetchall()
        return [{"player_name": row[0], "wins": row[1]} for row in rows]