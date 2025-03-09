from dataclasses import dataclass


@dataclass(frozen=True)
class PokemonData:
    id: int
    name: str
    height: int
    weight: int
    type_1: str
    type_2: str = None
