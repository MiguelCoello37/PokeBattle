from pb_pokeapi.pokeapi_move_non_detail import PokeApiMoveNonDetail


def create_pokeapi_move_non_detail(pokemon_data: dict):
    name = pokemon_data["move"]["name"]
    url = pokemon_data["move"]["url"]

    return PokeApiMoveNonDetail(name, url)
