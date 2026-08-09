import sqlite3
from pathlib import Path


# ============================================================
# DATABASE PATH
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "pokeverse.db"


# ============================================================
# TIMELINE DATA
# ============================================================

timeline_events = [

    (
        1,
        1996,
        2,
        "Pokémon Begins",
        "Pokémon Red and Pokémon Green were released in Japan for the Game Boy on February 27, 1996. Players were introduced to the world of Pokémon, where they could explore the Kanto region, catch Pokémon, train their teams, and challenge other Trainers. This marked the beginning of one of the world's biggest entertainment franchises.",
        "Games",
        "1.jpg"
    ),

    (
        2,
        1997,
        4,
        "The Anime Begins",
        "The Pokémon animated series premiered in Japan on April 1, 1997. The story introduced Ash Ketchum and his partner Pikachu as they began their journey toward becoming Pokémon Masters. The anime quickly became one of the most recognizable parts of the Pokémon franchise and helped bring its characters to an even wider audience.",
        "Anime",
        "2.png"
    ),

    (
        3,
        1998,
        9,
        "Pokémon Goes Global",
        "Pokémon Red and Pokémon Blue were released in North America on September 28, 1998, bringing the Pokémon video game experience to a massive international audience. The success of the international releases helped transform Pokémon from a Japanese hit into a global cultural phenomenon.",
        "Global Release",
        "3.jpg"
    ),

    (
        4,
        1998,
        7,
        "The First Pokémon Movie",
        "Pokémon: The First Movie — Mewtwo Strikes Back premiered in Japan on July 18, 1998. The film focused on Mewtwo and explored themes of identity, creation, and the relationship between humans and Pokémon. It established theatrical movies as an important part of the Pokémon franchise.",
        "Movie",
        "4.jpg"
    ),

    (
        5,
        1999,
        11,
        "Generation II Arrives",
        "Pokémon Gold and Pokémon Silver were released in Japan on November 21, 1999, introducing Trainers to the Johto region and 100 new Pokémon. The games expanded the original formula with features such as Pokémon breeding, a day-and-night cycle, held items, and the ability to return to the original Kanto region.",
        "Games",
        "5.png"
    ),

    (
        6,
        1999,
        1,
        "TCG Goes Worldwide",
        "The Pokémon Trading Card Game expanded beyond Japan, with the Pokémon TCG Base Set arriving in North America in January 1999. The cards quickly became a major part of Pokémon culture, giving fans another way to collect Pokémon and compete against one another outside of the video games.",
        "Trading Card Game",
        "6.jpg"
    ),

    (
        7,
        2002,
        11,
        "Hoenn Era Begins",
        "Pokémon Ruby and Pokémon Sapphire launched in Japan on November 21, 2002, introducing the Hoenn region and a new generation of Pokémon. The games added features such as Pokémon Abilities, Double Battles, Contests, and a much larger focus on the relationship between Pokémon and their Trainers.",
        "Games",
        "7.jpg"
    ),

    (
        8,
        2004,
        8,
        "TCG World Championships",
        "The first Pokémon Trading Card Game World Championships were held in 2004, creating an international competitive stage for Pokémon TCG players. This helped establish organized Pokémon competition as a major part of the franchise alongside the video games and anime.",
        "Competitive",
        "8.png"
    ),

    (
        9,
        2006,
        9,
        "Generation IV Arrives",
        "Pokémon Diamond and Pokémon Pearl launched in Japan on September 28, 2006, introducing the Sinnoh region and the fourth generation of Pokémon. The games also brought the main series to the Nintendo DS, taking advantage of the system's dual screens and wireless capabilities.",
        "Games",
        "9.jpg"
    ),

    (
        10,
        2009,
        4,
        "The Pokémon Company International",
        "Pokémon USA and Pokémon UK merged in 2009 to form The Pokémon Company International. The organization became responsible for managing and promoting the Pokémon brand across markets outside Asia, helping create a more unified global presence for the franchise.",
        "Global Expansion",
        "10.jpg"
    ),

    (
        11,
        2010,
        9,
        "Generation V Begins",
        "Pokémon Black and Pokémon White launched in Japan on September 18, 2010, introducing the Unova region and a new generation of Pokémon. The games took a different approach by initially featuring a regional Pokédex made up almost entirely of newly introduced Pokémon.",
        "Games",
        "11.jpg"
    ),

    (
        12,
        2013,
        10,
        "Worldwide Releases Begin",
        "Pokémon X and Pokémon Y launched simultaneously around the world on October 12, 2013. This was a major change for the franchise, as players across different regions could experience a new generation at the same time rather than waiting months for localized releases.",
        "Global Release",
        "12.jpg"
    ),

    (
        13,
        2016,
        7,
        "Pokémon GO Changes Everything",
        "Pokémon GO launched in July 2016 and brought Pokémon into the real world through smartphones, GPS, and augmented reality. Its enormous popularity encouraged millions of people to explore their surroundings while catching Pokémon and introduced the franchise to a huge audience of mobile players.",
        "Mobile",
        "13.jpg"
    ),

    (
        14,
        2018,
        11,
        "Pokémon Comes to Nintendo Switch",
        "Pokémon: Let's Go, Pikachu! and Pokémon: Let's Go, Eevee! launched on November 16, 2018. Inspired by Pokémon Yellow and designed around the Nintendo Switch, the games offered a modern reimagining of the original Kanto adventure while introducing Pokémon GO-inspired catching mechanics.",
        "Games",
        "14.jpg"
    ),

    (
        15,
        2019,
        5,
        "Detective Pikachu Goes Live-Action",
        "POKÉMON Detective Pikachu premiered in May 2019 and became the first live-action Pokémon feature film. The movie brought Pokémon into a realistic modern city filled with humans and Pokémon living together, giving audiences a completely different interpretation of the franchise.",
        "Live Action",
        "15.jpg"
    ),

    (
        16,
        2019,
        11,
        "Generation VIII Begins",
        "Pokémon Sword and Pokémon Shield launched worldwide on November 15, 2019, introducing the Galar region and bringing the core Pokémon adventure to Nintendo Switch. The games introduced the Wild Area, Dynamax and Gigantamax mechanics, and a new approach to exploring the Pokémon world.",
        "Games",
        "16.jpg"
    ),

    (
        17,
        2020,
        2,
        "Pokémon HOME Launches",
        "Pokémon HOME launched in February 2020 as a cloud-based service for storing and transferring Pokémon between compatible games. It provided Trainers with a central place to manage their Pokémon collections across different Pokémon titles and helped connect the franchise's growing ecosystem.",
        "Service",
        "17.jpg"
    ),

    (
        18,
        2021,
        2,
        "Pokémon Turns 25",
        "Pokémon celebrated its 25th anniversary in 2021 with celebrations across games, music, merchandise, and other parts of the franchise. The anniversary highlighted how Pokémon had grown from a pair of Game Boy games into a global phenomenon spanning generations of fans.",
        "Anniversary",
        "18.jpg"
    ),

    (
        19,
        2022,
        1,
        "Pokémon Legends: Arceus",
        "Pokémon Legends: Arceus launched on January 28, 2022, taking players into the distant past of the Sinnoh region, known as Hisui. The game introduced a more action-oriented style of exploration and catching, giving players a new way to experience the Pokémon world.",
        "Legends",
        "19.jpg"
    ),

    (
        20,
        2022,
        11,
        "Generation IX Begins",
        "Pokémon Scarlet and Pokémon Violet launched worldwide on November 18, 2022, introducing the Paldea region. The games expanded the series into a more open-world structure, allowing players to explore the region with greater freedom while following their own adventure.",
        "Games",
        "20.jpg"
    ),

    (
        21,
        2023,
        3,
        "The End of an Era",
        "On March 24, 2023, the final episode of Ash and Pikachu's long-running journey aired in Japan. After more than two decades at the center of the animated series, Ash's story reached its conclusion, marking an emotional turning point for generations of Pokémon fans.",
        "Anime",
        "21.jpg"
    ),

    (
        22,
        2023,
        4,
        "A New Anime Era",
        "Pokémon Horizons premiered in Japan in April 2023, introducing new protagonists Liko and Roy. The series moved the anime into a new chapter with a different central cast, new mysteries, and a broader journey across the Pokémon world.",
        "Anime",
        "22.jpg"
    ),

    (
        23,
        2024,
        10,
        "Pokémon TCG Pocket",
        "Pokémon Trading Card Game Pocket launched on October 30, 2024, bringing the collecting experience of the Pokémon TCG to mobile devices. Players could open digital booster packs, collect cards, and build a digital collection designed around quick and accessible mobile play.",
        "Mobile TCG",
        "23.jpg"
    ),

    (
        24,
        2025,
        10,
        "Pokémon Legends: Z-A",
        "Pokémon Legends: Z-A launched on October 16, 2025, returning players to the Kalos region and focusing on Lumiose City. The game continued the Legends approach to the series while bringing Mega Evolution back into the spotlight.",
        "Legends",
        "24.jpg"
    ),

    (
        25,
        2026,
        2,
        "Pokémon Turns 30",
        "On February 27, 2026, Pokémon celebrated its 30th anniversary, marking three decades since Pokémon Red and Pokémon Green first launched in Japan. The anniversary celebrates a franchise that has expanded across games, animation, trading cards, movies, mobile experiences, and generations of fans.",
        "Anniversary",
        "25.jpg"
    )
]


# ============================================================
# CONNECT TO DATABASE
# ============================================================

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


# ============================================================
# INSERT TIMELINE EVENTS
# ============================================================

cursor.executemany("""
INSERT OR REPLACE INTO timeline_events
(
    id,
    year,
    month,
    title,
    description,
    category,
    image
)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", timeline_events)


# ============================================================
# SAVE
# ============================================================

connection.commit()
connection.close()


print("25 Pokémon timeline events inserted successfully!")
print(f"Database: {DATABASE_PATH}")