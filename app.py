from flask import Flask, render_template, request, session, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from urllib.parse import urlparse
import os
import requests
import random
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv("config.env")

DATABASE_URL = os.getenv("DATABASE_URL")

all_pokemon_names = []

pokemon_list = requests.get(
    "https://pokeapi.co/api/v2/pokemon?limit=1025"
).json()

for pokemon in pokemon_list["results"]:

    all_pokemon_names.append(
        pokemon["name"].title()
    )

TYPE_MASCOTS = {
    "fire": "charizard",
    "water": "greninja",
    "grass": "venusaur",
    "electric": "pikachu",
    "ice": "lapras",
    "fighting": "lucario",
    "poison": "nidoking",
    "ground": "garchomp",
    "flying": "talonflame",
    "psychic": "mewtwo",
    "bug": "scizor",
    "rock": "tyranitar",
    "ghost": "gengar",
    "dragon": "dragonite",
    "dark": "umbreon",
    "steel": "metagross",
    "fairy": "gardevoir",
    "normal": "snorlax"
}

TYPE_DESCRIPTIONS = {
    "normal": "Normal-type Pokémon are balanced and versatile creatures that rely on adaptability rather than elemental powers. They are often easy to learn and can fit into many different battle strategies.",

    "fire": "Fire-type Pokémon are known for their aggressive battling style and powerful offensive moves. They are associated with heat, passion, volcanoes, and explosive attacks that can overwhelm opponents.",

    "water": "Water-type Pokémon are among the most adaptable Pokémon in the world. They excel in both offense and defense, drawing power from oceans, rivers, lakes, and the endless flow of water.",

    "electric": "Electric-type Pokémon are fast, energetic, and capable of delivering devastating shocks. Their speed and offensive pressure make them some of the most dangerous opponents in battle.",

    "grass": "Grass-type Pokémon are deeply connected to nature, growth, and healing. They often specialize in recovery, status effects, and strategies that slowly wear down their opponents.",

    "ice": "Ice-type Pokémon command freezing temperatures and snowy environments. They are known for powerful attacks that can slow or immobilize enemies with chilling force.",

    "fighting": "Fighting-type Pokémon rely on physical strength, discipline, and martial skill. They are fearless warriors that excel in close combat and direct confrontations.",

    "poison": "Poison-type Pokémon use toxins, venom, and status effects to weaken opponents over time. They often win battles through strategy, patience, and persistent pressure.",

    "ground": "Ground-type Pokémon draw their power from the earth itself. Known for their durability and strength, they can unleash devastating attacks inspired by deserts, mountains, and earthquakes.",

    "flying": "Flying-type Pokémon dominate the skies with incredible speed and freedom of movement. They are agile battlers that often strike quickly before opponents can react.",

    "psychic": "Psychic-type Pokémon possess extraordinary mental abilities and intelligence. Their powers include telekinesis, mind control, and other mysterious psychic phenomena.",

    "bug": "Bug-type Pokémon may appear small, but many evolve into surprisingly powerful battlers. They represent adaptability, rapid growth, and the diversity of the natural world.",

    "rock": "Rock-type Pokémon are sturdy and resilient creatures formed from stone and minerals. Their incredible toughness allows them to endure attacks that would overwhelm others.",

    "ghost": "Ghost-type Pokémon are mysterious beings connected to spirits, shadows, and the supernatural. Their unpredictable powers make them some of the most unique Pokémon in existence.",

    "dragon": "Dragon-type Pokémon are legendary for their immense power and rarity. They combine overwhelming strength with majestic appearances and are often considered elite battlers.",

    "dark": "Dark-type Pokémon fight using cunning tactics, deception, and intimidation. They excel at exploiting weaknesses and disrupting opponents' strategies.",

    "steel": "Steel-type Pokémon possess unmatched durability and defensive strength. Their metallic bodies make them some of the toughest Pokémon to defeat in battle.",

    "fairy": "Fairy-type Pokémon embody magic, charm, and wonder. Despite their cute appearance, they are powerful opponents capable of standing up to even the mightiest dragons."
}

