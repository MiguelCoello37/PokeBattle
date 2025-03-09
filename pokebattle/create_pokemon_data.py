from pb_pokeapi.pokeapi import PokeAPI
from pokebattle.pokemon_data import PokemonData


def create_pokemon(name: str, pokeapi: PokeAPI):
    pokemon_data = pokeapi.get_pokemon_by_name(name)
    pokemon_id = pokemon_data["id"]
    pokemon_name = pokemon_data["name"]
    pokemon_height = pokemon_data["height"]
    pokemon_weight = pokemon_data["weight"]
    pokemon_types = {type_info["slot"]: pokeapi.get_type_in_spanish(type_info) for type_info in pokemon_data["types"]}

    return PokemonData(pokemon_id, pokemon_name, pokemon_height, pokemon_weight, pokemon_types.get(1), pokemon_types.get(2))
