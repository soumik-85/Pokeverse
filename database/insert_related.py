import sqlite3
from pathlib import Path


# ============================================================
# DATABASE PATH
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "pokeverse.db"


# ============================================================
# RELATED GAMES
# ============================================================

related_games = [
    ('red', 'blue'),
    ('red', 'yellow'),
    ('red', 'firered'),
    ('red', 'leafgreen'),
    ('blue', 'red'),
    ('blue', 'yellow'),
    ('blue', 'firered'),
    ('blue', 'leafgreen'),
    ('yellow', 'red'),
    ('yellow', 'blue'),
    ('yellow', 'firered'),
    ('yellow', 'leafgreen'),
    ('gold', 'silver'),
    ('gold', 'crystal'),
    ('gold', 'heartgold'),
    ('gold', 'soulsilver'),
    ('silver', 'gold'),
    ('silver', 'crystal'),
    ('silver', 'heartgold'),
    ('silver', 'soulsilver'),
    ('crystal', 'gold'),
    ('crystal', 'silver'),
    ('crystal', 'heartgold'),
    ('crystal', 'soulsilver'),
    ('ruby', 'sapphire'),
    ('ruby', 'emerald'),
    ('ruby', 'omegaruby'),
    ('ruby', 'alphasapphire'),
    ('sapphire', 'ruby'),
    ('sapphire', 'emerald'),
    ('sapphire', 'omegaruby'),
    ('sapphire', 'alphasapphire'),
    ('emerald', 'ruby'),
    ('emerald', 'sapphire'),
    ('emerald', 'omegaruby'),
    ('emerald', 'alphasapphire'),
    ('firered', 'leafgreen'),
    ('firered', 'red'),
    ('firered', 'blue'),
    ('firered', 'yellow'),
    ('leafgreen', 'firered'),
    ('leafgreen', 'red'),
    ('leafgreen', 'blue'),
    ('leafgreen', 'yellow'),
    ('diamond', 'pearl'),
    ('diamond', 'platinum'),
    ('diamond', 'brilliantdiamond'),
    ('diamond', 'shiningpearl'),
    ('pearl', 'diamond'),
    ('pearl', 'platinum'),
    ('pearl', 'brilliantdiamond'),
    ('pearl', 'shiningpearl'),
    ('platinum', 'diamond'),
    ('platinum', 'pearl'),
    ('platinum', 'brilliantdiamond'),
    ('platinum', 'shiningpearl'),
    ('heartgold', 'soulsilver'),
    ('heartgold', 'gold'),
    ('heartgold', 'silver'),
    ('heartgold', 'crystal'),
    ('soulsilver', 'heartgold'),
    ('soulsilver', 'gold'),
    ('soulsilver', 'silver'),
    ('soulsilver', 'crystal'),
    ('black', 'white'),
    ('black', 'black2'),
    ('black', 'white2'),
    ('white', 'black'),
    ('white', 'black2'),
    ('white', 'white2'),
    ('black2', 'white2'),
    ('black2', 'black'),
    ('black2', 'white'),
    ('white2', 'black2'),
    ('white2', 'black'),
    ('white2', 'white'),
    ('x', 'y'),
    ('y', 'x'),
    ('omegaruby', 'alphasapphire'),
    ('omegaruby', 'ruby'),
    ('omegaruby', 'sapphire'),
    ('omegaruby', 'emerald'),
    ('alphasapphire', 'omegaruby'),
    ('alphasapphire', 'ruby'),
    ('alphasapphire', 'sapphire'),
    ('alphasapphire', 'emerald'),
    ('sun', 'moon'),
    ('sun', 'ultrasun'),
    ('sun', 'ultramoon'),
    ('moon', 'sun'),
    ('moon', 'ultrasun'),
    ('moon', 'ultramoon'),
    ('ultrasun', 'ultramoon'),
    ('ultrasun', 'sun'),
    ('ultrasun', 'moon'),
    ('ultramoon', 'ultrasun'),
    ('ultramoon', 'sun'),
    ('ultramoon', 'moon'),
    ('letsgo_pikachu', 'letsgo_eevee'),
    ('letsgo_pikachu', 'yellow'),
    ('letsgo_pikachu', 'red'),
    ('letsgo_pikachu', 'blue'),
    ('letsgo_eevee', 'letsgo_pikachu'),
    ('letsgo_eevee', 'yellow'),
    ('letsgo_eevee', 'red'),
    ('letsgo_eevee', 'blue'),
    ('sword', 'shield'),
    ('shield', 'sword'),
    ('brilliantdiamond', 'shiningpearl'),
    ('brilliantdiamond', 'diamond'),
    ('brilliantdiamond', 'pearl'),
    ('brilliantdiamond', 'platinum'),
    ('shiningpearl', 'brilliantdiamond'),
    ('shiningpearl', 'diamond'),
    ('shiningpearl', 'pearl'),
    ('shiningpearl', 'platinum'),
    ('legends_arceus', 'diamond'),
    ('legends_arceus', 'pearl'),
    ('legends_arceus', 'platinum'),
    ('legends_arceus', 'brilliantdiamond'),
    ('legends_arceus', 'shiningpearl'),
    ('scarlet', 'violet'),
    ('violet', 'scarlet'),

]


# ============================================================
# INSERT RELATED GAMES
# ============================================================

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

# Safe to re-run without creating duplicate records.
cursor.execute("DELETE FROM related_games")

cursor.executemany(
    '''
    INSERT INTO related_games (
        game_slug,
        related_slug
    )
    VALUES (?, ?)
    ''',
    related_games
)

connection.commit()
connection.close()


print(
    f"Successfully inserted {len(related_games)} related-game records "
    f"into PokeVerse."
)
print(f"Games covered: {len(set(slug for slug, _ in related_games))}")