FEATURED_POKEMON = {
    "fire": ["arcanine", "ninetales", "typhlosion", "houndoom", "rapidash"],
    "water": ["blastoise", "gyarados", "lapras", "vaporeon", "swampert"],
    "grass": ["venusaur", "sceptile", "leafeon", "torterra", "roserade"],
    "electric": ["raichu", "jolteon", "luxray", "electivire", "ampharos"],
    "ice": ["lapras", "glaceon", "mamoswine", "weavile", "abomasnow"],
    "ghost": ["gengar", "mimikyu", "banette", "chandelure", "dragapult"],
    "dragon": ["dragonite", "salamence", "garchomp", "hydreigon", "goodra"],
    "dark": ["umbreon", "absol", "zoroark", "tyranitar", "bisharp"],
    "steel": ["metagross", "aggron", "lucario", "scizor", "empoleon"],
    "fairy": ["gardevoir", "togekiss", "sylveon", "clefable", "grimmsnarl"],
    "fighting": ["machamp", "hariyama", "lucario", "conkeldurr", "hawlucha"],
    "psychic": ["alakazam", "espeon", "gardevoir", "metagross", "gallade"],
    "rock": ["tyranitar", "aerodactyl", "rhyperior", "lycanroc", "golem"],
    "ground": ["garchomp", "excadrill", "flygon", "mamoswine", "clodsire"],
    "bug": ["scizor", "heracross", "volcarona", "vikavolt", "genesect"],
    "poison": ["nidoking", "toxicroak", "crobat", "toxapex", "gengar"],
    "flying": ["staraptor", "talonflame", "corviknight", "pidgeot", "noivern"],
    "normal": ["snorlax", "eevee", "porygon-z", "zangoose", "cinccino"]
}

TYPE_MOVES = {
    "fire": ["Flamethrower", "Fire Blast", "Heat Wave", "Flare Blitz"],
    "water": ["Surf", "Hydro Pump", "Scald", "Waterfall"],
    "grass": ["Leaf Blade", "Leaf Storm", "Energy Ball", "Solar Beam"],
    "electric": ["Thunderbolt", "Thunder", "Volt Tackle", "Wild Charge"],
    "ice": ["Ice Beam", "Blizzard", "Freeze-Dry", "Icicle Crash"],
    "fighting": ["Close Combat", "Aura Sphere", "Brick Break", "Mach Punch"],
    "poison": ["Sludge Bomb", "Gunk Shot", "Cross Poison", "Toxic"],
    "ground": ["Earthquake", "Bulldoze", "High Horsepower", "Earth Power"],
    "flying": ["Brave Bird", "Hurricane", "Air Slash", "Fly"],
    "psychic": ["Psychic", "Psyshock", "Future Sight", "Zen Headbutt"],
    "bug": ["X-Scissor", "Bug Buzz", "Megahorn", "Signal Beam"],
    "rock": ["Stone Edge", "Rock Slide", "Rock Tomb", "Power Gem"],
    "ghost": ["Shadow Ball", "Shadow Sneak", "Hex", "Phantom Force"],
    "dragon": ["Dragon Claw", "Outrage", "Draco Meteor", "Dragon Pulse"],
    "dark": ["Crunch", "Dark Pulse", "Knock Off", "Night Slash"],
    "steel": ["Iron Head", "Flash Cannon", "Steel Wing", "Meteor Mash"],
    "fairy": ["Moonblast", "Dazzling Gleam", "Play Rough", "Draining Kiss"],
    "normal": ["Hyper Beam", "Body Slam", "Extreme Speed", "Swift"]
}

TYPE_FACTS = {
    "fire":"Fire types burn with powerful offensive attacks.",
    "water":"Water is the most common Pokémon type.",
    "grass":"Grass types excel at healing and status effects.",
    "electric":"Electric Pokémon are among the fastest attackers.",
    "ice":"Ice has some of the strongest offensive coverage in Pokémon.",
    "fighting":"Fighting excels against Normal, Rock and Dark.",
    "poison":"Poison specializes in wearing opponents down.",
    "ground":"Ground is immune to Electric attacks.",
    "flying":"Flying Pokémon avoid Ground-type attacks.",
    "psychic":"Psychic once dominated competitive Pokémon.",
    "bug":"Bug evolves earlier than most types.",
    "rock":"Rock Pokémon have naturally high Defense.",
    "ghost":"Ghost is immune to Normal and Fighting.",
    "dragon":"Dragon Pokémon are usually rare and powerful.",
    "dark":"Dark counters Psychic strategies.",
    "steel":"Steel has the highest number of resistances.",
    "fairy":"Fairy was introduced in Generation VI.",
    "normal":"Normal Pokémon are the most versatile."
}

TYPES = [
    "Normal",
    "Fire",
    "Water",
    "Electric",
    "Grass",
    "Ice",
    "Fighting",
    "Poison",
    "Ground",
    "Flying",
    "Psychic",
    "Bug",
    "Rock",
    "Ghost",
    "Dragon",
    "Dark",
    "Steel",
    "Fairy"
]

app = Flask(__name__)

app.secret_key = os.environ.get(
    "SECRET_KEY",
    "pokeverse_master_challenge"
)

def get_next_evolution(pokemon):

    species_url = pokemon["species"]["url"]

    species_data = requests.get(species_url).json()

    evolution_chain_url = species_data["evolution_chain"]["url"]

    evolution_data = requests.get(evolution_chain_url).json()

    next_evolution = "No Further Evolution"

    chain = evolution_data["chain"]

    current_name = pokemon["name"]

    while chain:

        if chain["species"]["name"] == current_name:

            if chain["evolves_to"]:

                next_evolution = chain["evolves_to"][0]["species"]["name"].title()

            break

        if chain["evolves_to"]:

            chain = chain["evolves_to"][0]

        else:

            break

    return next_evolution

