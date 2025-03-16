from pb_pokeapi.pokeapi_move import PokeApiMove


def create_pokeapi_move(data: dict):
    name = data.get("name")

    return PokeApiMove(name)
