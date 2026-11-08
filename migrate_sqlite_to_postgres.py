import os
import sqlite3
import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import execute_batch

# Load configuration
load_dotenv("config.env")

DATABASE_URL = os.getenv("DATABASE_URL")

# Existing SQLite database
SQLITE_DB = os.path.join(
    os.path.dirname(__file__),
    "database",
    "pokeverse.db"
)

# PostgreSQL table definitions
TABLES = {
    "games": """
        CREATE TABLE IF NOT EXISTS games (
            id BIGSERIAL PRIMARY KEY,
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
            difficulty INTEGER NOT NULL CHECK (difficulty >= 0 AND difficulty <= 100),
            accent_color TEXT NOT NULL,
            cover_image TEXT NOT NULL
        )
    """,

    "game_challenges": """
        CREATE TABLE IF NOT EXISTS game_challenges (
            id BIGSERIAL PRIMARY KEY,
            game_slug TEXT NOT NULL REFERENCES games(slug) ON DELETE CASCADE,
            challenge_type TEXT NOT NULL,
            challenge_name TEXT NOT NULL,
            leader_name TEXT NOT NULL,
            challenge_order INTEGER NOT NULL
        )
    """,

    "game_features": """
        CREATE TABLE IF NOT EXISTS game_features (
            id BIGSERIAL PRIMARY KEY,
            game_slug TEXT NOT NULL REFERENCES games(slug) ON DELETE CASCADE,
            feature TEXT NOT NULL
        )
    """,

    "game_legendaries": """
        CREATE TABLE IF NOT EXISTS game_legendaries (
            id BIGSERIAL PRIMARY KEY,
            game_slug TEXT NOT NULL REFERENCES games(slug) ON DELETE CASCADE,
            pokemon_name TEXT NOT NULL
        )
    """,

    "game_starters": """
        CREATE TABLE IF NOT EXISTS game_starters (
            id BIGSERIAL PRIMARY KEY,
            game_slug TEXT NOT NULL REFERENCES games(slug) ON DELETE CASCADE,
            pokemon_name TEXT NOT NULL
        )
    """,

    "related_games": """
        CREATE TABLE IF NOT EXISTS related_games (
            id BIGSERIAL PRIMARY KEY,
            game_slug TEXT NOT NULL REFERENCES games(slug) ON DELETE CASCADE,
            related_slug TEXT NOT NULL REFERENCES games(slug) ON DELETE CASCADE
        )
    """,

    "timeline_events": """
        CREATE TABLE IF NOT EXISTS timeline_events (
            id BIGSERIAL PRIMARY KEY,
            year INTEGER NOT NULL,
            month INTEGER NOT NULL,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            category TEXT NOT NULL,
            image TEXT NOT NULL
        )
    """
}


def migrate():

    if not DATABASE_URL:
        raise ValueError("DATABASE_URL missing in config.env")

    if not os.path.exists(SQLITE_DB):
        raise FileNotFoundError(f"SQLite database not found: {SQLITE_DB}")

    sqlite_conn = sqlite3.connect(SQLITE_DB)
    sqlite_conn.row_factory = sqlite3.Row

    pg_conn = None

    try:
        pg_conn = psycopg2.connect(DATABASE_URL)

        with pg_conn:
            with pg_conn.cursor() as cursor:

                # Create all tables
                for table, schema in TABLES.items():
                    cursor.execute(schema)
                    print(f"Table ready: {table}")

                # Parent table must be migrated first
                migration_order = [
                    "games",
                    "game_challenges",
                    "game_features",
                    "game_legendaries",
                    "game_starters",
                    "related_games",
                    "timeline_events"
                ]

                for table in migration_order:

                    rows = sqlite_conn.execute(
                        f'SELECT * FROM "{table}"'
                    ).fetchall()

                    if not rows:
                        print(f"{table}: No records found")
                        continue

                    columns = rows[0].keys()

                    column_names = ", ".join(
                        f'"{column}"' for column in columns
                    )

                    placeholders = ", ".join(
                        ["%s"] * len(columns)
                    )

                    update_columns = [
                        column for column in columns if column != "id"
                    ]

                    update_clause = ", ".join(
                        f'"{column}" = EXCLUDED."{column}"'
                        for column in update_columns
                    )

                    query = f"""
                        INSERT INTO "{table}" ({column_names})
                        VALUES ({placeholders})
                        ON CONFLICT (id) DO UPDATE SET {update_clause}
                    """

                    values = [
                        tuple(row[column] for column in columns)
                        for row in rows
                    ]

                    execute_batch(cursor, query, values)

                    print(f"{table}: {len(rows)} records migrated")

                # Reset ID sequences
                for table in migration_order:
                    cursor.execute(f"""
                        SELECT setval(
                            pg_get_serial_sequence('{table}', 'id'),
                            COALESCE((SELECT MAX(id) FROM "{table}"), 1),
                            EXISTS (SELECT 1 FROM "{table}")
                        )
                    """)

                # Verify record counts
                print("\n--- Migration Verification ---")

                for table in migration_order:

                    sqlite_count = sqlite_conn.execute(
                        f'SELECT COUNT(*) FROM "{table}"'
                    ).fetchone()[0]

                    cursor.execute(
                        f'SELECT COUNT(*) FROM "{table}"'
                    )

                    pg_count = cursor.fetchone()[0]

                    print(
                        f"{table}: SQLite={sqlite_count}, "
                        f"PostgreSQL={pg_count}"
                    )

                    if sqlite_count != pg_count:
                        raise RuntimeError(
                            f"Count mismatch in table: {table}"
                        )

        print("\nMigration completed successfully!")

    finally:
        sqlite_conn.close()

        if pg_conn:
            pg_conn.close()


if __name__ == "__main__":
    migrate()