def generate_who_pokemon_question():

    pokemon_id = random.randint(1, 1025)

    pokemon = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    ).json()

    correct_answer = pokemon["name"].title()

    image = pokemon[
        "sprites"
    ][
        "other"
    ][
        "official-artwork"
    ][
        "front_default"
    ]

    options = [correct_answer]

    while len(options) < 4:

        wrong_name = random.choice(
            all_pokemon_names
        )

        if wrong_name not in options:

            options.append(wrong_name)

    random.shuffle(options)

    return {
        "question": "Who's That Pokémon?",
        "image": image,
        "correct_answer": correct_answer,
        "options": options
    }

def generate_type_question():

    pokemon_id = random.randint(1, 1025)

    pokemon = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    ).json()

    pokemon_name = pokemon["name"].title()

    correct_type = pokemon["types"][0]["type"]["name"].title()

    image = pokemon[
        "sprites"
    ][
        "other"
    ][
        "official-artwork"
    ][
        "front_default"
    ]

    options = [correct_type]

    while len(options) < 4:

        wrong_type = random.choice(TYPES)

        if wrong_type not in options:

            options.append(wrong_type)

    random.shuffle(options)

    return {
        "question": f"What is {pokemon_name}'s primary type?",
        "image": image,
        "correct_answer": correct_type,
        "options": options
    }

def generate_evolution_question():

    while True:

        pokemon_id = random.randint(1, 1025)

        pokemon = requests.get(
            f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
        ).json()

        next_evolution = get_next_evolution(pokemon)

        if next_evolution != "No Further Evolution":
            break

    image = pokemon["sprites"]["other"]["official-artwork"]["front_default"]

    correct_answer = next_evolution

    options = [correct_answer]

    while len(options) < 4:

        wrong_name = random.choice(all_pokemon_names)

        if wrong_name not in options:

            options.append(wrong_name)

    random.shuffle(options)

    return {
        "question": f"Who does {pokemon['name'].title()} evolve into?",
        "image": image,
        "correct_answer": correct_answer,
        "options": options
    }

def generate_quiz_questions():

    questions = []

    # 4 Pokémon Identification
    for _ in range(4):
        questions.append(
            generate_who_pokemon_question()
        )

    # 3 Primary Type
    for _ in range(3):
        questions.append(
            generate_type_question()
        )

    # 3 Evolution
    for _ in range(3):
        questions.append(
            generate_evolution_question()
        )

    random.shuffle(questions)

    return questions

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/pokemon")
def pokemon_hub():
    return render_template("pokemon_hub.html")


@app.route("/pokedex")
def pokedex():

    page = request.args.get("page", 1, type=int)

    # Prevent invalid page numbers
    page = max(1, page)

    limit = 50
    offset = (page - 1) * limit

    url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={offset}"

    response = requests.get(url, timeout=15)
    response.raise_for_status()

    data = response.json()
    pokemon_list = data["results"]

    all_pokemon = requests.get(
        "https://pokeapi.co/api/v2/pokemon?limit=1025",
        timeout=15
    ).json()["results"]

    # Get logged-in user's favourites
    favourite_ids = set()

    if session.get('user_id'):
        connection = get_database_connection()
        cursor = connection.cursor()

        try:
            cursor.execute("""
                SELECT pokemon_id
                FROM user_favourites
                WHERE user_id = %s
            """, (session['user_id'],))

            favourite_ids = {
                row['pokemon_id']
                for row in cursor.fetchall()
            }

        finally:
            cursor.close()
            connection.close()

    return render_template(
        "pokemon.html",
        pokemon_list=pokemon_list,
        page=page,
        start_number=offset,
        all_pokemon=all_pokemon,
        favourite_ids=favourite_ids
    )


@app.route("/random")
def random_page():
    return render_template("random.html")


@app.route("/random/generate")
def generate_random():

    random_id = random.randint(1, 1025)

    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{random_id}"

    pokemon = requests.get(pokemon_url).json()

    next_evolution = get_next_evolution(pokemon)

    return render_template(
        "pokemon_details.html",
        pokemon=pokemon,
        next_evolution=next_evolution,
        random_mode=True
    )

@app.route("/compare")
def compare():

    all_pokemon = requests.get(
        "https://pokeapi.co/api/v2/pokemon?limit=1025"
    ).json()["results"]

    return render_template(
        "compare.html",
        all_pokemon=all_pokemon
    )

