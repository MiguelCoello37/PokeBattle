from pb_pokeapi.pokeapi import PokeAPI
from pokebattle.moveset_factory import create_moveset
from pokebattle.pokemon_data import PokemonData


def create_pokemon(name: str, pokeapi: PokeAPI):
    data = pokeapi.get_pokemon_by_name(name)
    id = data["id"]
    name = data["name"]
    height = data["height"]
    weight = data["weight"]
    types = {type_info["slot"]: pokeapi.get_type_in_spanish(type_info) for type_info in data["types"]}
    stats = {stat["stat"]["name"]: stat["base_stat"] for stat in data["stats"]}
    moveset = create_moveset(data["moves"])

    return PokemonData(
        id,
        name,
        height,
        weight,
        types.get(1),
        types.get(2),
        stats["hp"],
        stats["attack"],
        stats["defense"],
        stats["special-attack"],
        stats["special-defense"],
        stats["speed"],
        moveset        
    )
