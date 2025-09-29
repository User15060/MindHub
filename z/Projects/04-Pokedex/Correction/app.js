const pokemonName = document.querySelector("#namePokemon");
const pokemonImg = document.querySelector("#imagePokemon");
const pokemonId = document.querySelector("#idPokemon");
const pokemonType = document.querySelector("#typePokemon");
const pokemonStat = document.querySelector("#statPokemon");

const typeColors = {
  electric: "#ffc800",
  normal: "#939393",
  fire: "#c21d1d",
  water: "#1d43c2",
  ice: "#1da9c2",
  rock: "#3a3b3b",
  flying: "#b4b8b8",
  grass: "#054f09",
  psychic: "#ffc6d9",
  ghost: "#561d25",
  bug: "#a2faa3",
  poison: "#795663",
  ground: "#d2b074",
  dragon: "#da627d",
  steel: "#1d8a99",
  fighting: "#2f2f2f",
  default: "#2a1a1f",
};

function searchPokemon(event) {
  event.preventDefault();

  const inputValue = event.target.pokemon.value.trim().toLowerCase();
  if (!inputValue) return alert("Please enter a Pokemon name or ID");

  fetch(`https://pokeapi.co/api/v2/pokemon/${inputValue}`)
    .then((res) => {
      if (!res.ok) throw new Error("Pokemon not found");
      return res.json();
    })
    .then((data) => displayPokemonData(data))
    .catch((error) => {
      alert(error.message);
      clearPokemonData();
    });
}

function displayPokemonData(data) {
  const sprite = data.sprites.front_default;
  const { stats, types } = data;

  pokemonName.textContent = data.name.toUpperCase();
  pokemonImg.src = sprite || "";
  pokemonImg.alt = data.name;
  pokemonId.textContent = `N°${data.id}`;

  displayPokemonTypes(types);
  displayPokemonStats(stats);
}

function displayPokemonTypes(types) {
  pokemonType.innerHTML = "";

  types.forEach(({ type }) => {
    const typeSpan = document.createElement("span");
    typeSpan.textContent = type.name.toUpperCase();
    typeSpan.style.backgroundColor = typeColors[type.name] || typeColors.default;
    typeSpan.style.padding = "0.2rem 0.5rem";
    typeSpan.style.marginRight = "0.3rem";
    typeSpan.style.borderRadius = "5px";
    pokemonType.appendChild(typeSpan);
  });
}

function displayPokemonStats(stats) {
  pokemonStat.innerHTML = "";

  stats.forEach(({ stat, base_stat }) => {
    const statDiv = document.createElement("div");

    const statNameP = document.createElement("p");
    statNameP.textContent = stat.name.toUpperCase();

    const statValueP = document.createElement("p");
    statValueP.textContent = base_stat;

    statDiv.appendChild(statNameP);
    statDiv.appendChild(statValueP);

    pokemonStat.appendChild(statDiv);
  });
}

function clearPokemonData() {
  pokemonName.textContent = "Search Pokemon";
  pokemonImg.src = "";
  pokemonImg.alt = "";
  pokemonId.textContent = "";
  pokemonType.innerHTML = "";
  pokemonStat.innerHTML = "";
}