@app.route("/compare-result", methods=["POST"])
def compare_result():

    pokemon1_name = request.form["pokemon1"].lower()
    pokemon2_name = request.form["pokemon2"].lower()

    pokemon1 = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{pokemon1_name}"
    ).json()

    pokemon2 = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{pokemon2_name}"
    ).json()

    max_stats = {
        "hp": 255,
        "attack": 190,
        "defense": 250,
        "special-attack": 194,
        "special-defense": 250,
        "speed": 200
    }

    for stat in pokemon1["stats"]:
        stat["width"] = (
            stat["base_stat"] /
            max_stats[stat["stat"]["name"]]
        ) * 100

    for stat in pokemon2["stats"]:
        stat["width"] = (
            stat["base_stat"] /
            max_stats[stat["stat"]["name"]]
        ) * 100

    total1 = sum(
        stat["base_stat"]
        for stat in pokemon1["stats"]
    )

    total2 = sum(
        stat["base_stat"]
        for stat in pokemon2["stats"]
    )

    if total1 > total2:
        winner = pokemon1["name"].title()

    elif total2 > total1:
        winner = pokemon2["name"].title()

    else:
        winner = "Tie"

    return render_template(
        "compare_result.html",
        pokemon1=pokemon1,
        pokemon2=pokemon2,
        winner=winner
    )
    

@app.route("/pokemon/<name>")
def pokemon_details(name):

    from_type = request.args.get("from_type")

    page = request.args.get("page")

    pokemon = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{name}"
    ).json()

    species = requests.get(
        pokemon["species"]["url"]
    ).json()

    evolution_data = requests.get(
        species["evolution_chain"]["url"]
    ).json()

    evolution_chain = get_evolution_chain(
        evolution_data["chain"]
    )

    overview = ""

    for entry in species["flavor_text_entries"]:

        if entry["language"]["name"] == "en":

            overview = (
                entry["flavor_text"]
                .replace("\n", " ")
                .replace("\f", " ")
            )

            break

    category = "Unknown"

    for genus in species["genera"]:

        if genus["language"]["name"] == "en":

            category = genus["genus"]

            break

    habitat = "Unknown"

    if species["habitat"]:

        habitat = species["habitat"]["name"].title()

    generation = species["generation"]["name"] \
        .replace("generation-", "Generation ") \
        .upper()

    top_moves = []

    for move in pokemon["moves"][:6]:

        move_data = requests.get(
            move["move"]["url"]
        ).json()

        move_type = move_data["type"]["name"].title()

        power = move_data["power"]

        if power is None:

            power = "--"

        top_moves.append({

            "name": move["move"]["name"]
                    .replace("-", " ")
                    .title(),

            "type": move_type,

            "power": power

        })

    max_stats = {

        "hp":255,
        "attack":190,
        "defense":250,
        "special-attack":194,
        "special-defense":250,
        "speed":200

    }

    for stat in pokemon["stats"]:

        stat["width"] = (

            stat["base_stat"] /
            max_stats[stat["stat"]["name"]]

        ) * 100

        primary_type = pokemon["types"][0]["type"]["name"]    

    return render_template(

        "pokemon_details.html",

        pokemon=pokemon,

        page=page,

        from_type=from_type,

        random_mode=False,

        overview=overview,

        category=category,

        habitat=habitat,

        generation=generation,

        evolution_chain=evolution_chain,

        top_moves=top_moves,

        primary_type=primary_type

    )

def get_evolution_chain(chain):

    evolution = []

    while chain:

        pokemon_name = chain["species"]["name"]

        pokemon_data = requests.get(
            f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
        ).json()

        artwork = pokemon_data["sprites"]["other"]["official-artwork"]["front_default"]

        evolution.append({
            "name": pokemon_name.title(),
            "image": artwork
        })

        if chain["evolves_to"]:

            chain = chain["evolves_to"][0]

        else:

            break

    return evolution

@app.route("/evolution")
def evolution():

    all_pokemon = requests.get(
        "https://pokeapi.co/api/v2/pokemon?limit=1025"
    ).json()["results"]

    return render_template(
        "evolution.html",
        all_pokemon=all_pokemon
    )

@app.route("/types")
def types():

    return render_template(
        "types.html"
    )

@app.route("/types/<type_name>")
def type_details(type_name):

    url = f"https://pokeapi.co/api/v2/type/{type_name}"

    response = requests.get(url)

    type_data = response.json()

    mascot_name = TYPE_MASCOTS.get(type_name)

    type_description = TYPE_DESCRIPTIONS.get(
    type_name,
    "No description available."
     )
    
    featured_names = FEATURED_POKEMON.get(type_name, [])

    if mascot_name in featured_names:
       featured_names.remove(mascot_name)

    featured_pokemon = []

    for pokemon_name in featured_names:

        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"

        print("Loading:", pokemon_name)
        print("URL:", url)

        response = requests.get(url)

        print("Status:", response.status_code)

        if response.status_code != 200:
         print("FAILED POKEMON:", pokemon_name)
         continue

        pokemon_data = response.json()

        featured_pokemon.append({
           "name": pokemon_name.title(),
           "image": pokemon_data["sprites"]["other"]["official-artwork"]["front_default"]
   })

    mascot = requests.get(
          f"https://pokeapi.co/api/v2/pokemon/{mascot_name}"
).json()

    pokemon_list = type_data["pokemon"][:20]

    type_colors = {
    "fire": "#EE8130",
    "water": "#6390F0",
    "grass": "#7AC74C",
    "electric": "#F7D02C",
    "ice": "#96D9D6",
    "fighting": "#C22E28",
    "poison": "#A33EA1",
    "ground": "#E2BF65",
    "flying": "#A98FF3",
    "psychic": "#F95587",
    "bug": "#A6B91A",
    "rock": "#B6A136",
    "ghost": "#B784F7",
    "dragon": "#6F35FC",
    "dark": "#705746",
    "steel": "#B7B7CE",
    "fairy": "#D685AD",
    "normal": "#A8A77A"
}
    type_color = type_colors.get(type_name, "#ffcb05")



    return render_template(
    "type_details.html",
    type_data=type_data,
    pokemon_list=pokemon_list,
    type_color=type_colors.get(type_name, "#ffcb05"),
    mascot=mascot,
    type_description=type_description,
    featured_pokemon=featured_pokemon,
    notable_moves=TYPE_MOVES[type_name],
    did_you_know=TYPE_FACTS[type_name],
    
)

