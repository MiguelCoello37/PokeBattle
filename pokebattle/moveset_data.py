from dataclasses import dataclass

from pokebattle.move_data import MoveData


@dataclass(frozen=True)
class MovesetData:
    level_up: list[MoveData]
    tutor: list[MoveData]
    machine: list[MoveData]
