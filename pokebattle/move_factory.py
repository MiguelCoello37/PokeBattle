from pb_pokeapi.pokeapi_move_factory import create_pokeapi_move
from pokebattle.move_data import MoveData


def create_move(data: dict):
    pokeapi_move = create_pokeapi_move(data)

    name = pokeapi_move.name

    return MoveData(name)
