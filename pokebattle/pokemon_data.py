from dataclasses import dataclass
from typing import Optional

from pokebattle.moveset_data import MovesetData


@dataclass(frozen=True)
class PokemonData:
    id: int
    name: str
    height: int
    weight: int
    type_1: str
    type_2: Optional[str]
    hp: int
    attack: int
    defense: int
    special_attack: int
    special_defense: int
    speed: int
    moves: MovesetData
