from pb_pokeapi import pokeapi
from pokebattle.pokemon_data_factory import create_pokemon


def start():
    # pokemon_name = input("Elige tu Pokémon: ")
    pokemon_name = "celebi"
    poke_api = pokeapi.PokeAPI()
    pokemon = create_pokemon(pokemon_name, poke_api)
    print(pokemon)


if __name__ == "__main__":
    start()
