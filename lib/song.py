from config import CONN, CURSOR

import sqlite3

# Create a connection to the database
conn = sqlite3.connect('music.db')
CURSOR = conn.cursor()

class Song:
    def __init__(self, name, album):
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        CURSOR.execute('''CREATE TABLE IF NOT EXISTS songs (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            album TEXT
                        )''')
        conn.commit()

    def save(self):
        CURSOR.execute('INSERT INTO songs (name, album) VALUES (?, ?)', (self.name, self.album))
        conn.commit()

    @classmethod
    def create(cls, name, album):
        song = cls(name, album)
        song.save()
        return song
