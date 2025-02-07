function filterPokemon() {
    let searchText = document.getElementById("search-bar").value.toLowerCase();
    let pokemonCards = document.querySelectorAll(".pokemon-card");

    pokemonCards.forEach(card => {
        let name = card.querySelector(".pokemon-name").textContent.toLowerCase();
        let types = Array.from(card.querySelectorAll(".pokemon-type")).map(type => type.textContent.toLowerCase());

        if (name.includes(searchText) || types.some(type => type.includes(searchText))) {
            card.style.display = "block";
        } else {
            card.style.display = "none";
        }
    });
}