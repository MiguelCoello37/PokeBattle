from pokebattle.move_factory import create_move
from pokebattle.moveset_data import MovesetData


def create_moveset(data: list[dict]):
    version = "emerald"
    moves_data_by_learn_method = {
        learn_method: get_moves_data_by_learn_method(data, learn_method, version=version)
        for learn_method in ["level-up", "machine", "tutor"]
    }

    moves = {
        learn_method: [
            create_move(move_data)
            for move_data in moves_data
        ]
        for learn_method, moves_data in moves_data_by_learn_method.items()
    }

    return MovesetData(
        moves["level-up"],
        moves["machine"],
        moves["tutor"]
    )


def get_moves_data_by_learn_method(data: dict, learn_method: str, version: str):
    return [
        move
        for move in data
        for version_group_detail in move["version_group_details"]
        if version_group_detail["move_learn_method"]["name"] == learn_method
        and version_group_detail["version_group"]["name"] == version
    ]