@app.route("/type-chart")
def type_chart():

    types = [
        "normal", "fire", "water", "electric",
        "grass", "ice", "fighting", "poison",
        "ground", "flying", "psychic", "bug",
        "rock", "ghost", "dragon", "dark",
        "steel", "fairy"
    ]

    type_data = {}

    for type_name in types:

     response = requests.get(
        f"https://pokeapi.co/api/v2/type/{type_name}"
    )

     type_data[type_name] = response.json()
    
    print(type_data.keys())

    return render_template(
    "type_chart.html",
    types=types,
    type_data=type_data
)

@app.route("/quiz")
def quiz():
    return render_template("quiz.html")


@app.route("/quiz/master")
def quiz_master():
    return render_template("quiz_master.html")

@app.route("/quiz/play")
def quiz_play():

    questions = generate_quiz_questions()

    print("Questions Generated:",
          len(questions))

    question = questions[0]

    return render_template(
        "quiz_play.html",
        question=question,
        questions=questions
    )

@app.route("/quiz/results")
def quiz_results():

    score = session.get("score", 0)

    if score <= 3:

        rank = "Rookie Trainer"
        badge = "rookie_badge.png"
        message = "Every Pokémon Master starts somewhere!"
        background = "rookie_bg.png"

    elif score <= 6:

        rank = "Trainer"
        badge = "trainer_badge.png"
        message = "You're learning the world of Pokémon!"
        background = "trainer_bg.png"

    elif score <= 8:

        rank = "Ace Trainer"
        badge = "ace_badge.png"
        message = "Strong knowledge and great potential!"
        background = "ace_bg.png"

    elif score <= 9:

        rank = "Gym Leader"
        badge = "gym_leader_badge.png"
        message = "Impressive Pokémon expertise!"
        background = "gym_leader_bg.png"

    else:

        rank = "Pokémon Master"
        badge = "pokemon_master_badge.png"
        message = "Perfect Score! Incredible!"
        background = "pokemon_master_bg.png"

    return render_template(
        "quiz_results.html",
        score=score,
        rank=rank,
        badge=badge,
        message=message,
        background=background
    )

@app.route("/quiz/save-score/<int:score>")
def save_score(score):

    session["score"] = score
    return "", 204

@app.route("/quiz/quiz_who_pokemon")
def who_pokemon():

    question = generate_who_pokemon_question()

    return render_template(
        "quiz_who_pokemon.html",
        question=question
    )

@app.route("/quiz/type")
def type_quiz():

    question = generate_type_question()

    return render_template(
        "type_quiz.html",
        question=question
    )

@app.route("/quiz/evolution")
def evolution_quiz():

    question = generate_evolution_question()

    return render_template(
        "evolution_quiz.html",
        question=question
    )

# ============================================================
# GAMES
# ============================================================


def get_database_connection():
    connection = psycopg2.connect(
        DATABASE_URL,
        cursor_factory=RealDictCursor
    )
    return connection

    
# ============================================================
# QUIZ LEADERBOARD - SAVE RECORDS
# ============================================================

