from pb_pokeapi import pokeapi
from pokebattle.create_pokemon_data import create_pokemon


def start():
    # pokemon_name = input("Elige tu Pokémon: ")
    pokemon_name = "celebi"
    poke_api = pokeapi.PokeAPI()
    pokemon = create_pokemon(pokemon_name, poke_api)
    print(pokemon.type_1)
    print(pokemon.type_2)


if __name__ == "__main__":
    start()
