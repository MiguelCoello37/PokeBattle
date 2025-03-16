from pb_pokeapi.pokeapi import PokeAPI
from pokebattle.pokemon_data_factory import create_pokemon


def start():
    # pokemon_name = input("Elige tu Pokémon: ")
    pokemon_name = "celebi"
    language = "es"
    pokeapi = PokeAPI()
    pokemon_moves = pokeapi.get_pokemon_moves_in_language(pokemon_name, language)
    pokemon_moves_json = {"data": pokemon_moves}
    print(pokemon_moves_json)

    # pokemon = create_pokemon(pokemon_name, pokeapi)
    # print(pokemon)


if __name__ == "__main__":
    start()
