import sqlite3
from pathlib import Path


# ============================================================
# DATABASE PATH
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "pokeverse.db"


# ============================================================
# LEGENDARY POKÉMON
# ============================================================

legendaries = [
    ('red', 'articuno'),
    ('red', 'zapdos'),
    ('red', 'moltres'),
    ('red', 'mewtwo'),
    ('blue', 'articuno'),
    ('blue', 'zapdos'),
    ('blue', 'moltres'),
    ('blue', 'mewtwo'),
    ('yellow', 'articuno'),
    ('yellow', 'zapdos'),
    ('yellow', 'moltres'),
    ('yellow', 'mewtwo'),
    ('gold', 'raikou'),
    ('gold', 'entei'),
    ('gold', 'suicune'),
    ('gold', 'lugia'),
    ('gold', 'ho-oh'),
    ('silver', 'raikou'),
    ('silver', 'entei'),
    ('silver', 'suicune'),
    ('silver', 'lugia'),
    ('silver', 'ho-oh'),
    ('crystal', 'raikou'),
    ('crystal', 'entei'),
    ('crystal', 'suicune'),
    ('crystal', 'lugia'),
    ('crystal', 'ho-oh'),
    ('ruby', 'regirock'),
    ('ruby', 'regice'),
    ('ruby', 'registeel'),
    ('ruby', 'latias'),
    ('ruby', 'rayquaza'),
    ('sapphire', 'regirock'),
    ('sapphire', 'regice'),
    ('sapphire', 'registeel'),
    ('sapphire', 'latios'),
    ('sapphire', 'rayquaza'),
    ('emerald', 'regirock'),
    ('emerald', 'regice'),
    ('emerald', 'registeel'),
    ('emerald', 'latias'),
    ('emerald', 'latios'),
    ('emerald', 'rayquaza'),
    ('firered', 'articuno'),
    ('firered', 'zapdos'),
    ('firered', 'moltres'),
    ('firered', 'mewtwo'),
    ('leafgreen', 'articuno'),
    ('leafgreen', 'zapdos'),
    ('leafgreen', 'moltres'),
    ('leafgreen', 'mewtwo'),
    ('diamond', 'uxie'),
    ('diamond', 'mesprit'),
    ('diamond', 'azelf'),
    ('diamond', 'dialga'),
    ('diamond', 'regigigas'),
    ('diamond', 'heatran'),
    ('pearl', 'uxie'),
    ('pearl', 'mesprit'),
    ('pearl', 'azelf'),
    ('pearl', 'palkia'),
    ('pearl', 'regigigas'),
    ('pearl', 'heatran'),
    ('platinum', 'uxie'),
    ('platinum', 'mesprit'),
    ('platinum', 'azelf'),
    ('platinum', 'dialga'),
    ('platinum', 'palkia'),
    ('platinum', 'giratina'),
    ('platinum', 'regigigas'),
    ('platinum', 'heatran'),
    ('heartgold', 'raikou'),
    ('heartgold', 'entei'),
    ('heartgold', 'suicune'),
    ('heartgold', 'lugia'),
    ('heartgold', 'ho-oh'),
    ('soulsilver', 'raikou'),
    ('soulsilver', 'entei'),
    ('soulsilver', 'suicune'),
    ('soulsilver', 'lugia'),
    ('soulsilver', 'ho-oh'),
    ('black', 'cobalion'),
    ('black', 'terrakion'),
    ('black', 'virizion'),
    ('black', 'tornadus'),
    ('black', 'reshiram'),
    ('black', 'kyurem'),
    ('white', 'cobalion'),
    ('white', 'terrakion'),
    ('white', 'virizion'),
    ('white', 'thundurus'),
    ('white', 'zekrom'),
    ('white', 'kyurem'),
    ('black2', 'cobalion'),
    ('black2', 'terrakion'),
    ('black2', 'virizion'),
    ('black2', 'tornadus'),
    ('black2', 'reshiram'),
    ('black2', 'zekrom'),
    ('black2', 'kyurem'),
    ('white2', 'cobalion'),
    ('white2', 'terrakion'),
    ('white2', 'virizion'),
    ('white2', 'thundurus'),
    ('white2', 'reshiram'),
    ('white2', 'zekrom'),
    ('white2', 'kyurem'),
    ('x', 'xerneas'),
    ('x', 'mewtwo'),
    ('x', 'articuno'),
    ('y', 'yveltal'),
    ('y', 'mewtwo'),
    ('y', 'moltres'),
    ('omegaruby', 'regirock'),
    ('omegaruby', 'regice'),
    ('omegaruby', 'registeel'),
    ('omegaruby', 'latias'),
    ('omegaruby', 'groudon'),
    ('omegaruby', 'rayquaza'),
    ('alphasapphire', 'regirock'),
    ('alphasapphire', 'regice'),
    ('alphasapphire', 'registeel'),
    ('alphasapphire', 'latios'),
    ('alphasapphire', 'kyogre'),
    ('alphasapphire', 'rayquaza'),
    ('sun', 'cosmog'),
    ('sun', 'solgaleo'),
    ('sun', 'lunala'),
    ('sun', 'necrozma'),
    ('moon', 'cosmog'),
    ('moon', 'solgaleo'),
    ('moon', 'lunala'),
    ('moon', 'necrozma'),
    ('ultrasun', 'cosmog'),
    ('ultrasun', 'solgaleo'),
    ('ultrasun', 'lunala'),
    ('ultrasun', 'necrozma'),
    ('ultramoon', 'cosmog'),
    ('ultramoon', 'solgaleo'),
    ('ultramoon', 'lunala'),
    ('ultramoon', 'necrozma'),
    ('letsgo_pikachu', 'articuno'),
    ('letsgo_pikachu', 'zapdos'),
    ('letsgo_pikachu', 'moltres'),
    ('letsgo_pikachu', 'mewtwo'),
    ('letsgo_eevee', 'articuno'),
    ('letsgo_eevee', 'zapdos'),
    ('letsgo_eevee', 'moltres'),
    ('letsgo_eevee', 'mewtwo'),
    ('sword', 'zacian'),
    ('sword', 'eternatus'),
    ('shield', 'zamazenta'),
    ('shield', 'eternatus'),
    ('brilliantdiamond', 'uxie'),
    ('brilliantdiamond', 'mesprit'),
    ('brilliantdiamond', 'azelf'),
    ('brilliantdiamond', 'dialga'),
    ('brilliantdiamond', 'regigigas'),
    ('brilliantdiamond', 'heatran'),
    ('shiningpearl', 'uxie'),
    ('shiningpearl', 'mesprit'),
    ('shiningpearl', 'azelf'),
    ('shiningpearl', 'palkia'),
    ('shiningpearl', 'regigigas'),
    ('shiningpearl', 'heatran'),
    ('legends_arceus', 'uxie'),
    ('legends_arceus', 'mesprit'),
    ('legends_arceus', 'azelf'),
    ('legends_arceus', 'dialga'),
    ('legends_arceus', 'palkia'),
    ('legends_arceus', 'giratina'),
    ('legends_arceus', 'heatran'),
    ('legends_arceus', 'regigigas'),
    ('legends_arceus', 'cresselia'),
    ('legends_arceus', 'tornadus'),
    ('legends_arceus', 'thundurus'),
    ('legends_arceus', 'landorus'),
    ('legends_arceus', 'enamorus'),
    ('legends_arceus', 'shaymin'),
    ('legends_arceus', 'darkrai'),
    ('legends_arceus', 'manaphy'),
    ('legends_arceus', 'phione'),
    ('legends_arceus', 'arceus'),
    ('scarlet', 'wo-chien'),
    ('scarlet', 'chien-pao'),
    ('scarlet', 'ting-lu'),
    ('scarlet', 'chi-yu'),
    ('scarlet', 'koraidon'),
    ('scarlet', 'terapagos'),
    ('violet', 'wo-chien'),
    ('violet', 'chien-pao'),
    ('violet', 'ting-lu'),
    ('violet', 'chi-yu'),
    ('violet', 'miraidon'),
    ('violet', 'terapagos'),

]


# ============================================================
# INSERT LEGENDARIES
# ============================================================

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

# Safe to re-run without creating duplicate records.
cursor.execute("DELETE FROM game_legendaries")

cursor.executemany(
    '''
    INSERT INTO game_legendaries (
        game_slug,
        pokemon_name
    )
    VALUES (?, ?)
    ''',
    legendaries
)

connection.commit()
connection.close()


print(
    f"Successfully inserted {len(legendaries)} legendary Pokémon records "
    f"into PokeVerse."
)
print(f"Games covered: {len(set(slug for slug, _ in legendaries))}")