@app.route("/quiz/leaderboard/save-streak", methods=["POST"])
def save_streak_record():

    if "user_id" not in session:
        return {"error": "Login required"}, 401

    data = request.get_json(silent=True) or {}

    mode = data.get("mode")
    streak = data.get("streak")

    valid_modes = ["pokemon", "type", "evolution"]

    if mode not in valid_modes:
        return {"error": "Invalid quiz mode"}, 400

    try:
        streak = int(streak)
    except (TypeError, ValueError):
        return {"error": "Invalid streak"}, 400

    if streak < 0:
        return {"error": "Invalid streak"}, 400

    connection = get_database_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO quiz_streak_leaderboard
                (user_id, mode, best_streak)
            VALUES (%s, %s, %s)

            ON CONFLICT (user_id, mode)
            DO UPDATE SET
                best_streak = EXCLUDED.best_streak,
                achieved_at = CURRENT_TIMESTAMP

            WHERE EXCLUDED.best_streak >
                  quiz_streak_leaderboard.best_streak
            """,
            (session["user_id"], mode, streak)
        )

        connection.commit()

        return {"success": True}, 200

    except Exception:
        connection.rollback()
        return {"error": "Could not save streak"}, 500

    finally:
        cursor.close()
        connection.close()


# ============================================================
# QUIZ LEADERBOARD - FETCH RANKINGS
# ============================================================

@app.route("/quiz/leaderboard/<leaderboard_type>")
def get_leaderboard(leaderboard_type):

    if leaderboard_type not in ["challenge", "pokemon", "type", "evolution"]:
        return {"error": "Invalid leaderboard type"}, 400

    connection = get_database_connection()
    cursor = connection.cursor()

    try:
        if leaderboard_type == "challenge":
            cursor.execute(
                """
                SELECT
                    u.id AS user_id,
                    u.username,
                    u.avatar,
                    l.best_score,
                    l.completion_time,
                    l.achieved_at
                FROM quiz_challenge_leaderboard l
                JOIN users u ON u.id = l.user_id
                ORDER BY
                    l.best_score DESC,
                    l.completion_time ASC,
                    l.achieved_at ASC,
                    l.user_id ASC
                """
            )

        else:
            cursor.execute(
                """
                SELECT
                    u.id AS user_id,
                    u.username,
                    u.avatar,
                    l.best_streak,
                    l.achieved_at
                FROM quiz_streak_leaderboard l
                JOIN users u ON u.id = l.user_id
                WHERE l.mode = %s
                ORDER BY
                    l.best_streak DESC,
                    l.achieved_at ASC,
                    l.user_id ASC
                """,
                (leaderboard_type,)
            )

        all_players = cursor.fetchall()

        current_user_id = session.get("user_id")

        ranked_players = []
        current_user = None

        for rank, player in enumerate(all_players, start=1):
            player_data = dict(player)
            player_data["rank"] = rank

            if current_user_id and player_data["user_id"] == current_user_id:
                current_user = player_data

            if rank <= 10:
                ranked_players.append(player_data)

        return {
            "top_10": ranked_players,
            "current_user": current_user
        }

    except Exception:
        return {"error": "Could not fetch leaderboard"}, 500

    finally:
        cursor.close()
        connection.close()




@app.route("/quiz/leaderboard/save-challenge", methods=["POST"])
def save_challenge_record():

    data = request.get_json(silent=True) or {}

    try:
        score = int(data.get("score"))
        completion_time = int(data.get("completion_time"))
    except (TypeError, ValueError):
        return {"error": "Invalid score or time"}, 400

    if not 0 <= score <= 10 or completion_time <= 0:
        return {"error": "Invalid challenge result"}, 400

    # Save score for the results page, even if user is logged out
    session["score"] = score

    # Login is required only for leaderboard submission
    if "user_id" not in session:
        return {"error": "Login required"}, 401

    connection = get_database_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO quiz_challenge_leaderboard
                (user_id, best_score, completion_time)
            VALUES (%s, %s, %s)

            ON CONFLICT (user_id)
            DO UPDATE SET
                best_score = EXCLUDED.best_score,
                completion_time = EXCLUDED.completion_time,
                achieved_at = CURRENT_TIMESTAMP

            WHERE
                EXCLUDED.best_score >
                    quiz_challenge_leaderboard.best_score

                OR (
                    EXCLUDED.best_score =
                        quiz_challenge_leaderboard.best_score

                    AND EXCLUDED.completion_time <
                        quiz_challenge_leaderboard.completion_time
                )
            """,
            (session["user_id"], score, completion_time)
        )

        connection.commit()

        return {"success": True}, 200

    except Exception:
        connection.rollback()
        return {"error": "Could not save challenge result"}, 500

    finally:
        cursor.close()
        connection.close()





