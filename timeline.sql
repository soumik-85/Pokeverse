-- =========================================================
-- PokeVerse - Pokémon Timeline
-- 25 Major Events | 1996 - 2026
-- =========================================================


-- ---------------------------------------------------------
-- 1. Create Timeline Table
-- ---------------------------------------------------------

CREATE TABLE IF NOT EXISTS timeline_events (
    id INTEGER PRIMARY KEY,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    category TEXT NOT NULL,
    image TEXT NOT NULL
);


-- ---------------------------------------------------------
-- 2. Insert Timeline Events
-- ---------------------------------------------------------

INSERT INTO timeline_events
(id, year, month, title, description, category, image)
VALUES

-- 01
(
    1,
    1996,
    2,
    'Pokémon Begins',
    'Pokémon Red and Pokémon Green were released in Japan for the Game Boy on February 27, 1996. These games introduced the world to Pokémon and began a franchise that would grow far beyond video games.',
    'Games',
    '1.jpg'
),

-- 02
(
    2,
    1997,
    4,
    'The Anime Begins',
    'The Pokémon animated series premiered in Japan on April 1, 1997. The first episode introduced Ash Ketchum and Pikachu and began one of the longest-running animated journeys in television history.',
    'Anime',
    '2.png'
),

-- 03
(
    3,
    1998,
    9,
    'Pokémon Goes Global',
    'Pokémon Red and Pokémon Blue launched in North America on September 28, 1998, bringing the main series games to a huge new audience outside Japan.',
    'Global Release',
    '3.jpg'
),

-- 04
(
    4,
    1998,
    7,
    'The First Pokémon Movie',
    'Pokémon: The First Movie — Mewtwo Strikes Back premiered in Japan on July 18, 1998. It became the first theatrical Pokémon movie and established a major new part of the franchise.',
    'Movie',
    '4.jpg'
),

-- 05
(
    5,
    1999,
    11,
    'Generation II Arrives',
    'Pokémon Gold and Pokémon Silver were released in Japan on November 21, 1999. The games introduced the Johto region, 100 new Pokémon, and major new mechanics such as Pokémon breeding and the day-and-night cycle.',
    'Games',
    '5.png'
),

-- 06
(
    6,
    1999,
    1,
    'TCG Goes Worldwide',
    'The Pokémon Trading Card Game expanded internationally with the English Base Set launching in North America in January 1999, helping Pokémon become a major trading-card phenomenon alongside its games and anime.',
    'Trading Card Game',
    '6.jpg'
),

-- 07
(
    7,
    2002,
    11,
    'Hoenn Era Begins',
    'Pokémon Ruby and Pokémon Sapphire launched in Japan on November 21, 2002. The games introduced the Hoenn region, new Pokémon, Double Battles, Abilities, and a new generation of Pokémon adventures.',
    'Games',
    '7.jpg'
),

-- 08
(
    8,
    2004,
    8,
    'TCG World Championships',
    'The first Pokémon Trading Card Game World Championships were held in 2004, establishing a global competitive stage for Pokémon TCG players.',
    'Competitive',
    '8.png'
),

-- 09
(
    9,
    2006,
    9,
    'Generation IV Arrives',
    'Pokémon Diamond and Pokémon Pearl launched in Japan on September 28, 2006. The games introduced the Sinnoh region and brought the series to the Nintendo DS.',
    'Games',
    '9.jpg'
),

-- 10
(
    10,
    2009,
    4,
    'The Pokémon Company International',
    'Pokémon USA and Pokémon UK merged in 2009 to form The Pokémon Company International, strengthening the organization responsible for managing Pokémon outside Asia.',
    'Global Expansion',
    '10.jpg'
),

-- 11
(
    11,
    2010,
    9,
    'Generation V Begins',
    'Pokémon Black and Pokémon White launched in Japan on September 18, 2010. The games introduced the Unova region and a completely new regional Pokédex at the beginning of the adventure.',
    'Games',
    '11.jpg'
),

