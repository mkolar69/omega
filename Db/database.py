# database.py
import sqlite3
import json

def init_db():
    connection = sqlite3.connect("songs.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS songs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            category TEXT NOT NULL,
            lyrics TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()

import json

def save_song_to_db(title, author, category, lyrics):
    song = {"title": title, "author": author, "category": category, "lyrics": lyrics}

    try:
        with open("songs.json", "r") as file:
            songs = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        songs = []

    songs.append(song)

    with open("songs.json", "w") as file:
        json.dump(songs, file)

def load_songs():
    try:
        with open("songs.json", "r") as file:
            songs = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        songs = []

    return songs

if __name__ == "__main__":
    init_db()
