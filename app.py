from flask import Flask, render_template, request, session
import requests
import random

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

app.secret_key = "pokeverse_master_challenge"

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

def generate_quiz_questions():

        questions = []

        for i in range(10):

          questions.append(
            generate_who_pokemon_question()
        )

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

    limit = 50

    offset = (page - 1) * limit

    url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={offset}"

    response = requests.get(url)

    data = response.json()

    pokemon_list = data["results"]

    all_pokemon = requests.get(
    "https://pokeapi.co/api/v2/pokemon?limit=1025"
   ).json()["results"]

    return render_template(
        "pokemon.html",
        pokemon_list=pokemon_list,
        page=page,
        start_number=offset,
        all_pokemon=all_pokemon
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

    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{name}"

    pokemon = requests.get(pokemon_url).json()

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

        print("PAGE =", page)

    return render_template (
        "pokemon_details.html",
        pokemon=pokemon,
        next_evolution=next_evolution,
        random_mode=False,
        from_type=from_type,
        page=page
        
    )

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
    featured_pokemon=featured_pokemon
    
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

if __name__ == "__main__":
    app.run(debug=True)