-- 12
(
    12,
    2013,
    10,
    'Worldwide Releases Begin',
    'Pokémon X and Pokémon Y became the first core Pokémon games to launch simultaneously worldwide on October 12, 2013, marking a major change in how new generations were released.',
    'Global Release',
    '12.jpg'
),

-- 13
(
    13,
    2016,
    7,
    'Pokémon GO Changes Everything',
    'Pokémon GO launched in July 2016 and brought Pokémon into the real world through smartphones, GPS, and augmented reality. Its explosive popularity introduced Pokémon to millions of new players.',
    'Mobile',
    '13.jpg'
),

-- 14
(
    14,
    2018,
    11,
    'Pokémon Comes to Nintendo Switch',
    'Pokémon: Let''s Go, Pikachu! and Pokémon: Let''s Go, Eevee! launched on November 16, 2018. They marked the first mainline-style Pokémon adventures built specifically for Nintendo Switch.',
    'Games',
    '14.jpg'
),

-- 15
(
    15,
    2019,
    5,
    'Detective Pikachu Goes Live-Action',
    'POKÉMON Detective Pikachu premiered on May 10, 2019, becoming the first live-action Pokémon movie and bringing the world of Pokémon to the big screen in a new way.',
    'Live Action',
    '15.jpg'
),

-- 16
(
    16,
    2019,
    11,
    'Generation VIII Begins',
    'Pokémon Sword and Pokémon Shield launched worldwide on November 15, 2019. The games introduced the Galar region and brought the core series to Nintendo Switch.',
    'Games',
    '16.jpg'
),

-- 17
(
    17,
    2020,
    2,
    'Pokémon HOME Launches',
    'Pokémon HOME launched in February 2020 as a cloud-based service designed to help Trainers store, transfer, and manage Pokémon across compatible games and services.',
    'Service',
    '17.jpg'
),

-- 18
(
    18,
    2021,
    2,
    'Pokémon Turns 25',
    'Pokémon celebrated its 25th anniversary in 2021 with special events, music, merchandise, and celebrations across the franchise.',
    'Anniversary',
    '18.jpg'
),

-- 19
(
    19,
    2022,
    1,
    'Pokémon Legends: Arceus',
    'Pokémon Legends: Arceus launched on January 28, 2022. Set in the distant past of the Sinnoh region, the game introduced a new action-focused approach to exploring, catching, and researching Pokémon.',
    'Legends',
    '19.jpg'
),

-- 20
(
    20,
    2022,
    11,
    'Generation IX Begins',
    'Pokémon Scarlet and Pokémon Violet launched on November 18, 2022, introducing the Paldea region and a new open-world approach to the core Pokémon adventure.',
    'Games',
    '20.jpg'
),

-- 21
(
    21,
    2023,
    3,
    'The End of an Era',
    'On March 24, 2023, Ash and Pikachu''s long-running story as the central protagonists of the Pokémon animated series reached its conclusion in Japan after more than 25 years.',
    'Anime',
    '21.jpg'
),

-- 22
(
    22,
    2023,
    4,
    'A New Anime Era',
    'Pokémon Horizons premiered in Japan on April 14, 2023, introducing new protagonists Liko and Roy and beginning a new chapter of the Pokémon animated series.',
    'Anime',
    '22.jpg'
),

-- 23
(
    23,
    2024,
    10,
    'Pokémon TCG Pocket',
    'Pokémon Trading Card Game Pocket launched on October 30, 2024, bringing a digital collecting-focused Pokémon TCG experience to mobile devices.',
    'Mobile TCG',
    '23.jpg'
),

-- 24
(
    24,
    2025,
    10,
    'Pokémon Legends: Z-A',
    'Pokémon Legends: Z-A launched on October 16, 2025. The game takes Trainers to Lumiose City in the Kalos region and brings Mega Evolution back into the spotlight.',
    'Legends',
    '24.jpg'
),

-- 25
(
    25,
    2026,
    2,
    'Pokémon Turns 30',
    'Pokémon celebrated its 30th anniversary on February 27, 2026, marking three decades since Pokémon Red and Pokémon Green first launched in Japan.',
    'Anniversary',
    '25.jpg'
);


-- =========================================================
-- End of PokeVerse Timeline Data
-- =========================================================