@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')

        # Get selected avatar
        avatar = request.form.get('avatar', '')

        # Allowed avatars
        allowed_avatars = {
            'ash.png',
            'serena.png',
            'pikachu.png'
        }

        if not username or not email or not password:
            flash('Please fill in all fields.', 'error')
            return redirect(url_for('register'))

        if len(username) < 3 or len(username) > 30:
            flash('Username must be between 3 and 30 characters.', 'error')
            return redirect(url_for('register'))

        if len(password) < 8:
            flash('Password must contain at least 8 characters.', 'error')
            return redirect(url_for('register'))

        if password != confirm_password:
            flash('Passwords do not match.', 'error')
            return redirect(url_for('register'))

        # Validate avatar
        if avatar not in allowed_avatars:
            flash('Please select an avatar.', 'error')
            return redirect(url_for('register'))

        password_hash = generate_password_hash(password)

        connection = get_database_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                INSERT INTO users
                (username, email, password_hash, avatar)
                VALUES (%s, %s, %s, %s)
                """,
                (username, email, password_hash, avatar)
            )

            connection.commit()

            flash(
                'Account created successfully! Please log in.',
                'success'
            )
            return redirect(url_for('login'))

        except psycopg2.errors.UniqueViolation:
            connection.rollback()
            flash('Username or email already exists.', 'error')
            return redirect(url_for('register'))

        finally:
            cursor.close()
            connection.close()

    return render_template('register.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        identifier = request.form.get('identifier', '').strip()
        password = request.form.get('password', '')

        connection = get_database_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                SELECT id, username, email, password_hash, avatar
                FROM users
                WHERE LOWER(username) = LOWER(%s)
                   OR email = LOWER(%s)
                """,
                (identifier, identifier)
            )

            user = cursor.fetchone()

        finally:
            cursor.close()
            connection.close()

        if user and check_password_hash(user['password_hash'], password):
            session.clear()
            session['user_id'] = user['id']
            session['username'] = user['username']
            session['email'] = user['email']
            session['avatar'] = user['avatar'] or 'pikachu.png'

            return redirect(url_for('home'))

        flash('Invalid username/email or password.', 'error')
        return redirect(url_for('login'))

    return render_template('login.html')



@app.route('/logout', methods=['GET', 'POST'])
def logout():
    # Clear the user's login session
    session.clear()

    flash('You have been logged out successfully.', 'success')

    # Get the page the user was visiting
    previous_page = request.referrer

    # Redirect only to a page on our own website
    if previous_page:
        parsed_url = urlparse(previous_page)

        if parsed_url.netloc == request.host:
            return redirect(previous_page)

    # Fallback if there is no valid previous page
    return redirect(url_for('home'))


# ============================================================
# FAVOURITES
# ============================================================


@app.route('/favourites/toggle/<int:pokemon_id>', methods=['POST'])
def toggle_favourite(pokemon_id):

    if not session.get('user_id'):
        return {
            "success": False,
            "message": "Please log in first.",
            "login_required": True
        }, 401

    if pokemon_id < 1 or pokemon_id > 1025:
        return {"success": False, "message": "Invalid Pokémon ID."}, 400

    connection = get_database_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            DELETE FROM user_favourites
            WHERE user_id = %s AND pokemon_id = %s
            RETURNING id
        """, (session['user_id'], pokemon_id))

        removed = cursor.fetchone()

        if removed:
            action = "removed"
        else:
            cursor.execute("""
                INSERT INTO user_favourites (user_id, pokemon_id)
                VALUES (%s, %s)
                ON CONFLICT (user_id, pokemon_id) DO NOTHING
            """, (session['user_id'], pokemon_id))

            action = "added"

        connection.commit()

        return {
            "success": True,
            "action": action,
            "pokemon_id": pokemon_id
        }

    except Exception:
        connection.rollback()
        return {"success": False, "message": "Could not update favourites."}, 500

    finally:
        cursor.close()
        connection.close()



@app.route('/favourites')
def favourites():

    # Login required
    if not session.get('user_id'):
        flash('Please log in to view your favourites.', 'error')
        return redirect(url_for('login'))

    connection = get_database_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT pokemon_id
            FROM user_favourites
            WHERE user_id = %s
            ORDER BY created_at DESC
        """, (session['user_id'],))

        saved_pokemon = cursor.fetchall()

    finally:
        cursor.close()
        connection.close()

    favourite_pokemon = []

    for item in saved_pokemon:

        pokemon_id = item['pokemon_id']

        try:
            response = requests.get(
                f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}",
                timeout=10
            )
            response.raise_for_status()

            pokemon_data = response.json()
            favourite_pokemon.append(pokemon_data)

        except requests.RequestException:
            continue

    return render_template(
        'favourites.html',
        favourite_pokemon=favourite_pokemon
    )



