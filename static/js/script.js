function scrollToFeatures() {

    const explore = document.getElementById("explore");

    if (explore) {

        explore.scrollIntoView({
            behavior: "smooth"
        });

    }

}


const searchInput = document.getElementById("searchInput");
const suggestions = document.getElementById("suggestions");

if(searchInput && suggestions){

    searchInput.addEventListener("input", function(){

        const value = this.value.toLowerCase();

        suggestions.innerHTML = "";

        if(value.length === 0){
            suggestions.style.display = "none";
            return;
        }

        const matches = pokemonList.filter(function(pokemon){
            return pokemon.startsWith(value);
        }).slice(0, 10);

        matches.forEach(function(pokemon){

            const pokemonId = pokemonList.indexOf(pokemon) + 1;

            suggestions.innerHTML += `
                <div class="suggestion-item"
                     onclick="window.location.href='/pokemon/${pokemon}'">

                    <img
                        src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${pokemonId}.png"
                        class="suggestion-sprite">

                    <div class="suggestion-info">

                        <span class="suggestion-name">
                            ${pokemon.charAt(0).toUpperCase() + pokemon.slice(1)}
                        </span>

                        <span class="suggestion-id">
                            #${String(pokemonId).padStart(3, '0')}
                        </span>

                    </div>

                </div>
            `;
        });
        
        suggestions.style.display =
            matches.length ? "block" : "none";

    });

}