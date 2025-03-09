from pokebattle.move_data import MoveData


def create_move(data: dict):
    name = data["move"]["name"]

    return MoveData(name)
