from pb_pokeapi.pokeapi_move import PokeApiMove


def create_pokeapi_move(data: dict):
    name = data["move"]["name"]
    url = data["move"]["url"]

    return PokeApiMove(name, url)
