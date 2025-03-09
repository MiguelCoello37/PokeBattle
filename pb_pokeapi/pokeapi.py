import requests


class PokeAPI:
    def __init__(self):
        self.base_url = "https://pokeapi.co/api/v2/"

    def get_pokemon_by_name(self, name):
        url = self.base_url + f"pokemon/{name.lower()}"
        response = requests.get(url)
        if response.status_code != 200:
            return None

        return response.json()

    def get_pokemon_moves_in_spanish(self, name):
        pokemon = self.get_pokemon_by_name(name)
        if not pokemon:
            return None

        moves_in_spanish = [
            self.get_move_in_spanish(move)
            for move in pokemon["moves"]
        ]

        return moves_in_spanish

    def get_move_in_spanish(self, move):
        move_response = requests.get(move["move"]["url"])
        if move_response.status_code != 200:
            return None

        move_info = move_response.json()

        move_info_spanish = [
            language_info
            for language_info in move_info["names"]
            if language_info["language"]["name"] == "es"
        ][0]
        if not move_info_spanish:
            return None
        
        move_name_spanish = move_info_spanish.get("name", None)
        if not move_name_spanish:
            print(move_info_spanish)

        return move_name_spanish

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
