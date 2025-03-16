from dataclasses import dataclass


@dataclass(frozen=True)
class PokeApiMoveNonDetail:
    name: str
    url: str