@app.route('/update-profile', methods=['POST'])
def update_profile():

    if not session.get('user_id'):
        return redirect(url_for('login'))

    username = request.form.get('username', '').strip()
    email = request.form.get('email', '').strip().lower()
    avatar = request.form.get('avatar', '')

    allowed_avatars = {
        'ash.png',
        'serena.png',
        'pikachu.png'
    }

    if not username or not email:
        flash('Username and email are required.', 'error')
        return redirect(url_for('home'))

    if len(username) < 3 or len(username) > 30:
        flash('Username must be between 3 and 30 characters.', 'error')
        return redirect(url_for('home'))

    if avatar not in allowed_avatars:
        flash('Invalid avatar selection.', 'error')
        return redirect(url_for('home'))

    connection = get_database_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            UPDATE users
            SET username = %s, email = %s, avatar = %s
            WHERE id = %s
            """,
            (username, email, avatar, session['user_id'])
        )

        connection.commit()

        session['username'] = username
        session['email'] = email
        session['avatar'] = avatar

        flash('Profile updated successfully!', 'success')

    except psycopg2.errors.UniqueViolation:
        connection.rollback()
        flash('That username or email is already in use.', 'error')

    except Exception:
        connection.rollback()
        flash('Could not update your profile. Please try again.', 'error')

    finally:
        cursor.close()
        connection.close()

    return redirect(url_for('home'))


@app.route('/change-password', methods=['POST'])
def change_password():

    if not session.get('user_id'):
        return redirect(url_for('login'))

    current_password = request.form.get('current_password', '')
    new_password = request.form.get('new_password', '')
    confirm_password = request.form.get('confirm_password', '')

    if len(new_password) < 8:
        flash('New password must contain at least 8 characters.', 'error')
        return redirect(url_for('home'))

    if new_password != confirm_password:
        flash('New passwords do not match.', 'error')
        return redirect(url_for('home'))

    connection = get_database_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            "SELECT password_hash FROM users WHERE id = %s",
            (session['user_id'],)
        )

        user = cursor.fetchone()

        if not user or not check_password_hash(
            user['password_hash'], current_password
        ):
            flash('Your current password is incorrect.', 'error')
            return redirect(url_for('home'))

        if check_password_hash(user['password_hash'], new_password):
            flash('Choose a password different from your current one.', 'error')
            return redirect(url_for('home'))

        new_password_hash = generate_password_hash(new_password)

        cursor.execute(
            """
            UPDATE users
            SET password_hash = %s
            WHERE id = %s
            """,
            (new_password_hash, session['user_id'])
        )

        connection.commit()

        flash('Password changed successfully!', 'success')

    except Exception:
        connection.rollback()
        flash('Could not change your password. Please try again.', 'error')

    finally:
        cursor.close()
        connection.close()

    return redirect(url_for('home'))


@app.route("/games")
def games_home():

    connection = get_database_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM games
        ORDER BY generation, display_order
    """)

    games = cursor.fetchall()

    connection.close()

    return render_template(
        "games/games_home.html",
        games=games
    )


@app.route("/games/generation/<int:generation>")
def generation_page(generation):

    connection = get_database_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM games
        WHERE generation = %s
        ORDER BY display_order
    """, (generation,))

    games = cursor.fetchall()

    connection.close()

    if not games:
        return "Generation not found", 404

    return render_template(
        "games/generation.html",
        generation=generation,
        games=games
    )


@app.route("/games/<slug>")
def game_details(slug):

    connection = get_database_connection()
    cursor = connection.cursor()

    # --------------------------------------------------------
    # Main game
    # --------------------------------------------------------

    cursor.execute("""
        SELECT *
        FROM games
        WHERE slug = %s
    """, (slug,))

    game = cursor.fetchone()

    if game is None:
        connection.close()
        return "Game not found", 404

    # --------------------------------------------------------
    # Key features
    # --------------------------------------------------------

    cursor.execute("""
        SELECT feature
        FROM game_features
        WHERE game_slug = %s
        ORDER BY id
    """, (slug,))

    features = cursor.fetchall()

    # --------------------------------------------------------
    # Challenges
    # --------------------------------------------------------

    cursor.execute("""
        SELECT
            challenge_type,
            challenge_name,
            leader_name,
            challenge_order
        FROM game_challenges
        WHERE game_slug = %s
        ORDER BY challenge_order
    """, (slug,))

    challenges = cursor.fetchall()

    # --------------------------------------------------------
    # Starter Pokémon
    # --------------------------------------------------------

    cursor.execute("""
        SELECT pokemon_name
        FROM game_starters
        WHERE game_slug = %s
        ORDER BY id
    """, (slug,))

    starters = cursor.fetchall()

    # --------------------------------------------------------
    # Legendary Pokémon
    # --------------------------------------------------------

    cursor.execute("""
        SELECT pokemon_name
        FROM game_legendaries
        WHERE game_slug = %s
        ORDER BY id
    """, (slug,))

    legendaries = cursor.fetchall()

    # --------------------------------------------------------
    # Related games
    #
    # Join back to games so the template receives the complete
    # game records instead of only the related slugs.
    # --------------------------------------------------------

    cursor.execute("""
        SELECT g.*
        FROM related_games r
        JOIN games g
            ON g.slug = r.related_slug
        WHERE r.game_slug = %s
        ORDER BY g.generation, g.display_order
    """, (slug,))

    related_games = cursor.fetchall()

    connection.close()

    return render_template(
        "games/game_details.html",
        game=game,
        features=features,
        challenges=challenges,
        starters=starters,
        legendaries=legendaries,
        related_games=related_games
    )

# ============================================================
# TIMELINE
# ============================================================

@app.route("/timeline")
def timeline():

    connection = get_database_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM timeline_events
        ORDER BY year, month, id
    """)

    events = cursor.fetchall()

    connection.close()

    return render_template(
        "timeline.html",
        events=events
    )

if __name__ == "__main__":
    app.run(debug=True)