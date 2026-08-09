const randomContent =
document.getElementById("randomContent");

const buttonArea =
document.querySelector(".button-area");

let firstGeneration = true;

const button = document.getElementById("generateBtn");

const card = document.getElementById("pokemonCard");

const image = document.getElementById("pokemonImage");

const nameText = document.getElementById("pokemonName");

const number = document.getElementById("pokemonNumber");

const types = document.getElementById("pokemonTypes");



async function generatePokemon() {

    button.disabled = true;
    button.innerHTML = "🎲 Generating...";

    // Hide current card
    card.classList.remove("show");

    await new Promise(resolve => setTimeout(resolve,300));

    const id = Math.floor(Math.random()*1025)+1;

    const response = await fetch(
        `https://pokeapi.co/api/v2/pokemon/${id}`
    );

    const pokemon = await response.json();

    image.alt = pokemon.name;

    nameText.innerHTML =
        pokemon.name.charAt(0).toUpperCase() +
        pokemon.name.slice(1);

    number.innerHTML =
        "#" + String(pokemon.id).padStart(3,"0");

    card.href =
        "/pokemon/" + pokemon.id;

    types.innerHTML = "";

    pokemon.types.forEach(type => {

        const badge = document.createElement("div");

        badge.className =
            "type-badge " + type.type.name;

        badge.innerHTML =
            type.type.name.charAt(0).toUpperCase() +
            type.type.name.slice(1);

        types.appendChild(badge);

    });

    await new Promise(resolve => {

    image.onload = resolve;

    image.src =
        pokemon.sprites.other["official-artwork"].front_default;

});

// First time only → reveal the hidden container
if(firstGeneration){

    randomContent.style.display = "flex";

    buttonArea.after(randomContent);

    firstGeneration = false;

}

// Now fade the card in
card.classList.add("show");

button.disabled = false;
button.innerHTML = "🎲 Generate Another";

}



button.addEventListener(

    "click",

    generatePokemon

);

