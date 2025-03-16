import requests

from pb_pokeapi.pokeapi_move_factory import create_pokeapi_move
from pb_pokeapi.pokeapi_move_non_detail_factory import create_pokeapi_move_non_detail
from pb_pokeapi.pokeapi_move_non_detail import PokeApiMoveNonDetail


class PokeAPI:
    def __init__(self):
        self.base_url = "https://pokeapi.co/api/v2/"

    def get_pokemon_by_name(self, name):
        url = self.base_url + f"pokemon/{name.lower()}"
        response = requests.get(url)
        if response.status_code != 200:
            return None

        return response.json()

    def get_pokemon_moves_in_language(self, name, language="es"):
        pokemon = self.get_pokemon_by_name(name)
        if not pokemon:
            return None

        moves_in_language = self._get_pokemon_moves_in_language(pokemon, language)

        return moves_in_language

    def _get_pokemon_moves_in_language(self, pokemon, language="es"):
        return [
            self.get_move_in_language(move, language)
            for move in pokemon["moves"]
        ]

    def get_move_in_language(self, move_data: dict, language: str):
        move = create_pokeapi_move_non_detail(move_data)
        move_info = self._get_move_info(move)
        move_info_in_language = self._get_move_info_in_language(move_info, language)
        pokeapi_move = create_pokeapi_move(move_info_in_language)

        return pokeapi_move

    def _get_move_info(self, move_non_detail: PokeApiMoveNonDetail):
        move_response = requests.get(move_non_detail.url)
        if move_response.status_code != 200:
            return None

        return move_response.json()

    def _get_move_info_in_language(self, move_info, language):
        move_name_in_language = next((
            language_info["name"]
            for language_info in move_info["names"]
            if language_info["language"]["name"] == language
        ), None)

        move_info["name"] = move_name_in_language

        return move_info

    def get_type_in_spanish(self, type: dict):
        type_response = requests.get(type["type"]["url"])
        if type_response.status_code != 200:
            return None

        type_info = type_response.json()

        type_info_spanish = [
            language_info
            for language_info in type_info["names"]
            if language_info["language"]["name"] == "es"
        ][0]
        if not type_info_spanish:
            return None

        type_name_spanish = type_info_spanish.get("name", None)
        if not type_name_spanish:
            print(type_info_spanish)

        return type_name_spanish
