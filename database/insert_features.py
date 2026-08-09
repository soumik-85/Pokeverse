import sqlite3
from pathlib import Path


# ============================================================
# DATABASE PATH
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "pokeverse.db"


# ============================================================
# KEY FEATURES
# ============================================================

features = [
    ('red', '151 Original Pokémon'),
    ('red', 'Pokémon Catching, Training and Battling'),
    ('red', 'Pokémon Trading'),
    ('red', 'Gym Leader Challenge'),
    ('red', 'Pokémon League'),
    ('blue', '151 Original Pokémon'),
    ('blue', 'Pokémon Catching, Training and Battling'),
    ('blue', 'Pokémon Trading'),
    ('blue', 'Gym Leader Challenge'),
    ('blue', 'Pokémon League'),
    ('yellow', 'Pikachu Partner System'),
    ('yellow', 'Anime-Inspired Kanto Journey'),
    ('yellow', 'All Three Original Starters'),
    ('yellow', 'Pokémon Trading'),
    ('yellow', 'Surfing and Fishing'),
    ('gold', '100 New Pokémon'),
    ('gold', 'Day and Night Cycle'),
    ('gold', 'Pokémon Breeding'),
    ('gold', 'Pokémon Eggs'),
    ('gold', 'Kanto Post-Game'),
    ('silver', '100 New Pokémon'),
    ('silver', 'Day and Night Cycle'),
    ('silver', 'Pokémon Breeding'),
    ('silver', 'Pokémon Eggs'),
    ('silver', 'Kanto Post-Game'),
    ('crystal', 'Animated Pokémon Sprites'),
    ('crystal', 'Female Player Character'),
    ('crystal', 'Suicune-Focused Story'),
    ('crystal', 'Battle Tower'),
    ('crystal', 'Kanto Post-Game'),
    ('ruby', '135 New Pokémon'),
    ('ruby', 'Abilities'),
    ('ruby', 'Pokémon Natures'),
    ('ruby', 'Double Battles'),
    ('ruby', 'PokéNav'),
    ('sapphire', '135 New Pokémon'),
    ('sapphire', 'Abilities'),
    ('sapphire', 'Pokémon Natures'),
    ('sapphire', 'Double Battles'),
    ('sapphire', 'PokéNav'),
    ('emerald', 'Battle Frontier'),
    ('emerald', 'Double Battles'),
    ('emerald', 'PokéNav'),
    ('emerald', 'Team Aqua and Team Magma Story'),
    ('emerald', 'Rayquaza-Focused Story'),
    ('firered', 'Kanto Remake'),
    ('firered', 'Updated Third-Generation Mechanics'),
    ('firered', 'Sevii Islands'),
    ('firered', 'Pokémon Trading'),
    ('firered', 'Expanded Post-Game'),
    ('leafgreen', 'Kanto Remake'),
    ('leafgreen', 'Updated Third-Generation Mechanics'),
    ('leafgreen', 'Sevii Islands'),
    ('leafgreen', 'Pokémon Trading'),
    ('leafgreen', 'Expanded Post-Game'),
    ('diamond', 'New Sinnoh Pokémon'),
    ('diamond', 'Physical/Special Split'),
    ('diamond', 'Pokémon Contests'),
    ('diamond', 'Underground'),
    ('diamond', 'Pokémon Super Contests'),
    ('pearl', 'New Sinnoh Pokémon'),
    ('pearl', 'Physical/Special Split'),
    ('pearl', 'Pokémon Contests'),
    ('pearl', 'Underground'),
    ('pearl', 'Pokémon Super Contests'),
    ('platinum', 'Distortion World'),
    ('platinum', 'Expanded Sinnoh Pokédex'),
    ('platinum', 'Battle Frontier'),
    ('platinum', 'Giratina-Focused Story'),
    ('platinum', 'Wi-Fi Plaza'),
    ('heartgold', 'Pokémon Following the Player'),
    ('heartgold', 'Pokéathlon'),
    ('heartgold', 'Touch-Screen Features'),
    ('heartgold', 'Kanto Post-Game'),
    ('heartgold', 'Hoenn and Sinnoh Sound Items'),
    ('soulsilver', 'Pokémon Following the Player'),
    ('soulsilver', 'Pokéathlon'),
    ('soulsilver', 'Touch-Screen Features'),
    ('soulsilver', 'Kanto Post-Game'),
    ('soulsilver', 'Hoenn and Sinnoh Sound Items'),
    ('black', '156 New Pokémon'),
    ('black', 'Triple Battles'),
    ('black', 'Rotation Battles'),
    ('black', 'Seasons'),
    ('black', 'Pokémon Musical'),
    ('white', '156 New Pokémon'),
    ('white', 'Triple Battles'),
    ('white', 'Rotation Battles'),
    ('white', 'Seasons'),
    ('white', 'Pokémon Musical'),
    ('black2', 'New Unova Story'),
    ('black2', 'Expanded Pokédex'),
    ('black2', 'Pokémon World Tournament'),
    ('black2', 'Join Avenue'),
    ('black2', 'Pokéstar Studios'),
    ('white2', 'New Unova Story'),
    ('white2', 'Expanded Pokédex'),
    ('white2', 'Pokémon World Tournament'),
    ('white2', 'Join Avenue'),
    ('white2', 'Pokéstar Studios'),
    ('x', 'Full 3D Pokémon World'),
    ('x', 'Mega Evolution'),
    ('x', 'Fairy Type'),
    ('x', 'Pokémon-Amie'),
    ('x', 'Super Training'),
    ('y', 'Full 3D Pokémon World'),
    ('y', 'Mega Evolution'),
    ('y', 'Fairy Type'),
    ('y', 'Pokémon-Amie'),
    ('y', 'Super Training'),
    ('omegaruby', 'Hoenn 3D Remake'),
    ('omegaruby', 'Mega Evolution'),
    ('omegaruby', 'Primal Reversion'),
    ('omegaruby', 'Delta Episode'),
    ('omegaruby', 'Soaring in the Sky'),
    ('alphasapphire', 'Hoenn 3D Remake'),
    ('alphasapphire', 'Mega Evolution'),
    ('alphasapphire', 'Primal Reversion'),
    ('alphasapphire', 'Delta Episode'),
    ('alphasapphire', 'Soaring in the Sky'),
    ('sun', 'Alola Region'),
    ('sun', 'Regional Pokémon Forms'),
    ('sun', 'Z-Moves'),
    ('sun', 'Island Challenge'),
    ('sun', 'Ultra Beasts'),
    ('moon', 'Alola Region'),
    ('moon', 'Regional Pokémon Forms'),
    ('moon', 'Z-Moves'),
    ('moon', 'Island Challenge'),
    ('moon', 'Ultra Beasts'),
    ('ultrasun', 'Expanded Alola Story'),
    ('ultrasun', 'Ultra Recon Squad'),
    ('ultrasun', 'Ultra Wormholes'),
    ('ultrasun', 'Z-Moves'),
    ('ultrasun', 'Mantine Surf'),
    ('ultramoon', 'Expanded Alola Story'),
    ('ultramoon', 'Ultra Recon Squad'),
    ('ultramoon', 'Ultra Wormholes'),
    ('ultramoon', 'Z-Moves'),
    ('ultramoon', 'Mantine Surf'),
    ('letsgo_pikachu', 'Kanto 3D Reimagining'),
    ('letsgo_pikachu', 'Pikachu Partner System'),
    ('letsgo_pikachu', 'Pokémon GO-Inspired Catching'),
    ('letsgo_pikachu', 'Pokémon Following'),
    ('letsgo_pikachu', 'Cooperative Play'),
    ('letsgo_eevee', 'Kanto 3D Reimagining'),
    ('letsgo_eevee', 'Eevee Partner System'),
    ('letsgo_eevee', 'Pokémon GO-Inspired Catching'),
    ('letsgo_eevee', 'Pokémon Following'),
    ('letsgo_eevee', 'Cooperative Play'),
    ('sword', 'Wild Area'),
    ('sword', 'Dynamax Battles'),
    ('sword', 'Gigantamax Pokémon'),
    ('sword', 'Pokémon Camp'),
    ('sword', 'Max Raid Battles'),
    ('shield', 'Wild Area'),
    ('shield', 'Dynamax Battles'),
    ('shield', 'Gigantamax Pokémon'),
    ('shield', 'Pokémon Camp'),
    ('shield', 'Max Raid Battles'),
    ('brilliantdiamond', 'Faithful Sinnoh Remake'),
    ('brilliantdiamond', 'Grand Underground'),
    ('brilliantdiamond', 'Pokémon Hideaways'),
    ('brilliantdiamond', 'Pokémon Super Contests'),
    ('brilliantdiamond', 'Expanded Underground Features'),
    ('shiningpearl', 'Faithful Sinnoh Remake'),
    ('shiningpearl', 'Grand Underground'),
    ('shiningpearl', 'Pokémon Hideaways'),
    ('shiningpearl', 'Pokémon Super Contests'),
    ('shiningpearl', 'Expanded Underground Features'),
    ('legends_arceus', 'Open-Zone Exploration'),
    ('legends_arceus', 'Real-Time Pokémon Catching'),
    ('legends_arceus', 'Pokémon Research Tasks'),
    ('legends_arceus', 'Crafting'),
    ('legends_arceus', 'Noble Pokémon Battles'),
    ('scarlet', 'Open-World Exploration'),
    ('scarlet', 'Three Story Paths'),
    ('scarlet', 'Terastal Phenomenon'),
    ('scarlet', 'Tera Raid Battles'),
    ('scarlet', 'Cooperative Exploration'),
    ('violet', 'Open-World Exploration'),
    ('violet', 'Three Story Paths'),
    ('violet', 'Terastal Phenomenon'),
    ('violet', 'Tera Raid Battles'),
    ('violet', 'Cooperative Exploration'),
]


# ============================================================
# INSERT FEATURES
# ============================================================

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

# Clear existing feature data so the script can be safely
# re-run without creating duplicates.
cursor.execute("DELETE FROM game_features")

cursor.executemany("""
INSERT INTO game_features (
    game_slug,
    feature
)
VALUES (?, ?)
""", features)

connection.commit()
connection.close()


print(f"Successfully inserted {len(features)} key features into PokeVerse.")
print(f"Games covered: {len(set(slug for slug, _ in features))}")