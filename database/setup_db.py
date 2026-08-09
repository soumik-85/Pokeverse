import sqlite3
from pathlib import Path


# ============================================================
# DATABASE PATH
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "pokeverse.db"


# ============================================================
# CONNECT
# ============================================================

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

# Enable foreign-key support
cursor.execute("PRAGMA foreign_keys = ON")


# ============================================================
# GAMES
# ============================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS games (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    slug TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,

    generation INTEGER NOT NULL,
    display_order INTEGER NOT NULL,

    region TEXT NOT NULL,

    hero_description TEXT NOT NULL,
    overview TEXT NOT NULL,
    region_description TEXT NOT NULL,

    japan_release TEXT NOT NULL,
    worldwide_release TEXT NOT NULL,

    platform TEXT NOT NULL,
    developer TEXT NOT NULL,
    publisher TEXT NOT NULL,

    average_play_time TEXT NOT NULL,

    difficulty INTEGER NOT NULL
        CHECK (difficulty >= 0 AND difficulty <= 100),

    accent_color TEXT NOT NULL,

    cover_image TEXT NOT NULL

)
""")


# ============================================================
# KEY FEATURES
# ============================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS game_features (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    game_slug TEXT NOT NULL,

    feature TEXT NOT NULL,

    FOREIGN KEY (game_slug)
        REFERENCES games(slug)
        ON DELETE CASCADE

)
""")


# ============================================================
# GAME CHALLENGES
# Gym Leaders / Elite Four / Champion
# ============================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS game_challenges (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    game_slug TEXT NOT NULL,

    challenge_type TEXT NOT NULL,

    challenge_name TEXT NOT NULL,

    leader_name TEXT NOT NULL,

    challenge_order INTEGER NOT NULL,

    FOREIGN KEY (game_slug)
        REFERENCES games(slug)
        ON DELETE CASCADE

)
""")


# ============================================================
# STARTER POKÉMON
# ============================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS game_starters (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    game_slug TEXT NOT NULL,

    pokemon_name TEXT NOT NULL,

    FOREIGN KEY (game_slug)
        REFERENCES games(slug)
        ON DELETE CASCADE

)
""")


# ============================================================
# LEGENDARY POKÉMON
# ============================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS game_legendaries (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    game_slug TEXT NOT NULL,

    pokemon_name TEXT NOT NULL,

    FOREIGN KEY (game_slug)
        REFERENCES games(slug)
        ON DELETE CASCADE

)
""")


# ============================================================
# RELATED GAMES
# ============================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS related_games (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    game_slug TEXT NOT NULL,

    related_slug TEXT NOT NULL,

    FOREIGN KEY (game_slug)
        REFERENCES games(slug)
        ON DELETE CASCADE,

    FOREIGN KEY (related_slug)
        REFERENCES games(slug)
        ON DELETE CASCADE

)
""")

# ============================================================
# TIMELINE EVENTS
# ============================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS timeline_events (

    id INTEGER PRIMARY KEY,

    year INTEGER NOT NULL,

    month INTEGER NOT NULL,

    title TEXT NOT NULL,

    description TEXT NOT NULL,

    category TEXT NOT NULL,

    image TEXT NOT NULL

)
""")

# ============================================================
# SAVE
# ============================================================

connection.commit()
connection.close()


print("PokeVerse Games database created successfully!")
print(f"Database: {DATABASE_PATH}")