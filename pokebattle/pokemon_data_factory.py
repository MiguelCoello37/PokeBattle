from pb_pokeapi.pokeapi import PokeAPI
from pokebattle.moveset_factory import create_moveset
from pokebattle.pokemon_data import PokemonData


def create_pokemon(name: str, pokeapi: PokeAPI):
    pokemon_data = pokeapi.get_pokemon_by_name(name)
    id = pokemon_data["id"]
    name = pokemon_data["name"]
    height = pokemon_data["height"]
    weight = pokemon_data["weight"]
    types = {type_info["slot"]: pokeapi.get_type_in_spanish(type_info) for type_info in pokemon_data["types"]}
    stats = {stat["stat"]["name"]: stat["base_stat"] for stat in pokemon_data["stats"]}
    moveset = create_moveset(pokemon_data["moves"])

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
