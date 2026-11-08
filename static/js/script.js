function scrollToFeatures() {
    const features = document.querySelector(".features-grid");

    if (features) {
        features.scrollIntoView({
            behavior: "smooth",
            block: "start"
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

// Your existing JavaScript code above...

// Profile Dropdown
window.scrollToFeatures = function () {

    const features = document.getElementById("explore");

    if (features) {
        features.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });
    }

};

document.addEventListener("DOMContentLoaded", function () {

    const avatarBtn = document.getElementById("avatarBtn");
    const dropdown = document.getElementById("profileDropdown");

    const openProfileBtn = document.getElementById("openProfileModal");
    const profileModal = document.getElementById("profileModal");
    const closeProfileBtn = document.getElementById("closeProfileModal");

    // Open and close profile dropdown
    if (avatarBtn && dropdown) {

        avatarBtn.addEventListener("click", function (event) {
            event.stopPropagation();
            dropdown.hidden = !dropdown.hidden;
        });

        document.addEventListener("click", function (event) {
            if (!avatarBtn.contains(event.target) &&
                !dropdown.contains(event.target)) {
                dropdown.hidden = true;
            }
        });

        document.addEventListener("keydown", function (event) {
            if (event.key === "Escape") {
                dropdown.hidden = true;
            }
        });
    }

    // Open profile modal when username is clicked
    if (openProfileBtn && profileModal) {

        openProfileBtn.addEventListener("click", function () {
            dropdown.hidden = true;
            profileModal.hidden = false;
            document.body.style.overflow = "hidden";
        });

    }

    // Close profile modal
    if (closeProfileBtn && profileModal) {

        closeProfileBtn.addEventListener("click", function () {
            profileModal.hidden = true;
            document.body.style.overflow = "";
        });

        // Close when clicking outside the modal
        profileModal.addEventListener("click", function (event) {
            if (event.target === profileModal) {
                profileModal.hidden = true;
                document.body.style.overflow = "";
            }
        });

        // Close with Escape key
        document.addEventListener("keydown", function (event) {
            if (event.key === "Escape" && !profileModal.hidden) {
                profileModal.hidden = true;
                document.body.style.overflow = "";
            }
        });

    }

});
