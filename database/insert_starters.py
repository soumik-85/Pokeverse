import sqlite3
from pathlib import Path


# ============================================================
# DATABASE PATH
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "pokeverse.db"


# ============================================================
# STARTER POKÉMON
# ============================================================

starters = [
    ('red', 'bulbasaur'),
    ('red', 'charmander'),
    ('red', 'squirtle'),
    ('blue', 'bulbasaur'),
    ('blue', 'charmander'),
    ('blue', 'squirtle'),
    ('yellow', 'pikachu'),
    ('gold', 'chikorita'),
    ('gold', 'cyndaquil'),
    ('gold', 'totodile'),
    ('silver', 'chikorita'),
    ('silver', 'cyndaquil'),
    ('silver', 'totodile'),
    ('crystal', 'chikorita'),
    ('crystal', 'cyndaquil'),
    ('crystal', 'totodile'),
    ('ruby', 'treecko'),
    ('ruby', 'torchic'),
    ('ruby', 'mudkip'),
    ('sapphire', 'treecko'),
    ('sapphire', 'torchic'),
    ('sapphire', 'mudkip'),
    ('emerald', 'treecko'),
    ('emerald', 'torchic'),
    ('emerald', 'mudkip'),
    ('firered', 'bulbasaur'),
    ('firered', 'charmander'),
    ('firered', 'squirtle'),
    ('leafgreen', 'bulbasaur'),
    ('leafgreen', 'charmander'),
    ('leafgreen', 'squirtle'),
    ('diamond', 'turtwig'),
    ('diamond', 'chimchar'),
    ('diamond', 'piplup'),
    ('pearl', 'turtwig'),
    ('pearl', 'chimchar'),
    ('pearl', 'piplup'),
    ('platinum', 'turtwig'),
    ('platinum', 'chimchar'),
    ('platinum', 'piplup'),
    ('heartgold', 'chikorita'),
    ('heartgold', 'cyndaquil'),
    ('heartgold', 'totodile'),
    ('soulsilver', 'chikorita'),
    ('soulsilver', 'cyndaquil'),
    ('soulsilver', 'totodile'),
    ('black', 'snivy'),
    ('black', 'tepig'),
    ('black', 'oshawott'),
    ('white', 'snivy'),
    ('white', 'tepig'),
    ('white', 'oshawott'),
    ('black2', 'snivy'),
    ('black2', 'tepig'),
    ('black2', 'oshawott'),
    ('white2', 'snivy'),
    ('white2', 'tepig'),
    ('white2', 'oshawott'),
    ('x', 'chespin'),
    ('x', 'fennekin'),
    ('x', 'froakie'),
    ('y', 'chespin'),
    ('y', 'fennekin'),
    ('y', 'froakie'),
    ('omegaruby', 'treecko'),
    ('omegaruby', 'torchic'),
    ('omegaruby', 'mudkip'),
    ('alphasapphire', 'treecko'),
    ('alphasapphire', 'torchic'),
    ('alphasapphire', 'mudkip'),
    ('sun', 'rowlet'),
    ('sun', 'litten'),
    ('sun', 'popplio'),
    ('moon', 'rowlet'),
    ('moon', 'litten'),
    ('moon', 'popplio'),
    ('ultrasun', 'rowlet'),
    ('ultrasun', 'litten'),
    ('ultrasun', 'popplio'),
    ('ultramoon', 'rowlet'),
    ('ultramoon', 'litten'),
    ('ultramoon', 'popplio'),
    ('letsgo_pikachu', 'pikachu'),
    ('letsgo_eevee', 'eevee'),
    ('sword', 'grookey'),
    ('sword', 'scorbunny'),
    ('sword', 'sobble'),
    ('shield', 'grookey'),
    ('shield', 'scorbunny'),
    ('shield', 'sobble'),
    ('brilliantdiamond', 'turtwig'),
    ('brilliantdiamond', 'chimchar'),
    ('brilliantdiamond', 'piplup'),
    ('shiningpearl', 'turtwig'),
    ('shiningpearl', 'chimchar'),
    ('shiningpearl', 'piplup'),
    ('legends_arceus', 'rowlet'),
    ('legends_arceus', 'cyndaquil'),
    ('legends_arceus', 'oshawott'),
    ('scarlet', 'sprigatito'),
    ('scarlet', 'fuecoco'),
    ('scarlet', 'quaxly'),
    ('violet', 'sprigatito'),
    ('violet', 'fuecoco'),
    ('violet', 'quaxly'),

]


# ============================================================
# INSERT STARTERS
# ============================================================

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

# Safe to re-run without creating duplicate records.
cursor.execute("DELETE FROM game_starters")

cursor.executemany(
    '''
    INSERT INTO game_starters (
        game_slug,
        pokemon_name
    )
    VALUES (?, ?)
    ''',
    starters
)

connection.commit()
connection.close()


print(f"Successfully inserted {len(starters)} starter Pokémon records into PokeVerse.")
print(f"Games covered: {len(set(slug for slug, _ in starters))}")